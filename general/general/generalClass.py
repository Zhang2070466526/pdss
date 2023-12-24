# -*- coding: utf-8 -*-
# @Time    : 2023/5/8 13:55
# @Author  : zhuang
# @Site    : 
# @File    : generalClass.py
# @Software: PyCharm
from django.db.models import Q

from controller.controller import Controller, upload_file
from rest_framework.response import Response

from employee.models import HrDepartment
from employeeCare.models import Colloquium
from employeeInspect.models import EmployeeInspect
from internalEvaluation.models import InternalEvaluationList
from memorabilia.models import MemorabiliaList
from salarySurvey.models import *
from externalHonors.models import *
# from memorabilia.models import *
from ..models import *
from employeeActivities.models import *

from internalEvaluation.models import *
from employeeInspect.models import *
from employeeCare.models import *
from ..models import *
from utils.check_token import *
from auther.models import *
from datetime import *
import datetime
import json

from django.utils.deprecation import MiddlewareMixin


class LogMiddleware(MiddlewareMixin):  # 日志存储中间件
    def process_request(self, request):
        new_token = CheckToken()
        try:
            check_token = new_token.check_token(request.headers['Authorization'])
        except:
            check_token = None
        # print(check_token)
        try:
            if len(request.body):
                body = json.loads(request.body)
            else:
                body = None
        except:
            body = None

        # print('GET',dict(request.GET))
        # print('POST', dict(request.POST))
        # print('FILES', dict(request.FILES))

        data = {
            "log_user_id": check_token,
            "log_requestMethod": request.method,
            'log_token': request.headers.get('Authorization', None),
            'log_host': request.headers.get('Host', None),
            'log_createTime': datetime.datetime.now(),
            'log_requestAPI': str(request).split("'")[1],
            'log_requestGET': dict(request.GET) if dict(request.GET) else None,
            'log_requestPOST': dict(request.POST) if dict(request.POST) else None,
            'log_requestFILES': dict(request.FILES) if dict(request.FILES) else None,
            'log_requestBody': body,
        }
        Admin_log.objects.create(**data)


class TokenMiddleware(MiddlewareMixin):  # token中间件
    def process_request(self, request):
        new_token = CheckToken()
        try:
            check_token = new_token.check_token(request.headers['Authorization'])
            # print(check_token)
            user_base_list = AdminUser.objects.filter(pk=check_token).values("user_base")
            user_base = [item['user_base'] for item in user_base_list]
            request.user_base = user_base
            # print(request.user_base)

            user_jobRank_list=AdminUser.objects.filter(pk=check_token).values("user_jobrank")
            # print(user_jobRank_list)
            user_jobRank= [item['user_jobrank'] for item in user_jobRank_list]
            request.user_jobRank= user_jobRank

            # user_jobRank_list_hik=AdminUser.objects.filter(pk=check_token).values("user_jobrank_hik")
            # user_jobRank_hik= [item['user_jobrank_hik'] for item in user_jobRank_list_hik]
            # request.user_jobRank_hik= user_jobRank_hik
            # print(request.user_jobRank_hik)

            user_jobRank_list_employee=AdminUser.objects.filter(pk=check_token).values("user_jobrank_employee")
            user_jobRank_employee= [item['user_jobrank_employee'] for item in user_jobRank_list_employee]
            request.user_jobRank_employee= user_jobRank_employee

            user_department_list_employee = AdminUser.objects.filter(pk=check_token).values("user_department_employee")
            # print('111111',user_department_list_employee)
            user_department_employee = [item['user_department_employee'] for item in user_department_list_employee]
            # print('2222',user_department_employee)
            # print('middle1', user_department_employee)
            # for child in user_department_employee:
            #     base_child_ls = list(HrDepartment.objects.filter(~Q(department_parent_id=1),department_parent_id=child).values_list('id', flat=True))  #in
            #     user_department_employee+=base_child_ls
            # request.user_department_employee = user_department_employee
            # print('middle2',user_department_employee)
            # ids_with_parent_1 = HrDepartment.objects.filter(department_parent_id=1,id__in=user_department_list_employee).values_list('id', flat=True)

            # 打印查找结果

            first_father=list(HrDepartment.objects.filter(department_status=1,id__in=user_department_employee).values_list('department_parent_id',flat=True))
            user_department_employee+=first_father
            second_father=list(HrDepartment.objects.filter(department_status=1,id__in=user_department_employee).values_list('department_parent_id',flat=True))
            user_department_employee += second_father
            third_father = list(HrDepartment.objects.filter(department_status=1, id__in=user_department_employee).values_list('department_parent_id', flat=True))
            user_department_employee += third_father
            overdue_dept_id=list(HrDepartment.objects.filter(Q(department_expiry_date__isnull=False) | Q(department_expiry_date__lte=datetime.datetime.now())).values_list('id',flat=True))#过期的部门
            user_department_employee = [x for x in user_department_employee if x not in [0, 2, None,999999]+overdue_dept_id]  # 排除0和2的
            request.user_department_employee=list(set(user_department_employee))
            # print(len(list(set(user_department_employee))))





        except:
            check_token = None
        request.check_token = check_token


