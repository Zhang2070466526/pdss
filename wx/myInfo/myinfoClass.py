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


class Info:
    def __init__(self, request):
        self.request = request
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功'
        }
        self.meth = {
            'get_info': self.get_info,
            'edit_info': self.edit_info,
            'drop_down_menu': self.drop_down_menu,
            'get_index_bar': self.get_index_bar,

            'get_approve_list': self.get_approve_list,
            'edit_approve_list': self.edit_approve_list,
        }
        self.edit_status = ['待审核', '已审核', '已退回']

    def method_center(self, method):
        self.meth[method]()
        return JsonResponse(self.return_data)

    # 获取待审批列表
    def get_approve_list(self):
        # department_list = self.request.user_department_employee
        # if len(department_list) == 0:
        department_list = [i for i in range(1, 1000)]
        count = EditRecord.objects.filter(employee__employee_department_id__in=department_list,
                                          editor_id__isnull=True, status=True).count()
        edit_obj = EditRecord.objects.filter(employee__employee_department_id__in=department_list,
                                             editor_id__isnull=True, status=True).values('id',
                                                                            'employee__employee_name',
                                                                            'employee__employee_department_id__department_name',
                                                                            'select_edit_data',
                                                                            'select_edit_data_pre',
                                                                            'create_time',
                                                                            "edit_status")
        new_data = []
        field_to_mean = {}
        for field in HrEmployee._meta.fields:
            field_to_mean[field.name] = field.verbose_name
        for i in edit_obj:
            kwargs = {
                'id': i['id'],
                'name': f"{i['employee__employee_name']}--信息修改申请",
                'deptName': i['employee__employee_department_id__department_name'],
                'applyTime': arrow.get(i['create_time']).format("YYYY-MM-DD HH:MM:SS"),
                'edit_date': [],
                'edit_date_pre': [],
                'edit_status': self.edit_status[i['edit_status'] - 1],
                'remark': '',
            }
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
                'count': count,
                'tableList': new_data,
                # 'modelField': field_to_mean,
            }
        }

    # 审批
    def edit_approve_list(self):
        token = self.request.check_token
        info = json.loads(self.request.body)
        print(info)
        remark = info['remark']
        pk = info['id']
        edit_statue = info['edit_statue']
        edit_obj = EditRecord.objects.filter(pk=pk)
        if edit_obj.exists():
            if edit_obj[0].editor_id is not None:
                self.return_data = {
                    'code': 400,
                    'msg': '该条记录已被他人审核，您无需编辑'
                }
                return
        else:
            self.return_data = {
                'code': 400,
                'msg': '该条记录不存在'
            }
            return
        if edit_statue == 3:
            edit_obj.update(edit_status=3, editor_id=token, read_time=None, remark=remark)
            self.return_data = {
                'code': 200,
                'msg': '已退回'
            }
        if edit_statue == 2:
            edit_obj.update(edit_status=2, remark=remark, editor_id=token, read_time=None)
            edit_data = edit_obj[0].edit_data
            emp_id = edit_obj[0].employee_id
            HrEmployee.objects.filter(pk=emp_id).update(**edit_data)
            self.return_data = {
                'code': 200,
                'msg': '已审批'
            }

    def edit_info(self):
        kwargs = {}
        diff_kwargs = {}
        info = json.loads(self.request.body)
        judge_obj = EditRecord.objects.filter(edit_type='我的信息', employee_id=info['id'], edit_status=1, status=True)
        if judge_obj.exists():
            self.return_data = {
                'code': 400,
                'msg': '申请待审核中，请审核完成后再次申请'
            }
            return
        kwargs['edit_data'] = json.dumps(info)
        emp_obj = self.info_data_tidy_up(info['id'])
        if emp_obj == 0:
            self.return_data = {
                'code': 400,
                'msg': '修改失败'
            }
            return
        kwargs['old_data'] = json.dumps(emp_obj)
        kwargs['employee_id'] = info['id']
        diff_kwargs_pre = {}
        for key, value in info.items():
            if value != emp_obj[key]:
                diff_kwargs[key] = value
                diff_kwargs_pre[key] = emp_obj[key]
        if len(diff_kwargs) == 0:
            return
        kwargs['select_edit_data'] = json.dumps(diff_kwargs)
        kwargs['select_edit_data_pre'] = json.dumps(diff_kwargs_pre)
        kwargs['edit_type'] = '我的信息'
        create_edit = EditRecord.objects.create(**kwargs)
        # 142
        deptName = HrEmployee.objects.filter(pk=info['id']).values_list("employee_department__department_name")[0][0]
        obj = AdminUser.objects.filter(user_menu=142).values("id", "user_department_employee__department_full_name")
        kwargs = {}
        for i in obj:
            if i['id'] not in kwargs and deptName in i['user_department_employee__department_full_name']:
                kwargs[i['id']] = {
                    'deal_record_id': create_edit.id,
                    'deal_person_id': i['id'],
                }
        for key, value in kwargs.items():
            DealEditRecordPerson.objects.create(**value)

        self.return_data = {
            'code': 200,
            'msg': '修改申请已提交'
        }

    def get_info(self):
        # column = {
        #     'employee_sex': '',
        #     'employee_nation__nation_name': '',
        #     'employee_identity_no': '',
        #     'employee_identity_no_effective_date': '',
        #     'employee_identity_no_failre_date': '',
        #     'employee_birthday': '',
        #     'employee_email': '',
        #     'employee_marriage_status': '',
        #     'employee_nation_address': '',
        #     'employee_now_address': '',
        #     'employee_phone': '',
        #     'employee_political_status': '',
        #     'employee_emergency_contact': '',
        #     'employee_emergency_contact_relation': '',
        #     'employee_emergency_contact_phone': '',
        #     'employee_first_degree__edu_degree_name': '',
        #     'employee_first_degree_school': '',
        #     'employee_first_degree_major': '',
        #     'employee_first_degree_type': '',
        #     'employee_first_degree_graduate_date': '',
        #     'employee_train_degree': '',
        #     'employee_train_degree_school': '',
        #     'employee_train_degree_major': '',
        #     'employee_train_degree_type': '',
        #     'employee_train_degree_graduate_date': '',
        #     'employee_bank_deposit': '',
        #     'employee_bank_no': '',
        #     'employee_submit_button': '',
        #     'employee_please_choose': '',
        #     'confirm': '',
        # }
        column = {
            'employee_sex': '',
            'employee_nation__nation_name': '',
            'employee_identity_no': '',
            'employee_identity_no_effective_date': '',
            'employee_identity_no_failre_date': '',
            'employee_birthday': '',
            'employee_email': '',
            'employee_marriage_status': '',
            'employee_nation_address': '',
            'employee_now_address': '',
            'employee_phone': '',
            'employee_political_status': '',
            'employee_emergency_contact': '',
            'employee_emergency_contact_relation': '',
            'employee_emergency_contact_phone': '',
            'employee_emergency_contact_company': '',
            'employee_emergency_contact_2': '',
            'employee_emergency_contact_phone_2': '',
            'employee_emergency_contact_relation_2': '',
            'employee_emergency_contact_company_2': '',
            'employee_first_degree__edu_degree_name': '',
            'employee_first_degree_school': '',
            'employee_first_degree_major': '',
            'employee_first_degree_type': '',
            'employee_first_degree_graduate_date': '',
            'employee_train_degree': '',
            'employee_train_degree_school': '',
            'employee_train_degree_major': '',
            'employee_train_degree_type': '',
            'employee_train_degree_graduate_date': '',
            'employee_bank_deposit': '',
            'employee_bank_no': '',
            'employee_submit_button': '',
            'employee_please_choose': '',
            'confirm': '',
        }
        try:
            code = json.loads(self.request.body)["code"]
        except:
            code = None
        try:
            language = json.loads(self.request.body)["language"]
        except:
            language = 'Chinese'
        column = translate(column, language)
        if code is None or code == 'None' or code == '':
            self.return_data = {
                'code': 400,
                'msg': '请选择正确的工号'
            }
        employee = self.info_data_tidy_up(code)
        if employee == 0:
            return

        self.return_data = {
            'code': 200,
            'msg': '信息返回成功',
            'data': employee,
            'column': column,
        }

    def drop_down_menu(self):
        dept_drop = []
        posi_drop = []
        jobClass_drop = []
        jobGrade_drop = []
        jobDuty_drop = []
        payType_drop = []
        jobRank_drop = []
        nation_drop = []
        candidate_political_status_drop = []
        candidate_marriage_status_drop = []
        candidate_identity_type_drop = []
        candidate_train_degree_type_drop = []
        candidate_first_degree_type_drop = []
        candidate_first_degree_drop = []
        candidate_dl_drop = []
        candidate_nation_place = []
        sex_drop = []
        candidate_status_drop = []
        # for index, k in enumerate(['待提交', '待审核', '已审核', '已退回', '放弃入职', '已删除']):
        #     candidate_status_drop.append({
        #         'text': k,
        #         'value': index + 1,
        #     })
        # for k in ['DL', 'IDL', 'SAL']:
        #     candidate_dl_drop.append({
        #         'text': k,
        #         'value': k,
        #     })
        for k in ['男', '女']:
            sex_drop.append({
                'text': k,
                'value': str(['男', '女'].index(k) + 1),
            })
        education_obj = HrEducationDegree.objects.filter(edu_degree_status=True).values('id', 'edu_degree_name')
        for obj in education_obj:
            candidate_first_degree_drop.append({
                'text': obj['edu_degree_name'],
                'value': obj['id'],
            })
        for k in ['全日制']:
            candidate_first_degree_type_drop.append({
                'text': k,
                'value': k,
            })
        for k in ['全日制', '自考', '远程教育', '成人高考']:
            candidate_train_degree_type_drop.append({
                'text': k,
                'value': k,
            })
        # index = 1
        # for k in ['身份证', '行驶证', '驾驶证', '护照', '其他']:
        #     candidate_identity_type_drop.append({
        #         'text': k,
        #         'value': str(index),
        #     })
        #     index += 1
        for k in ['未婚', '已婚', '离异']:
            candidate_marriage_status_drop.append({
                'text': k,
                'value': str(['未婚', '已婚', '离异'].index(k)),
            })
        for k in ['党员', '预备党员', '共青团员', '民族党派', '群众']:
            candidate_political_status_drop.append({
                'text': k,
                'value': k,
            })
        nations = HrNationPlace.objects.filter(nation_place_status=True,
                                               nation_code_id__isnull=True).values("id", "nation_place_code",
                                                                                   "nation_place_name",
                                                                                   "nation_code_id")
        for n in nations:
            candidate_nation_place.append({
                'text': n['nation_place_name'],
                'value': n['id'],
                'children': []
            })
            children_list = HrNationPlace.objects.filter(nation_place_status=True,
                                                         nation_code_id=n['nation_place_code']).values("id",
                                                                                                       "nation_place_name")
            for child in children_list:
                candidate_nation_place[-1]['children'].append({
                    'text': child['nation_place_name'],
                    'value': child['id'],
                })
        # nation_obj = HrNation.objects.filter(nation_status=True).values('id', 'nation_name')
        # for obj in nation_obj:
        #     nation_drop.append({
        #         'text': obj['nation_name'],
        #         'value': obj['id'],
        #     })
        # dept_obj = HrDepartment.objects.filter(department_status=True).values('id', 'department_full_name')
        # for obj in dept_obj:
        #     dept_drop.append({
        #         'text': obj['department_full_name'],
        #         'value': obj['id'],
        #     })
        #
        # posi_obj = HrPosition.objects.filter(department_status=True).values('position_name', 'id')
        # for obj in posi_obj:
        #     posi_drop.append({
        #         'text': obj['position_name'],
        #         'value': obj['id'],
        #     })
        #
        # jobClass_obj = HrJobClass.objects.filter(job_class_status=True).values('job_class_name', 'id')
        # for obj in jobClass_obj:
        #     jobClass_drop.append({
        #         'text': obj['job_class_name'],
        #         'value': obj['id'],
        #     })
        #
        # jobGrade_obj = HrJobGrade.objects.filter(job_grade_status=True).values('job_grade_name', 'id')
        # for obj in jobGrade_obj:
        #     jobGrade_drop.append({
        #         'text': obj['job_grade_name'],
        #         'value': obj['id'],
        #     })
        #
        # jobDuty_obj = HrJobDuty.objects.filter(job_duty_status=True).values('job_duty_name', 'id')
        # for obj in jobDuty_obj:
        #     jobDuty_drop.append({
        #         'text': obj['job_duty_name'],
        #         'value': obj['id'],
        #     })
        #
        # payType_obj = HrPayType.objects.filter(pay_type_status=True).values('pay_type_name', 'id')
        # for obj in payType_obj:
        #     payType_drop.append({
        #         'text': obj['pay_type_name'],
        #         'value': obj['id'],
        #     })
        #
        # payType_obj = HrJobRank.objects.filter(job_rank_status=True).values('job_rank_name', 'id')
        # for obj in payType_obj:
        #     jobRank_drop.append({
        #         'text': obj['job_rank_name'],
        #         'value': obj['id'],
        #     })

        self.return_data = {
            'code': 200,
            'msg': '信息返回成功',
            'data': {
                # 'departmentOptions': dept_drop,
                # 'positionOptions': posi_drop,
                # 'jobClassOptions': jobClass_drop,
                # 'jobGradeOptions': jobGrade_drop,
                # 'payTypeOptions': payType_drop,
                # 'jobRankOptions': jobRank_drop,
                # 'jobDutyOptions': jobDuty_drop,
                # 'nationOptions': nation_drop,
                'politicalOptions': candidate_political_status_drop,
                'marriageOptions': candidate_marriage_status_drop,
                # 'identityOptions': candidate_identity_type_drop,
                'trainDegreeOptions': candidate_train_degree_type_drop,
                'firstDegreeTypeOptions': candidate_first_degree_type_drop,
                'firstDegreeOptions': candidate_first_degree_drop,
                # 'candidateDLOption': candidate_dl_drop,
                # 'nationPlaceOption': candidate_nation_place,
                'sexOption': sex_drop,
                # 'candidateStatusOption': candidate_status_drop,
            }
        }

    def get_index_bar(self):
        info = json.loads(self.request.body)
        try:
            language = info['language']
        except:
            language = 'Chinese'
        bar_obj = IndexBar.objects.all().values(
            'title_field',
            'icon',
            'url',
        )
        field_list = {}
        for bar in bar_obj:
            field_list[bar['title_field']] = ''
        field_list = translate(field_list, language)
        tableList = []
        for bar in bar_obj:
            tableList.append({
                'title': field_list[bar['title_field']],
                'icon': bar['icon'],
                'url': bar['url'],
            })
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功',
            'data': {
                'barList': tableList
            }
        }

    # 数据整理
    def info_data_tidy_up(self, code):
        print(code)
        flag = re.search(r'[a-zA-z]', str(code))
        if flag:
            employee_obj = HrEmployee.objects.filter(employee_code=code).values(
                'id',
                'employee_name',
                'employee_sex',
                'employee_nation_id',
                'employee_nation__nation_name',
                'employee_identity_no',
                'employee_identity_no_effective_date',
                'employee_identity_no_failre_date',
                'employee_birthday',
                'employee_email',
                'employee_nation_address',
                'employee_now_address',
                'employee_marriage_status',
                'employee_phone',
                'employee_political_status',
                'employee_emergency_contact',
                'employee_emergency_contact_phone',
                'employee_emergency_contact_relation',
                'employee_emergency_contact_company',
                'employee_emergency_contact_2',
                'employee_emergency_contact_phone_2',
                'employee_emergency_contact_relation_2',
                'employee_emergency_contact_company_2',
                'employee_first_degree_id',
                'employee_first_degree__edu_degree_name',
                'employee_first_degree_school',
                'employee_first_degree_major',
                'employee_first_degree_type',
                'employee_first_degree_graduate_date',
                'employee_train_degree',
                'employee_train_degree_school',
                'employee_train_degree_major',
                'employee_train_degree_type',
                'employee_train_degree_graduate_date',
                'employee_bank_deposit',
                'employee_bank_no',
                'employee_nationality',
                'employee_group_join_date',
                'employee_department__department_name',
                'employee_position__position_name',

            )
        else:
            employee_obj = HrEmployee.objects.filter(Q(employee_code=code) | Q(pk=code)).values(
                'id',
                'employee_name',
                'employee_sex',
                'employee_nation_id',
                'employee_nation__nation_name',
                'employee_identity_no',
                'employee_identity_no_effective_date',
                'employee_identity_no_failre_date',
                'employee_birthday',
                'employee_email',
                'employee_nation_address',
                'employee_now_address',
                'employee_marriage_status',
                'employee_phone',
                'employee_political_status',
                'employee_emergency_contact',
                'employee_emergency_contact_phone',
                'employee_emergency_contact_relation',
                'employee_emergency_contact_company',
                'employee_emergency_contact_2',
                'employee_emergency_contact_phone_2',
                'employee_emergency_contact_relation_2',
                'employee_emergency_contact_company_2',
                'employee_first_degree_id',
                'employee_first_degree__edu_degree_name',
                'employee_first_degree_school',
                'employee_first_degree_major',
                'employee_first_degree_type',
                'employee_first_degree_graduate_date',
                'employee_train_degree',
                'employee_train_degree_school',
                'employee_train_degree_major',
                'employee_train_degree_type',
                'employee_train_degree_graduate_date',
                'employee_bank_deposit',
                'employee_bank_no',
                'employee_nationality',
                'employee_group_join_date',
                'employee_department__department_name',
                'employee_position__position_name',
            )
        if employee_obj.exists() is False:
            self.return_data = {
                'code': 400,
                'msg': '未找到该工号信息'
            }
            return 0
        employee = employee_obj[0]
        for key, value in employee.items():
            if value == 'None' or value is None:
                employee[key] = ''
            elif value == 99999 or value == '99999' or value == '999999' or value == 999999:
                employee[key] = '未选择'
            if key == 'employee_group_join_date' and value != '' and value is not None:
                days = (arrow.now() - arrow.get(value)).days
                year = 0
                month = 0
                while days >= 365:
                    year += 1
                    days -= 365
                month = int(days / 30)
                employee[key] = f"在职{year}年{month}个月"
                value = f"在职{year}年{month}个月"
            if type(value) == datetime.date:
                employee[key] = arrow.get(value).format("YYYY-MM-DD")
            if type(value) == datetime.datetime:
                employee[key] = arrow.get(value).format("YYYY-MM-DD")
        if employee['employee_sex'] == '2':
            employee['employee_sex'] = '女'
        elif employee['employee_sex'] == '1':
            employee['employee_sex'] = '男'
        employee['experience_info'] = get_person_work_experience(employee['id'])
        employee['file'] = get_person_file(employee['id'])
        print(employee)
        return employee


