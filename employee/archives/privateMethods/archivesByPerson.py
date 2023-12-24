import json, os,arrow,openpyxl,time,requests

from django.db.models import Q,F
from rest_framework import status
from django.http import JsonResponse

from auther.models import AdminUser
from employee.models import *

from datetime import datetime, date,timedelta

from socialSecurity.Anomalies.models import *
from pdss.settings import BASE_DIR
from socialSecurity.publicMethods import *
from utils.wechat_interface import *

class ArchivesByPerson:
    def __init__(self, request,meth):
        self.request = request
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功'
        }
        self.meth = meth
        self.now = arrow.now()
        self.t1 = self.now.format('YYYY-MM-DD')
        self.t2 = self.now.timestamp()
        self.methods = {
            'categorized_by_person': self.categorized_by_person,        #按人员分类

        }
        self.Enterprise_WeChat=Enterprise_WeChat()   #企业微信的接口
    def method_center(self):
        if self.meth in []:
            pass
        else:
            if self.request.check_token is None:
                self.return_data = {'code': status.HTTP_403_FORBIDDEN, "msg": '没有权限访问!'}
                return JsonResponse(self.return_data)

        self.methods[self.meth]()
        return JsonResponse(self.return_data)

    # 获取信息列表
    def categorized_by_person(self):
        pass
        # columnList = [{'label': 'index', 'value': '序号', 'width': 60},
        #               {'label': 'anomalies_people__employee_code', 'value': '工号', 'width': 100},
        #               {'label': 'anomalies_people__employee_name', 'value': '姓名', 'width':100},
        #               {'label': 'anomalies_people__employee_identity_no', 'value': '身份证号', 'width': ""},
        #               {'label': 'anomalies_people__employee_job_rank__job_rank_name', 'value': '合同归属', 'width': ""},
        #               {'label': 'anomalies_people__employee_department__department_manage', 'value': '管理归属', 'width': ""},
        #               {'label': 'anomalies_people__employee_department__department_first_name', 'value': '一级部门', 'width': ""},
        #               {'label': 'anomalies_people__employee_department__department_second_name', 'value': '二级部门','width': ""},
        #               {'label': 'anomalies_people__employee_department__department_third_name', 'value': '三级部门','width': ""},
        #               {'label': 'anomalies_insurance_type', 'value': '险种', 'width': ""},
        #               {'label': '_anomalies_month', 'value': '月份', 'width': ""},
        #               {'label': 'anomalies_fail_reason', 'value': '增员失败原因','width': ""},
        #               {'label': 'anomalies_return_reason', 'value': '返回原因', 'width': ""},
        #               {'label': 'anomalies_dispose', 'value': '需如何处理', 'width': ""},
        #               {'label': 'anomalies_process_results', 'value': '员工处理结果', 'width': ""},
        #               ]
        # currentPage = json.loads(self.request.body).get('currentPage')
        # pageSize = json.loads(self.request.body).get('pageSize')
        #
        # totalNumber = SocialSecurityAnomalies.objects.filter(anomalies_status=True).count()
        tableList = list(
            HrEmployeeFiles.objects.filter(anomalies_status=True).values('id',
                                                                                 'anomalies_people_id',
                                                                        'anomalies_people__employee_name',
                                                                        'anomalies_people__employee_code',
                                                                        'anomalies_people__employee_identity_no',
                                                                        'anomalies_people__employee_job_rank__job_rank_name',
                                                                        'anomalies_people__employee_department__department_manage',
                                                                        'anomalies_people__employee_department__department_first_name',
                                                                        'anomalies_people__employee_department__department_second_name',
                                                                        'anomalies_people__employee_department__department_third_name',

                                                                        'anomalies_fail_reason',    #失败原因唯一
                                                                        'anomalies_insurance_type',  #险种唯一
                                                                        'anomalies_month',         #月份唯一

                                                                        # 'anomalies_return_reason',
                                                                        # 'anomalies_dispose',
                                                                        # 'anomalies_process_results',
                                                            ))
        #
        # all_id = [item['id'] for item in tableList]     #所有记录的id
        # results_list=list(SocialSecurityAnomaliesResults.objects.filter(results_anomalies_id__in=all_id,results_status=True).values('id','results_people_id','results_anomalies_id','return_dispose','return_cause','results_process'))
        # fils_list=list(SocialSecurityFiles.objects.filter(anomalies_file_id__in=all_id,file_status=True).values('id','file_type','file_name','file_url','anomalies_file_id'))
        #
        #
        # anomalies_file = {}  # 员工凭证表
        #
        # for item in fils_list:  # 查找每份提案对应的文件
        #     anomalies_file_id = item.get('anomalies_file_id')
        #     if item['file_type'] == 1:  # 活动照片
        #         if anomalies_file_id not in anomalies_file:
        #             anomalies_file[anomalies_file_id] = []
        #         anomalies_file[anomalies_file_id].append(item)
        # for index, item in enumerate(tableList):
        #     item['index'] = (currentPage - 1) * pageSize + index + 1
        #     item['return_cause'] =','.join([line['return_cause'] for line in results_list if line['results_anomalies_id'] == item['id'] and line['results_people_id']==item['anomalies_people_id'] and line['return_cause'] is not None ])
        #     item['return_dispose'] = ','.join([line['return_dispose'] for line in results_list if line['results_anomalies_id'] == item['id'] and line['results_people_id'] == item['anomalies_people_id']  and line['return_dispose'] is not None])
        #     item['results_process'] =','.join([line['results_process'] for line in results_list if line['results_anomalies_id'] == item['id'] and line['results_people_id']==item['anomalies_people_id'] and line['results_process'] is not None])
        #     if item['id'] in anomalies_file:
        #         item['anomalies_file_ls'] = anomalies_file[item['id']]
        #         item['anomalies_file_num'] = len(anomalies_file[item['id']])
        #     else:
        #         item['anomalies_file_ls'] = []
        #         item['anomalies_file_num'] = 0
        #
        #
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "信息返回成功",
            "data": {
                # 'columnList': columnList,
                'tableList': tableList,
                # 'totalNumber': totalNumber,
            }
        }


