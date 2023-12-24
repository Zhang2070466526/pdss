import json

from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ViewSet, GenericViewSet

from rest_framework.decorators import APIView
from wx.salary.salaryClass import *


class Salary(APIView):
    def post(self, request):
        req_data = request.data
        salary_data = SalaryInfo()
        return JsonResponse(
            salary_data.get_month_salary_data(req_data['code'], req_data['period'], req_data['language_type']))


class SalaryList(APIView):
    def post(self, request):
        req_data = request.data
        salary_list_data = SalaryInfo()
        return JsonResponse(
            salary_list_data.get_year_salary_list(req_data['code'], req_data['year'], req_data['language_type']))


def is_have_password(request):
    req_data = json.loads(request.body)
    salary = SalaryInfo()
    return JsonResponse(
        salary.is_have_password(req_data['code'], req_data['language_type'])
    )


def forget_password_page(request):
    req_data = json.loads(request.body)
    salary = SalaryInfo()
    return JsonResponse(
        salary.forget_password_page(req_data['language_type'])
    )


def forget_password(request):
    req_data = json.loads(request.body)
    salary = SalaryInfo()
    return JsonResponse(
        salary.forget_password(req_data['sfz'], req_data['code'], req_data['password'], req_data['password2'], )
    )


def check_password(request):
    req_data = json.loads(request.body)
    salary = SalaryInfo()
    return JsonResponse(
        salary.check_password(req_data['code'], req_data['password'])
    )


def salary_confirm(request):
    req_data = json.loads(request.body)
    salary = SalaryInfo()
    return JsonResponse(
        salary.salary_confirm(req_data['code'], req_data['period'])
    )
