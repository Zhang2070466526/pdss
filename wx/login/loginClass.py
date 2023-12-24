import json

from django.http import JsonResponse
from employee.models import *
from translate.translateAPI.method import *


class Login:
    def __init__(self, request):
        self.request = request
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功'
        }
        self.meth = {
            'login_judge': self.login_judge,
            'get_login_page': self.get_login_page,
        }

    def method_center(self, method):
        self.return_data = {
            'code': 200,
            'msg': '登录成功'
        }
        self.meth[method]()
        return JsonResponse(self.return_data)

    def get_login_page(self):
        info = json.loads(self.request.body)
        translate_obj = {
            'hrssc_login_username': '',
            'hrssc_login_password': '',
            'confirm': '',
        }
        translate_obj = translate(translate_obj, info['language_type'])
        self.return_data = {
            'code': 200,
            'msg': '',
            'data': translate_obj
        }

    def login_judge(self):
        info = json.loads(self.request.body)
        emp = HrEmployee.objects.filter(employee_code=info['code'], employee_identity_no__endswith=info['password'])
        if emp.exists():
            data = {
                'employee_name': emp[0].employee_name,
                'code': emp[0].employee_code,
                'employee_department': emp[0].employee_department.department_name,
                'employee_position': emp[0].employee_position.position_name,
            }
            tableList = EditRecord.objects.filter(employee_id=emp[0].id)
            self.return_data = {
                'code': 200,
                'msg': '登录成功',
                'data': {
                    'personInfo': data,
                }
            }
        else:
            self.return_data = {
                'code': 400,
                'msg': '账号或密码错误'
            }
