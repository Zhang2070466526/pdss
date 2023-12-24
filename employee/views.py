from django.http import HttpResponse
from django.shortcuts import render
from employee.employeeClass.dataSync import DataSync
from django.http import JsonResponse
from rest_framework import status

from auther.models import AdminUser
from employee.models import HrEmployee, HrEmployeeFiles, HrDepartment, HrPayType
from django.db import models
from employee.employeeClass.rosterClass import *
from datetime import datetime
from employee.employeeClass.dataReport import *
# Create your views here.
from rest_framework.views import APIView
from utils.save_data_to_redis import *

# 部门同步 数据同步
def basic_sync(request):
    sync = DataSync()
    sync.dept_Sync()
    # sync.dimissionType_sync()
    sync.dimissionReason_sync()

    # sync.position_Sync()
    # sync.jobClass_Sync()
    # sync.jobGrade_Sync()
    # sync.jobDuty_Sync()
    # sync.payType_Sync()
    # sync.jobRank_Sync()
    # sync.Nation_Sync()
    # sync.nationPlace_Sync()
    # sync.educationDegree_Sync()
    sync.employee_Sync()
    return HttpResponse("同步成功")


def get_user_field(request,parent_id):
    """

    :param request:
    :param parent_id:    菜单该字段的nav_parent_id
    :return:
    """
    user_id = request.check_token
    user_field_all = list(
        AdminUser.objects.filter(user_menu__nav_parent_id=parent_id, pk=user_id, user_menu__nav_type=3, ).values_list(
            'user_menu__nav_name_field', flat=True))

    user_field_all = list(
        AdminUser.objects.filter(user_menu__nav_parent_id=parent_id, pk=user_id, user_menu__nav_type=3).values(
            'user_menu__nav_name_field', 'user_menu__nav_name'))
    user_field_all_dict = []

    for dictionary in user_field_all:
        key = dictionary['user_menu__nav_name_field']
        value = dictionary['user_menu__nav_name']
        new_dict = {key: value}
        user_field_all_dict.append(new_dict)
    # print(user_field_all_dict)
    file_field_ls = []
    # user_field_all_dict=[{'employee_identity_no': '身份证号码'}, {'employee_phone': '联系电话'},{'employee_identity_file':'身份证文件'}]
    for userdict in user_field_all_dict:
        for field_name, verbose_name in userdict.items():
            # print(field_name,verbose_name)
            try:  # 存在关联查询即会报错 例如employee_department__department_name,即不在HrEmployee表
                if isinstance(HrEmployee._meta.get_field(field_name), models.ManyToManyField) and str(field_name)[-4:] == 'file':  # 是多对多关系,同时是文件
                    exclude_field = ['creator', 'modifier', 'create_time', 'modify_time']
                    for file_field in HrEmployeeFiles._meta.fields:  # 文件表中所有的字段
                        if file_field.name not in exclude_field:
                            # print(field_name,file_field.name,file_field.verbose_name)
                            user_field_all_dict.append(
                                {str(field_name) + "__" + file_field.name: verbose_name + file_field.verbose_name})
                    file_field_ls.append(
                        {str(field_name): verbose_name})  # 所有多对多关系且是文件的字段  [{'employee_identity_file': '身份证文件'}]
            except:
                pass
    # print(file_field_ls)
    result_field = user_field_all_dict
    return result_field
    # return_data = {'code': status.HTTP_200_OK, "msg": "成功",'data':result_field}
    # return JsonResponse(return_data)


def get_roster_info(request):
    roster = Roster(request, 'get_roster_info')
    res = roster.method_center()
    return res


def download_roster_info(request):
    roster = Roster(request, 'download_roster_info')
    res = roster.method_center()
    return res


def get_roster_options(request):
    if request.check_token is not None:
        jobrank_all = AdminUser.objects.filter(id=request.check_token,
                                               user_jobrank_employee__job_rank_status=True).values_list(
            'user_jobrank_employee__id',
            'user_jobrank_employee__job_rank_name').all()
        employee_pay_type_list = list(
            HrPayType.objects.filter(pay_type_status=True).exclude(id=999999).values('id', 'pay_type_name'))  # 计薪方式
        return_data = {
            'data': {
                'content_type_list': [
                    {"value": item["id"], "label": item["pay_type_name"]}
                    for item in employee_pay_type_list
                ],
                'jobrank_list': [
                    {"id": item[0], "label": item[1]}
                    for item in jobrank_all
                ]
            },
            "code": status.HTTP_200_OK,
            "msg": "下拉菜单返回成功",
            'hidden': True,
        }

    else:
        return_data = {
            "code": status.HTTP_403_FORBIDDEN,
            "msg": "没有权限访问",
            'hidden': False
        }
    return JsonResponse(return_data)


def get_jobrank_option(request):
    return_data = {
        "code": 200,
        "msg": "下拉菜单返回成功",
        "data": [],
        'hidden': True
    }

    if request.check_token != None:
        jobrankAll = AdminUser.objects.filter(id=request.check_token,
                                              user_jobrank_employee__job_rank_status=True).values_list(
            'user_jobrank_employee__id',
            'user_jobrank_employee__job_rank_name').all()

        # jobrankAll = JobRank.objects.filter(jobrank_status=True).values_list('id', 'JobRankName').all()
        '''
        id=check_token,
        '''
        for i in jobrankAll:
            return_data['data'].append({
                "label": i[1],
                "id": i[0]
            })
    else:
        return_data = {
            "code": status.HTTP_403_FORBIDDEN,
            "msg": "没有权限访问",
            'hidden': False
        }
    # return HttpResponse(json.dumps(return_data))
    return JsonResponse(return_data)


def get_trees(data,
              key_column='id',
              parent_column='parent_id',
              child_column='children',
              current_column=None,
              current_path=None):
    """
    :param data: 数据列表
    :param key_column: 主键字段，默认id
    :param parent_column: 父ID字段名，父ID默认从0开始
    :param child_column: 子列表字典名称
    :param current_column: 当前展开值字段名，若找到展开值增加['open'] = '1'
    :param current_path: 当前展开值
    :return: 树结构
    """
    data_dic = {}
    for d in data:
        data_dic[d.get(key_column)] = d  # 以自己的权限主键为键,以新构建的字典为值,构造新的字典
    # print(data_dic)

    data_tree_list = []  # 整个数据大列表
    for d_id, d_dic in data_dic.items():
        d_dic['label'] = d_dic.pop('department_name')
        d_dic['value'] = d_id  # Change the key name 'id' to 'value'
        # print(d_id,d_dic)
        pid = d_dic.get(parent_column)  # 取每一个字典中的父id
        if pid == 0:  # 父id=0，就直接加入数据大列表
            data_tree_list.append(d_dic)
        else:  # 父id>0 就加入父id队对应的那个的节点列表
            try:  # 判断异常代表有子节点，增加子节点列表=[]
                data_dic[pid][child_column].append(d_dic)
            except KeyError:
                data_dic[pid][child_column] = []
                data_dic[pid][child_column].append(d_dic)
    return data_tree_list