def create_menu(data):
    pass


# 获取员工工作经历
def get_person_work_experience(employee_id):
    experience_obj = HrWorkExperience.objects.filter(employee_id=employee_id,
                                                     work_experience_status=True).values(
        "work_experience_hire_date", "work_experience_departure_date", "work_experience_company",
        "work_experience_position", "id", "employee_id")
    if experience_obj.exists():
        experience = [i for i in experience_obj]
    else:
        experience = []
    for expe in experience:
        for key, value in expe.items():
            if type(value) == datetime.date or type(value) == datetime.datetime:
                expe[key] = arrow.get(value).format("YYYY-MM-DD")
    return experience


# 获取员工文件信息
def get_person_file(employee_id):
    file_num = {
        1: 'candidate_identity_file',
        2: 'candidate_diploma_file',
        3: 'candidate_degree_file',
        4: 'candidate_title_or_skill_file',
        5: 'candidate_labor_contract_file',
        6: 'candidate_confidentiality_agreement_file',
        7: 'candidate_competition_file',
        8: 'candidate_base_info_file',
        9: 'candidate_legal_delivery_file',
        10: 'candidate_important_notice_file',
        11: 'candidate_entry_confire_file',
        12: 'candidate_leave_certificate_file',
        13: 'candidate_medical_report_file',
        14: 'candidate_resume_file',
        15: 'candidate_photo_file',
        16: 'candidate_bank_card_file',
        17: 'candidate_honest_file',
    }
    file_deal_obj = {}
    file_obj = HrEmployeeFiles.objects.filter(employee_id=employee_id, employee_file_status=True).annotate(
        name=F("employee_file_name"),
        url=F("employee_file_url"),
    ).values(
        "employee_id", "name", "url", "employee_file_type", "id")
    if file_obj.exists():
        for file in file_obj:
            if file['employee_id'] in file_deal_obj:
                if file['employee_file_type'] in file_deal_obj[file['employee_id']]:
                    file_deal_obj[file.pop('employee_id')][file.pop('employee_file_type')].append(file)
                else:
                    file_deal_obj[file.pop('employee_id')][file.pop('employee_file_type')] = [file]
            else:
                file_deal_obj[file.pop('employee_id')] = {file.pop('employee_file_type'): [file]}
    else:
        file_deal_obj[employee_id] = {}
    file_ = {}
    for file_type_num, file_field in file_deal_obj[employee_id].items():
        file_[file_num[file_type_num] + '_info'] = file_field
    return file_


def create_translate(field, language, value):
    pass
