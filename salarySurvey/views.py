from django.shortcuts import render
from rest_framework.authentication import BaseAuthentication
from rest_framework.viewsets import ViewSet, GenericViewSet

from utils.check_token import *
from salarySurvey.salary.salaryClass import *


from .serializers import *


def verify(request):
    return_data = {'code': '', "message": ''}
    new_token = CheckToken()
    try:
        check_token = new_token.check_token(request.headers['Authorization'])
    except:
        return_data['code'] = 400
        return_data['message'] = '请求参数出错啦'
        return return_data
    if check_token is None:
        return_data['code'] = 403
        return_data['message'] = '没有权限查询'
        return return_data


class Salary(GenericViewSet):
    authentication_classes = []
    serializer_class = SalarySurveyRecordGetSerializers

    def get_upload(self, request):
        obj = salaryClass(request, "get_upload")
        res = obj.meth_center()
        return res

    def get_list(self, request):
        obj = salaryClass(request, "get_list")
        res = obj.meth_center()
        return res

    def patch_data(self, request):
        obj = salaryClass(request, "patch_data")
        res = obj.meth_center()
        return res

    def delete_data(self, request):
        obj = salaryClass(request, "delete_data")
        res = obj.meth_center()
        return res

    # 下载数据
    def download_file(self, request):
        obj = salaryClass(request, "download_file")
        res = obj.meth_center()
        return res

    def delete_other_file(self, request):
        obj = salaryClass(request, "delete_other_file")
        res = obj.meth_center()
        return res

    def upload_other_file(self, request):
        obj = salaryClass(request, "upload_other_file")
        res = obj.meth_center()
        return res