def get_department_option(request):
    return_data = {
        "code": 200,
        "msg": "下拉菜单返回成功",
        "data": [],
        'hidden': True
    }
    from datetime import datetime

    if request.check_token is not None:

        # def get_department_hierarchy(parent_id=0):
        #     departments = HrDepartment.objects.filter(
        #         Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gt=datetime.now()),
        #         department_parent_id=parent_id, department_status=1)
        #     # print(departments)
        #     hierarchy = []
        #     for department in departments:
        #         department_data = {
        #             'id': department.id,
        #             'label': department.department_name,
        #             'children': get_department_hierarchy(parent_id=department.id)
        #         }
        #         hierarchy.append(department_data)
        #
        #     return hierarchy
        # hrbase_data = get_department_hierarchy(parent_id=0)

        #
        #

        # def replace_id_with_value(data, start_index=1):
        #     for item in data:
        #         item["value"] = item.pop("id")
        #         item["index"] = start_index
        #         start_index += 1
        #         if "children" in item:
        #             start_index = replace_id_with_value(item["children"], start_index)
        #     return start_index
        # #
        # replace_id_with_value(hrbase_data)
        # #
        # hrbase_boss_obj = HrDepartment.objects.filter(
        #     Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gte=datetime.now()), department_status=1,
        #     department_parent_id=0).values('id', 'department_name')
        # # hrbase_data = [
        # #     {"value": hrbase_boss_obj[0]['id'], "label": hrbase_boss_obj[0]['department_name'], "children": hrbase_data,"index": 0,}]
        # print(hrbase_data)
        # base_ls = list(AdminUser.objects.filter(id=request.check_token, user_department_employee__department_status=1).values_list('user_department_employee__id',flat=True))

        # print(base_ls)

        departments = HrDepartment.objects.filter(
            ~Q(id=999999),
            Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gt=datetime.now()),
            department_status=1
        ).values('id', 'department_name', 'department_parent_id')
        # from setup.userClass.userClass import get_trees
        hrbase_data = get_trees(departments, 'id', 'department_parent_id')

        base_ls = [1, ] + request.user_department_employee

        def filter_nodes(node):
            if 'children' in node:
                node['children'] = [child for child in node['children'] if child['id'] in base_ls]
                for child in node['children']:
                    filter_nodes(child)

        data = [node for node in hrbase_data if node['id'] in base_ls]
        for node in data:
            filter_nodes(node)

        # def remove_empty_children(node):
        #     if isinstance(node, dict):
        #         if "children" in node and node["children"] == []:
        #             del node["children"]
        #         else:
        #             for key, value in node.items():
        #                 if isinstance(value, list):
        #                     node[key] = [remove_empty_children(child) for child in value]
        #                 elif isinstance(value, dict):
        #                     node[key] = remove_empty_children(value)
        #     return node
        #
        # cleaned_data = remove_empty_children(hrbase_data[0])
        # return_data = {
        #     "data_list":[cleaned_data]
        # }
        #
        #
        #

        def add_indexes(node_list, index=0):
            for node in node_list:
                node['index'] = index
                index += 1
                children = node.get('children', [])
                if children:
                    index = add_indexes(children, index)
            return index

        return_data['data'] = hrbase_data
        add_indexes(return_data['data'])
        base_ls = request.user_department_employee
        # # base=base_ls
        # print('bae',base_ls)

        # departments = HrDepartment.objects.filter(
        #     ~Q(id=999999),
        #     Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gt=datetime.now()),
        #     department_status=1
        #  ).values('id', 'department_name', 'department_parent_id')
        # from setup.userClass.userClass import get_trees
        # hrbase_data = get_trees(departments,'id','department_parent_id')
        # z=[31, 32, 33, 77, 80, 81, 82, 119, 143, 144, 167, 183, 237, 238, 239, 292, 293, 338, 339, 340, 358, 409, 410, 411, 413, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 670]






    else:
        return_data = {
            "code": status.HTTP_403_FORBIDDEN,
            "msg": "没有权限访问",
            'hidden': False
        }
    # return HttpResponse(json.dumps(return_data))
    return JsonResponse(return_data)


# ——————————————————————————————————————————————————————————————————————————报表平台————————————————————————————————————————————————————————————


def dimissionReason_sync(request):
    sync = DataSync()
    sync.dimissionReason_sync()
    return HttpResponse("同步成功")
def dimissionType_sync(request):
    sync = DataSync()
    sync.dimissionType_sync()
    return HttpResponse("同步成功")


