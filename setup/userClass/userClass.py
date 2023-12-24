# # -*- coding: utf-8 -*-
# # @Time    : 2023/5/22 8:27
# # @Author  : zhuang
# # @Site    :
# # @File    : userClass.py
# # @Software: PyCharm
# import json
# import time
# from datetime import datetime
# from django.db.models import Q
# from rest_framework.response import Response
# from auther.models import AdminUser
# from ..serializers import *
# from general.models import center_base
# from setup.models import *
# from controller.controller import upload_file
#
#
# class userMgmt:
#     def __init__(self, request, meth):
#         self.now = None
#         self.operator = None
#         self.return_data = None
#         self.request = request
#         self.token = request.check_token
#         self.meth = meth
#         self.field_name = []
#         self.method = {
#             "add_user": self.add_user,
#             "update_user": self.update_user,
#             "get_list": self.get_list,
#             "delete_user": self.delete_user,
#         }
#
#     def center_meth(self):
#         if self.token is None:
#             self.return_data = {
#                 "code": 400,
#                 "msg": "无任何权限响应"
#             }
#             return Response(self.return_data)
#         for i in AdminUser._meta.fields:
#             self.field_name.append(i.name)
#         self.operator = AdminUser.objects.filter(pk=self.token)[0]
#         self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.method[self.meth]()
#         return Response(self.return_data)
#
#     def add_user(self):
#         print("POST:", self.request.POST)
#         info = self.request.POST['createData']
#
#         info = json.loads(info)
#         info['creator_id'] = self.token
#         info['modifier_id'] = self.token
#         print(self.token)
#         try:
#             obj = AdminUser.objects.get(username=info['username'])
#             self.return_data = {
#                 'code': 404,
#                 "message": "用户名重复，请重新选择"
#             }
#         except AdminUser.DoesNotExist:
#             obj = AdminUserAddSerializers(data=info)
#             if obj.is_valid():
#                 obj.save()
#             else:
#                 error = obj.errors
#                 print(error)
#                 self.return_data = {
#                     'code': 401,
#                     "message": error
#                 }
#
#     def update_user(self):
#         print("patch", self.request.body)
#         info = json.loads(self.request.body)
#         info['modify_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         info['modifier_id'] = self.token
#         print(info)
#         pk = AdminUser.objects.get(pk=info["id"])
#         obj = AdminUserAddSerializers(instance=pk, data=info)
#         if obj.is_valid():
#             obj.save()
#         else:
#             error = obj.errors
#             print(error)
#             self.return_data = {
#                 'code': 401,
#                 "message": error
#             }
#
#     def get_list(self):
#         columnList = [
#             {"value": "序号", "label": "index", "width": "60"},
#             {"value": "用户名", "label": "username", "width": "90"},
#             {"value": "登录名", "label": "user", "width": "60"},
#             {"value": "是否为管理员", "label": "is_superuser", "width": "180"},
#             {"value": "备注", "label": "user_remark", "width": ""},
#         ]
#         tableList = [
#         ]
#         base_data = []
#         nav_data = []
#         args = ()
#         searchName = self.request.GET.get("searchName", None)
#         currentPage = eval(self.request.GET.get("currentPage", None)) if self.request.GET.get("currentPage",
#                                                                                               None) != "" else 1
#         pageSize = eval(self.request.GET.get("pageSize", None)) if self.request.GET.get("pageSize", None) != "" else 25
#         if searchName is not None and searchName != "":
#             args = (Q(username__contains=searchName) | Q(user__contains=searchName))
#         user_obj = AdminUser.objects.filter(is_used=1, *args)
#         obj = AdminUserGetSerializers(instance=user_obj[(currentPage - 1) * pageSize:currentPage * pageSize],
#                                       many=True).data
#         index = (currentPage - 1) * pageSize + 1
#         for i in obj:
#             data = dict(i)
#             data['index'] = index
#             tableList.append(data)
#             index += 1
#         base_obj = center_base.objects.filter(status=1).values()
#         base_data = [{"id": i['id'], "name": i['name'], } for i in base_obj]
#
#         nav_obj = AdminNavMenuList.objects.filter(nav_type=1, nav_parent_id=None).values()
#         nav_data = [{"id": i['id'], "label": i['nav_name']} for i in nav_obj]
#         for nav in nav_data:
#             parent_data = AdminNavMenuList.objects.filter(nav_type=1, nav_parent_id=nav['id']).values()
#             nav['children'] = [{"id": i['id'], "label": i['nav_name']} for i in parent_data]
#
#         self.return_data = {
#             "code": 200,
#             "msg": "信息返回成功",
#             "data": {
#                 'totalNumber': user_obj.count(),
#                 'tableList': tableList,
#                 'columnList': columnList,
#                 "navList": nav_data,
#                 "baseList": base_data
#             },
#         }
#
#     def delete_user(self):
#         info = json.loads(self.request.body)
#         idList = info['idList']
#         for i in idList:
#             print(i)
#             AdminUser.objects.filter(pk=i).update(is_used=False, modifier_id=self.token, modify_time = self.now)
#         self.return_data = {
#             "code": 200,
#             "msg": "删除成功"
#         }
#
#
# class picMgmt:
#     def __init__(self, request, meth):
#         self.return_data = None
#         self.request = request
#         self.token = request.check_token
#         self.meth = meth
#         self.operator = ""
#         self.field_name = []
#         self.method = {
#             "add_pic": self.add_pic,
#             "delete_pic": self.delete_pic,
#             "get_pic": self.get_pic,
#         }
#         self.now = ""
#
#     def center_meth(self):
#         if self.token is None:
#             self.return_data = {
#                 "code": 400,
#                 "msg": "无任何权限响应"
#             }
#             return Response(self.return_data)
#         self.operator = AdminUser.objects.filter(pk=self.token)[0]
#         self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.method[self.meth]()
#         return Response(self.return_data)
#
#     def add_pic(self):
#         searchTime = datetime.now().strftime("%Y-%m-%d")
#         files = self.request.FILES.getlist("file", None)
#         if files is None or len(files) <= 0:
#             self.return_data = {
#                 "code": 400,
#                 "msg": "文件为空"
#             }
#             return
#         for file in files:
#             fileName = searchTime + "_" + "".join(list(str(time.time()))[0:10]) + "_" + file.name
#             fileName = upload_file(file, "slides", "", fileName)
#             kwargs = {
#                 "url": "static/" + "slides/" + searchTime + "/" + fileName,
#                 "creator": self.operator,
#                 "modifier": self.operator,
#                 "name": fileName
#             }
#             PicManage.objects.create(**kwargs)
#         self.return_data = {
#             "code": 200,
#             "msg": "保存成功"
#         }
#
#     def delete_pic(self):
#         id = json.loads(self.request.body)['file_id']
#         PicManage.objects.filter(pk=id).update(pic_status=0, modify_time=self.now, modifier=self.operator)
#         self.return_data = {
#             "code": 200,
#             "msg": "删除成功"
#         }
#
#
#     def get_pic(self):
#         obj = PicManage.objects.filter(pic_status=True).order_by('-create_time')
#         serializer = PicManageviewsSerializers(instance=obj, many=True)
#         tableList = []
#         for i in serializer.data:
#             tableList.append(dict(i))
#         self.return_data = {
#             "code": 200,
#             "msg": "信息返回成功",
#             "data": {
#                 'tableList': tableList,
#             },
#         }
# -*- coding: utf-8 -*-
# @Time    : 2023/5/22 8:27
# @Author  : zhuang
# @Site    :
# @File    : userClass.py
# @Software: PyCharm
import json
import time
from datetime import datetime
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN

from auther.models import AdminUser
from employee.models import HrJobRank, HrDepartment
from hikCanteen.models import JobRank
from ..serializers import *
from general.models import center_base
from setup.models import *
from controller.controller import upload_file
from volumeContracts.models import *


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

class userMgmt:
    def __init__(self, request, meth):
        self.now = None
        self.operator = None
        self.return_data = None
        self.request = request
        self.token = request.check_token
        self.meth = meth
        self.field_name = []
        self.method = {
            "add_user": self.add_user,
            "update_user": self.update_user,
            "get_list": self.get_list,
            "delete_user": self.delete_user,
        }

    def center_meth(self):
        if self.token is None:
            self.return_data = {
                "code": 403,
                "msg": "无任何权限响应"
            }
            return Response(self.return_data)
        for i in AdminUser._meta.fields:
            self.field_name.append(i.name)
        self.operator = AdminUser.objects.filter(pk=self.token)[0]
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.method[self.meth]()
        return Response(self.return_data)

    def add_user(self):
        info = self.request.POST['createData']
        info = json.loads(info)
        info['creator_id'] = self.token
        info['modifier_id'] = self.token

        try:
            obj = AdminUser.objects.get(username=info['username'])
            self.return_data = {
                'code': 404,
                "msg": "用户名重复，请重新选择"
            }
        except AdminUser.DoesNotExist:
            obj = AdminUserAddSerializers(data=info)
            if obj.is_valid():
                obj.save()
                self.return_data = {
                    'code': 200,
                    "msg": "用户新增成功"
                }
            else:
                error = obj.errors
                self.return_data = {
                    'code': 401,
                    "msg": error
                }
        # print(self.return_data)
    def update_user(self):
        info = json.loads(self.request.body)
        # print(info)
        info['modify_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        info['modifier_id'] = self.token
        pk = AdminUser.objects.get(pk=info["id"])
        obj = AdminUserAddSerializers(instance=pk, data=info)
        if obj.is_valid():
            obj.save()
            self.return_data = {
                'code': status.HTTP_200_OK,
                "msg": "修改成功"
            }
        else:
            error = obj.errors
            # print(error)
            self.return_data = {
                'code': 401,
                "msg": error
            }

    def get_list(self):
        print(self.request.GET)
        columnList = [
            {"value": "序号", "label": "index", "width": "60"},
            {"value": "用户名", "label": "username", "width": "120"},
            {"value": "登录名", "label": "user", "width": "120"},
            {"value": "是否为管理员", "label": "is_superuser", "width": "120"},
            {"value": "备注", "label": "user_remark", "width": ""},
        ]
        tableList = [
        ]
        base_data = []
        nav_data = []
        args = ()

        searchName = self.request.GET.get("searchName", None)
        # print("search",searchName)
        currentPage = eval(self.request.GET.get("currentPage", None)) if self.request.GET.get("currentPage",
                                                                                              None) != "" else 1
        pageSize = eval(self.request.GET.get("pageSize", None)) if self.request.GET.get("pageSize", None) != "" else 25
        if searchName is not None and searchName != "":
            args = (Q(username__contains=searchName) | Q(user__contains=searchName))
        # print(args)
        user_obj = AdminUser.objects.filter(Q(username__contains=searchName) | Q(user__contains=searchName), is_used=1)
        # user_obj = AdminUser.objects.filter(is_used=1,username__contains=searchName)
        # user_obj = AdminUser.objects.filter(is_used=1, *args)
        obj = AdminUserGetSerializers(instance=user_obj[(currentPage - 1) * pageSize:currentPage * pageSize],
                                      many=True).data
        index = (currentPage - 1) * pageSize + 1
        for i in obj:
            data = dict(i)
            data['index'] = index
            tableList.append(data)
            index += 1

        base_obj = center_base.objects.filter(status=1, base_parent_id=None).values()
        base_data = [{"id": i['id'], "label": i['name']} for i in base_obj]
        for nav in base_data:
            parent_data = center_base.objects.filter(status=1, base_parent_id=nav['id']).values()
            nav['children'] = [{"id": i['id'], "label": i['name']} for i in parent_data]

        nav_obj = AdminNavMenuList.objects.filter(nav_type=1, nav_parent_id=None).values()     #主路由
        nav_data = [{"id": i['id'], "label": i['nav_name']} for i in nav_obj]
        for nav in nav_data:
            parent_data = AdminNavMenuList.objects.filter(nav_type=1, nav_parent_id=nav['id']).values()
            nav['children'] = []
            for line in parent_data:
                nav_item = {
                    "id": line['id'],
                    "label": line['nav_name'],
                    "children": []
                }
                nav['children'].append(nav_item)
                field_data=AdminNavMenuList.objects.filter(nav_type=3, nav_parent_id=line['id']).values()   #字段
                for children in nav['children']:
                    for field in field_data:   #每个字段的详细数据
                        if children['id']==field['nav_parent_id']:
                            children['children'].append({"id": field['id'], "label": field['nav_name']})
                nav_child_data=AdminNavMenuList.objects.filter(nav_type=1, nav_parent_id=line['id']).values()   #路由
                for children in nav['children']:
                    for field in nav_child_data:   #每个字段的详细数据
                        if children['id']==field['nav_parent_id']:
                            children['children'].append({"id": field['id'], "label": field['nav_name']})





        jobRank_obj = ContractsJobrank.objects.filter(jobrank_status=True).values()
        jobRank_data = [{"id": i['id'], "label": i['jobrank_name']} for i in jobRank_obj]
        # for nav in jobRank_data:
        #     parent_data = ContractsJobrank.objects.filter(jobrank_status=True).values()
        #     nav['children'] = [{"id": i['id'], "label": i['nav_name']} for i in parent_data]

        # jobRank_hik_obj = JobRank.objects.filter(status=True,).values()
        # jobRank_hik_data = [{"id": i['id'], "label": i['JobRankName']} for i in jobRank_hik_obj]
        # print(nav_data)

        jobRank_employee_obj = HrJobRank.objects.filter(job_rank_status=True).exclude(id=999999).values()
        jobRank_employee_data = [{"id": i['id'], "label": i['job_rank_name']} for i in jobRank_employee_obj]
        # print(jobRank_employee_data)

        # hrbase_obj = HrDepartment.objects.filter(Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gte=datetime.now()),department_status=1, department_parent_id=1).values('id','department_name')
        # hrbase_data = [{"id": i['id'], "label": i['department_name']} for i in hrbase_obj]  # 一级部门
        # for first in hrbase_data:
        #     second_data = list(
        #         HrDepartment.objects.filter(Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gte=datetime.now()),department_status=1, department_parent_id=first['id']).values('id',
        #                                                                                                   'department_name'))
        #     # print('parent',second_data)
        #     first['children'] = []
        #     for second in second_data:
        #         second_item = {
        #             "id": second['id'],
        #             "label": second['department_name'],
        #             # "children": []
        #         }
        #         first['children'].append(second_item)  # 二级
        #         third_data = list(
        #             HrDepartment.objects.filter(Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gte=datetime.now()),department_status=1, department_parent_id=second['id']).values('id',
        #                                                                                                        'department_name'))
        #         second['children'] = []
        #         for third in third_data:
        #             third_item = {
        #                 "id": third['id'],
        #                 "label": third['department_name'],
        #             }
        #             second['children'].append(third_item)  # 二级
        #
        #             fourth_data = list(
        #                 HrDepartment.objects.filter(
        #                     Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gte=datetime.now()),
        #                     department_status=1, department_parent_id=third['id']).values('id',
        #                                                                                    'department_name'))
        #             third['children'] = []
        #             for fourth in fourth_data:
        #                 fourth_item = {
        #                     "id": fourth['id'],
        #                     "label": fourth['department_name'],
        #                 }
        #                 third['children'].append(fourth_item)  # 三级
        #
        # hrbase_boss_obj=HrDepartment.objects.filter(Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gte=datetime.now()),department_status=1, department_parent_id=0).values('id','department_name')
        # hrbase_data=[{"id": hrbase_boss_obj[0]['id'], "label": hrbase_boss_obj[0]['department_name'],"children":hrbase_data}]


        # def get_department_hierarchy(parent_id=0):
        #     departments = HrDepartment.objects.filter(
        #         Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gt=datetime.now()),
        #         department_parent_id=parent_id,department_status=1)
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
        # print(hrbase_data)



        departments = HrDepartment.objects.filter(
            ~Q(id=999999),
            Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gt=datetime.now()),
            department_status=1
         ).values('id', 'department_name', 'department_parent_id')

        hrbase_data = get_trees(departments,'id','department_parent_id')

        self.return_data = {
            "code": 200,
            "msg": "信息返回成功",
            "data": {
                'totalNumber': user_obj.count(),
                'tableList': tableList,
                'columnList': columnList,
                "navList": nav_data,
                "baseList": base_data,
                'jobRankList': jobRank_data,
                # 'jobRankHikList': jobRank_hik_data,
                "jobRankEmployeeList":jobRank_employee_data,
                'hrbaseList':hrbase_data
            },
        }


    def delete_user(self):
        # print("++++delete---------")
        info = json.loads(self.request.body)
        # print(info)
        idList = info['idList']
        for i in idList:
            # print(i)
            AdminUser.objects.filter(pk=i).update(is_used=False)
            # AdminUser.objects.filter(pk=i).update(is_used=False, modifier_id=self.token, modify_time=self.now)
        self.return_data = {
            "code": 200,
            "msg": "删除成功"
        }


