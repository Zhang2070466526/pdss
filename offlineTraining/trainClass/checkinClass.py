import json, os,arrow,openpyxl
import time

from django.db.models import Q,F
from rest_framework import status
from django.http import JsonResponse

from auther.models import AdminUser
from employee.models import HrEmployee, HrEmployeeFiles, HrDepartment, HrJobRank
from rest_framework.response import Response
from datetime import datetime, date

from django.utils import timezone
from offlineTraining.models import TrainingLecturer, TrainingLecturerLevel, TrainingContentType, TrainingContent, \
    TrainingSessions, TrainingCheckin
from pdss.settings import BASE_DIR
from employee import views
from offlineTraining.trainClass.contentClass import Content

class Checkin:
    def __init__(self, request,meth):
        self.request = request
        self.now = arrow.now()
        self.t1 = self.now.format('YYYY-MM-DD')
        self.t2 = self.now.timestamp()
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功'
        }
        self.meth = meth
        self.methods = {
            'get_training_checkin': self.get_training_checkin, #培训签到 查询
            'post_training_checkin':self.post_training_checkin,#培训签到 新增
            'down_training_checkin': self.down_training_checkin,  # 培训签到 下载
            'batch_training_checkin': self.batch_training_checkin,  # 培训签到 上传
            'del_training_checkin':self.del_training_checkin,#培训签到 删除
            'edit_training_checkin': self.edit_training_checkin,  # 培训签到 修改
        }

    def method_center(self):
        self.return_data = {'code': status.HTTP_403_FORBIDDEN, "msg": '没有权限访问'}
        if self.request.check_token is None:
            return JsonResponse(self.return_data)
        self.methods[self.meth]()
        return JsonResponse(self.return_data)

    # 获取信息列表
    def get_training_checkin(self):
        columnList = [{'label': 'index', 'value': '序号', 'width': 60},
                      {'label': 'checkin_people__employee_name_code', 'value': '填写人', 'width': ""},
                      {'label': 'checkin_people__employee_department__department_name', 'value': '所在部门',
                       'width': ""},
                      {'label': 'checkin_content__content_title', 'value': '参训课程', 'width': ""},
                      # {'label': 'checkin_time', 'value': '填写时间', 'width':""},
                      # {'label': 'checkin_user_type', 'value': '用户类型', 'width': ""},
                      {'label': 'checkin_content__content_duration', 'value': '培训时长', 'width': ""},
                      {'label': 'checkin_content__content_type__type_name', 'value': '培训类型', 'width': ""},
                      {'label': 'checkin_content__content_begin_date', 'value': '开始培训日期', 'width': ""},
                      {'label': 'checkin_content__content_end_date', 'value': '结束培训日期', 'width': ""},
                      # {'label': 'checkin_address', 'value': '您在那个会场集训', 'width':""},
                      {'label': 'checkin_remark', 'value': '备注', 'width': ""},
                      ]
        info = json.loads(self.request.body)

        params = {
            'beginDate': info['beginDate'],
            'endDate': info['endDate'],
            'searchName': info['searchName'],
            'department_id': info['baseNameId'],
            'currentPage': info['currentPage'],
            'pageSize': info['pageSize']
        }
        currentPage = params['currentPage'] if params['currentPage'] != "" else 1
        pageSize = params['pageSize'] if params['pageSize'] != "" else 25

        kwargs = {
            'checkin_people__employee_department__id__in': params['department_id'],
            'checkin_content__content_status': True,
        }
        if params['department_id'] == '':
            kwargs['checkin_people__employee_department__id__in'] = self.request.user_department_employee

        if params['beginDate'] != "" and params['endDate'] != "":
            kwargs['checkin_content__content_begin_date__gte'] = datetime(1901, 10, 29, 7, 17, 1, 177) if params[
                                                                                                              'beginDate'] is None or len(
                params['beginDate']) == 0 else params['beginDate']
            kwargs['checkin_content__content_begin_date__lte'] = datetime(3221, 10, 29, 7, 17, 1, 177) if params[
                                                                                                              'endDate'] is None or len(
                params['endDate']) == 0 else params['endDate']

        kwargs = {key: value for key, value in kwargs.items() if value is not None and value != ''}  # 过滤掉值为None或''的项
        # print(kwargs)
        totalNumber = TrainingCheckin.objects.filter(
            Q(checkin_people__employee_name__contains=params['searchName']) | Q(
                checkin_people__employee_code__contains=params['searchName']) | Q(
                checkin_content__content_title__contains=params['searchName']) | Q(
                checkin_address__contains=params['searchName']), checkin_status=True, **kwargs).count()
        tableList = list(TrainingCheckin.objects.filter(
            Q(checkin_people__employee_name__contains=params['searchName']) | Q(
                checkin_people__employee_code__contains=params['searchName']) | Q(
                checkin_content__content_title__contains=params['searchName']) | Q(
                checkin_address__contains=params['searchName']), checkin_status=True, **kwargs).values('id',
                                                                                                       'checkin_people_id',
                                                                                                       'checkin_people__employee_name',
                                                                                                       'checkin_people__employee_code',
                                                                                                       'checkin_people__employee_department__department_name',
                                                                                                       'checkin_content__content_title',

                                                                                                       'checkin_content__content_duration',
                                                                                                       'checkin_content__content_type__type_name',
                                                                                                       'checkin_content__content_begin_date',
                                                                                                       'checkin_content__content_end_date',

                                                                                                       'checkin_time',
                                                                                                       'checkin_address',
                                                                                                       'checkin_user_type',
                                                                                                       ).order_by(
            '-checkin_createTime'))
        # print("查询",tableList)
        all_people_id = list(TrainingCheckin.objects.filter(
            Q(checkin_people__employee_name__contains=params['searchName']) | Q(
                checkin_people__employee_code__contains=params['searchName']) | Q(
                checkin_content__content_title__contains=params['searchName']) | Q(
                checkin_address__contains=params['searchName']), checkin_status=True, **kwargs).values_list(
            'checkin_people_id', flat=True).distinct())

        data_list = list(TrainingCheckin.objects.filter(
            Q(checkin_people__employee_name__contains=params['searchName']) | Q(
                checkin_people__employee_code__contains=params['searchName']) | Q(
                checkin_content__content_title__contains=params['searchName']) | Q(
                checkin_address__contains=params['searchName']), checkin_status=True,
            checkin_people_id__in=all_people_id, **kwargs).values('checkin_people__employee_name',
                                                                  'checkin_people__employee_department__department_name',
                                                                  'checkin_people__employee_code',
                                                                  'checkin_content__content_duration'))

        result_dict = {}

        for item in data_list:
            employee_name = item['checkin_people__employee_name']
            employee_code = item['checkin_people__employee_code']
            department_name = item['checkin_people__employee_department__department_name']
            try:
                duration = float(item['checkin_content__content_duration'])
            except:
                # print('1111',item['checkin_content__content_duration'],len(item['checkin_content__content_duration']))
                duration =0
            key = (employee_name, employee_code, department_name)
            if key in result_dict:
                result_dict[key] += duration
            else:
                result_dict[key] = duration

        result_list = []

        for (employee_name, employee_code, department_name), total_duration in result_dict.items():
            result_list.append({
                'checkin_people__employee_name': employee_name,
                'checkin_people__employee_code': employee_code,
                'checkin_content__content_duration': str(total_duration),
                'checkin_people__employee_department__department_name': department_name,
                'checkin_remark': '合计',
            })

        tableList += result_list
        for index, item in enumerate(tableList):
            item['index'] = index + 1
            try:
                item['checkin_people__employee_name_code'] = "{}({})".format(item['checkin_people__employee_name'],
                                                                             item['checkin_people__employee_code'])

                item['checkin_content__content_begin_date'] = item['checkin_content__content_begin_date'].strftime(
                    "%Y-%m-%d %H:%M:%S") if item['checkin_content__content_begin_date'] is not None else None
                item['checkin_content__content_end_date'] = item['checkin_content__content_end_date'].strftime(
                    "%Y-%m-%d %H:%M:%S") if item['checkin_content__content_end_date'] is not None else None
            except:
                pass
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "信息返回成功",
            "data": {
                'columnList': columnList,
                'tableList': tableList[(currentPage - 1) * pageSize:currentPage * pageSize],
                'totalNumber': totalNumber + len(result_list),
            }
        }

    # def get_training_checkin(self):
    #     columnList = [{'label': 'index', 'value': '序号', 'width': 60},
    #                   {'label': 'checkin_people__employee_name_code', 'value': '填写人', 'width': ""},
    #                   {'label': 'checkin_people__employee_department__department_name', 'value': '所在部门', 'width':""},
    #                   {'label': 'checkin_content__content_title', 'value': '参训课程', 'width':""},
    #                   # {'label': 'checkin_time', 'value': '填写时间', 'width':""},
    #                   # {'label': 'checkin_user_type', 'value': '用户类型', 'width': ""},
    #                   {'label': 'checkin_content__content_duration', 'value': '培训时长', 'width':""},
    #                   {'label': 'checkin_content__content_type__type_name', 'value': '培训类型', 'width': ""},
    #                   {'label': 'checkin_content__content_begin_date', 'value': '开始培训日期', 'width': ""},
    #                   {'label': 'checkin_content__content_end_date', 'value': '结束培训日期', 'width': ""},
    #                   # {'label': 'checkin_address', 'value': '您在那个会场集训', 'width':""},
    #                   {'label': 'checkin_remark', 'value': '备注', 'width': ""},
    #                   ]
    #     info = json.loads(self.request.body)
    #
    #     params = {
    #         'beginDate': info['beginDate'],
    #         'endDate': info['endDate'],
    #         'searchName': info['searchName'],
    #         'department_id': info['baseNameId'],
    #         'currentPage':info['currentPage'],
    #         'pageSize':info['pageSize']
    #     }
    #     print(params)
    #     currentPage = params['currentPage'] if params['currentPage'] != "" else 1
    #     pageSize = params['pageSize'] if params['pageSize'] != "" else 25
    #
    #     kwargs = {
    #         'checkin_people__employee_department__id__in': params['department_id'],
    #         'checkin_content__content_status':True,
    #     }
    #
    #     if params['department_id']=='':
    #         kwargs['checkin_people__employee_department__id__in'] = self.request.user_department_employee
    #
    #     if params['beginDate'] != "" and params['endDate'] != "":
    #         kwargs['checkin_content__content_begin_date__gte'] = datetime(1901, 10, 29, 7, 17, 1, 177) if params['beginDate'] is None or len(params['beginDate']) == 0 else params['beginDate']
    #         kwargs['checkin_content__content_begin_date__lte'] = datetime(3221, 10, 29, 7, 17, 1, 177) if params['endDate'] is None or len(params['endDate']) == 0 else params['endDate']
    #
    #     kwargs = {key: value for key, value in kwargs.items() if value is not None and value != ''}  # 过滤掉值为None或''的项
    #     # print(kwargs)
    #     totalNumber = TrainingCheckin.objects.filter(Q(checkin_people__employee_name__contains=params['searchName']) | Q(checkin_people__employee_code__contains=params['searchName'])| Q(checkin_content__content_title__contains=params['searchName'])| Q(checkin_address__contains=params['searchName']),checkin_status=True,**kwargs).count()
    #     tableList = list(TrainingCheckin.objects.filter(Q(checkin_people__employee_name__contains=params['searchName']) | Q(checkin_people__employee_code__contains=params['searchName'])| Q(checkin_content__content_title__contains=params['searchName'])| Q(checkin_address__contains=params['searchName']),checkin_status=True,**kwargs).values('id',
    #               'checkin_people_id',
    #               'checkin_people__employee_name',
    #               'checkin_people__employee_code',
    #               'checkin_people__employee_department__department_name',
    #               'checkin_content__content_title',
    #
    #              'checkin_content__content_duration',
    #              'checkin_content__content_type__type_name',
    #              'checkin_content__content_begin_date',
    #              'checkin_content__content_end_date',
    #
    #               'checkin_time',
    #               'checkin_address',
    #             'checkin_user_type',
    #               ).order_by('-checkin_createTime'))
    #     # print("查询",tableList)
    #     all_people_id = list(TrainingCheckin.objects.filter(Q(checkin_people__employee_name__contains=params['searchName']) | Q(checkin_people__employee_code__contains=params['searchName'])| Q(checkin_content__content_title__contains=params['searchName'])| Q(checkin_address__contains=params['searchName']),checkin_status=True,**kwargs).values_list('checkin_people_id',flat=True).distinct())
    #
    #     data_list=list(TrainingCheckin.objects.filter(Q(checkin_people__employee_name__contains=params['searchName']) | Q(checkin_people__employee_code__contains=params['searchName'])| Q(checkin_content__content_title__contains=params['searchName'])| Q(checkin_address__contains=params['searchName']),checkin_status=True,checkin_people_id__in=all_people_id,**kwargs).values('checkin_people__employee_name','checkin_people__employee_department__department_name','checkin_people__employee_code','checkin_content__content_duration'))
    #
    #     result_dict = {}
    #
    #     for item in data_list:
    #         employee_name = item['checkin_people__employee_name']
    #         employee_code = item['checkin_people__employee_code']
    #         department_name = item['checkin_people__employee_department__department_name']
    #         duration = float(item['checkin_content__content_duration'])
    #         key = (employee_name, employee_code, department_name)
    #         if key in result_dict:
    #             result_dict[key] += duration
    #         else:
    #             result_dict[key] = duration
    #
    #     result_list = []
    #
    #     for (employee_name, employee_code, department_name), total_duration in result_dict.items():
    #         result_list.append({
    #             'checkin_people__employee_name': employee_name,
    #             'checkin_people__employee_code': employee_code,
    #             'checkin_content__content_duration': str(total_duration),
    #             'checkin_people__employee_department__department_name': department_name,
    #             'checkin_remark':'合计',
    #         })
    #
    #     tableList+=result_list
    #     for index, item in enumerate(tableList):
    #         item['index'] = index + 1
    #         try:
    #             item['checkin_people__employee_name_code']="{}({})".format(item['checkin_people__employee_name'],item['checkin_people__employee_code'])
    #
    #             item['checkin_content__content_begin_date'] = item['checkin_content__content_begin_date'].strftime("%Y-%m-%d %H:%M:%S") if item['checkin_content__content_begin_date'] is not None else None
    #             item['checkin_content__content_end_date'] = item['checkin_content__content_end_date'].strftime("%Y-%m-%d %H:%M:%S") if item['checkin_content__content_end_date'] is not None else None
    #         except:
    #             pass
    #     self.return_data = {
    #         "code": status.HTTP_200_OK,
    #         "msg": "信息返回成功",
    #         "data": {
    #             'columnList': columnList,
    #             'tableList': tableList[(currentPage - 1) * pageSize:currentPage * pageSize],
    #             'totalNumber': totalNumber+len(result_list),
    #         }
    #     }

    def post_training_checkin(self):
        checkin_info={}
        info=json.loads(self.request.body)
        people_obj=HrEmployee.objects.filter(employee_code=info['code'],employee_status=1).values_list('id',flat=True)
        if people_obj.exists():
            checkin_info['checkin_people_id'] =people_obj[0]
            content_obj=TrainingContent.objects.filter(content_title=info['checkin_content']).values_list('id', flat=True)
            if content_obj.exists():
                if len(people_obj)==1:
                    checkin_info['checkin_content_id'] = content_obj[0]
                    checkin_info['checkin_time'] = self.now.format('YYYY-MM-DD hh:mm:ss')
                    checkin_info['checkin_address'] = info['checkin_address']
                    checkin_info['checkin_user_type'] = None
                    TrainingCheckin.objects.update_or_create(defaults=checkin_info,
                                                             checkin_people_id=checkin_info['checkin_people_id'],
                                                             checkin_content_id=checkin_info['checkin_content_id'],
                                                             checkin_time=checkin_info['checkin_time'],
                                                             checkin_address=checkin_info['checkin_address'],
                                                             checkin_status=True
                                                             )
                    self.return_data = {
                        "code": status.HTTP_200_OK,
                        "msg": "新增成功",
                    }
                else:
                    self.return_data = {
                        "code": status.HTTP_401_UNAUTHORIZED,
                        "msg": "有多门课程,无法签到",
                    }
            else:
                self.return_data = {
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "msg": "该门课程不存在，无法签到",
                }
        else:
            self.return_data = {
                "code": status.HTTP_401_UNAUTHORIZED,
                "msg": "该员工不存在或已离职，无法签到",
            }

    def down_training_checkin(self):
        dummy_path = os.path.join(BASE_DIR, 'static', 'offlineTrainingFile', 'download_file', str(self.t1), str(self.t2))  # 创建文件夹
        self.mkdir(dummy_path)
        template_path = os.path.join(BASE_DIR, 'static', 'offlineTrainingFile', 'template_file', '培训签到下载模板.xlsx')  # 创建文件夹
        import shutil
        # 指定原始文件路径和目标路径
        source_path = template_path  # 例如：C:\\原始文件夹\\文件名.xlsx
        destination_path = os.path.join(BASE_DIR, 'static', 'offlineTrainingFile', 'download_file', str(self.t1), str(self.t2),'培训签到下载模板.xlsx')  # 例如：D:\\目标文件夹\\文件名.xlsx

        # 使用shutil库进行复制操作
        shutil.copy(source_path, destination_path)
        id_list = json.loads(self.request.body).get('idList')
        download_all = json.loads(self.request.body).get('downloadAll')
        # print(id_list,download_all)
        # self.get_training_checkin()
        # table_list = self.sort_list_of_dicts(self.return_data['data']['tableList'])

        row_data = []
        if download_all == True:  # 是下载全部   有条件
            info = json.loads(self.request.body)
            params = {
                'beginDate': info['beginDate'],
                'endDate': info['endDate'],
                'searchName': info['searchName'],
                'department_id': info['baseNameId'],
            }

            kwargs = {
                'checkin_people__employee_department__id__in': params['department_id'],
                'checkin_content__content_status': True,
            }

            if params['beginDate'] != "" and params['endDate'] != "":
                kwargs['checkin_content__content_begin_date__gte'] = datetime(1901, 10, 29, 7, 17, 1, 177) if params[
                                                                                                                  'beginDate'] is None or len(
                    params['beginDate']) == 0 else params['beginDate']
                kwargs['checkin_content__content_begin_date__lte'] = datetime(3221, 10, 29, 7, 17, 1, 177) if params[
                                                                                                                  'endDate'] is None or len(
                    params['endDate']) == 0 else params['endDate']
            if params['department_id'] == '':
                kwargs['checkin_people__employee_department__id__in'] = self.request.user_department_employee
            kwargs = {key: value for key, value in kwargs.items() if
                      value is not None and value != ''}  # 过滤掉值为None或''的项

            tableList = list(TrainingCheckin.objects.filter(
                Q(checkin_people__employee_name__contains=params['searchName']) | Q(
                    checkin_people__employee_code__contains=params['searchName']) | Q(
                    checkin_content__content_title__contains=params['searchName']) | Q(
                    checkin_address__contains=params['searchName']), checkin_status=True, **kwargs).values(
                                                                                                           'checkin_people_id',
                                                                                                           'checkin_people__employee_name',
                                                                                                           'checkin_people__employee_code',
                                                                                                           'checkin_people__employee_department__department_name',
                                                                                                           'checkin_content__content_title',

                                                                                                           'checkin_content__content_duration',
                                                                                                           'checkin_content__content_type__type_name',
                                                                                                           'checkin_content__content_begin_date',
                                                                                                           'checkin_content__content_end_date',
                                                                                                            'checkin_address',

                                                                                                           ))


            # all_people_id = [item['checkin_people_id'] for item in tableList]
            all_people_id = list(TrainingCheckin.objects.filter(
                Q(checkin_people__employee_name__contains=params['searchName']) | Q(
                    checkin_people__employee_code__contains=params['searchName']) | Q(
                    checkin_content__content_title__contains=params['searchName']) | Q(
                    checkin_address__contains=params['searchName']), checkin_status=True, **kwargs).values_list(
                'checkin_people_id', flat=True).distinct())

            print(all_people_id)
            data_list = list(TrainingCheckin.objects.filter(
                Q(checkin_people__employee_name__contains=params['searchName']) | Q(
                    checkin_people__employee_code__contains=params['searchName']) | Q(
                    checkin_content__content_title__contains=params['searchName']) | Q(
                    checkin_address__contains=params['searchName']), checkin_status=True,
                checkin_people_id__in=all_people_id, **kwargs).values('checkin_people__employee_name',
                                                                      'checkin_people__employee_department__department_name',
                                                                      'checkin_people__employee_code',
                                                                      'checkin_content__content_duration'))   #求和数据
            print(len(data_list))
            #
            result_dict = {}
            #
            for item in data_list:
                employee_name = item['checkin_people__employee_name']
                employee_code = item['checkin_people__employee_code']
                department_name = item['checkin_people__employee_department__department_name']
                try:
                    duration = float(item['checkin_content__content_duration'])
                except:
                    # print('1111',item['checkin_content__content_duration'],len(item['checkin_content__content_duration']))
                    duration = 0

                key = (employee_name, employee_code, department_name)

                if key in result_dict:
                    result_dict[key] += duration
                else:
                    result_dict[key] = duration

            result_list = []

            for (employee_name, employee_code, department_name), total_duration in result_dict.items():
                result_list.append({
                    'checkin_people__employee_name': employee_name,
                    'checkin_people__employee_code': employee_code,
                    'checkin_people__employee_department__department_name': department_name,
                    'checkin_content__content_title': None,
                    'checkin_content__content_duration': str(total_duration),
                                        'checkin_content__content_type__type_name':None,
                    'checkin_content__content_begin_date':None,
                    'checkin_content__content_end_date':None,
                    'checkin_address':None,
                    'checkin_remark': '合计',


                })

            tableList+=result_list
            index = 1
            for line in tableList:
                line_data=[]

                for k, v in line.items():
                    if k not in ('checkin_people_id'):
                        line_data.append(v)

                line_data.insert(0, index)

                name_code = "{}({})".format(line_data[1], line_data[2])
                line_data[1] = name_code
                del line_data[2]
                row_data.append(line_data)
                if len(line_data) == 0:
                    index = index
                index += 1
        else:
            row_data = []
            # print(id_list)
            tableList = list(TrainingCheckin.objects.filter(id__in=id_list, checkin_status=True).values(
                'checkin_people_id',
                'checkin_people__employee_name',
                'checkin_people__employee_code',
                'checkin_people__employee_department__department_name',
                'checkin_content__content_title',

                'checkin_content__content_duration',
                'checkin_content__content_type__type_name',
                'checkin_content__content_begin_date',
                'checkin_content__content_end_date',
                'checkin_address'
            ))

            all_people_id = [item['checkin_people_id'] for item in tableList]
            # print(all_people_id)
            data_list = list(TrainingCheckin.objects.filter( checkin_status=True,id__in=id_list, ).values('checkin_people__employee_name',
                                                                      'checkin_people__employee_department__department_name',
                                                                      'checkin_people__employee_code',
                                                                      'checkin_content__content_duration'))   #求和数据
            # print(data_list)
            #
            result_dict = {}
            #
            for item in data_list:
                employee_name = item['checkin_people__employee_name']
                employee_code = item['checkin_people__employee_code']
                department_name = item['checkin_people__employee_department__department_name']
                try:
                    duration = float(item['checkin_content__content_duration'])
                except:
                    # print('1111',item['checkin_content__content_duration'],len(item['checkin_content__content_duration']))
                    duration = 0

                key = (employee_name, employee_code, department_name)

                if key in result_dict:
                    result_dict[key] += duration
                else:
                    result_dict[key] = duration

            result_list = []

            for (employee_name, employee_code, department_name), total_duration in result_dict.items():
                result_list.append({
                    'checkin_people__employee_name': employee_name,
                    'checkin_people__employee_code': employee_code,
                    'checkin_people__employee_department__department_name': department_name,
                    'checkin_content__content_title': None,
                    'checkin_content__content_duration': str(total_duration),

                    'checkin_content__content_type__type_name':None,
                    'checkin_content__content_begin_date':None,
                    'checkin_content__content_end_date':None,
                    'checkin_address':None,
                    'checkin_remark': '合计',


                })

            tableList+=result_list

            index = 1
            for line in tableList:
                line_data=[]

                for k, v in line.items():
                    if k not in ('checkin_people_id'):
                        line_data.append(v)

                line_data.insert(0, index)

                name_code = "{}({})".format(line_data[1], line_data[2])
                line_data[1] = name_code
                del line_data[2]
                row_data.append(line_data)
                if len(line_data) == 0:
                    index = index
                index += 1





            # for id in id_list:
            #     data = list(TrainingCheckin.objects.filter(pk=id, checkin_status=True).values_list(
            #         'checkin_people_id',
            #         'checkin_people__employee_name',
            #         'checkin_people__employee_code',
            #         'checkin_people__employee_department__department_name',
            #         'checkin_content__content_title',
            #
            #         'checkin_content__content_duration',
            #         'checkin_content__content_type__type_name',
            #         'checkin_content__content_begin_date',
            #         'checkin_content__content_end_date',
            #         'checkin_address'
            #     ))[0]
            #
            #
            #
            #     data = (index,) + data
            #     data = list(data)
            #     name_code = "{}({})".format(data[1], data[2])
            #     data[1] = name_code
            #     del data[2]
            #     row_data.append(data)
            #     if len(data) == 0:
            #         index = index
            #     index += 1

        exc = openpyxl.load_workbook(destination_path)  # 打开整个excel文件
        sheet = exc.worksheets[0]  # 打开第0张工作表(也就是第一张)
        for row in row_data:
            sheet.append(row)  # 在工作表中添加一行
        # 将"备注"写入到J1单元格中
        # sheet.cell(row=1, column=10, value='备注')
        exc.save(destination_path)  # 指定路径,保存文件

        # 使用字符串替换将\替换为/
        destination_path = destination_path.replace('\\', '/')
        destination_path = 'static/' + destination_path.split('static/')[1]
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "下载成功",
            "downloadUrl": destination_path
        }
    def batch_training_checkin(self):
        file = self.request.FILES.get('file')
        try:
            title_name=str(file).split('培训签到表')[0]
            # print(title_name)
            now = arrow.now()
            t1 = now.format('YYYY-MM-DD')
            t2 = now.format('YYYY-MM-DD_HH_mm_ss')
            dummy_path = os.path.join(BASE_DIR, 'static', 'offlineTrainingFile', 'upload_file', t1,'培训签到文件上传')  # 创建文件夹
            Content.mkdir(dummy_path)
            file_url, file_name, file_suffix = Content.createPath(file, '培训签到文件上传', str(title_name)+'培训签到表' + str(t2))
            Content.saveFile(file_url, file)
            exc = openpyxl.load_workbook(file_url, data_only=True)
            sheet = exc.active
            for line in range(1, sheet.max_row):  # 每行数据
                checkin_info = {}
                name_code=sheet.cell(line + 1, 1).value
                name,code=name_code.split("(")[0],name_code.split("(")[1].replace(")", "")
                employee_obj = HrEmployee.objects.filter(employee_code=code,employee_status=1).values_list('id',flat=True)
                if employee_obj.exists():
                    content_obj = TrainingContent.objects.filter(content_title=title_name).values_list('id',flat=True)
                    # print(content_obj)
                    if content_obj.exists():
                        if len(content_obj) == 1:
                            checkin_info['checkin_people_id'] = employee_obj[0]
                            checkin_info['checkin_content_id'] = content_obj[0]
                            checkin_info['checkin_time'] = sheet.cell(line + 1, 3).value
                            checkin_info['checkin_address'] = sheet.cell(line + 1,5).value
                            checkin_info['checkin_user_type'] = sheet.cell(line + 1, 4).value
                            TrainingCheckin.objects.update_or_create(defaults=checkin_info,
                                                                     checkin_people_id=checkin_info['checkin_people_id'],
                                                                     checkin_content_id=checkin_info['checkin_content_id'],
                                                                     checkin_time=checkin_info['checkin_time'],
                                                                     checkin_address=checkin_info['checkin_address'],
                                                                     checkin_status=True
                                                                     )
                            self.return_data = {
                                "code": status.HTTP_200_OK,
                                "msg": "上传成功·!"
                            }
                        else:
                            self.return_data = {
                                "code": status.HTTP_401_UNAUTHORIZED,
                                "msg": "{}课程有多个，无法识别!".format(title_name)
                            }
                    else:
                        self.return_data = {
                            "code": status.HTTP_401_UNAUTHORIZED,
                            "msg": "{}课程不存在，无法上传!".format(title_name)
                        }

                else:
                    self.return_data = {
                        "code": status.HTTP_401_UNAUTHORIZED,
                        "msg": "该讲师已离职,或不是公司员工,无法上传!"
                    }
        except:
            self.return_data = {
                "code": status.HTTP_401_UNAUTHORIZED,
                "msg": "文件名称错误，可能不是培训签到表"
            }
    def del_training_checkin(self):
        info=json.loads(self.request.body)
        TrainingCheckin.objects.filter(pk__in=info['idList']).update(checkin_status=False)
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "删除成功",
        }
    def edit_training_checkin(self):
        info = json.loads(self.request.body)
        people_obj = HrEmployee.objects.filter(employee_code=info['checkin_people__employee_code'], employee_status=1).values_list('id',flat=True)
        checkin_info = {}
        if people_obj.exists():
            checkin_info['checkin_people_id'] = people_obj[0]
            content_obj = TrainingContent.objects.filter(content_title=info['checkin_content__content_title']).values_list('id',flat=True)
            if content_obj.exists():
                if len(people_obj) == 1:
                    checkin_info['checkin_content_id'] = content_obj[0]
                    checkin_info['checkin_time'] =  datetime.strptime(info['checkin_time'], '%Y-%m-%d %H:%M:%S') if info['checkin_time']  is not None else None

                    checkin_info['checkin_address'] = info['checkin_address']
                    checkin_info['checkin_user_type'] = info['checkin_user_type']
                    TrainingCheckin.objects.filter(pk=info['id']).update(**checkin_info)
                    self.return_data = {
                        "code": status.HTTP_200_OK,
                        "msg": "修改成功",
                    }
                else:
                    self.return_data = {
                        "code": status.HTTP_401_UNAUTHORIZED,
                        "msg": "改课程存在多个,无法修改",
                    }
            else:
                self.return_data = {
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "msg": "该门课程不存在，无法修改",
                }


        else:
            self.return_data = {
                "code": status.HTTP_401_UNAUTHORIZED,
                "msg": "该员工不存在或已离职，无法修改",
            }



    @staticmethod
    def mkdir(path):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
        else:
            pass

    @staticmethod
    def sort_list_of_dicts(list_of_dicts):
        """
        对列表中的字典按照指定的顺序排序。

        Args:
        list_of_dicts (list): 包含多个字典的列表。
        order (list): 指定排序顺序的键的列表。

        Returns:
        list: 排序后的列表中的字典。
        """
        # 对列表中的每个字典按照指定的顺序排序
        # 指定排序顺序
        order = [
            'checkin_people__employee_name_code',
            'checkin_people__employee_department__department_name',
            'checkin_content__content_title',
            'checkin_time',
            'checkin_user_type',
            'checkin_address',
            'id', 'index',

        ]
        sorted_list_of_dicts = [dict(sorted(d.items(), key=lambda x: order.index(x[0]))) for d in list_of_dicts]
        return sorted_list_of_dicts