# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 13:55
# @Author  : zhuang
# @Site    :
# @File    : controller.py
# @Software: PyCharm
import json
import os
import datetime
import time
from django.db import connection
from rest_framework.status import *

import competeRestrictions
from auther.models import *
from externalHonors.models import *
from pdss.settings import BASE_DIR
from salarySurvey.models import *
from salarySurvey.serializers import *
from externalHonors.serializers import *
from internalEvaluation.serializers import *
from employeeInspect.serializers import *
from rest_framework import status
from auther.models import *
from general.models import *
from employeeActivities.serializers import *
from rewardsPunishments.serializers import *
from employeeCare.serializers import *
from volumeContracts.serializers import *
from django.db.models import Q
from competeRestrictions.serializers import *


def upload_file(file, model_file, method, fileName):
    searchTime = datetime.datetime.now().strftime("%Y-%m-%d")
    if fileName == "" or fileName is None:
        fileName = searchTime + "_" + "".join(list(str(time.time()))[0:10]) + "_" + file.name
    try:
        if not os.path.exists(os.path.join(os.path.join(BASE_DIR, 'static'), model_file)):
            os.mkdir(os.path.join(os.path.join(BASE_DIR, 'static'), model_file))
        if not os.path.exists(os.path.join(os.path.join(os.path.join(BASE_DIR, 'static'), model_file), method)):
            os.mkdir(os.path.join(os.path.join(os.path.join(BASE_DIR, 'static'), model_file), method))
        dirname = os.path.join(os.path.join(os.path.join(BASE_DIR, 'static'), model_file), method)
        if not os.path.exists(os.path.join(dirname, searchTime)):
            os.mkdir(os.path.join(dirname, searchTime))
        else:
            pass
        fp = open(os.path.join(os.path.join(dirname, searchTime), fileName), 'wb+')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
        return os.path.join(os.path.join(dirname, searchTime), fileName), fileName
    except:
        pass
    return 0