# def active_employee_seniority(request):  # 司龄分布
#     reset = EmployeeDataReport()
#     info = request.GET
#     params = {
#         # 'dl_idl':info['dl_idl'],
#         # 'job_class':info['job_class'],
#         # 'job_sequence':info['job_sequence'],
#         # 'job_sequence':None,
#         'currentPage': int(info['currentPage']),
#         'pageSize': int(info['pageSize']),
#         'search_date': info['search_date'],
#     }
#
#     if "department_id" in request.GET:
#         department_id = request.GET.get('department_id', None)
#         if len(department_id) == 0:
#             department_id = request.user_department_employee
#         params['department_id'] = department_id
#     if "department_id[]" in request.GET:
#         department_id = request.GET.getlist('department_id[]', None)
#         params['department_id'] = department_id
#     if "job_class" in request.GET:
#         params['job_class'] = request.GET.get('job_class', None)
#     if "job_class[]" in request.GET:
#         params['job_class'] = request.GET.getlist('job_class[]', None)
#     if "job_sequence" in request.GET:
#         params['job_sequence'] = request.GET.get('job_sequence', None)
#     if "job_sequence[]" in request.GET:
#         params['job_sequence'] = request.GET.getlist('job_sequence[]', None)
#     if "dl_idl" in request.GET:
#         params['dl_idl'] = request.GET.get('dl_idl', None)
#     if "dl_idl[]" in request.GET:
#         params['dl_idl'] = request.GET.getlist('dl_idl[]', None)
#     response_data = reset.active_employee_seniority(**params)
#     return JsonResponse(response_data)
# def active_employee_age(request):
#     reset = EmployeeDataReport()
#     info = request.GET
#     params = {
#         # 'dl_idl':info['dl_idl'],
#         # 'job_grade':info['job_grade'],
#         # 'job_class':info['job_class'],
#         'currentPage': int(info['currentPage']),
#         'pageSize': int(info['pageSize']),
#         'search_date': info['search_date'],
#         # 'department_id':info['department_id']
#     }
#     if "department_id" in request.GET:
#         department_id = request.GET.get('department_id', None)
#         if len(department_id) == 0:
#             department_id = request.user_department_employee
#         params['department_id'] = department_id
#     if "department_id[]" in request.GET:
#         department_id = request.GET.getlist('department_id[]', None)
#         params['department_id'] = department_id
#     if "job_class" in request.GET:
#         params['job_class'] = request.GET.get('job_class', None)
#     if "job_class[]" in request.GET:
#         params['job_class'] = request.GET.getlist('job_class[]', None)
#     if "job_sequence" in request.GET:
#         params['job_sequence'] = request.GET.get('job_sequence', None)
#     if "job_sequence[]" in request.GET:
#         params['job_sequence'] = request.GET.getlist('job_sequence[]', None)
#     if "dl_idl" in request.GET:
#         params['dl_idl'] = request.GET.get('dl_idl', None)
#     if "dl_idl[]" in request.GET:
#         params['dl_idl'] = request.GET.getlist('dl_idl[]', None)
#     response_data = reset.active_employee_age(**params)
#     return JsonResponse(response_data)
# def active_employee_education(request):
#     reset = EmployeeDataReport()
#     info = request.GET
#     params = {
#         # 'dl_idl':info['dl_idl'],
#         # 'job_class':info['job_class'],
#         'currentPage': int(info['currentPage']),
#         'pageSize': int(info['pageSize']),
#         'search_date': info['search_date'],
#         # 'department_id':info['department_id']
#     }
#     if "department_id" in request.GET:
#         department_id = request.GET.get('department_id', None)
#         if len(department_id) == 0:
#             department_id = request.user_department_employee
#         params['department_id'] = department_id
#     if "department_id[]" in request.GET:
#         department_id = request.GET.getlist('department_id[]', None)
#         params['department_id'] = department_id
#     if "job_class" in request.GET:
#         params['job_class'] = request.GET.get('job_class', None)
#     if "job_class[]" in request.GET:
#         params['job_class'] = request.GET.getlist('job_class[]', None)
#     if "job_sequence" in request.GET:
#         params['job_sequence'] = request.GET.get('job_sequence', None)
#     if "job_sequence[]" in request.GET:
#         params['job_sequence'] = request.GET.getlist('job_sequence[]', None)
#     if "dl_idl" in request.GET:
#         params['dl_idl'] = request.GET.get('dl_idl', None)
#     if "dl_idl[]" in request.GET:
#         params['dl_idl'] = request.GET.getlist('dl_idl[]', None)
#     response_data = reset.active_employee_education(**params)
#     return JsonResponse(response_data)
# def active_employee_nationality(request):
#     reset = EmployeeDataReport()
#     info = request.GET
#     params = {
#         # 'job_class':info['job_class'],
#         'currentPage': int(info['currentPage']),
#         'pageSize': int(info['pageSize']),
#         'search_date': info['search_date'],
#         # 'department_id':info['department_id']
#     }
#     if "department_id" in request.GET:
#         department_id = request.GET.get('department_id', None)
#         if len(department_id) == 0:
#             department_id = request.user_department_employee
#         params['department_id'] = department_id
#     if "department_id[]" in request.GET:
#         department_id = request.GET.getlist('department_id[]', None)
#         params['department_id'] = department_id
#     if "job_class" in request.GET:
#         params['job_class'] = request.GET.get('job_class', None)
#     if "job_class[]" in request.GET:
#         params['job_class'] = request.GET.getlist('job_class[]', None)
#     if "job_sequence" in request.GET:
#         params['job_sequence'] = request.GET.get('job_sequence', None)
#     if "job_sequence[]" in request.GET:
#         params['job_sequence'] = request.GET.getlist('job_sequence[]', None)
#     response_data = reset.active_employee_nationality(**params)
#     return JsonResponse(response_data)
# def active_employee_sex(request):
#     reset = EmployeeDataReport()
#     info = request.GET
#     params = {
#         # 'job_grade':info['job_grade'],
#         # 'job_class':info['job_class'],
#         'currentPage': int(info['currentPage']),
#         'pageSize': int(info['pageSize']),
#         'search_date': info['search_date'],
#         # 'department_id':info['department_id']
#     }
#     if "department_id" in request.GET:
#         department_id = request.GET.get('department_id', None)
#         if len(department_id) == 0:
#             department_id = request.user_department_employee
#         params['department_id'] = department_id
#     if "department_id[]" in request.GET:
#         department_id = request.GET.getlist('department_id[]', None)
#         params['department_id'] = department_id
#     if "job_class" in request.GET:
#         params['job_class'] = request.GET.get('job_class', None)
#     if "job_class[]" in request.GET:
#         params['job_class'] = request.GET.getlist('job_class[]', None)
#     if "job_sequence" in request.GET:
#         params['job_sequence'] = request.GET.get('job_sequence', None)
#     if "job_sequence[]" in request.GET:
#         params['job_sequence'] = request.GET.getlist('job_sequence[]', None)
#     response_data = reset.active_employee_sex(**params)
#     return JsonResponse(response_data)
# def active_employee_job_grade(request):
#     reset = EmployeeDataReport()
#     info = request.GET
#     params = {
#         # 'job_grade':info['job_grade'],
#         # 'job_class':info['job_class'],
#         'currentPage': int(info['currentPage']),
#         'pageSize': int(info['pageSize']),
#         'search_date': info['search_date'],
#         # 'department_id':info['department_id']
#     }
#     if "department_id" in request.GET:
#         department_id = request.GET.get('department_id', None)
#         if len(department_id) == 0:
#             department_id = request.user_department_employee
#         params['department_id'] = department_id
#     if "department_id[]" in request.GET:
#         department_id = request.GET.getlist('department_id[]', None)
#         params['department_id'] = department_id
#     if "job_class" in request.GET:
#         params['job_class'] = request.GET.get('job_class', None)
#     if "job_class[]" in request.GET:
#         params['job_class'] = request.GET.getlist('job_class[]', None)
#     if "job_sequence" in request.GET:
#         params['job_sequence'] = request.GET.get('job_sequence', None)
#     if "job_sequence[]" in request.GET:
#         params['job_sequence'] = request.GET.getlist('job_sequence[]', None)
#     response_data = reset.active_employee_job_grade(**params)
#     return JsonResponse(response_data)
# def departure_employee_reason(request):
#     reset = EmployeeDataReport()
#     info = request.GET
#     params = {
#         # 'job_grade':info['job_grade'],
#         # 'job_class':info['job_class'],
#         'currentPage': int(info['currentPage']),
#         'pageSize': int(info['pageSize']),
#         'search_date': info['search_date'],
#         # 'departure_reason':info['departure_reason'],
#         # 'department_id':info['department_id']
#     }
#     if "department_id" in request.GET:
#         department_id = request.GET.get('department_id', None)
#         if len(department_id) == 0:
#             department_id = request.user_department_employee
#         params['department_id'] = department_id
#     if "department_id[]" in request.GET:
#         department_id = request.GET.getlist('department_id[]', None)
#         params['department_id'] = department_id
#     if "job_class" in request.GET:
#         params['job_class'] = request.GET.get('job_class', None)
#     if "job_class[]" in request.GET:
#         params['job_class'] = request.GET.getlist('job_class[]', None)
#     if "job_sequence" in request.GET:
#         params['job_sequence'] = request.GET.get('job_sequence', None)
#     if "job_sequence[]" in request.GET:
#         params['job_sequence'] = request.GET.getlist('job_sequence[]', None)
#     if "departure_reason" in request.GET:
#         params['departure_reason'] = request.GET.get('departure_reason', None)
#     if "departure_reason[]" in request.GET:
#         params['departure_reason'] = request.GET.getlist('departure_reason[]', None)
#
#     response_data = reset.departure_employee_reason(**params)
#     return JsonResponse(response_data)
# def departure_employee_seniority(request):
#     reset = EmployeeDataReport()
#     info = request.GET
#     params = {
#         # 'job_grade':info['job_grade'],
#         # 'job_class':info['job_class'],
#         'currentPage': int(info['currentPage']),
#         'pageSize': int(info['pageSize']),
#         'search_date': info['search_date'],
#         # 'department_id':info['department_id']
#     }
#     if "department_id" in request.GET:
#         department_id = request.GET.get('department_id', None)
#         if len(department_id) == 0:
#             department_id = request.user_department_employee
#         params['department_id'] = department_id
#     if "department_id[]" in request.GET:
#         department_id = request.GET.getlist('department_id[]', None)
#         params['department_id'] = department_id
#     if "job_class" in request.GET:
#         params['job_class'] = request.GET.get('job_class', None)
#     if "job_class[]" in request.GET:
#         params['job_class'] = request.GET.getlist('job_class[]', None)
#     if "job_sequence" in request.GET:
#         params['job_sequence'] = request.GET.get('job_sequence', None)
#     if "job_sequence[]" in request.GET:
#         params['job_sequence'] = request.GET.getlist('job_sequence[]', None)
#     response_data = reset.departure_employee_seniority(**params)
#     return JsonResponse(response_data)
# def active_employee_promotion(request):
#     reset = EmployeeDataReport()
#     info = request.GET
#     params = {
#         # 'job_grade':info['job_grade'],
#         # 'job_class':info['job_class'],
#         'currentPage': int(info['currentPage']),
#         'pageSize': int(info['pageSize']),
#         'search_date': info['search_date'],
#         # 'department_id':info['department_id']
#     }
#     if "department_id" in request.GET:
#         department_id = request.GET.get('department_id', None)
#         if len(department_id) == 0:
#             department_id = request.user_department_employee
#         params['department_id'] = department_id
#     if "department_id[]" in request.GET:
#         department_id = request.GET.getlist('department_id[]', None)
#         params['department_id'] = department_id
#     if "job_class" in request.GET:
#         params['job_class'] = request.GET.get('job_class', None)
#     if "job_class[]" in request.GET:
#         params['job_class'] = request.GET.getlist('job_class[]', None)
#     if "job_sequence" in request.GET:
#         params['job_sequence'] = request.GET.get('job_sequence', None)
#     if "job_sequence[]" in request.GET:
#         params['job_sequence'] = request.GET.getlist('job_sequence[]', None)
#     print(params)
#     response_data = reset.active_employee_promotion(**params)
#     return JsonResponse(response_data)
# def active_employee_total(request):
#     reset = EmployeeDataReport()
#     info = request.GET
#     params = {
#         'currentPage': int(info['currentPage']),
#         'pageSize': int(info['pageSize']),
#         'begin_date': info['begin_date'],
#         'end_date': info['end_date'],
#         # 'department_id': info['department_id'],
#         # 'job_grade': info['job_grade'],
#         # 'job_class': info['job_class'],
#     }
#     if "department_id" in request.GET:
#         department_id = request.GET.get('department_id', None)
#         if len(department_id) == 0:
#             department_id = request.user_department_employee
#         params['department_id'] = department_id
#     if "department_id[]" in request.GET:
#         department_id = request.GET.getlist('department_id[]', None)
#         params['department_id'] = department_id
#     if "job_class" in request.GET:
#         params['job_class'] = request.GET.get('job_class', None)
#     if "job_class[]" in request.GET:
#         params['job_class'] = request.GET.getlist('job_class[]', None)
#     if "job_sequence" in request.GET:
#         params['job_sequence'] = request.GET.get('job_sequence', None)
#     if "job_sequence[]" in request.GET:
#         params['job_sequence'] = request.GET.getlist('job_sequence[]', None)
#     print(params)
#     response_data = reset.active_employee_total(**params)
#     return JsonResponse(response_data)
#
# def basic_data(request):
#     reset = EmployeeDataReport()
#     info = request.GET
#
#     department_id = request.user_department_employee
#     if "department_id" in request.GET:
#         department_id = request.GET.get('department_id', None)
#         if len(department_id) == 0:
#             department_id = request.user_department_employee
#     if "department_id[]" in request.GET:
#         department_id = request.GET.getlist('department_id[]', None)
#     params = {
#         'currentPage': int(info['currentPage']),
#         'pageSize': int(info['pageSize']),
#         'effect_date': info['effect_date'],
#         'department_id': department_id
#     }
#
#     response_data = reset.basic_data(**params)
#     return JsonResponse(response_data)