class picMgmt:
    def __init__(self, request, meth):
        self.return_data = None
        self.request = request
        self.token = request.check_token
        self.meth = meth
        self.operator = ""
        self.field_name = []
        self.method = {
            "add_pic": self.add_pic,
            "delete_pic": self.delete_pic,
            "get_pic": self.get_pic,
        }
        self.now = ""

    def center_meth(self):
        if self.token is None:
            self.return_data = {
                "code": HTTP_403_FORBIDDEN,
                "msg": "无任何权限响应"
            }
            return Response(self.return_data)
        self.operator = AdminUser.objects.filter(pk=self.token)[0]
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.method[self.meth]()
        return Response(self.return_data)

    def add_pic(self):
        searchTime = datetime.now().strftime("%Y-%m-%d")
        files = self.request.FILES.getlist("file", None)
        if files is None or len(files) <= 0:
            self.return_data = {
                "code": 400,
                "msg": "文件为空"
            }
            return
        for file in files:
            fileName = searchTime + "_" + "".join(list(str(time.time()))[0:10]) + "_" + file.name
            fileName = upload_file(file, "slides", "", fileName)
            kwargs = {
                "url": "static/" + "slides/" + searchTime + "/" + fileName,
                "creator": self.operator,
                "modifier": self.operator,
                "name": fileName
            }
            PicManage.objects.create(**kwargs)
        self.return_data = {
            "code": 200,
            "msg": "保存成功"
        }

    def delete_pic(self):
        id = json.loads(self.request.body)['file_id']
        PicManage.objects.filter(pk=id).update(pic_status=0, modify_time=self.now, modifier=self.operator)
        self.return_data = {
            "code": 200,
            "msg": "删除成功"
        }

    def get_pic(self):
        obj = PicManage.objects.filter(pic_status=True).order_by('-create_time')
        serializer = PicManageviewsSerializers(instance=obj, many=True)
        tableList = []
        for i in serializer.data:
            tableList.append(dict(i))
        self.return_data = {
            "code": 200,
            "msg": "信息返回成功",
            "data": {
                'tableList': tableList,
            },
        }


