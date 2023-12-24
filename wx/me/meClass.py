import datetime
import json
import re

import arrow
from django.http import JsonResponse

from employee.models import *
from django.db.models import Q, F
from openpyxl import Workbook, load_workbook

from wx.models import *
from employee.models import *
from translate.translateAPI.method import *


class Me:
    def __init__(self, request):
        self.request = request
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功'
        }
        self.meth = {
            'get_me_page': self.get_me_page,
            'get_notice_info': self.get_notice_info,
            'delete_notice_info': self.delete_notice_info,
        }
        self.edit_status = ['待审核', '已审核', '已退回']

    def method_center(self, method):
        self.meth[method]()
        return JsonResponse(self.return_data)

    def get_me_page(self):
        translate_obj = {
            'hrssc_me_avatar': '',
            'hrssc_me_code': '',
            'hrssc_me_name': '',
            'hrssc_me_deptName': '',
            'hrssc_me_postName': '',
            'hrssc_me_language': '',
            'sign_out': ''
        }
        info = json.loads(self.request.body)
        language = info['language_type']
        translate_obj = translate(translate_obj, language)
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功',
            'data': {
                'translate': translate_obj
            }
        }

    def get_notice_info(self):
        info = json.loads(self.request.body)
        kwargs = {
            'status': True,
            # 'read_time__isnull': True,
        }
        if 'code' in info:
            code = info['code']
            kwargs['employee__employee_code'] = code

        if 'id' in info:
            kwargs['pk'] = info['id']
            EditRecord.objects.filter(pk=info['id']).update(read_time=arrow.now().format("YYYY-MM-DD"))
        edit_obj = EditRecord.objects.filter(**kwargs).values(
            'id',
            'employee__employee_name',
            'employee__employee_department_id__department_name',
            'create_time',
            'modify_time',
            'edit_status',
            'select_edit_data',
            'select_edit_data_pre',
            'edit_type',
            'remark',
        ).order_by('-create_time')
        count = EditRecord.objects.filter(**kwargs, read_time__isnull=True).count()
        new_data = []
        field_to_mean = {}
        for field in HrEmployee._meta.fields:
            field_to_mean[field.name] = field.verbose_name
        for i in edit_obj:
            kwargs = {
                'id': i['id'],
                'name': "",
                'deptName': i['employee__employee_department_id__department_name'],
                'applyTime': arrow.get(i['create_time']).format("YYYY-MM-DD HH:MM:SS"),
                'dealTime': arrow.get(i['modify_time']).format("YYYY-MM-DD HH:MM:SS"),
                'edit_date': [],
                'edit_date_pre': [],
                'edit_status': self.edit_status[i['edit_status'] - 1],
                'remark': i['remark'],
            }
            if i['edit_type'] == "我的信息":
                kwargs['name'] += "信息修改申请"
                kwargs['icon'] = "compose"
            else:
                kwargs['name'] += "文件增/删申请"
                kwargs['icon'] = "upload-filled"
            kwargs['name'] += f"({kwargs['edit_status']})"
            for key, value in eval(i['select_edit_data']).items():
                kwargs['edit_date'].append({
                    'label': field_to_mean[key],
                    'value': value,
                    'field': key,
                })
            for key, value in eval(i['select_edit_data_pre']).items():
                kwargs['edit_date_pre'].append({
                    'label': field_to_mean[key],
                    'value': value,
                    'field': key,
                })
            new_data.append(kwargs)

        self.return_data = {
            'code': 200,
            'msg': '信息返回成功',
            'data': {
                'count': str(count),
                'tableList': new_data,
                # 'modelField': field_to_mean,
            }
        }
        if count == 0:
            del self.return_data['data']['count']

    def delete_notice_info(self):
        info = json.loads(self.request.body)
        notice_id = info['id']
        EditRecord.objects.filter(pk=notice_id).update(status=False)