#+======================================================== 报表平台   =============================================================


def retrieve_and_sum_redis_data(redis_key, column_names, labels):
    df = pd.DataFrame(get_list_data_from_redis(redis_key))
    data = [int(df[col].sum()) for col in column_names]
    return data, labels


def limit_get_data(request):
    reset = EmployeeDataReport()
    info = json.loads(request.body)
    params = {
        'search_date': info['search_date'],
        'department_id': info['department_id'],
        'currentPage': int(info['currentPage']),
        'pageSize': int(info['pageSize']),
    }
    response_data = reset.limit_get_data(**params)
    return JsonResponse(response_data)
def limit_post_data(request):
    reset = EmployeeDataReport()
    info = eval(request.POST.get('createData'))
    # info=json.loads(request.body)
    response_data = reset.limit_post_data(info)
    return JsonResponse(response_data)
def limit_batch_data(request):
    reset = EmployeeDataReport()
    file = request.FILES.get('file')
    response_data = reset.limit_batch_data(file)
    return JsonResponse(response_data)
def limit_edit_data(request):
    reset = EmployeeDataReport()
    info = json.loads(request.body)
    response_data = reset.limit_edit_data(info)
    return JsonResponse(response_data)
def limit_down_data(request):
    reset = EmployeeDataReport()
    response_data = reset.limit_down_data(request)
    return JsonResponse(response_data)

def target_get_data(request):
    reset = EmployeeDataReport()
    info = json.loads(request.body)
    params = {
        'search_date': info['search_date'],
        'department_id': info['department_id'],
        'currentPage': int(info['currentPage']),
        'pageSize': int(info['pageSize']),
    }
    response_data = reset.target_get_data(**params)
    return JsonResponse(response_data)
def target_post_data(request):
    reset = EmployeeDataReport()
    info = eval(request.POST.get('createData'))
    # info = json.loads(request.body)
    response_data = reset.target_post_data(info)
    return JsonResponse(response_data)
def target_batch_data(request):
    reset = EmployeeDataReport()
    file = request.FILES.get('file')
    response_data = reset.target_batch_data(file)
    return JsonResponse(response_data)
def target_edit_data(request):
    reset = EmployeeDataReport()
    info = json.loads(request.body)
    response_data = reset.target_edit_data(info)
    return JsonResponse(response_data)
def target_down_data(request):
    reset = EmployeeDataReport()
    response_data = reset.target_down_data(request)
    return JsonResponse(response_data)

from rest_framework.generics import GenericAPIView

class Basic_Data_RecordView(GenericAPIView):
    def post(self, request):  # 查询
        reset = EmployeeDataReport()
        info = json.loads(request.body)
        params = {
            'effect_date': info['effect_date'],
            'department_id':info['department_id'],
            'currentPage': int(info['currentPage']),
            'pageSize': int(info['pageSize']),
        }
        if len(params['department_id']) == 0:
            params['department_id'] = request.user_department_employee
        response_data = reset.basic_data(**params)
        return JsonResponse(response_data)
    def put(self, request):  # 下载
        reset = EmployeeDataReport()
        response_data = reset.basic_down_data(request)
        return JsonResponse(response_data)

class Active_Employee_Total_RecordView(GenericAPIView):  # 汇总数据
    def post(self, request):  # 查询
        currentPage = json.loads(request.body).get('currentPage')
        pageSize = json.loads(request.body).get('pageSize')
        response_data = self.get_response_data(request)
        response_data['data']['tableList']=response_data['data']['tableList'][(currentPage - 1) * pageSize:currentPage * pageSize]
        response_data['data']['sumLabelsList'] = ['begin_incumbency', 'duration_onboarding', 'duration_dimission', 'turnover_rate', 'duration_tune', 'duration_pull', 'end_incumbency', 'manage_trainees_incumbency','chaser_light_incumbency','Key_core_incumbency','SAL_incumbency','IDL_incumbency','DL_incumbency']
        return JsonResponse(response_data)

    def put(self, request):  # 下载   #单个传序号
        reset = EmployeeDataReport()
        response_data = self.get_response_data(request)['data']['tableList']
        response_data = reset.active_employee_total_down(request,response_data)
        return JsonResponse(response_data)

    def get_response_data(self, request):
        reset = EmployeeDataReport()
        info = json.loads(request.body)
        params = {
            'begin_date': info['begin_date'],
            'end_date': info['end_date'],
            'job_sequence': info['job_sequence'],
            'job_class': info['job_class'],
            'department_id':info['department_id']
        }
        if len(params['department_id']) == 0:
            params['department_id'] = request.user_department_employee
        response_data = reset.active_employee_total(**params)
        return response_data

class Departure_Employee_Seniority_RecordView(GenericAPIView):     #司龄原因
    def post(self, request,flag=0):  # 查询
        response_data = self.get_response_data(request)
        if flag:
            save_list_data_to_redis('Departure_Employee_Seniority_RecordView_POST_' + str(request.check_token)+'_default',
                                    response_data['data']['tableList'])  # 存储数据到redis中
        else:
            currentPage = json.loads(request.body).get('currentPage')
            pageSize = json.loads(request.body).get('pageSize')
            save_list_data_to_redis('Departure_Employee_Seniority_RecordView_POST_'+str(request.check_token),response_data['data']['tableList'])  # 存储数据到redis中
            try:
                departure_active_employee_seniority_data, departure_active_employee_seniority_xaxis = retrieve_and_sum_redis_data(
                    'Departure_Employee_Seniority_RecordView_POST_'+str(request.check_token), ['7-d', '1-m', '3-m', '6-m', '12-m', '2-y', '2-y-gt'],
                    ['7天内', '1个月内', '1-3个月', '3-6个月', '6-12个月', '1-2年', '2年以上'])  # 离职率分析-司龄原因
            except:
                departure_active_employee_seniority_data=[]
                departure_active_employee_seniority_xaxis=[]
            viewDataList={
                        "type": "departure_active_employee_seniority",
                        "data": {
                            'title': '离职率分析-司龄原因',
                            'data': departure_active_employee_seniority_data,
                            'xAxis': departure_active_employee_seniority_xaxis
                        }
                                }
            response_data['data']['tableList']=response_data['data']['tableList'][(currentPage - 1) * pageSize:currentPage * pageSize]
            response_data['data']['viewDataList'] =viewDataList
            response_data['data']['sumLabelsList'] = ['7-d', '1-m', '3-m', '6-m','12-m','2-y','2-y-gt','total_person']
            return JsonResponse(response_data)

    def put(self, request):  # 下载   #单个传序号
        reset = EmployeeDataReport()
        response_data = self.get_response_data(request)['data']['tableList']
        response_data = reset.departure_employee_seniority_down(request,response_data)
        return JsonResponse(response_data)

    def get_response_data(self, request):
        reset = EmployeeDataReport()
        try:
            info = json.loads(request.body)
        except:
            info = {}
        params = {
            'search_date': info.get('search_date',''),
            'job_sequence': info.get('job_sequence',''),
            'job_class': info.get('job_class',''),
            'department_id': info.get('department_id',''),
            'departure_reason': info.get('departure_reason',''),  # 离职原因
            'departure_type': info.get('departure_type',''),  # 离职类型
            'job_grade': info.get('job_grade',''),
        }
        if len(params['department_id']) == 0:
            params['department_id'] = request.user_department_employee
        response_data = reset.departure_employee_seniority(**params)
        return response_data