class generalClass:
    def __init__(self, request, meth):
        self.request = request
        self.model_choice = {
            "salarySurvey": SalarySurveyRecord,
            "SalarySurveyRecord": SalarySurveyRecord,
            "externalHonors": ExternalHonorsList,
            "ExternalHonors": ExternalHonorsList,
            "externalHonorsList": ExternalHonorsList,
            "ExternalHonorsList": ExternalHonorsList,
            "MemorabiliaList": MemorabiliaList,
            "EmployeeActivitiesList": EmployeeActivitiesList,
            "InternalEvaluationList": InternalEvaluationList,
            "Colloquium": Colloquium,
            "EmployeeInspect": EmployeeInspect,

            # "InternalEvaluationList": InternalEvaluationList,
            # 'EmployeeInspect': EmployeeInspect,
            # 'Colloquium': Colloquium,
        }
        self.model = ''
        self.meth = meth
        self.return_data = {}
        self.methods = {
            "delete_other_file": self.delete_other_file,
            "upload_other_file": self.upload_other_file,
            "center_drop": self.center_drop,
        }

    def meth_center(self):
        self.methods[self.meth]()
        # print(self.return_data)
        return Response(self.return_data)

    # 上传附件
    def upload_other_file(self):
        type_name = self.request.POST.get("type", None)
        if type_name is not None:
            obj = Controller(self.model_choice[type_name], "upload_other_file", self.request)
            self.return_data = obj.data_start()
        else:
            self.return_data = {
                "code": 401,
                "msg": "参数有误，请检查参数"
            }

    # 删除附件
    def delete_other_file(self):
        obj = Controller(SalarySurveyRecord, "delete_other_file", self.request)
        self.return_data = obj.data_start()

    def patch(self):
        type_name = self.request.POST.get("type", "None")
        obj = Controller(self.model_choice[type_name], "patch", self.request)
        self.return_data = obj.data_start()

    def center_drop(self):
        self.return_data = {
            "code": 200,
            "msg": "下拉菜单返回成功",
            "data": [],
            'hidden': True
        }
        new_token = CheckToken()
        check_token = new_token.check_token(self.request.headers['Authorization'])
        user_base = self.request.user_base
        if check_token!=None:
            admin_base = AdminUser.objects.filter(id=check_token, user_base__status=1,
                                                  user_base__base_parent_id=None).values_list('user_base__id',
                                                                                              'user_base__name').all()
            count = 0

            for i in admin_base:
                child = center_base.objects.filter(base_parent_id=i[0], status=1).values_list("id", "name")
                if len(child) > 0:
                    self.return_data['data'].append({
                        "label": i[1],
                        "value": i[0],
                        "index": count,
                        "children": []
                    })
                    for p in child:
                        if p[0] in user_base:
                            self.return_data['data'][-1]["children"].append({"label": p[1], "value": p[0]})
                else:
                    self.return_data['data'].append({
                        "label": i[1],
                        "value": i[0],
                        "index": count,
                    })
                count += 1
        else:
            self.return_data = {
                "code": 403,
                "msg": "没有权限访问",
                'hidden': False
            }

        # obj = center_base.objects.all()
        # count = 0
        # for i in obj:
        #     self.return_data['data'].append({
        #         "label": i.name,
        #         "value": i.id,
        #         "index": count,
        #     })
        #     count += 1


# from cryptography.fernet import Fernet
# import json
# class EncryptionMiddleware:   #加密数据中间件
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.key = '0ptHdOL49TuYNJz-uRYrl3mgw_A-Xr4Y3a-Lbign3OU='
#
#     def __call__(self, request):
#         # 解密请求数据
#         encrypted_data = json.loads(request.body)
#         print("encrypted_data",encrypted_data['data'],type(encrypted_data['data']))
#         # SECRET_KEY = Fernet.generate_key()#生成密钥
#         # print(SECRET_KEY)
#         if type(encrypted_data)==bytes:#字节数据 是加密数据:
#             decrypted_data = self.decrypt_data(encrypted_data)
#             print("decrypted_data",decrypted_data)
#             request.POST = decrypted_data  # 替换原始的请求数据
#             print("post",request.POST)
#
#         # 处理请求
#         response = self.get_response(request)
#
#         # 加密响应数据
#         response_data = response.content
#         print("response",response_data)
#         encrypted_response_data = self.encrypt_data(response_data)
#         response.content = encrypted_response_data
#
#         return response
#
#     def decrypt_data(self, data):   #解密
#         cipher_suite = Fernet(self.key)
#         decrypted_data = cipher_suite.decrypt(data.encode())
#         return decrypted_data.decode()
#
#     def encrypt_data(self, data):  #加密
#         cipher_suite = Fernet(self.key)
#         encrypted_data = cipher_suite.encrypt(data)
#         return encrypted_data
