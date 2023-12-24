from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.response import Response
from expatriateRecord.immigration.immigrationMethods import *
from expatriateRecord.models import ImmigrationBase


class RecordQueryVietnamRecordView(APIView):     # 越南的
    def post(self, request, **kwargs):
        new_query = Immigration(request, 'get_immigration_vietnam')
        query = new_query.method_center()
        return query
class RecordQueryThailandNotRecordView(APIView): # 泰国没有签证的
    def post(self, request, **kwargs):
        new_query = Immigration(request, 'get_immigration_thailand_not')
        query = new_query.method_center()
        return query
class RecordQueryThailandRecordView(APIView): # 泰国有签证的
    def post(self, request, **kwargs):
        new_query = Immigration(request, 'get_immigration_thailand')
        query = new_query.method_center()
        return query


class RecordDownVietnamRecordView(APIView):   #签证下载  越南
    def post(self, request, **kwargs):
        new_query = Immigration(request, 'down_immigration_vietnam')
        query = new_query.method_center()
        return query


class RecordEditRecordView(APIView): # 签证组修改
    def post(self, request, **kwargs):
        new_query = Immigration(request, 'edit_immigration_info')
        query = new_query.method_center()
        return query

class RecordDelRecordView(APIView):#签证删除
    def post(self, request, **kwargs):
        new_query = Immigration(request, 'del_immigration_info')
        query = new_query.method_center()
        return query

class RecordImportRecordView(APIView):   #签证导入
    def post(self, request, **kwargs):
        new_query = Immigration(request, 'import_immigration_info')
        query = new_query.method_center()
        return query
class RecordPostRecordView(APIView):#签证新增
    def post(self, request, **kwargs):
        new_query = Immigration(request, 'post_immigration_info')
        query = new_query.method_center()
        return query




class AlertInfoRecordView(APIView):   #信息提醒   定时任务
    def get(self, request, **kwargs):
        new_query = Immigration(request, 'alert_info')
        query = new_query.method_center()
        return query
class AttendanceRecordView(APIView): #计算考勤   定时任务
    def get(self, request, **kwargs):
        new_query = Immigration(request, 'calculate_attendance')
        query = new_query.method_center()
        return query

class EmployeeFillRecordView(APIView):   #员工填写
    def post(self, request, **kwargs):
        new_query = Immigration(request, 'employee_fill')
        query = new_query.method_center()
        return query
    def get(self, request, **kwargs):
        new_query = Immigration(request, 'employee_fill_verify')
        query = new_query.method_center()
        return query
class EmployeeFillOverruleRecordView(APIView):# 员工填写驳回
    def post(self, request, **kwargs):
        new_query = Immigration(request, 'employee_fill_overrule')
        query = new_query.method_center()
        return query

def immigration_options(request): #下拉框
    immigration_base_list = list(ImmigrationBase.objects.filter(base_status=True).values('id','base_name'))  # 派驻基地
    immigration_country_list = list(ImmigrationCountry.objects.filter(country_status=True).values('id', 'country_name'))     # 派驻国家
    immigration_reason_list = list(ImmigrationTripReason.objects.filter(reason_status=True).values('id', 'reason_name'))    # 出入境行程原因
    country_id=request.GET.get('country_id',None)

    if len(country_id)==0 or country_id is  None:
        immigration_type_list = []
    else:
        immigration_type_list = list(ImmigrationType.objects.filter(type_status=True, type_classify_id=country_id).values('id','type_name'))  # 出入境状态

    return_data = {
        'data': {
            'insurance_type_list': [
                {"value": item["id"], "label": item["base_name"]}
                for item in immigration_base_list
            ],
            'immigration_country_list': [
                {"value": item["id"], "label": item["country_name"]}
                for item in immigration_country_list
            ],
            'immigration_reason_list': [
                {"value": item["id"], "label": item["reason_name"]}
                for item in immigration_reason_list
            ],
            'immigration_type_list': [
                {"value": item["id"], "label": item["type_name"]}
                for item in immigration_type_list
            ],
            'fill_approval_status_list': [
                {
                    "value": 1,
                    "label": "未审核"
                },
                {
                    "value": 2,
                    "label": "已审核"
                },
                {
                    "value": 3,
                    "label": "已驳回"
                },

            ],
        },
        "code": status.HTTP_200_OK,
        "msg": "下拉菜单返回成功",
        'hidden': True,
    }
    try:
        code = request.GET.get('code', None)
        tableList = list(
            HrEmployee.objects.filter(Q(employee_name__contains=code) | Q(employee_code__contains=code),employee_status=1).values("employee_code","employee_name","employee_job_duty__job_duty_name"))
        return_data['data']['records_people_list'] = [
            {
                "value": item['employee_code'] + "-" + item["employee_name"] + '-' + item[
                    'employee_job_duty__job_duty_name'],
                "address": {
                    "employee_name": item["employee_name"],  # 姓名
                    'employee_code': item['employee_code'],
                }
            }
            for item in tableList
        ]
    except:
        pass



    return JsonResponse(return_data)