class Departure_Employee_Reason_RecordView(GenericAPIView):   #离职原因
    def post(self, request,flag=0):  # 查询
        response_data = self.get_response_data(request)
        if flag:
            save_list_data_to_redis('Departure_Employee_Reason_RecordView_POST_' + str(request.check_token)+'_default',response_data['data']['tableList'])  # 存储数据到redis中
        else:
            currentPage = json.loads(request.body).get('currentPage')
            pageSize = json.loads(request.body).get('pageSize')

            save_list_data_to_redis('Departure_Employee_Reason_RecordView_POST_'+str(request.check_token),
                                    response_data['data']['tableList'])  # 存储数据到redis中
            try:
                departure_reason_retrieved_data = get_list_data_from_redis(
                    "Departure_Employee_Reason_RecordView_POST_" + str(request.check_token))  # 离职原因
                departure_reason_df = pd.DataFrame(departure_reason_retrieved_data)
                departure_reason_df_filtered = departure_reason_df.loc[
                    departure_reason_df['departure_reason'] != '合计']  # 排除合计
                departure_reason_sums = departure_reason_df_filtered.groupby('departure_reason')[
                    ['SAL', 'IDL', 'DL']].sum()  # 按departure_reason分组并计算 SAL、IDL 和 DL 的总和
                list_of_dicts = departure_reason_sums.reset_index().to_dict('records')  # 将 DataFrame 转换为字典列表
            except:
                list_of_dicts = []
            view_data_list={
                'title': '离职率分析-离职原因',
                'source': list_of_dicts,
                'dimensions': ['departure_reason', 'SAL', 'IDL', 'DL'],
            },
            response_data['data']['tableList']=response_data['data']['tableList'][(currentPage - 1) * pageSize:currentPage * pageSize]
            response_data['data']['viewDataList'] = {} if len(view_data_list)==0 else view_data_list[0]
            response_data['data']['sumLabelsList'] = ['SAL','IDL','DL','total_person']
            return JsonResponse(response_data)

    def put(self, request):  # 下载   #单个传序号
        reset = EmployeeDataReport()
        response_data = self.get_response_data(request)['data']['tableList']
        response_data = reset.departure_employee_reason_down(request,response_data)
        return JsonResponse(response_data)

    def get_response_data(self, request):
        reset = EmployeeDataReport()
        try:
            info = json.loads(request.body)
        except:
            info = {}
        params = {
            'search_date': info.get('search_date',''),
            'job_sequence': info.get('job_sequence',''),
            'job_class': info.get('job_class',''),
            'department_id': info.get('department_id',''),
            'departure_reason': info.get('departure_reason',''),  # 离职原因
            'departure_type': info.get('departure_type',''),  # 离职类型
            'job_grade': info.get('job_grade',''),
        }
        if len(params['department_id']) == 0:
            params['department_id'] = request.user_department_employee
        response_data = reset.departure_employee_reason(**params)
        return response_data

class Active_Employee_Job_Grade_RecordView(GenericAPIView):     #职级分布
    def post(self, request,flag=0):  # 查询
        response_data = self.get_response_data(request)
        if flag:
            save_list_data_to_redis('Active_Employee_Job_Grade_RecordView_POST_' + str(request.check_token)+'_default',response_data['data']['tableList'])  # 存储数据到redis中
        else:
            currentPage = json.loads(request.body).get('currentPage')
            pageSize = json.loads(request.body).get('pageSize')

            columnList_result = [d for d in response_data['data']['columnList'] if d.get('value') == '在职人员职等分布'][0]['children']
            sum_labels = [d['label'] for d in columnList_result]
            save_list_data_to_redis('Active_Employee_Job_Grade_RecordView_POST_'+str(request.check_token),response_data['data']['tableList'])  # 存储数据到redis中
            try:
                active_employee_job_grade_data_raw, active_employee_job_grade_xaxis_raw = retrieve_and_sum_redis_data(
                    'Active_Employee_Job_Grade_RecordView_POST_' + str(request.check_token),
                    ['t-1', 't-2', 't-2-2', 't-3', 't-4', 't-5', 't-6', 't-7', 'm-2', 'm-3', 'm-4', 'm-5', 'm-6', 'm-7',
                     'm-8', 'p-1', 'p-2', 'p-3', 'p-4', 'p-5', 'p-6', 'o-1', 'o-2-1', 'o-2-2'],
                    ['T1-助工级', 'T2-工程师级', 'T2.2-技术员级', 'T3-中工级', 'T4-高工级', 'T5-资工级', 'T6-专家级',
                     'T7-总工级', 'M2-班长级', 'M3-倒班主管级', 'M4-主管级', 'M5-经理级', 'M6-总监级', 'M7-总经理级',
                     'M8-总裁级',
                     'P1-助理级', 'P2-专员级', 'P3-中专级', 'P4-专业主管级', 'P5-专业经理级', 'P6-专家级', 'O1-作业员级',
                     'O2-技工级', 'O2-技师级'])  # 职级分布
                active_employee_job_grade_data, active_employee_job_grade_xaxis = [
                    sum(active_employee_job_grade_data_raw[:8]), sum(active_employee_job_grade_data_raw[8:15]),
                    sum(active_employee_job_grade_data_raw[15:21]), sum(active_employee_job_grade_data_raw[21:])], [
                    'T-技术序列', 'M-管理序列', 'P-专业序列', 'O-操作序列']  # 职级分布
            except:
                active_employee_job_grade_data = []
                active_employee_job_grade_xaxis = []
            viewDataList={
                "type": "active_employee_job_grade",
                "data": {
                    'title': '职级分布',
                    'data': active_employee_job_grade_data,
                    'xAxis': active_employee_job_grade_xaxis
                }
            }
            response_data['data']['tableList']=response_data['data']['tableList'][(currentPage - 1) * pageSize:currentPage * pageSize]
            response_data['data']['viewDataList'] =viewDataList
            response_data['data']['sumLabelsList'] = sum_labels
            return JsonResponse(response_data)

    def put(self, request):  # 下载   #单个传序号
        reset = EmployeeDataReport()
        response_data = self.get_response_data(request)['data']['tableList']
        response_data = reset.active_employee_job_grade_down(request,response_data)
        return JsonResponse(response_data)

    def get_response_data(self, request):
        reset = EmployeeDataReport()
        try:
            info = json.loads(request.body)
        except:
            info = {}
        params = {
            'search_date': info.get('search_date',''),
            'job_sequence': info.get('job_sequence',''),
            'job_class': info.get('job_class',''),
            'department_id': info.get('department_id',''),
            'job_grade':  info.get('job_grade',''),
        }
        if len(params['department_id']) == 0:
            params['department_id'] = request.user_department_employee
        response_data = reset.active_employee_job_grade(**params)
        return response_data