class Controller:
    def __init__(self, model, meth, request):
        self.return_data = {}
        self.model = model
        # self.user_id=user_id
        self.meth = meth
        self.model_name = ''
        self.fileName = ''
        self.request = request
        self.model_many_obj = ''
        # self.user_base=()
        self.user_base = []
        self.user_jobRank = []
        # self.user_base =()
        # self.token = request.check_token
        self.file_path = {
            "salarySurvey": 'salaryFile',
            "SalarySurveyRecord": 'salaryFile',
            "externalHonors": 'externalFile',
            "ExternalHonorsList": 'externalFile',
            "MemorabiliaList": 'memorabiliaFile',
            "EmployeeActivitiesList": 'employeeFile',
            'InternalEvaluationList': 'internalEvaluationFile',
            'EmployeeInspect': 'employeeInspectFile',
            'ProjectBonus': 'projectBonusFile',
            'RewardsAndPunishments': 'rewardsAndPunishmentsFile',
            'TalentSubsidies': 'talentSubsidiesFile',
            'ExitInterviews': 'exitInterviewsFile',
            'Colloquium': 'colloquiumFile',
            'JobInterviews': 'jobInterviewsFile'
        }
        # 允许方法
        self.methods = {
            "patch": self.patch,
            "delete": self.delete,
            "get_list": self.get_list,
            "delete_other_file": self.delete_other_file,
            "upload_other_file": self.upload_other_file,
        }
        # 接受每个模型的条件查找的字段
        self.model_key = {
            "SalarySurveyRecord": ["searchName", "beginDate", "endDate"],
            "ExternalHonorsList": ["searchName", "beginDate", "endDate", "baseNameId"],
            "EmployeeActivitiesList": ["searchName", "beginDate", "endDate", "baseNameId"],
            'InternalEvaluationList': ["searchName", "beginDate", "endDate", 'searchBase'],
            'EmployeeInspect': ["beginDate", "endDate", 'baseNameId'],
            'ProjectBonus': ["beginDate", "endDate", 'baseNameId'],
            'RewardsAndPunishments': ['beginDate', 'endDate', 'baseNameId'],
            'TalentSubsidies': ['beginDate', 'endDate', 'baseNameId'],
            'ExitInterviews': ['beginDate', 'endDate', 'baseNameId'],
            'Colloquium': ['beginDate', 'endDate', 'searchBase'],
            'JobInterviews': ['beginDate', 'endDate', 'baseNameId'],
            # 'ContractsInfo': ['beginDate', 'endDate'],
            'ContractsInfo': ['beginDate', 'endDate', 'jobRankId', 'name', 'code'],
            'CompeteRestrictions': ['beginDate', 'endDate', 'name', 'idCard'],
            # 'CompeteRestrictionsWhitelist':['beginDate', 'endDate','name','idCard']
            'CompeteRestrictionsWhitelist': ['name', 'idCard']

        }
        # 查找条件
        self.model_fields = {
            "EmployeeActivitiesList": {
                "searchName": "employee_activities_name__contains",
                "beginDate": "employee_activities_date__gte",
                "endDate": "employee_activities_date__lte",
                "baseNameId": "employee_base_id",
                "user_base": "employee_base__in",
            },
            "InternalEvaluationList": {  # models名 内部评优
                "searchName": "awards_name__contains",  # 奖项名称
                "beginDate": "awards_date__gte",
                "endDate": "awards_date__lte",
                # 'searchBase': 'evaluation_company__contains'  # 公司名
                "searchBase": "evaluation_company_id",
                "user_base": "evaluation_company__in",
            },
            "EmployeeInspect": {  # models名  员工稽核
                "beginDate": "employee_inspect_date__gte",
                "endDate": "employee_inspect_date__lte",
                "baseNameId": "employee_inspect_base_id",
                "user_base": "employee_inspect_base__in",
            },
            "ProjectBonus": {
                "beginDate": "project_bonus_date__gte",
                "endDate": "project_bonus_date__lte",
                "baseNameId": "project_bonus_base_id",
                "user_base": "project_bonus_base__in",
            },
            'RewardsAndPunishments': {
                "beginDate": "r_p_date__gte",
                "endDate": "r_p_date__lte",
                "baseNameId": "r_p_base_id",
                "user_base": "r_p_base__in",
            },

            "JobInterviews": {  # 在职访谈
                "beginDate": "job_interviews_date__gte",
                "endDate": "job_interviews_date__lte",
                "baseNameId": "job_interviews_base_id",
                "user_base": "job_interviews_base__in",
            },
            "Colloquium": {  # 座談會
                "beginDate": "colloquium_date__gte",
                "endDate": "colloquium_date__lte",
                "searchBase": "colloquium_base_id",
                "user_base": "colloquium_base__in",
            },
            "ExitInterviews": {  # 离职访谈
                "beginDate": "exit_interviews_date__gte",
                "endDate": "exit_interviews_date__lte",
                "baseNameId": "exit_interviews_base_id",
                "user_base": "exit_interviews_base__in",
            },
            'TalentSubsidies': {  # 人才补贴
                "beginDate": "talent_subsidies_date__gte",
                "endDate": "talent_subsidies_date__lte",
                "baseNameId": "talent_subsidies_base_id",
                "user_base": "talent_subsidies_base__in",
            },
            'ContractsInfo': {
                "beginDate": "entryData__gte",
                "endDate": "entryData__lte",
                # "user_base": "talent_subsidies_base__in",
                'baseNameId': 'jobRank__in',
                # "name": "name__contains",
                # "searchName":"(Q(name__contains=searchName) | Q(code__contains=searchName))"
            },
            'CompeteRestrictions': {
                "beginDate": "cycleData__gte",
                "endDate": "cycleData__lte",
                'baseNameId': 'jobRank__in',
                # "searchName": "name__contains",
            },
            'CompeteRestrictionsWhitelist': {
                # "beginDate": "cycleData__gte",
                # "endDate": "cycleData__lte",
                # 'baseNameId': 'cr_base__in',
                "baseNameId": "cr_base_id",
                "user_base": "cr_base__in",
                # "searchName": "idCard__contains",
            }

        }
        # 序列化模型
        self.serializers = {
            "ExternalHonorsList": HonorRecordGetSerializers,
            "SalarySurveyRecord": SalarySurveyRecordGetSerializers,
            "EmployeeActivitiesList": EmployeeActivitiesListGetSerializers,
            'InternalEvaluationList': InternalEvaluationListSerializers,
            'EmployeeInspect': EmployeeInspectSerializers,
            'ProjectBonus': ProjectBonusSerializers,
            'RewardsAndPunishments': RewardsAndPunishmentsSerializers,

            'TalentSubsidies': TalentSubsidiesSerializers,
            'ExitInterviews': ExitInterviewsSerializers,
            'Colloquium': ColloquiumSerializers,
            'JobInterviews': JobInterviewsSerializers,
            'ContractsInfo': ContractsInfoSerializers,
            'CompeteRestrictions': CompeteRestrictionSerializers,
            'CompeteRestrictionsWhitelist': CompeteRestrictionsWhitelistSerializers,

        }
        # 忽略的字段
        self.except_field = ["create_time", "modify_time", "fix_detail_creator", "fix_detail_modifier", "status",
                             'awards_status',
                             "other_file_info", "honor_status", "creator", "modifier", "employee_activities_status",
                             'employee_inspect_status', 'project_bonus_status', 'r_p_status', 'job_interviews_status',
                             'coll_interviews_status', 'exit_interviews_status', 'talent_subsidies_status',
                             'contracts_status', 'compete_status']
        # 每个模型对应的状态字段
        self.model_statues = {
            "ExternalHonorsList": "honor_status",
            "SalarySurveyRecord": "status",
            "EmployeeActivitiesList": "employee_activities_status",
            'InternalEvaluationList': 'awards_status',
            'EmployeeInspect': 'employee_inspect_status',
            'ProjectBonus': 'project_bonus_status',
            'RewardsAndPunishments': 'r_p_status',

            'ExitInterviews': 'exit_interviews_status',
            'Colloquium': 'coll_interviews_status',
            'JobInterviews': 'job_interviews_status',
            'TalentSubsidies': 'talent_subsidies_status',
            'ContractsInfo': 'contracts_status',
            'CompeteRestrictions': 'compete_status',
            'CompeteRestrictionsWhitelist': 'compete_status'
        }

    # 无返回的执行
    def start(self):

        self.return_data = {'code': HTTP_403_FORBIDDEN, "msg": '没有权限访问'}
        if self.request.check_token is None:
            return self.return_data
        self.model_name = self.model.__name__
        self.user_base = self.request.user_base
        self.methods[self.meth]()

        # #print(self.return_data)
        return self.return_data

    # 有返回的执行
    def data_start(self):
        self.return_data = {'code': HTTP_403_FORBIDDEN, "msg": '没有权限访问'}
        if self.request.check_token is None:
            return self.return_data
        self.model_name = self.model.__name__
        self.user_base = self.request.user_base
        self.methods[self.meth]()

        return self.return_data

    # 修改单行数据
    def patch(self):
        """
        需要添加修改的内容
        :return:
        """
        ls_file = ['awards_data']  # 必选字段
        info = json.loads(self.request.body)
        # #print(info,type(info))
        # pk = info['id']
        # EmployeeInspect.objects.filter(pk=pk).update(employee_inspect_night_shift_no=4, employee_inspect_day_shift_no=1)

        kwargs = {}
        kwargs['modifier_id'] = self.request.check_token
        for key, value in info.items():
            if key in ls_file and info[key] == '':
                self.return_data = {
                    "code": status.HTTP_200_OK,
                    "msg": "内部评优时间为空,必填"
                }
                # #print(self.return_data)
            else:
                break
        pk = info['id']
        # 不修改的数据
        no_patch = ['historical_payslip', 'honor_upload_declare_files', 'honor_medal_photos',
                    "employee_activities_plans",
                    "employee_activities_photos", 'awards_photos', 'employee_inspect_photos', 'employee_inspect_plans',
                    'colloquium_photos']
        del info['id']
        field_list = []
        for i in self.model._meta.get_fields():
            field_list.append(i.name)
        for i in info:
            if i in field_list and i not in no_patch:
                kwargs[i] = info[i]
        if "honor_base" in kwargs:
            kwargs["honor_base"] = info['honor_base_id']
        if "employee_base" in kwargs:
            kwargs["employee_base"] = info['employee_base_id']
        if "evaluation_company" in kwargs:
            kwargs["evaluation_company"] = info['evaluation_company_id']
        if "employee_inspect_base" in kwargs:
            kwargs["employee_inspect_base"] = info['employee_inspect_base_id']
        if "project_bonus_base" in kwargs:
            kwargs["project_bonus_base"] = info['project_bonus_base_id']
            if kwargs['project_bonus_total'] != None and kwargs['project_bonus_person_no'] != None:
                kwargs['project_bonus_average'] = eval(str(kwargs['project_bonus_total'])) / eval(
                    str(kwargs['project_bonus_person_no']))
        if "project_bonus_date" in kwargs:
            if info['project_bonus_date'] != None:
                if len(info['project_bonus_date']) == 7:  # 年月
                    kwargs["project_bonus_date"] = info['project_bonus_date'] + '-01'
                elif len(info['project_bonus_date']) == 10:  # 年月日
                    pass
            # #print(info['project_bonus_date'],type(info['project_bonus_date']))
        if "r_p_date" in kwargs:
            if info['r_p_date'] != None:
                if len(info['r_p_date']) == 7:  # 年月
                    kwargs["r_p_date"] = info['r_p_date'] + '-01'
                elif len(info['r_p_date']) == 10:  # 年月日
                    pass

        if "colloquium_date" in kwargs:
            if info['colloquium_date'] != None:
                if len(info['colloquium_date']) == 7:  # 年月
                    kwargs["colloquium_date"] = info['colloquium_date'] + '-01'
                elif len(info['colloquium_date']) == 10:  # 年月日
                    pass
        if "job_interviews_date" in kwargs:
            if info['job_interviews_date'] != None:
                if len(info['job_interviews_date']) == 7:  # 年月
                    kwargs["job_interviews_date"] = info['job_interviews_date'] + '-01'
                elif len(info['job_interviews_date']) == 10:  # 年月日
                    pass

        if "r_p_base" in kwargs:
            kwargs["r_p_base"] = info['r_p_base_id']
            if kwargs['rewards_money'] != None and kwargs['rewards_person_no'] != None:
                kwargs['rewards_average'] = eval(str(kwargs['rewards_money'])) / eval(str(kwargs['rewards_person_no']))
            if kwargs['punishments_money'] != None and kwargs['punishments_person_no'] != None:
                kwargs['punishments_average'] = eval(str(kwargs['punishments_money'])) / eval(
                    str(kwargs['punishments_person_no']))

        if "talent_subsidies_base" in kwargs:
            kwargs["talent_subsidies_base"] = info['talent_subsidies_base_id']
        if "exit_interviews_base" in kwargs:
            kwargs["exit_interviews_base"] = info['exit_interviews_base_id']
        if 'colloquium_base' in kwargs:
            kwargs['colloquium_base'] = info['colloquium_base_id']
        if 'job_interviews_base' in kwargs:
            kwargs['job_interviews_base'] = info['job_interviews_base_id']

        if self.model == TalentSubsidies:
            kwargs['talent_subsidies_claimed'] = self.decision_num(kwargs['talent_subsidies_claimed'], int)  # 已领取HC
            kwargs['talent_subsidies_applied'] = self.decision_num(kwargs['talent_subsidies_applied'], int)  # 已申请HC
            kwargs['talent_subsidies_conditions'] = self.decision_num(kwargs['talent_subsidies_conditions'],
                                                                      int)  # 满足条件HC
            if info['talent_subsidies_date'] != None:
                if len(info['talent_subsidies_date']) == 7:  # 年月
                    kwargs["talent_subsidies_date"] = info['talent_subsidies_date'] + '-01'
                elif len(info['talent_subsidies_date']) == 10:  # 年月日
                    pass

            # try:
            #     if type(kwargs['talent_subsidies_claimed']) == str:
            #         kwargs['talent_subsidies_claimed'] = eval(kwargs['talent_subsidies_claimed'])
            # except:
            #     kwargs['talent_subsidies_claimed'] =None
            #
            # try:
            #     if type(kwargs['talent_subsidies_applied']) == str:
            #         kwargs['talent_subsidies_applied'] = eval(kwargs['talent_subsidies_applied'])
            # except:
            #     kwargs['talent_subsidies_applied'] =None
            #
            # try:
            #     if type(kwargs['talent_subsidies_conditions']) == str:
            #         kwargs['talent_subsidies_conditions'] = eval(kwargs['talent_subsidies_conditions'])
            # except:
            #     kwargs['talent_subsidies_conditions'] = None
            # #print(restore)
            # #print(kwargs)
            if kwargs['talent_subsidies_conditions'] != None and kwargs['talent_subsidies_applied'] != None and kwargs[
                'talent_subsidies_claimed'] != None:  # 三条数据都存在
                if kwargs['talent_subsidies_conditions'] >= kwargs['talent_subsidies_applied'] >= kwargs[
                    'talent_subsidies_claimed']:
                    kwargs = kwargs
                else:
                    self.return_data = {
                        "code": status.HTTP_401_UNAUTHORIZED,
                        "msg": "修改失败，关系不对"
                    }
                    # print('不加3')
                    kwargs = {}
            elif (kwargs['talent_subsidies_conditions'] != None and kwargs['talent_subsidies_applied'] != None) or (
                    kwargs['talent_subsidies_conditions'] != None and kwargs['talent_subsidies_claimed'] != None) or (
                    kwargs['talent_subsidies_applied'] != None and kwargs[
                'talent_subsidies_claimed'] != None):  # 存在两条数据
                if kwargs['talent_subsidies_conditions'] == None:
                    if kwargs['talent_subsidies_applied'] >= kwargs['talent_subsidies_claimed']:
                        kwargs = kwargs
                    else:
                        self.return_data = {
                            "code": status.HTTP_401_UNAUTHORIZED,
                            "msg": "修改失败，关系不对"
                        }
                        # print('不加2')
                        kwargs = {}
                elif kwargs['talent_subsidies_applied'] == None:
                    if kwargs['talent_subsidies_conditions'] >= kwargs['talent_subsidies_claimed']:
                        kwargs = kwargs
                    else:
                        self.return_data = {
                            "code": status.HTTP_401_UNAUTHORIZED,
                            "msg": "修改失败，关系不对"
                        }
                        # print('不加2')
                        kwargs = {}
                elif kwargs['talent_subsidies_claimed'] == None:
                    if kwargs['talent_subsidies_conditions'] >= kwargs['talent_subsidies_applied']:
                        kwargs = kwargs
                    else:
                        self.return_data = {
                            "code": status.HTTP_401_UNAUTHORIZED,
                            "msg": "修改失败，关系不对"
                        }
                        # print('不加2')
                        kwargs = {}
            elif kwargs['talent_subsidies_conditions'] == None or kwargs['talent_subsidies_applied'] == None or kwargs[
                'talent_subsidies_claimed'] == None:
                kwargs = kwargs
                # #print("true:", data_kwargs,"有一条数据是空的也加")

        if self.model == ExitInterviews:
            kwargs['exit_interviews_numberInterviews'] = self.decision_num(kwargs['exit_interviews_numberInterviews'],
                                                                           int)
            kwargs['exit_interviews_retentionSuccess'] = self.decision_num(kwargs['exit_interviews_retentionSuccess'],
                                                                           int)
            if info['exit_interviews_date'] != None:
                if len(info['exit_interviews_date']) == 7:  # 年月
                    kwargs["exit_interviews_date"] = info['exit_interviews_date'] + '-01'
                elif len(info['exit_interviews_date']) == 10:  # 年月日
                    pass
            # try:
            #     if type(kwargs['exit_interviews_numberInterviews']) == str:
            #         kwargs['exit_interviews_numberInterviews'] = eval(kwargs['exit_interviews_numberInterviews'])
            #     elif type(kwargs['exit_interviews_numberInterviews']) == int:
            #         kwargs['exit_interviews_numberInterviews'] =kwargs['exit_interviews_numberInterviews']
            # except:
            #     kwargs['exit_interviews_numberInterviews'] =None
            #
            # try:
            #     if type(kwargs['exit_interviews_retentionSuccess']) == str:
            #         kwargs['exit_interviews_retentionSuccess'] = eval(kwargs['exit_interviews_retentionSuccess'])
            #     elif type(kwargs['exit_interviews_retentionSuccess']) == int:
            #         kwargs['exit_interviews_retentionSuccess'] =kwargs['exit_interviews_retentionSuccess']
            # except:
            #     kwargs['exit_interviews_retentionSuccess'] =None

            if kwargs['exit_interviews_numberInterviews'] != None and kwargs[
                'exit_interviews_retentionSuccess'] != None:
                if kwargs['exit_interviews_numberInterviews'] >= kwargs['exit_interviews_retentionSuccess']:
                    kwargs['exit_interviews_retentionSuccessRate'] = kwargs['exit_interviews_retentionSuccess'] / \
                                                                     kwargs['exit_interviews_numberInterviews']
                else:
                    kwargs = {}
                    self.return_data = {
                        "code": status.HTTP_401_UNAUTHORIZED,
                        "msg": "修改失败，关系不对"
                    }
                    # print('不加')
            else:
                kwargs['exit_interviews_retentionSuccessRate'] = None

        if self.model == Colloquium:
            kwargs['colloquium_numberSessions'] = self.decision_num(kwargs['colloquium_numberSessions'], int)
            kwargs['colloquium_numberParticipants'] = self.decision_num(kwargs['colloquium_numberParticipants'], int)
            kwargs['colloquium_percentage'] = self.decision_num(kwargs['colloquium_percentage'], float)
            kwargs['colloquium_outputItems'] = self.decision_num(kwargs['colloquium_outputItems'], int)
            kwargs['colloquium_closeItem'] = self.decision_num(kwargs['colloquium_closeItem'], int)
            if kwargs['colloquium_percentage'] != None:
                if kwargs['colloquium_percentage'] > 1 or kwargs['colloquium_percentage'] < 0:
                    kwargs['colloquium_percentage'] = None

            if kwargs['colloquium_outputItems'] == None or kwargs['colloquium_closeItem'] == None:
                kwargs['colloquium_completionRate'] = None
            elif kwargs['colloquium_outputItems'] != None and kwargs['colloquium_closeItem'] != None and kwargs[
                'colloquium_outputItems'] >= kwargs['colloquium_closeItem']:
                kwargs['colloquium_completionRate'] = kwargs['colloquium_closeItem'] / kwargs['colloquium_outputItems']
            else:
                kwargs = {}
                self.return_data = {
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "msg": "数据关系不符合,用户数据修改失败"
                }

        if self.model == JobInterviews:
            kwargs['job_interviews_number'] = self.decision_num(kwargs['job_interviews_number'], int)  # 访谈人次
            kwargs['job_interviews_percentage'] = self.decision_num(kwargs['job_interviews_percentage'], float)
            kwargs['job_interviews_outputItem'] = self.decision_num(kwargs['job_interviews_outputItem'], int)
            kwargs['job_interviews_closeItem'] = self.decision_num(kwargs['job_interviews_closeItem'], int)

            if kwargs['job_interviews_percentage'] != None:
                if kwargs['job_interviews_percentage'] > 1 or kwargs['job_interviews_percentage'] < 0:
                    kwargs['job_interviews_percentage'] = None

            if kwargs['job_interviews_outputItem'] == None or kwargs['job_interviews_closeItem'] == None:
                kwargs['job_interviews_completionRate'] = None
            elif kwargs['job_interviews_outputItem'] != None and kwargs['job_interviews_closeItem'] != None and kwargs[
                'job_interviews_outputItem'] >= kwargs['job_interviews_closeItem']:
                kwargs['job_interviews_completionRate'] = kwargs['job_interviews_closeItem'] / kwargs[
                    'job_interviews_outputItem']
            elif kwargs['job_interviews_outputItem'] != None and kwargs['job_interviews_closeItem'] != None and kwargs[
                'job_interviews_outputItem'] < kwargs['job_interviews_closeItem']:
                kwargs = {}
                self.return_data = {
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "msg": "数据关系不符合,用户数据修改失败"
                }
            else:
                kwargs = {}
                self.return_data = {
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "msg": "用户数据修改失败"
                }
                # {'id': 175, 'colloquium_base': '润阳新能源', 'colloquium_photos': 0, 'colloquium_date': None,
                #  'colloquium_numberSessions': '33', 'colloquium_numberParticipants': '3', 'colloquium_percentage': '3',
                #  'colloquium_outputItems': '3', 'colloquium_closeItem': 33, 'colloquium_completionRate': '32',
                #  'colloquium_typical': '2', 'colloquium_remark': '2', 'create_time': '2023-05-30T10:23:05.996892',
                #  'modify_time': '2023-05-30T10:23:05.996892', 'creator': 2, 'modifier': None, 'colloquium_base_id': 1,
                #  'colloquium_photos_files': [], 'index': 4}

        if self.model == EmployeeInspect:
            if len(str(kwargs['employee_inspect_day_shift_no'])) == 0:
                kwargs['employee_inspect_day_shift_no'] = None
            if len(str(kwargs['employee_inspect_night_shift_no'])) == 0:
                kwargs['employee_inspect_night_shift_no'] = None

            if kwargs['employee_inspect_day_shift_no'] != None:
                if int(kwargs['employee_inspect_day_shift_no']) < 0:
                    kwargs['employee_inspect_day_shift_no'] = None
                    self.return_data = {
                        "code": 400,
                        "msg": "数据关系不符,修改失败"
                    }
            if kwargs['employee_inspect_night_shift_no'] != None:
                if int(kwargs['employee_inspect_night_shift_no']) < 0:
                    kwargs['employee_inspect_night_shift_no'] = None
                    self.return_data = {
                        "code": 400,
                        "msg": "数据关系不符,修改失败"
                    }

        if self.model == ProjectBonus:
            kwargs['project_bonus_no'] = self.decision_num(kwargs['project_bonus_no'], int)
            kwargs['project_bonus_reach_no'] = self.decision_num(kwargs['project_bonus_reach_no'], int)
            kwargs['project_bonus_total'] = self.decision_num(kwargs['project_bonus_total'], float)
            kwargs['project_bonus_person_no'] = self.decision_num(kwargs['project_bonus_person_no'], int)
            if kwargs['project_bonus_no'] != None and kwargs['project_bonus_reach_no'] != None:
                if kwargs['project_bonus_no'] < kwargs['project_bonus_reach_no']:
                    kwargs['project_bonus_reach_no'] = None
            if kwargs['project_bonus_total'] != None and kwargs['project_bonus_person_no'] != None:
                kwargs['project_bonus_average'] = kwargs['project_bonus_total'] / kwargs['project_bonus_person_no']
        # kwargs['modifier_id']=self.request.check_token
        # print("kwargs", kwargs)
        self.model.objects.filter(pk=pk).update(**kwargs)
        # print(self.model.objects.filter(pk=pk).update(**kwargs))
        # print(type(self.model.objects.filter(pk=pk).update(**kwargs)))

        # #print(key,value)
        # c={'employee_inspect_night_shift_no': 5, 'employee_inspect_day_shift_no': 7}
        # EmployeeInspect.objects.filter(pk=pk).update(employee_inspect_night_shift_no=14,employee_inspect_day_shift_no=16)

        #
        # if info['awards_date'] == '':
        #     self.return_data = {
        #         "code": status.HTTP_200_OK,
        #         "msg": "内部评优时间为空,必填"
        #     }
        #     #print(self.return_data)
        # else:
        #     pk = info['id']
        #     #print('pk',pk)
        #     #不修改的数据
        #     no_patch = ['historical_payslip', 'honor_upload_declare_files', 'honor_medal_photos',
        #                 "employee_activities_plans",
        #                 "employee_activities_photos", 'awards_photos']
        #     del info['id']
        #     kwargs = {}
        #     field_list = []
        #     for i in self.model._meta.get_fields():
        #         field_list.append(i.name)
        #     for i in info:
        #         if i in field_list and i not in no_patch:
        #             kwargs[i] = info[i]
        #
        #     if "honor_base" in kwargs:
        #         kwargs["honor_base"] = info['honor_base_id']
        #     if "employee_base" in kwargs:
        #         kwargs["employee_base"] = info['employee_base_id']
        #     if "evaluation_company" in kwargs:
        #         kwargs["evaluation_company"] = info['evaluation_company_id']
        #
        #     self.model.objects.filter(pk=pk).update(**kwargs)

    # 删除选中数据
    def delete(self):
        # print(self.request.body)
        infos = json.loads(self.request.body)['idList']
        kwargs = {
            self.model_statues[self.model_name]: "0"
        }
        kwargs['modifier_id'] = self.request.check_token
        for pk in infos:
            self.model.objects.filter(pk=int(pk)).update(**kwargs)

    # 删除附件 通用
    def delete_other_file(self):
        file_id = json.loads(self.request.body)['file_id']
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "请求删除的附件为空"
        }
        if file_id != "":
            try:
                UploadFiles.objects.filter(id=file_id).update(status=0)
                self.return_data = {
                    "code": 200,
                    "msg": "附件删除成功"
                }
            except Exception as e:
                # print(e)
                self.return_data = {
                    "code": 400,
                    "msg": "附件删除失败"
                }

        return self.return_data

    # get获取数据
    def get_list(self):
        import arrow
        utc1 = arrow.utcnow()
        columnList = [{"value": "序号", "label": "index", "width": "60"}, ]
        tableList = []
        count_len = {}

        currentPage = eval(self.request.GET.get("currentPage", None)) if self.request.GET.get("currentPage",
                                                                                              None) != "" else 1
        pageSize = eval(self.request.GET.get("pageSize", None)) if self.request.GET.get("pageSize", None) != "" else 25
        kwargs = {
            self.model_statues[self.model_name]: 1
        }
        model_conditions = self.model_fields[self.model_name]
        get_obj = self.request.GET

        for key, value in get_obj.items():
            if value != "" and key in self.model_key[self.model_name]:
                kwargs[model_conditions[key]] = value

        for key, value in kwargs.items():
            if "period" in key:
                kwargs[key] = datetime.datetime.strptime(value, "%Y-%m-%d")
            if "name" in key:
                kwargs[key] = value.strip()

        # print(self.user_base,type(self.user_base))
        if self.model_name != "SalarySurveyRecord":
            if self.model_name == 'ContractsInfo' or self.model_name == 'CompeteRestrictions' or self.model_name == 'CompeteRestrictionsWhitelist':
                pass
            else:
                kwargs[model_conditions['user_base']] = self.user_base

        if self.model_name == 'ContractsInfo':
            # print(self.request.GET.get('searchName',''))
            searchName = self.request.GET.get('searchName', '')
            baseNameId = self.request.GET.get('baseNameId', None)
            # print(searchName)
            if len(baseNameId) == 0 or baseNameId == None:
                kwargs['jobRank__in'] = self.request.user_jobRank
                # kwargs['jobRank__in'] =[1,2,3,4,5,6,7,8,9,10,11]
            else:
                kwargs['jobRank'] = baseNameId
            # kwargs['jobRank__in'] = self.request.u_serjobRank
            # print(kwargs)
            obj = self.model.objects.filter(Q(name__contains=searchName) | Q(code__contains=searchName),
                                            **kwargs).order_by('-create_time')
            # print(obj)
        # elif self.model_name=='CompeteRestrictions':
        #     searchName = self.request.GET.get('searchName', '')
        #     baseNameId = self.request.GET.get('baseNameId', None)
        #     if len(baseNameId)==0 or baseNameId==None:
        #         kwargs['people__jobRank__in'] = self.request.user_jobRank
        #     else:
        #         kwargs['people__jobRank'] = baseNameId
        #     obj = self.model.objects.filter(Q(name__contains=searchName) | Q(idCard__contains=searchName),
        #                                     **kwargs).order_by('-create_time')
        elif self.model_name == 'CompeteRestrictionsWhitelist':  # 竞业
            searchName = self.request.GET.get('searchName', '')
            baseNameId = self.request.GET.get('baseNameId', None)
            deptName = self.request.GET.get("contract", None)
            isExpiration = self.request.GET.get("isExpiration", None)
            dept_list = CompeteRestrictionsWhitelist.objects.filter(Q(contract__isnull=False) & ~Q(contract=''),
                                                                    compete_status=True).values("contract").distinct()
            dept_list = [{"label": i['contract'], "value": i['contract']} for i in dept_list]
            if searchName == '' or searchName == None or len(str(searchName)) == 0 \
                    and baseNameId == '' or baseNameId == None or len(str(baseNameId)) == 0 \
                    and deptName == "" or deptName == None or len(str(deptName)) == 0 \
                    and isExpiration == "" or isExpiration == None or len(str(isExpiration)) == 0:  # 全查
                kwargs['cr_base__in'] = self.request.user_base

            if len(baseNameId) == 0 or baseNameId == None:
                kwargs['cr_base__in'] = self.user_base
            else:
                kwargs['cr_base'] = baseNameId

            if deptName is not None and deptName != '':
                kwargs['contract'] = deptName  # 合同归属
            if isExpiration != '':
                kwargs['isExpiration'] = isExpiration  # 是否届满
            # print(kwargs)
            obj = self.model.objects.filter(
                Q(name__contains=searchName) | Q(idCard__contains=searchName) | Q(workNumber__contains=searchName),
                **kwargs).order_by('-create_time')
            # print(obj)
            # print(obj)
            # beginDate1 = self.request.GET.get('beginDate', '')
            # endDate1 = self.request.GET.get('endDate', '')
            # kwargs2 = {}
            # if beginDate1 != "" and endDate1 != "":
            #     kwargs2['cycleData__gte'] = datetime.datetime(1901, 10, 29, 7, 17, 1,177) if beginDate1 == None else beginDate1
            #     kwargs2['cycleData__lte'] = datetime.datetime(2521, 10, 29, 7, 17, 1, 177) if endDate1 == None else endDate1
            # if len(kwargs2) >= 2:
            #     obj3 = []
            #     for i in obj:
            #         obj2 = i.people.filter(**kwargs2).order_by('-create_time')
            #         if obj2.exists():
            #             obj3.append(i)
            #         else:
            #             pass
            #     id_list = [i.id for i in obj3]
            #     obj = self.model.objects.filter(pk__in=id_list)
            #
            # # print(kwargs)
            # print(obj)


        else:
            print(kwargs)
            obj = self.model.objects.filter(**kwargs, ).order_by('-create_time')
    #     all_whiteid = [item['id'] for item in tableList]
        yeshu = obj.count()
        database_time = time.time()
        serializer_obj = self.serializers[self.model_name](
            instance=obj,
            many=True).data

        # print("计算tableList花费{0}s".format(time.time() - database_time))

        for field in self.model._meta.get_fields():
            # print("1111",field.verbose_name)
            if field.name not in self.except_field:
                try:
                    if field.verbose_name == "公司":
                        columnList.append({
                            "value": "中心/事业部",
                            "label": "base_father",
                            "width": "180",
                        })
                    field_label = {
                        "value": field.verbose_name,
                        "label": field.name,
                        "width": self.count_character(field.verbose_name),
                    }
                    if "period" in field_label['label']:
                        field_label['width'] = "120"
                    # print(field_label)
                    columnList.append(field_label)
                except AttributeError:
                    pass

        for i in serializer_obj:
            try:
                del i['awards_status']
            except:
                pass
            try:
                del i['project_bonus_status']
            except:
                pass
            try:
                del i['employee_inspect_status']
            except:
                pass
            try:
                del i['r_p_status']
            except:
                pass
            try:
                del i['talent_subsidies_status']
            except:
                pass
            try:
                del i['exit_interviews_status']
            except:
                pass
            try:
                del i['coll_interviews_status']
            except:
                pass

            base_ls = ['evaluation_company', 'employee_inspect_base', 'project_bonus_base', 'r_p_base',
                       'talent_subsidies_base', 'exit_interviews_base', 'colloquium_base', 'job_interviews_base',
                       'cr_base']
            file_ls = ['awards_photos', 'employee_inspect_photos', 'employee_inspect_plans', 'colloquium_photos']

            # file_ls2=['insured_file','incomeTax_file','accumulationFund_file','workPhotos_file','workVideo_file','dailyPhotos_file','dailyVideo_file','incumbency_file','noWork_file']

            choice_ls = [
                'gender',
                'nativePlaceId',
                'politicsStatus',
                'accountNature',
                'nationId',
                'marriage',
                'urgentRelation',
                'latestDegreeId',
                'educateMethod',
                'summerSize',
                'jobRank',
            ]
            for key, value in dict(i).items():

                count_len[key] = self.count_character(value) if key not in count_len or count_len[
                    key] < self.count_character(value) else self.count_character(value)
                if key in base_ls:

                    k = {
                        'name': i[key],
                        'status': True,
                    }

                    try:
                        id = list(center_base.objects.filter(**k).values_list('id', flat=True))[0]
                    except:
                        id = None
                    i[key + '_id'] = id
                    # print('1',i[key + '_id'])

                if key in file_ls:
                    # #print(key)
                    ooo = self.model.objects.filter(id=int(i['id'])).first()
                    if key == 'awards_photos':
                        i[key + '_files'] = ooo.awards_photos.filter(status=True).values('id', 'file_url', 'file_name')
                    elif key == 'employee_inspect_photos':
                        i[key + '_files'] = ooo.employee_inspect_photos.filter(status=True).values('id', 'file_url',
                                                                                                   'file_name')
                    elif key == 'employee_inspect_plans':
                        i[key + '_files'] = ooo.employee_inspect_plans.filter(status=True).values('id', 'file_url',
                                                                                                  'file_name')
                    elif key == 'colloquium_photos':
                        i[key + '_files'] = ooo.colloquium_photos.filter(status=True).values('id', 'file_url',
                                                                                             'file_name')
                    # #print(i)
                    for j in i[key + '_files']:
                        j['name'] = j['file_name']
                        j['url'] = j['file_url']
                        del j['file_url']
                        del j['file_name']

                if key in choice_ls:
                    if self.model_name == 'ContractsInfo':
                        i[key + '_id'] = \
                            ContractsInfo.objects.filter(contracts_status=True, id=i['id']).values_list(key, flat=True)[
                                0]
                    elif self.model_name == 'CompeteRestrictions':
                        i[key + '_id'] = \
                            CompeteRestrictions.objects.filter(compete_status=True, id=i['id']).values_list(
                                'people__' + key, flat=True)[0]

                # if key in file_ls2:
                #     print('11111',i)
                #     # ooo = self.model.objects.filter(id=int(i['id'])).first()
                #     # if key == 'insured_file':
                #     #     i[key + '_files'] = ooo.insured_file.filter(file_status=True).values('id', 'url', 'name')
                #     # if key == 'incomeTax_file':
                #     #     i[key + '_files'] = ooo.incomeTax_file.filter(file_status=True).values('id', 'url', 'name')
                #     # if key == 'accumulationFund_file':
                #     #     i[key + '_files'] = ooo.accumulationFund_file.filter(file_status=True).values('id', 'url', 'name')
                #     # if key == 'workPhotos_file':
                #     #     i[key + '_files'] = ooo.workPhotos_file.filter(file_status=True).values('id', 'url', 'name')
                #     # if key == 'workVideo_file':
                #     #     i[key + '_files'] = ooo.workVideo_file.filter(file_status=True).values('id', 'url', 'name')
                #     # if key == 'dailyPhotos_file':
                #     #     i[key + '_files'] = ooo.dailyPhotos_file.filter(file_status=True).values('id', 'url', 'name')
                #     # if key == 'dailyVideo_file':
                #     #     i[key + '_files'] = ooo.dailyVideo_file.filter(file_status=True).values('id', 'url', 'name')
                #     # if key == 'incumbency_file':
                #     #     i[key + '_files'] = ooo.incumbency_file.filter(file_status=True).values('id', 'url', 'name')
                #     # if key == 'noWork_file':
                #     #     i[key + '_files'] = ooo.noWork_file.filter(file_status=True).values('id', 'url', 'name')
                #     #

            tableList.append(dict(i))

        if self.model != CompeteRestrictionsWhitelist:
            for i, item in enumerate(tableList):
                item["index"] = pageSize * (currentPage - 1) + i + 1
            else:
                pass
        else:
            pass
        peoples = []
        for i in tableList:
            if self.model == EmployeeInspect:
                if i['employee_inspect_base_id'] == None or i['employee_inspect_date'] == None:
                    # #print(i['employee_inspect_date'],type(i['employee_inspect_date']))
                    pass
                else:
                    restore = i['employee_inspect_date']
                    i['employee_inspect_date'] = datetime.datetime.strptime(i['employee_inspect_date'], '%Y-%m-%d')
                    # #print(i['employee_inspect_date'],type(i['employee_inspect_date']))
                    month_day_count = EmployeeInspect.objects.filter(employee_inspect_status=True,
                                                                     employee_inspect_base_id=i[
                                                                         'employee_inspect_base_id'],
                                                                     employee_inspect_date__gte=
                                                                     self.get_first_last(i['employee_inspect_date'])[0],
                                                                     employee_inspect_date__lte=
                                                                     self.get_first_last(i['employee_inspect_date'])[
                                                                         1]).values_list(
                        'employee_inspect_day_shift_no', flat=True)

                    month_day_count = list(filter(None, month_day_count))

                    month_night_count = EmployeeInspect.objects.filter(employee_inspect_status=True,
                                                                       employee_inspect_base_id=i[
                                                                           'employee_inspect_base_id'],
                                                                       employee_inspect_date__gte=
                                                                       self.get_first_last(i['employee_inspect_date'])[
                                                                           0],
                                                                       employee_inspect_date__lte=
                                                                       self.get_first_last(i['employee_inspect_date'])[
                                                                           1]).values_list(
                        'employee_inspect_night_shift_no', flat=True)
                    month_night_count = list(filter(None, month_night_count))
                    month_count = sum(month_day_count) + sum(month_night_count)  # 该月白班稽查次数+夜班稽查次数
                    i['month_inspect_count'] = month_count

                    year_day_count = EmployeeInspect.objects.filter(employee_inspect_status=True,
                                                                    employee_inspect_base_id=i[
                                                                        'employee_inspect_base_id'],
                                                                    employee_inspect_date__gte=
                                                                    self.get_first_last(i['employee_inspect_date'])[2],
                                                                    employee_inspect_date__lte=
                                                                    self.get_first_last(i['employee_inspect_date'])[
                                                                        3]).values_list('employee_inspect_day_shift_no',
                                                                                        flat=True)

                    year_night_count = EmployeeInspect.objects.filter(employee_inspect_status=True,
                                                                      employee_inspect_base_id=i[
                                                                          'employee_inspect_base_id'],
                                                                      employee_inspect_date__gte=
                                                                      self.get_first_last(i['employee_inspect_date'])[
                                                                          2],
                                                                      employee_inspect_date__lte=
                                                                      self.get_first_last(i['employee_inspect_date'])[
                                                                          3]).values_list(
                        'employee_inspect_night_shift_no', flat=True)
                    year_day_count = list(filter(None, year_day_count))
                    year_night_count = list(filter(None, year_night_count))

                    year_count = sum(year_day_count) + sum(year_night_count)  # 该年白班稽查次数+夜班稽查次数
                    i['year_inspect_count'] = year_count

                    i['employee_inspect_date'] = restore  # 还原  restore

            elif self.model == ProjectBonus:
                restore = i['project_bonus_date']
                if i['project_bonus_date'] != None:
                    i['project_bonus_date'] = datetime.datetime.strptime(i['project_bonus_date'], '%Y-%m-%d')

                    if i['project_bonus_base_id'] == None or i['project_bonus_date'] == None:
                        pass
                    else:
                        year_project_bonus_total_count = ProjectBonus.objects.filter(
                            project_bonus_status=True,
                            project_bonus_base_id=i['project_bonus_base_id'],
                            project_bonus_date__gte=self.get_first_last(i['project_bonus_date'])[2],
                            project_bonus_date__lte=self.get_first_last(i['project_bonus_date'])[3]).values_list(
                            'project_bonus_total', flat=True)  # 年度奖金总额
                        year_project_bonus_total_count = list(filter(None, year_project_bonus_total_count))  # 列表去除None
                        i['year_project_bonus_total'] = sum(year_project_bonus_total_count)

                    i['project_bonus_date'] = restore[:7]  # 还原  restore
                    if i['project_bonus_average'] != None:
                        i['project_bonus_average'] = self.round_down(i['project_bonus_average'])

            elif self.model == RewardsAndPunishments:
                restore = i['r_p_date']
                if i['r_p_date'] != None:
                    i['r_p_date'] = datetime.datetime.strptime(i['r_p_date'], '%Y-%m-%d')
                    if i['r_p_base_id'] == None or i['r_p_date'] == None:
                        pass
                    elif i['rewards_money'] == None or i['rewards_person_no'] == None:
                        pass
                    elif i['punishments_money'] == None or i['punishments_person_no'] == None:
                        pass
                    else:
                        year_rewards_person_count = RewardsAndPunishments.objects.filter(r_p_status=True,
                                                                                         r_p_base_id=i[
                                                                                             'r_p_base_id'],
                                                                                         r_p_date__gte=
                                                                                         self.get_first_last(
                                                                                             i['r_p_date'])[2],
                                                                                         r_p_date__lte=
                                                                                         self.get_first_last(
                                                                                             i['r_p_date'])[
                                                                                             3]).values_list(
                            'rewards_person_no', flat=True)  # 年奖励累计人次
                        year_rewards_money_count = RewardsAndPunishments.objects.filter(r_p_status=True,
                                                                                        r_p_base_id=i[
                                                                                            'r_p_base_id'],
                                                                                        r_p_date__gte=
                                                                                        self.get_first_last(
                                                                                            i['r_p_date'])[2],
                                                                                        r_p_date__lte=
                                                                                        self.get_first_last(
                                                                                            i['r_p_date'])[
                                                                                            3]).values_list(
                            'rewards_money', flat=True)  # 年奖励累计金额
                        year_punishments_person_count = RewardsAndPunishments.objects.filter(r_p_status=True,
                                                                                             r_p_base_id=i[
                                                                                                 'r_p_base_id'],
                                                                                             r_p_date__gte=
                                                                                             self.get_first_last(
                                                                                                 i['r_p_date'])[2],
                                                                                             r_p_date__lte=
                                                                                             self.get_first_last(
                                                                                                 i['r_p_date'])[
                                                                                                 3]).values_list(
                            'punishments_person_no', flat=True)  # 年惩处累计人次
                        year_punishments_money_count = RewardsAndPunishments.objects.filter(r_p_status=True,
                                                                                            r_p_base_id=i[
                                                                                                'r_p_base_id'],
                                                                                            r_p_date__gte=
                                                                                            self.get_first_last(
                                                                                                i['r_p_date'])[2],
                                                                                            r_p_date__lte=
                                                                                            self.get_first_last(
                                                                                                i['r_p_date'])[
                                                                                                3]).values_list(
                            'punishments_money', flat=True)  # 年惩处累计金额
                        year_rewards_person_count = list(filter(None, year_rewards_person_count))
                        year_rewards_money_count = list(filter(None, year_rewards_money_count))
                        year_punishments_person_count = list(filter(None, year_punishments_person_count))
                        year_punishments_money_count = list(filter(None, year_punishments_money_count))

                        i['year_rewards_person_no'] = sum(year_rewards_person_count)
                        i['year_rewards_money'] = sum(year_rewards_money_count)
                        i['year_punishments_person_no'] = sum(year_punishments_person_count)
                        i['year_punishments_money'] = sum(year_punishments_money_count)

                    i['r_p_date'] = restore[:7]  # 还原  restore

                if i['rewards_average'] != None:
                    i['rewards_average'] = self.round_down(i['rewards_average'])
                if i['punishments_average'] != None:
                    i['punishments_average'] = self.round_down(i['punishments_average'])

            elif self.model == ExitInterviews:
                restore = i['exit_interviews_date']
                if i['exit_interviews_retentionSuccessRate'] != None:
                    i['exit_interviews_retentionSuccessRate'] = '{:.2f}%'.format(
                        i['exit_interviews_retentionSuccessRate'] * 100)
                if i['exit_interviews_base_id'] == None or i['exit_interviews_date'] == None:  # 无法统计
                    # #print(i['employee_inspect_date'],type(i['employee_inspect_date']))
                    pass
                else:  # 两个都不为None
                    # pass
                    try:
                        i['exit_interviews_date'] = datetime.datetime.strptime(i['exit_interviews_date'], '%Y-%m-%d')
                        year_exit_interviews_numberInterviews = ExitInterviews.objects.filter(
                            exit_interviews_status=True,
                            exit_interviews_base_id=i['exit_interviews_base_id'],
                            exit_interviews_date__gte=self.get_first_last(i['exit_interviews_date'])[2],
                            exit_interviews_date__lte=self.get_first_last(i['exit_interviews_date'])[3]).values_list(
                            'exit_interviews_numberInterviews', flat=True)  # 年度累计人次
                        year_exit_interviews_numberInterviews = list(
                            filter(None, year_exit_interviews_numberInterviews))  # 列表去除None
                        i['year_exit_interviews_numberInterviews'] = sum(year_exit_interviews_numberInterviews)
                    except:
                        pass

                if i['exit_interviews_date'] != None:  # 无法统计
                    i['exit_interviews_date'] = restore[:7]

            elif self.model == Colloquium:
                if i['colloquium_base_id'] == None or i['colloquium_date'] == None:  # 无法统计
                    # #print(i['employee_inspect_date'],type(i['employee_inspect_date']))
                    pass
                else:  # 两个都不为None
                    restore = i['colloquium_date']
                    i['colloquium_date'] = datetime.datetime.strptime(i['colloquium_date'], '%Y-%m-%d')
                    # #print(i['colloquium_date'],type(i['colloquium_date']))
                    year_colloquium_numberSessions = Colloquium.objects.filter(coll_interviews_status=True,
                                                                               colloquium_base_id=i[
                                                                                   'colloquium_base_id'],
                                                                               colloquium_date__gte=self.get_first_last(
                                                                                   i['colloquium_date'])[2],
                                                                               colloquium_date__lte=self.get_first_last(
                                                                                   i['colloquium_date'])[
                                                                                   3]).values_list(
                        'colloquium_numberSessions', flat=True)  # 年度累计场次
                    year_colloquium_numberParticipants = Colloquium.objects.filter(coll_interviews_status=True,
                                                                                   colloquium_base_id=i[
                                                                                       'colloquium_base_id'],
                                                                                   colloquium_date__gte=
                                                                                   self.get_first_last(
                                                                                       i['colloquium_date'])[2],
                                                                                   colloquium_date__lte=
                                                                                   self.get_first_last(
                                                                                       i['colloquium_date'])[
                                                                                       3]).values_list(
                        'colloquium_numberParticipants', flat=True)  # 年度累计人次

                    year_colloquium_numberSessions = list(filter(None, year_colloquium_numberSessions))  # 列表去除None
                    year_colloquium_numberParticipants = list(
                        filter(None, year_colloquium_numberParticipants))  # 列表去除None
                    i['year_colloquium_numberSessions'] = sum(year_colloquium_numberSessions)
                    i['year_colloquium_numberParticipants'] = sum(year_colloquium_numberParticipants)
                    i['colloquium_date'] = restore[:7]

                if i['colloquium_percentage'] != None:
                    i['colloquium_percentage'] = '{:.2f}%'.format(i['colloquium_percentage'] * 100)
                if i['colloquium_completionRate'] != None:
                    i['colloquium_completionRate'] = '{:.2f}%'.format(i['colloquium_completionRate'] * 100)

            elif self.model == JobInterviews:
                if i['job_interviews_base_id'] == None or i['job_interviews_date'] == None:  # 无法统计
                    # #print(i['employee_inspect_date'],type(i['employee_inspect_date']))
                    pass
                else:  # 两个都不为None
                    restore = i['job_interviews_date']
                    i['job_interviews_date'] = datetime.datetime.strptime(i['job_interviews_date'], '%Y-%m-%d')
                    # #print(i['colloquium_date'],type(i['colloquium_date']))
                    year_job_interviews_number = JobInterviews.objects.filter(job_interviews_status=True,
                                                                              job_interviews_base_id=i[
                                                                                  'job_interviews_base_id'],
                                                                              job_interviews_date__gte=
                                                                              self.get_first_last(
                                                                                  i['job_interviews_date'])[2],
                                                                              job_interviews_date__lte=
                                                                              self.get_first_last(
                                                                                  i['job_interviews_date'])[
                                                                                  3]).values_list(
                        'job_interviews_number', flat=True)  # 年度累计人次

                    year_job_interviews_number = list(filter(None, year_job_interviews_number))  # 列表去除None
                    i['year_job_interviews_number'] = sum(year_job_interviews_number)
                    i['job_interviews_date'] = restore[:7]

                if i['job_interviews_completionRate'] != None:
                    i['job_interviews_completionRate'] = '{:.2f}%'.format(i['job_interviews_completionRate'] * 100)
                if i['job_interviews_percentage'] != None:
                    i['job_interviews_percentage'] = '{:.2f}%'.format(i['job_interviews_percentage'] * 100)

            elif self.model == TalentSubsidies:
                if i['talent_subsidies_date'] != None:
                    i['talent_subsidies_date'] = i['talent_subsidies_date'][:7]

            elif self.model == CompeteRestrictionsWhitelist:
                # print(i)
                if len(i['people']) != 0:
                    for people in i['people']:
                        p = dict(people)
                        # print(p)
                        competeObj = CompeteRestrictions.objects.filter(id=p['id'], compete_status=True).first()
                        p['pId'] = people['id']  # 竞业id
                        p['compete_remark'] = i['compete_remark']
                        p['id'] = i['id']  # 白名单id
                        p['cr_base'] = i['cr_base']
                        p['cr_base_id'] = competeObj.people.cr_base_id
                        p['base_father'] = i['base_father']
                        p['cycleBeginData'] = i['cycleBeginData']
                        p['cycleEndData'] = i['cycleEndData']
                        p['isWhite'] = False
                        p['cycleData'] = str(p['cycleData'])[:7]
                        p['contract'] = i['contract']
                        p['workNumber'] = i['workNumber']
                        p['isExpiration'] = i['isExpiration']
                        p['create_time1']=str(competeObj.create_time)[:10]
                        p['modify_time1']=str(competeObj.modify_time)[:10]
                        file_ls2 = ['insured_file', 'incomeTax_file', 'accumulationFund_file', 'workPhotos_file',
                                    'workVideo_file', 'dailyPhotos_file', 'dailyVideo_file', 'incumbency_file',
                                    'noWork_file', 'photograph_file','cllBack_file','firstlivevideo_file','secondlivevideo_file']
                        for key in file_ls2:
                            if key == 'insured_file':
                                p[key + '_files'] = competeObj.insured_file.filter(file_status=True).values('id', 'url',
                                                                                                            'name')
                            if key == 'incomeTax_file':
                                p[key + '_files'] = competeObj.incomeTax_file.filter(file_status=True).values('id',
                                                                                                              'url',
                                                                                                              'name')
                            if key == 'accumulationFund_file':
                                p[key + '_files'] = competeObj.accumulationFund_file.filter(file_status=True).values(
                                    'id', 'url', 'name')
                            if key == 'workPhotos_file':
                                p[key + '_files'] = competeObj.workPhotos_file.filter(file_status=True).values('id',
                                                                                                               'url',
                                                                                                               'name')
                            if key == 'workVideo_file':
                                p[key + '_files'] = competeObj.workVideo_file.filter(file_status=True).values('id',
                                                                                                              'url',
                                                                                                              'name')
                            if key == 'dailyPhotos_file':
                                p[key + '_files'] = competeObj.dailyPhotos_file.filter(file_status=True).values('id',
                                                                                                                'url',
                                                                                                                'name')
                            if key == 'dailyVideo_file':
                                p[key + '_files'] = competeObj.dailyVideo_file.filter(file_status=True).values('id',
                                                                                                               'url',
                                                                                                               'name')
                            if key == 'incumbency_file':
                                p[key + '_files'] = competeObj.incumbency_file.filter(file_status=True).values('id',
                                                                                                               'url',
                                                                                                               'name')
                            if key == 'noWork_file':
                                p[key + '_files'] = competeObj.noWork_file.filter(file_status=True).values('id', 'url',
                                                                                                           'name')
                            if key == 'photograph_file':
                                p[key + '_files'] = competeObj.photograph_file.filter(file_status=True).values('id',
                                                                                                               'url',
                                                                                                               'name')
                            if key == 'cllBack_file':
                                p[key + '_files'] = competeObj.cllBack_file.filter(file_status=True).values('id',
                                                                                                               'url',
                                                                                                               'name')
                            if key == 'firstlivevideo_file':
                                p[key + '_files'] = competeObj.firstlivevideo_file.filter(file_status=True).values('id',
                                                                                                               'url',
                                                                                                               'name')
                            if key == 'secondlivevideo_file':
                                p[key + '_files'] = competeObj.secondlivevideo_file.filter(file_status=True).values('id',
                                                                                                               'url',
                                                                                                               'name')

                        peoples.append(p)
                else:
                    i['isWhite'] = True
                    i['pId'] = ''  # 竞业id
                    # i['cr_base_id'] = i['cr_base']
                    # i['jobRank'] = self.model.objects.filter(id=i['id']).first().get_jobRank_display()
                    file_ls2 = ['insured_file', 'incomeTax_file', 'accumulationFund_file', 'workPhotos_file',
                                'workVideo_file', 'dailyPhotos_file', 'dailyVideo_file', 'incumbency_file',
                                'noWork_file', 'photograph_file','cllBack_file','firstlivevideo_file','secondlivevideo_file']
                    for key in file_ls2:
                        i[key] = ''

                    i['cr_base_id'] = self.model.objects.filter(id=i['id']).values('cr_base_id')[0]['cr_base_id']

                    # print(i['jobRank'])

                    peoples.append(i)

            else:
                pass
        utc5 = arrow.utcnow()
        # print("3", peoples)
        if self.model == CompeteRestrictionsWhitelist:
            tableList = peoples
            for i, item in enumerate(tableList):
                item["index"] = i+1
            else:
                pass
        else:
            pass
        del columnList[1]

        if self.model == ContractsInfo:
            # print(columnList)
            del columnList[-1]  # 删除合同文档

            del columnList[-2]  # 删除上传照片
        else:
            pass
        # if self.model==CompeteRestrictions:
        #     # print(columnList)
        #     del columnList[1]  # 删除竞业人员
        utc6 = arrow.utcnow()
        if len(count_len) > 0:
            count_len['index'] = "60"
            for i in columnList:
                # i['width'] = max(int(i['width']), int(count_len[i['label'].lower()]))
                i['width'] = max(int(i['width']), int(count_len[i['label']]))
        for i in columnList:
            # #print(i)
            i['width'] = 400 if int(i['width']) > 400 else int(i['width'])
            if i['label'][-7:] == '_remark':
                i['width'] = ''

            if i['label'][-5:] == '_base':
                i['width'] = 160

            if self.model == ProjectBonus:
                if i['label'] == 'project_bonus_base':
                    i['width'] = 200
                if i['label'] == 'project_bonus_date':
                    i['width'] = 100
                if i['label'] == 'project_bonus_average':
                    i['width'] = 120
            if self.model == RewardsAndPunishments:
                if i['label'] == 'r_p_base':
                    i['width'] = 200
                if i['label'] == 'r_p_date':
                    i['width'] = 100
                if i['label'] == 'rewards_average':
                    i['width'] = 100


            if self.model == JobInterviews:
                if i['label'] == 'job_interviews_percentage':
                    i['width'] = 100
                if i['label'] == 'job_interviews_typical':
                    i['width'] = 800
                if i['label'] == 'job_interviews_remark':
                    i['width'] = 500
            if self.model == Colloquium:
                if i['label'] == 'colloquium_typical':
                    i['width'] = 800
                if i['label'] == 'colloquium_remark':
                    i['width'] = 500
            if self.model == ExitInterviews:
                if i['label'] == 'exit_interviews_typicalCase':
                    i['width'] = 800
                if i['label'] == 'exit_interviews_remark':
                    i['width'] = 500
            if self.model == EmployeeInspect:
                if i['label'] == 'employee_inspect_remark':
                    i['width'] = 800


        if self.model == EmployeeInspect:
            columnList.extend([{"value": "月度总稽核次数", "label": "month_inspect_count", "width": "70"},
                               {"value": "年度总稽核次数", "label": "year_inspect_count", "width": "70"}])
        if self.model == ProjectBonus:
            columnList.extend([{"value": "年度累计金额", "label": "year_project_bonus_total", "width": ''}])
        if self.model == RewardsAndPunishments:
            columnList.extend([{"value": "年度奖励累计人次", "label": "year_rewards_person_no", "width": 70},
                               {"value": "年度奖励累计金额", "label": "year_rewards_money", "width": ""},
                               {"value": "年度惩处累计人次", "label": "year_punishments_person_no", "width": 70},
                               {"value": "年度惩处累计金额", "label": "year_punishments_money", "width": ""},
                               ])

        if self.model == Colloquium:
            columnList.extend([{"value": "年度累计场次", "label": "year_colloquium_numberSessions", "width": 70},
                               {"value": "年度累计人次", "label": "year_colloquium_numberParticipants", "width": 70}])
        if self.model == JobInterviews:
            columnList.extend([{"value": "年度累计人次", "label": "year_job_interviews_number", "width": 100}])
        if self.model == ExitInterviews:
            columnList.extend(
                [{"value": "年度累计人次", "label": "year_exit_interviews_numberInterviews", "width": 70}])
        if self.model == CompeteRestrictionsWhitelist:
            columnList.extend(
                [{"value": '联系电话', "label": "phone", "width": 100},
                 {"value": "联系地址", "label": "address", "width": 200},
                 {"value": "竞业周期", "label": "cycleData", "width": 100},
                 {"value": "电话回访", "label": "cllBack_file", "width": 400},
                 {"value": "实时视频(第一次)", "label": "firstlivevideo_file", "width": 400},
                 {"value": "实时视频(第二次)", "label": "secondlivevideo_file", "width": 400},

                 {"value": "参保证明", "label": "insured_file", "width": 300},
                 {"value": "所得税缴税证明", "label": "incomeTax_file", "width": 300},
                 {"value": "公积金账户信息", "label": "accumulationFund_file", "width": 300},
                 {"value": "工作照片", "label": "workPhotos_file", "width": 300},
                 {"value": "工作视频", "label": "workVideo_file", "width": 300},
                 {"value": "日常照片", "label": "dailyPhotos_file", "width": 300},
                 {"value": "日常视频", "label": "dailyVideo_file", "width": 300},
                 {"value": "在职证明", "label": "incumbency_file", "width": 300},
                 {"value": "无工作承诺函", "label": "noWork_file", "width": 300},
                 {"value": "强制拍照", "label": "photograph_file", "width": 300},



                 {"value": "经度", "label": "lon", "width": 100},
                 {"value": "纬度", "label": "lat", "width": 100},
                 {"value": "位置", "label": "location", "width": 200},
                 {"value": "创建时间", "label": "create_time1", "width": 100},
                 {"value": "修改时间", "label": "modify_time1", "width": 100},
                 ])
            for i in columnList:
                if i['label'] == 'jobRank':
                    i['width'] = 200
                if i['label']=='workNumber':
                    i['width']=150
            a = []
            for index, line in enumerate(tableList):
                # print(line)

                beginDate = self.request.GET.get('beginDate', '')
                endDate = self.request.GET.get('endDate', '')
                if beginDate != "" and endDate != "":
                    if 'cycleData' in line.keys():
                        # print(line)
                        # print("__________________")
                        # print(index,line)
                        # if line['people']==[]:
                        #     del tableList[index]
                        begin = datetime.datetime(1901, 10) if beginDate == '' else beginDate
                        end = datetime.datetime(2521, 10) if endDate == '' else endDate
                        # print(index,line)
                        if type(begin) == str:
                            # print(begin[:7])
                            begin = datetime.datetime.strptime(begin[:7], "%Y-%m")
                        if type(end) == str:
                            end = datetime.datetime.strptime(end[:7], "%Y-%m")
                        if self.is_year_month_in_range(line['cycleData'], begin, end):
                            a.append(line)
                            continue
                        else:
                            pass

                    else:
                        pass
                    tableList = a

                # print
                # line in tableList:
                file = ['insured_file', 'incomeTax_file', 'accumulationFund_file', 'workPhotos_file',
                        'workVideo_file', 'dailyPhotos_file', 'dailyVideo_file', 'incumbency_file',
                        'noWork_file', 'photograph_file','cllBack_file','firstlivevideo_file','secondlivevideo_file']
                for i in file:
                    if line[i] == 0:
                        line[i] = ''
                    elif line[i] == 1:
                        line[i] = list(line[i + "_files"])[0]['name']
                    else:
                        line[i] = ''
        # print("len",len(tableList))
        # print(len(peoples))
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "信息返回成功",
            "data": {
                'columnList': columnList,
                'tableList': tableList[(currentPage - 1) * pageSize:currentPage * pageSize],
                # 'tableList':tableList,
                'totalNumber': obj.count() if self.model != CompeteRestrictionsWhitelist else len(tableList),
                "deptList": [] if self.model != CompeteRestrictionsWhitelist else dept_list,
            }
        }
        # utc3 = arrow.utcnow()
        # print(utc2 - utc1,utc3 - utc1,utc3 - utc2,utc1,utc2,utc3,utc5,utc6)
        # print(self.return_data)

    # 附件上传

    def upload_other_file(self):
        user_id = self.request.POST.get('id', None)
        other_files = self.request.FILES.getlist("file", None)
        type_name = self.request.POST.get("type", "None")
        field_name = self.request.POST.get("field", None)
        searchTime = datetime.datetime.now().strftime("%Y-%m-%d")
        # #print('附件')
        if other_files and other_files != "":
            name = self.model.objects.filter(id=user_id).values_list()[0][1]
            # #print(name)
            # #print(name)
            for other_file in other_files:
                fileName = str(name) + "_" + searchTime + "_" + str(
                    "".join(list(str(time.time()))[0:10])) + "_" + other_file.name
                try:
                    self.fileName = upload_file(other_file, self.file_path[type_name], "other_file", fileName)
                    self.return_data = {
                        "msg": "保存附件成功",
                        "code": status.HTTP_200_OK
                    }
                    # try:
                    file_url = "static/" + self.file_path[type_name] + "/other_file/" + searchTime + "/" + fileName
                    file_name = fileName
                    file_kwargs = {
                        "file_url": file_url,
                        "file_name": file_name,
                    }
                    try:
                        obj = UploadFiles.objects.create(**file_kwargs)
                        self.model_many_obj = {
                            "SalarySurveyRecord": {"historical_payslip": obj.historical_payslip},
                            "ExternalHonorsList": {
                                "honor_upload_declare_files": obj.honor_upload_declare_files,
                                "honor_medal_photos": obj.honor_medal_photos
                            }, "MemorabiliaList": {
                                "memorabilia_plans": obj.memorabilia_plans,
                                "memorabilia_photos": obj.memorabilia_photos
                            }, "EmployeeActivitiesList": {
                                "employee_activities_plans": obj.employee_activities_plans,
                                "employee_activities_photos": obj.employee_activities_photos
                            },
                            "InternalEvaluationList": {
                                "awards_photos": obj.awards_photos,
                            },
                            'EmployeeInspect': {
                                'employee_inspect_plans': obj.employee_inspect_plans,
                                'employee_inspect_photos': obj.employee_inspect_photos
                            },
                            'Colloquium': {
                                'colloquium_photos': obj.colloquium_photos
                            }

                        }
                        obj = self.model.objects.filter(pk=user_id)[0]
                        if field_name is None or field_name == "":
                            field_name = list(self.model_many_obj[self.model_name].keys())[0]
                        self.model_many_obj[self.model_name][field_name].add(obj.id)
                    except Exception as e:
                        self.return_data = {
                            "msg": "附件信息存储失败,格式可能出错啦",
                            "code": status.HTTP_205_RESET_CONTENT
                        }
                        # #print(e)

                except Exception as e:
                    # print(e)
                    self.return_data = {
                        "msg": "保存附件错误",
                        "code": status.HTTP_400_BAD_REQUEST
                    }
        else:
            self.return_data = {
                "code": status.HTTP_200_OK,
                "msg": "空文件"
            }
        # print(self.return_data)

    # 统计字符
    def count_character(self, s):
        hanzi = 0
        num = 0
        for i in str(s):
            if u'\u4e00' <= i <= u'\u9fa5':  # \u4E00 ~ \u9FFF  中文字符
                hanzi = hanzi + 1
            else:
                num += 1

        return str(30 * hanzi + 20 * num)

    def get_first_last(self, date):
        import calendar
        import datetime
        year, month = int(date.year), int(date.month)
        weekDay, monthCountDay = calendar.monthrange(year, month)
        # #print(weekDay,monthCountDay)
        # range_day = str(datetime.date(year, month, day=1)) + "至" + str(datetime.date(year, month, day=monthCountDay))
        first_month = datetime.date(year, month, day=1)
        last_month = datetime.date(year, month, day=monthCountDay)
        first_year = datetime.date(year, 1, 1)
        last_year = datetime.date(year, 12, 31)
        return first_month, last_month, first_year, last_year

    def round_down(self, num):  # 小数向下取整2位
        import math
        return math.floor(num * 100) / 100

    def decision_num(self, num, typp):
        if num != None:
            try:
                if type(num) == str:
                    if eval(num) >= 0:
                        return eval(num)
                    else:
                        return
                elif type(num) == int:
                    if num >= 0:
                        return num
                    else:
                        return
                elif type(num) == typp:
                    if num >= 0:
                        return num
                    else:
                        return
            except:
                return
        else:
            return

    def is_year_month_in_range(self, year_month, start_date, end_date):
        from datetime import datetime
        # print(year_month, start_date, end_date, type(year_month), type(start_date), type(end_date))
        if type(start_date) == str:
            start_date = datetime.strptime(start_date[:7], "%Y-%m")
        if type(end_date) == str:
            end_date = datetime.strptime(end_date[:7], "%Y-%m")

        year_month = datetime.strptime(year_month[:7], "%Y-%m")
        # year_month_date = datetime.strptime(year_month, "%Y-%m")

        # if start_date.year <= year_month_date.year <= end_date.year:
        #     if start_date.month <= year_month_date.month <= end_date.month:
        #         return True
        if start_date <= year_month <= end_date:
            return True

        return False