class baseMgmt:
    def __init__(self, request, meth):
        self.return_data = None
        self.request = request
        self.token = request.check_token
        self.meth = meth
        self.operator = ""
        self.field_name = []
        self.method = {
            "add_base": self.add_base,
            "delete_base": self.delete_base,
            "get_base": self.get_base,
            "patch_base": self.patch_base
        }
        self.now = ""

    def center_meth(self):
        if self.token is None:
            self.return_data = {
                "code": HTTP_403_FORBIDDEN,
                "msg": "无任何权限响应"
            }
            return Response(self.return_data)
        self.operator = AdminUser.objects.filter(pk=self.token)[0]
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.method[self.meth]()
        return Response(self.return_data)

    def add_base(self):
        kwargs = {}
        info = self.request.POST['createData']
        dict = json.loads(info)
        baseName = dict.get('name')
        kwargs["name"] = baseName
        if dict.get('parentName') != "":
            kwargs['base_parent_id'] = dict.get('parentName')
        if center_base.objects.filter(name=baseName, status=True).count():
            self.return_data = {
                'code': 400,
                "msg": "用户名重复，请重新添加"
            }
        else:
            if len(str(baseName)) < 1:
                self.return_data = {
                    "code": 400,
                    "msg": "基地名不能为空,请重新添加"
                }
            add = center_base.objects.create(**kwargs)
            obj = AdminUser.objects.filter(is_superuser=1, is_used=1).values_list("id")
            if obj.exists():
                add_user_id = [i[0] for i in obj]
                for i in add_user_id:
                    AdminUser.objects.get(pk=i).user_base.add(add.id)
            self.return_data = {
                "code": 200,
                "msg": "新增成功"
            }
        return self.return_data

    def get_base(self):
        columnList = [
            {"value": "序号", "label": "index", "width": "60"},
            {"value": "一级部门", "label": "name", "width": ""},
            {"value": "二级部门", "label": "base_parent_id", "width": ""},
            # {"value": "备注", "label": "user_remark", "width": ""},
        ]
        tableList = []
        searchName = self.request.GET.get("searchName", None)
        currentPage = eval(self.request.GET.get("currentPage", None)) if self.request.GET.get("currentPage",
                                                                                              None) != "" else 1
        pageSize = eval(self.request.GET.get("pageSize", None)) if self.request.GET.get("pageSize", None) != "" else 25

        kwargs = {'status': True}
        beginDate = self.request.GET.get('beginDate', None)
        endDate = self.request.GET.get('endDate', None)

        if searchName == '' and beginDate == "" and endDate == "":  # 全查
            kwargs['status'] = True

        if searchName != '':
            kwargs['name'] = searchName
        if beginDate != "" and endDate != "":
            kwargs['create_time__gte'] = datetime(2001, 10, 29, 7, 17, 1, 177) if beginDate == None else beginDate
            kwargs['create_time__lte'] = datetime(2521, 10, 29, 7, 17, 1, 177) if endDate == None else endDate

        base_obj = center_base.objects.filter(**kwargs, base_parent_id=None).values("id", "name", "base_parent_id")

        index = (currentPage - 1) * pageSize + 1
        one_label_base = []
        for i in base_obj:
            data = dict(i)
            one_label_base.append({
                "id": i['id'],
                "name": i['name']
            })
            data['index'] = index
            tableList.append(data)
            index += 1
            obj = center_base.objects.filter(status=1, base_parent_id=data['id']).values("id", "name", "base_parent_id")
            for p in obj:
                data2 = dict(p)
                tableList.append({
                    "index": index,
                    "name": data['name'],
                    "base_parent_id": data2['name'],
                    "id": data2['id']
                })
                index += 1

        # all = center_base.objects.filter(status=True, base_parent_id=None).values('name', 'id')
        # for i in all:
        #     one_label_base.append({
        #         'id': i['id'],
        #         'name': i['name']
        #     })

        self.return_data = {
            "code": 200,
            "msg": "信息返回成功",
            "data": {
                'totalNumber': base_obj.count(),
                'tableList': tableList,
                'columnList': columnList,
                'oneLabelBase': one_label_base,

            },
        }
        return self.return_data

    def delete_base(self):
        info = json.loads(self.request.body)
        # print(info)
        idList = info['idList']
        for i in idList:
            center_base.objects.filter(id=i).update(status=False)
            center_base.objects.filter(base_parent_id=i).update(base_parent_id=None)
            # AdminUser.objects.filter(pk=i).update(is_used=False, modifier_id=self.token, modify_time=self.now)
        self.return_data = {
            "code": 200,
            "msg": "删除成功"
        }

    def patch_base(self):
        kwargs = {}
        info = json.loads(self.request.body)
        pk = info['id']

        if type(info['name']) == str:  # 都该
            kwargs = {
                'name': info['base_parent_id'],
                'base_parent_id':
                    center_base.objects.filter(status=True, base_parent_id=None, name=info['name']).values_list('id',
                                                                                                                flat=True)[
                        0]
            }
        else:
            # print("2", info)
            kwargs = {
                'name': info['base_parent_id'],
                'base_parent_id': info['name'],
            }

        # print(kwargs)
        try:
            center_base.objects.filter(pk=pk).update(**kwargs)
            self.return_data = {
                'code': 200,
                "msg": "修改成功"
            }
        except Exception as e:
            self.return_data = {
                'code': 401,
                "msg": "修改失败" + str(e)

            }

        # obj = BaseManageviewsSerializers(instance=pk, data=info)
        # if obj.is_valid():
        #     obj.save()
        # else:
        #     error = obj.errors
        #     # print(error)
        #     self.return_data = {
        #         'code': 401,
        #         "message": error
        #     }