class Active_Employee_Seniority_RecordView(GenericAPIView):     #司龄分布
    def post(self, request,flag=0):  # 查询
        response_data = self.get_response_data(request)
        if flag:
            save_list_data_to_redis('Active_Employee_Seniority_RecordView_POST_' + str(request.check_token)+'_default',
                                    response_data['data']['tableList'])  # 存储数据到redis中
        else:
            currentPage = json.loads(request.body).get('currentPage')
            pageSize = json.loads(request.body).get('pageSize')

            columnList_result = [d for d in response_data['data']['columnList'] if d.get('value') == '在职人员司龄人数分布'][0]['children']
            sum_labels = [d['label'] for d in columnList_result][:-1]
            save_list_data_to_redis('Active_Employee_Seniority_RecordView_POST_'+str(request.check_token), response_data['data']['tableList'])#存储数据到redis中
            try:
                active_employee_seniority_data, active_employee_seniority_xaxis = retrieve_and_sum_redis_data('Active_Employee_Seniority_RecordView_POST_'+str(request.check_token), ['0-1', '1-3', '3-6', '6-12', '12-24', '24-60', '60'], ['0-1月', '1-3月', '3-6月', '6-12月', '1-2年', '2-5年', '5年以上']) #司龄分布
                data=[{"name": active_employee_seniority_xaxis[i], "value": active_employee_seniority_data[i]}  for i in range(len(active_employee_seniority_xaxis))]
            except:
                data=[]
            viewDataList={
                    "type": "active_employee_seniority",
                    "data": {
                        'title': '司龄分布',
                        'data':data
                    }
            }
            response_data['data']['tableList']=response_data['data']['tableList'][(currentPage - 1) * pageSize:currentPage * pageSize]
            response_data['data']['viewDataList'] = viewDataList
            response_data['data']['sumLabelsList'] = sum_labels

            return JsonResponse(response_data)

    def put(self, request):  # 下载   #单个传序号
        reset = EmployeeDataReport()
        response_data = self.get_response_data(request)['data']['tableList']
        response_data = reset.active_employee_seniority_down(request,response_data)
        return JsonResponse(response_data)

    def get_response_data(self, request):
        reset = EmployeeDataReport()
        try:
            info = json.loads(request.body)
        except:
            info = {}
        params = {
            'search_date': info.get('search_date', ''),
            'job_sequence': info.get('job_sequence', ''),
            'job_class': info.get('job_class', ''),
            'department_id': info.get('department_id', ''),
            'job_grade': info.get('job_grade', ''),
            'dl_idl': info.get('dl_idl', ''),
        }

        if len(params['department_id']) == 0:
            params['department_id'] = request.user_department_employee
        response_data = reset.active_employee_seniority(**params)
        return response_data

class Active_Employee_Age_RecordView(GenericAPIView):     #年龄分布
    def post(self, request,flag=0):  # 查询
        response_data = self.get_response_data(request)
        if flag:
            save_list_data_to_redis('Active_Employee_Age_RecordView_POST_' + str(request.check_token)+'_default',
                                    response_data['data']['tableList'])  # 存储数据到redis中
        else:
            currentPage = json.loads(request.body).get('currentPage')
            pageSize = json.loads(request.body).get('pageSize')
            columnList_result = [d for d in response_data['data']['columnList'] if d.get('value') == '在职人员年龄人数分布'][0]['children']
            sum_labels = [d['label'] for d in columnList_result][:-1]
            save_list_data_to_redis('Active_Employee_Age_RecordView_POST_'+str(request.check_token),response_data['data']['tableList'])  # 存储数据到redis中

            try:
                active_employee_age_data, active_employee_age_xaxis = retrieve_and_sum_redis_data(
                    'Active_Employee_Age_RecordView_POST_' + str(request.check_token),
                    ['20', '21-25', '26-30', '31-35', '36-40', '40', 'other'],
                    ['<=20岁', '21-25岁', '26-30岁', '31-35岁', '36-40岁', '>40岁', '其他'])  # 年龄分布
                data = [{"name": active_employee_age_xaxis[i], "value": active_employee_age_data[i]} for i in
                        range(len(active_employee_age_xaxis))]
            except:
                data = []
            viewDataList={
                "type": "active_employee_age",
                "data": {
                    'title': '年龄分布',
                    'data': data,
                }
            }
            response_data['data']['tableList']=response_data['data']['tableList'][(currentPage - 1) * pageSize:currentPage * pageSize]
            response_data['data']['viewDataList'] = viewDataList
            response_data['data']['sumLabelsList'] = sum_labels
            return JsonResponse(response_data)

    def put(self, request):  # 下载   #单个传序号
        reset = EmployeeDataReport()
        response_data = self.get_response_data(request)['data']['tableList']
        response_data = reset.active_employee_age_down(request,response_data)
        return JsonResponse(response_data)

    def get_response_data(self, request):
        reset = EmployeeDataReport()
        try:
            info = json.loads(request.body)
        except:
            info = {}
        params = {
            'search_date': info.get('search_date', ''),
            'job_sequence': info.get('job_sequence', ''),
            'job_class': info.get('job_class', ''),
            'department_id': info.get('department_id', ''),
            'job_grade': info.get('job_grade', ''),
            'dl_idl': info.get('dl_idl', ''),
        }
        if len(params['department_id']) == 0:
            params['department_id'] = request.user_department_employee
        response_data = reset.active_employee_age(**params)
        return response_data

class Active_Employee_Education_RecordView(GenericAPIView):     #学历分布
    def post(self, request,flag=0):  # 查询
        response_data = self.get_response_data(request)
        if flag:
            save_list_data_to_redis('Active_Employee_Education_RecordView_POST_' + str(request.check_token)+'_default',
                                    response_data['data']['tableList'])  # 存储数据到redis中
        else:
            currentPage = json.loads(request.body).get('currentPage')
            pageSize = json.loads(request.body).get('pageSize')

            columnList_result = [d for d in response_data['data']['columnList'] if d.get('value') == '在职人员学历人数分布'][0]['children']
            sum_labels = [d['label'] for d in columnList_result]
            save_list_data_to_redis(
                'Active_Employee_Education_RecordView_POST_' + str(request.check_token) ,response_data['data']['tableList'])  # 存储数据到redis中
            try:
                active_employee_education_data, active_employee_education_xaxis = retrieve_and_sum_redis_data(
                    'Active_Employee_Education_RecordView_POST_' + str(request.check_token),
                    ['6', '5', '4', '3', '2', '1', 'other'],
                    ['博士级及以上', '硕士', '本科', '大专', '中专', '高中及以上', '其他'])  # 学历分布
                data = [{"name": active_employee_education_xaxis[i], "value": active_employee_education_data[i]} for i in
                        range(len(active_employee_education_xaxis))]
            except:
                data = []
            viewDataList={
                    "type": "active_employee_education",
                    "data": {
                        'title': '学历分布',
                        'data': data,
                    }
                }
            response_data['data']['tableList']=response_data['data']['tableList'][(currentPage - 1) * pageSize:currentPage * pageSize]
            response_data['data']['viewDataList'] =viewDataList
            response_data['data']['sumLabelsList'] = sum_labels
            return JsonResponse(response_data)

    def put(self, request):  # 下载   #单个传序号
        reset = EmployeeDataReport()
        response_data = self.get_response_data(request)['data']['tableList']
        response_data = reset.active_employee_education_down(request,response_data)
        return JsonResponse(response_data)

    def get_response_data(self, request):
        reset = EmployeeDataReport()
        try:
            info = json.loads(request.body)
        except:
            info = {}
        params = {
            'search_date': info.get('search_date', ''),
            'job_sequence': info.get('job_sequence', ''),
            'job_class': info.get('job_class', ''),
            'department_id': info.get('department_id', ''),
            'job_grade': info.get('job_grade', ''),
            'dl_idl': info.get('dl_idl', ''),
        }
        if len(params['department_id']) == 0:
            params['department_id'] = request.user_department_employee
        response_data = reset.active_employee_education(**params)
        return response_data

