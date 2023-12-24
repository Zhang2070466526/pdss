from rest_framework.generics import GenericAPIView

from employeePersonnel.archives.archive import *
from rest_framework.views import APIView
import calendar
from datetime import date, datetime, timedelta, time
from employeePersonnel.tasks import *
from datetime import time


class ArchiveSlicesInfoSelect(APIView):
    def post(self, request):
        reset = Archive(request, 'slice_info_select')
        response_data = reset.meth_center()
        return response_data
class ArchiveSlicesInfoDown(APIView):
    def post(self, request):
        reset = Archive(request, 'slice_info_down')
        response_data = reset.meth_center()
        return response_data

def slice_info_options(request):
    if request.check_token is not None:
        jobrank_all = HrJobRank.objects.filter().exclude(id=999999).values_list(
            'id',
            'job_rank_name').all()
        employee_pay_type_list = list(HrPayType.objects.filter(pay_type_status=True).exclude(id=999999).values('id', 'pay_type_name'))  # 计薪方式

        return_data = {
            'data': {
                'employee_pay_type_list': [
                    {"value": item["id"], "label": item["pay_type_name"]}
                    for item in employee_pay_type_list
                ],
                'jobrank_list': [
                    {"value": item[0], "label": item[1]}
                    for item in jobrank_all
                ],
                'employee_dl_list': [
                    {"value": 'DL', "label": 'DL'}, {"value": 'IDL', "label": 'IDL'}, {"value": 'SAL', "label": 'SAL'}
                ],
                'employee_status_list': [
                    {"value": '1', "label": '在职'}, {"value": '2', "label": '离职'}, {"value": '99', "label": '黑名单'}
                ],
                'employee_work_status_list': [
                    {"value": '正式工', "label": '正式工'}, {"value": '实习生', "label": '实习生'}, {"value": '试用期', "label": '试用期'},
                    {"value": '劳务工', "label": '劳务工'}, {"value": '产线承包', "label": '产线承包'}, {"value": '顾问',"label": '顾问'}
                ],
            },
            "code": status.HTTP_200_OK,
            "msg": "下拉菜单返回成功",
            'hidden': True,
        }

    else:
        return_data = {
            "code": status.HTTP_403_FORBIDDEN,
            "msg": "没有权限访问",
            'hidden': False
        }
    return JsonResponse(return_data)
