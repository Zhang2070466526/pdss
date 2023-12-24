from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from socialSecurity.Anomalies.anomaliesMethods import *





class Anomalies_Info_Get_RecordView(APIView): # 社保增员信息查询
    def post(self, request, **kwargs):
        new_query = Anomalies(request, 'get_anomalies_info')
        query = new_query.method_center()
        return query

class Anomalies_Info_Batch_RecordView(APIView): #上传
    def post(self, request, **kwargs):
        new_query = Anomalies(request, 'batch_anomalies_info')
        query = new_query.method_center()
        return query
class Anomalies_Info_Down_RecordView(APIView):#下载
    def post(self, request, **kwargs):
        new_query = Anomalies(request, 'down_anomalies_info')
        query = new_query.method_center()
        return query

class Disponse_Gather_POST_RecordView(APIView):#手机端   上传员工处理结果:
    def post(self, request, **kwargs):
        new_query = Anomalies(request, 'post_dispose_gather')
        query = new_query.method_center()
        return query

class Disponse_Overrule_POST_RecordView(APIView):#手机端   上传员工处理结果:
    def post(self, request, **kwargs):
        new_query = Anomalies(request, 'post_dispose_overrule')
        query = new_query.method_center()
        return query

class Anomalies_Employee_Reminders_RecordView(APIView):#定时任务 员工提醒
    def get(self, request, **kwargs):
        new_query = Anomalies(request, 'timing_employee_reminders')
        query = new_query.method_center()
        return query

def Social_Anomalies_Options(request):
    insurance_type_list = list(
        SocialSecurityInsuranceType.objects.filter(insurance_type_status=True).values('id', 'insurance_type_name'))  # 保险种类
    return_data = {
        'data': {
            'insurance_type_list': [
                {"value": item["id"], "label": item["job_grade_name"]}
                for item in insurance_type_list
            ],

        },
        "code": status.HTTP_200_OK,
        "msg": "下拉菜单返回成功",
        'hidden': True,
    }
    return JsonResponse(return_data)