class Active_Employee_Nationality_RecordView(GenericAPIView):     #国籍分布
    def post(self, request,flag=0):  # 查询
        response_data = self.get_response_data(request,flag)
        if flag:
            save_list_data_to_redis('Active_Employee_Nationality_RecordView_POST_' + str(request.check_token)+'_default',
                                    response_data['data']['tableList'])  # 存储数据到redis中
        else:
            currentPage = json.loads(request.body).get('currentPage')
            pageSize = json.loads(request.body).get('pageSize')

            columnList_result = [d for d in response_data['data']['columnList'] if d.get('value') == '在职人员国籍人数分布'][0]['children']
            sum_labels = [d['label'] for d in columnList_result]
            save_list_data_to_redis('Active_Employee_Nationality_RecordView_POST_'+str(request.check_token),response_data['data']['tableList'])  # 存储数据到redis中
            try:
                active_employee_nationality_name_data = get_list_data_from_redis(
                    "Active_Employee_Nationality_Name_POST_" + str(request.check_token))  # 国家名
                active_employee_nationality_data, active_employee_nationality_xaxis = retrieve_and_sum_redis_data(
                    'Active_Employee_Nationality_RecordView_POST_' + str(request.check_token),
                    active_employee_nationality_name_data, active_employee_nationality_name_data)  # 国籍分布
                data = [{"name": active_employee_nationality_xaxis[i], "value": active_employee_nationality_data[i]} for i
                        in range(len(active_employee_nationality_xaxis))]
            except:
                data = []

            '''
            from mtranslate import translate
            # 原始中文列表
            chinese_list = ['中国', '克罗地亚', '哥伦比亚', '墨西哥', '巴西', '法国', '泰国', '美国', '菲律宾', '西班牙', '越南', '马来西亚', '其他']
            # 转换为英文列表
            english_list = [translate(chinese, 'en') for chinese in chinese_list]
            # 打印结果
            print(english_list)

            '''

            # 创建一个中文到英文的映射字典
            translation_dict = {
                '中国': 'China',
                '克罗地亚': 'Croatia',
                '哥伦比亚': 'Colombia',
                '墨西哥': 'Mexico',
                '巴西': 'Brazil',
                '法国': 'France',
                '泰国': 'Thailand',
                '美国': 'United States',
                '菲律宾': 'Philippines',
                '西班牙': 'Spain',
                '越南': 'Vietnam',
                '马来西亚': 'Malaysia',
                '其他': 'Other'
            }


            chinese_list = [d['name'] for d in data]# 原始中文列表
            english_list = [translation_dict.get(chinese, chinese) for chinese in chinese_list]# 转换为英文列表
            # 使用 zip 函数将两个列表的元素一一对应
            zipped_lists = zip(english_list, chinese_list)
            result_dict = {chinese: english for chinese, english in zipped_lists}#构建字典
            viewDataList= {
                    "type": "active_employee_nationality",
                    "data": {
                        'title': '国籍分布',
                        'data': data,
                        'nameMap':result_dict
                    }
                }
            response_data['data']['tableList']=response_data['data']['tableList'][(currentPage - 1) * pageSize:currentPage * pageSize]
            response_data['data']['viewDataList'] = viewDataList
            response_data['data']['sumLabelsList'] = sum_labels
            return JsonResponse(response_data)

    def put(self, request):  # 下载   #单个传序号
        reset = EmployeeDataReport()
        response_data = self.get_response_data(request)['data']['tableList']
        table_header_data=self.get_response_data(request)['data']['columnList']
        response_data = reset.active_employee_nationality_down(request,response_data,table_header_data)
        return JsonResponse(response_data)

    def get_response_data(self, request,flag=0):
        reset = EmployeeDataReport()
        try:
            info = json.loads(request.body)
        except:
            info={}
        params = {
            'search_date': info.get('search_date', ''),
            'job_sequence': info.get('job_sequence', ''),
            'job_class': info.get('job_class', ''),
            'department_id': info.get('department_id', ''),
            'job_grade': info.get('job_grade', ''),
            'check_token':request.check_token,
            'flag':flag
        }
        if len(params['department_id']) == 0:
            params['department_id'] = request.user_department_employee
        response_data = reset.active_employee_nationality(**params)
        return response_data

class Active_Employee_Sex_RecordView(GenericAPIView):     #性别分布
    def post(self, request,flag=0):  # 查询
        response_data = self.get_response_data(request)
        if flag:
            save_list_data_to_redis('Active_Employee_Sex_RecordView_POST_' + str(request.check_token) + '_default',response_data['data']['tableList'])  # 存储数据到redis中
        else:
            currentPage = json.loads(request.body).get('currentPage',1)
            pageSize = json.loads(request.body).get('pageSize',25)
            columnList_result = [d for d in response_data['data']['columnList'] if d.get('value') == '在职人员性别人数分布'][0]['children']
            sum_labels = [d['label'] for d in columnList_result]
            save_list_data_to_redis('Active_Employee_Sex_RecordView_POST_'+str(request.check_token),response_data['data']['tableList'])  # 存储数据到redis中
            try:
                active_employee_sex_data, active_employee_sex_xaxis = retrieve_and_sum_redis_data(
                    'Active_Employee_Sex_RecordView_POST_' + str(request.check_token), ['man', 'woman','other'],
                    ['男', '女','其他'])  # 性别分布
                data = [{"name": active_employee_sex_xaxis[i], "value": active_employee_sex_data[i]} for i in
                        range(len(active_employee_sex_xaxis))]
            except:
                data = []
            viewDataList={
                    "type": "active_employee_sex",
                    "data": {
                        'title': '性别分布',
                        "data": data
                    }
                }
            response_data['data']['tableList']=response_data['data']['tableList'][(currentPage - 1) * pageSize:currentPage * pageSize]
            response_data['data']['viewDataList'] = viewDataList
            response_data['data']['sumLabelsList'] = sum_labels
            return JsonResponse(response_data)

    def put(self, request):  # 下载   #单个传序号
        reset = EmployeeDataReport()
        response_data = self.get_response_data(request)['data']['tableList']
        response_data = reset.active_employee_sex_down(request,response_data)
        return JsonResponse(response_data)

    def get_response_data(self, request):
        reset = EmployeeDataReport()
        try:
            info = json.loads(request.body)
        except:
            info={}
        params = {
            'search_date': info.get('search_date',''),
            'job_sequence': info.get('job_sequence',''),
            'job_class': info.get('job_class',''),
            'department_id': info.get('department_id',''),
            'job_grade':info.get('job_grade',''),
        }
        if len(params['department_id']) == 0:
            params['department_id'] = request.user_department_employee
        response_data = reset.active_employee_sex(**params)
        return response_data

class Active_Employee_Promotion_RecordView(GenericAPIView):     #晋升情况
    def post(self, request,flag=0):  # 查询
        response_data = self.get_response_data(request)
        if flag:
            save_list_data_to_redis('Active_Employee_Promotion_RecordView_POST_' + str(request.check_token)+'_default',
                                    response_data['data']['tableList'])  # 存储数据到redis中
        else:
            currentPage = json.loads(request.body).get('currentPage')
            pageSize = json.loads(request.body).get('pageSize')
            columnList_result = [d for d in response_data['data']['columnList'] if d.get('value') == '晋升/晋级'][0]['children']+[d for d in response_data['data']['columnList'] if d.get('value') == '降职/降级'][0]['children']
            sum_labels = [d['label'] for d in columnList_result]

            save_list_data_to_redis('Active_Employee_Promotion_RecordView_POST_'+str(request.check_token),response_data['data']['tableList'])  # 存储数据到redis中
            try:
                active_employee_promotion_data, active_employee_promotion_xaxis = retrieve_and_sum_redis_data(
                    'Active_Employee_Promotion_RecordView_POST_' + str(request.check_token),
                    ['demotion', 'downgrade', 'promote', 'rise'], ['降职', '降级', '晋升', '晋级'])  # 晋升情况
                active_employee_promotion_data[:2] = [-num for num in active_employee_promotion_data[:2]]
            except:
                active_employee_promotion_data = []
                active_employee_promotion_xaxis = []
            viewDataList={
                "type": "active_employee_promotion",
                "data": {
                    'title': '晋升情况',
                    'data': active_employee_promotion_data,
                    'xAxis': active_employee_promotion_xaxis
                }
            }
            response_data['data']['tableList']=response_data['data']['tableList'][(currentPage - 1) * pageSize:currentPage * pageSize]
            response_data['data']['viewDataList'] = viewDataList
            response_data['data']['sumLabelsList'] = sum_labels
            return JsonResponse(response_data)

    def put(self, request):  # 下载   #单个传序号
        reset = EmployeeDataReport()
        response_data = self.get_response_data(request)['data']['tableList']
        response_data = reset.active_employee_promotion_down(request,response_data)
        return JsonResponse(response_data)
    def get_response_data(self, request):
        reset = EmployeeDataReport()
        try:
            info = json.loads(request.body)
        except:
            info = {}
        params = {
            'begin_date': info.get('begin_date', ''),#调职开始日期
            'end_date': info.get('end_date', ''),#调制结束日期
            'job_sequence': info.get('job_sequence', ''),
            'job_class': info.get('job_class', ''),
            'department_id': info.get('department_id', ''),
            'new_job_grade': info.get('new_job_grade', ''),#新职级（职系）
            'old_job_grade': info.get('old_job_grade', ''),# 旧职级（职系）
        }
        if len(params['department_id']) == 0:
            params['department_id'] = request.user_department_employee
        response_data = reset.active_employee_promotion(**params)
        return response_data

