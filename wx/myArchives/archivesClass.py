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
from shoeCabinet.shoeFunction import upload_file


class Archives:
    def __init__(self, request):
        self.request = request
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功'
        }
        self.meth = {
            'get_file_info': self.get_file_info,
            'get_file_info_page': self.get_file_info_page,
        }

    def method_center(self, method):
        self.meth[method]()
        return JsonResponse(self.return_data)

    def upload_file_apply(self):
        info = json.loads(self.request.POST)
        file_type = info['type']
        add_or_delete = info['option']
        user_id = info['id']
        file = self.request.FILES.get('file')
        file_url = upload_file(file, 'wx', 'myArchives', '')
        kwargs = {
            'edit_type': '我的档案',
            'user_id': user_id,
            'select_edit_data': ''
        }
        EditRecord.objects.filter(**kwargs)

    def get_file_info_page(self):
        translate_obj = {
            'hrssc_archives_candidate_identity_file': "",
            'hrssc_archives_candidate_diploma_file': "",
            'hrssc_archives_candidate_degree_file': "",
            'hrssc_archives_candidate_title_or_skill_file': "",
            'hrssc_archives_candidate_labor_contract_file': "",
            'hrssc_archives_candidate_confidentiality_agreement_file': "",
            'hrssc_archives_candidate_competition_file': "",
            'hrssc_archives_candidate_base_info_file': "",
            'hrssc_archives_candidate_legal_delivery_file': "",
            'hrssc_archives_candidate_important_notice_file': "",
            'hrssc_archives_candidate_entry_confire_file': "",
            'hrssc_archives_candidate_leave_certificate_file': "",
            'hrssc_archives_candidate_medical_report_file': "",
            'hrssc_archives_candidate_resume_file': "",
            'hrssc_archives_candidate_photo_file': "",
            'hrssc_archives_candidate_bank_card_file': "",
            'hrssc_archives_candidate_honest_file': "",
        }
        info = json.loads(self.request.body)
        language_type = info['language_type']
        translate_obj = translate(translate_obj, language_type)
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功',
            'data': {
                'translate': translate_obj
            }
        }

    def get_file_info(self):
        field = {
            'candidate_identity_file': 'hrssc_archives_candidate_identity_file',
            'candidate_diploma_file': 'hrssc_archives_candidate_diploma_file',
            'candidate_degree_file': 'hrssc_archives_candidate_degree_file',
            'candidate_title_or_skill_file': 'hrssc_archives_candidate_title_or_skill_file',
            'candidate_labor_contract_file': 'hrssc_archives_candidate_labor_contract_file',
            'candidate_confidentiality_agreement_file': 'hrssc_archives_candidate_confidentiality_agreement_file',
            'candidate_competition_file': 'hrssc_archives_candidate_competition_file',
            'candidate_base_info_file': 'hrssc_archives_candidate_base_info_file',
            'candidate_legal_delivery_file': 'hrssc_archives_candidate_legal_delivery_file',
            'candidate_important_notice_file': 'hrssc_archives_candidate_important_notice_file',
            'candidate_entry_confire_file': 'hrssc_archives_candidate_entry_confire_file',
            'candidate_leave_certificate_file': 'hrssc_archives_candidate_leave_certificate_file',
            'candidate_medical_report_file': 'hrssc_archives_candidate_medical_report_file',
            'candidate_resume_file': 'hrssc_archives_candidate_resume_file',
            'candidate_photo_file': 'hrssc_archives_candidate_photo_file',
            'candidate_bank_card_file': 'hrssc_archives_candidate_bank_card_file',
            'candidate_honest_file': 'hrssc_archives_candidate_honest_file',
        }
        info = json.loads(self.request.body)
        code = info['code']
        file_type = info['file_type']
        emp_obj = HrEmployee.objects.filter(employee_code=code)
        if emp_obj.exists() is False:
            self.return_data = {
                'code': 400,
                'msg': "未找到该人员信息"
            }
            return
        emp_id = emp_obj[0].id
        file_obj = HrEmployeeFiles.objects.filter(employee_id=emp_id, employee_file_status=True, employee_file_type_id=file_type).values(
            'employee_file_name',
            'employee_file_url',
            'employee_file_type_id',
            'employee_file_type__file_name',
            'employee_file_type__field_name',
        )
        file_type = {}
        for obj in file_obj:
            if obj['employee_file_type__field_name'] in file_type:
                file_type[obj['employee_file_type__field_name']].append(obj)
            else:
                file_type[obj['employee_file_type__field_name']] = [obj]
        tableList = []
        for key, value in file_type.items():
            tableList.append(
                {field[key]: value}
            )
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功',
            'data': {
                # 'translate': translate_obj,
                'tableList': tableList,
            }
        }
