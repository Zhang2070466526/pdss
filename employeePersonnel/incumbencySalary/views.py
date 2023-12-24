

from rest_framework.generics import GenericAPIView

from employeePersonnel.incumbencySalary.salaryAnalyse import *
from rest_framework.views import APIView
import calendar
from datetime import date, datetime, timedelta, time
from employeePersonnel.tasks import *
from datetime import time


class AnalyseInfo(APIView):
    def post(self, request):
        reset = Salary(request, 'analyse_salary_info')
        response_data = reset.meth_center()
        return response_data
    def get(self, request):   #下拉框
        reset = Salary(request, 'analyse_salary_options')
        response_data = reset.meth_center()
        return response_data
    def put(self, request):   #下载
        reset = Salary(request, 'analyse_salary_down')
        response_data = reset.meth_center()
        return response_data