class Report_Visualization_RecordView(GenericAPIView):
    def post(self, request):  # 查询
        reset = EmployeeDataReport()
        response_data = reset.report_visualization(request)
        return JsonResponse(response_data)
class Report_Save_RecordView(GenericAPIView):
    def get(self, request):  # 查询
        user_obj_list=list(AdminUser.objects.filter(Q(user_menu__id__in=list(range(127,140))) | Q(is_superuser=1),is_used=1).values('id','user_menu__id','is_superuser'))  #管理员没加
        from collections import defaultdict
        merged_data = defaultdict(list)
        for d in user_obj_list:
            merged_data[str(d['id'])+'__'+str(d['is_superuser'])].append(d['user_menu__id'])
        merged_data2=dict(merged_data)
        for key, value in merged_data2.items():
            key_1,key_2=key.split('__')
            user_id=int(key_1)
            is_super=eval(key_2)
            user_menu_list=value
            user_department_list_employee = AdminUser.objects.filter(pk=user_id).values("user_department_employee")
            user_department_employee = [item['user_department_employee'] for item in user_department_list_employee]
            first_father=list(HrDepartment.objects.filter(department_status=1,id__in=user_department_employee).values_list('department_parent_id',flat=True))
            user_department_employee+=first_father
            second_father=list(HrDepartment.objects.filter(department_status=1,id__in=user_department_employee).values_list('department_parent_id',flat=True))
            user_department_employee += second_father
            third_father = list(HrDepartment.objects.filter(department_status=1, id__in=user_department_employee).values_list('department_parent_id', flat=True))
            user_department_employee += third_father
            overdue_dept_id=list(HrDepartment.objects.filter(Q(department_expiry_date__isnull=False) | Q(department_expiry_date__lte=datetime.now())).values_list('id',flat=True))#过期的部门
            user_department_employee = [x for x in user_department_employee if x not in [0, 2, None,999999]+overdue_dept_id]  # 排除0和2的
            user_department_employee_list=list(set(user_department_employee))

            request.user_department_employee = user_department_employee_list
            request.check_token=user_id
            if 131 in user_menu_list or is_super :#司龄分布
                active_employee_seniority_view = Active_Employee_Seniority_RecordView()
                active_employee_seniority_view.post(request,flag=1)
            if 132 in user_menu_list or is_super:#年龄分布
                active_employee_age_view = Active_Employee_Age_RecordView()
                active_employee_age_view.post(request, flag=1)
            if 133 in user_menu_list or is_super:#学历分布
                active_employee_education_view = Active_Employee_Education_RecordView()
                active_employee_education_view.post(request, flag=1)
            if 134 in user_menu_list or is_super:#国籍分布
                active_employee_nationality_view = Active_Employee_Nationality_RecordView()
                active_employee_nationality_view.post(request, flag=1)
            if 135 in user_menu_list or is_super:#性别分布
                active_employee_sex_view = Active_Employee_Sex_RecordView()
                active_employee_sex_view.post(request, flag=1)
            if 136 in user_menu_list or is_super:#晋升情况
                active_employee_promotion_view = Active_Employee_Promotion_RecordView()
                active_employee_promotion_view.post(request, flag=1)
            if 137 in user_menu_list or is_super:#职级分布
                active_employee_job_grade_view = Active_Employee_Job_Grade_RecordView()
                active_employee_job_grade_view.post(request, flag=1)
            if 138 in user_menu_list or is_super:#离职率分析-离职原因
                departure_employee_reason_view = Departure_Employee_Reason_RecordView()
                departure_employee_reason_view.post(request, flag=1)
            if 139 in user_menu_list or is_super:#离职率分析-司龄原因
                departure_employee_seniority_view = Departure_Employee_Seniority_RecordView()
                departure_employee_seniority_view.post(request, flag=1)
        print({'msg':'存储成功',"code": status.HTTP_200_OK,})
        return JsonResponse({'msg':'存储成功',"code": status.HTTP_200_OK,})



class Employee_Profile_Slices(GenericAPIView):  # 员工档案切片
    def post(self, request):  # 查询
        # currentPage = json.loads(request.body).get('currentPage')
        # pageSize = json.loads(request.body).get('pageSize')
        response_data = self.get_response_data(request)
        # response_data['data']['tableList']=response_data['data']['tableList'][(currentPage - 1) * pageSize:currentPage * pageSize]
        # return JsonResponse(response_data)
        return JsonResponse({
            'code': 200,
        })

    def get_response_data(self, request):
        reset = EmployeeDataReport()
        info = json.loads(request.body)
        params = {
            'slice_begin_date':info['slice_begin_date'],
            'slice_end_date': info['slice_end_date'],
            'slice_type':info['slice_type'],

            # 'search_date': info['search_date'],
            # 'job_sequence': info['job_sequence'],
            # 'job_class': info['job_class'],
            # 'department_id': info['department_id'],
            # 'job_grade': info['job_grade'],
        }
        # if len(params['department_id']) == 0:
        #     params['department_id'] = request.user_department_employee
        print(info['slice_begin_date'],type(info['slice_begin_date']))
        response_data = reset.employee_profile_slices(**params)   #本期的数据





        return response_data








def get_employee_options(request):
    if request.check_token is not None:
        job_grade_list = list(
            HrJobGrade.objects.filter(job_grade_status=True).exclude(id=999999).values('id', 'job_grade_name'))  # 职级
        job_class_list = list(
            HrJobClass.objects.filter(job_class_status=True).exclude(id=999999).values('id', 'job_class_name'))  # 职等
        dim_reason_list = list(
            HrDimissionReason.objects.filter(dim_reason_status=True).exclude(id=999999).values('id','dim_reason_name'))  # 离职原因
        dim_type_list=list(
            HrDimissionType.objects.filter().exclude(id=999999).values('id','dim_type_name'))  # 离职类型
        job_sequence_list = list(
            HrJobSequence.objects.filter(sequence_status=True).exclude(id=999999).values('id', 'sequence_name'))  # 职级序列
        return_data = {
            'data': {
                'job_grade_list': [
                    {"value": item["id"], "label": item["job_grade_name"]}
                    for item in job_grade_list
                ],
                'job_class_list': [
                    {"value": item["id"], "label": item["job_class_name"]}
                    for item in job_class_list
                ],
                'dl_idl_sal': [
                    {"value": 'DL', "label": 'DL'}, {"value": 'IDL', "label": 'IDL'}, {"value": 'SAL', "label": 'SAL'}
                ],
                'dim_reason_list': [
                    {"value": item["id"], "label": item["dim_reason_name"]}
                    for item in dim_reason_list
                ],
                'dim_type_list': [
                    {"value": item["id"], "label": item["dim_type_name"]}
                    for item in dim_type_list
                ],
                'job_sequence_list': [
                    {"value": item["id"], "label": item["sequence_name"]}
                    for item in job_sequence_list
                ],
            },
            "code": status.HTTP_200_OK,
            "msg": "下拉菜单返回成功",
            'hidden': True,
        }

    else:
        return_data = {
            "code": status.HTTP_403_FORBIDDEN,
            "msg": "没有权限访问",
            'hidden': False
        }
    return JsonResponse(return_data)


