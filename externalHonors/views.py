from django.shortcuts import render
from rest_framework.authentication import BaseAuthentication
from rest_framework.viewsets import ViewSet, GenericViewSet

from utils.check_token import *
from .serializers import *
from controller.controller import Controller
from .models import *
from externalHonors.honor.honorClass import *


# Create your views here.
def verify(request):
    return_data = {'code': '', "message": ''}
    new_token = CheckToken()
    try:
        check_token = new_token.check_token(request.headers['Authorization'])
    except Exception as e:
        # print(e)
        return_data['code'] = 400
        return_data['message'] = '请求参数出错啦'
        return return_data
    if check_token is None:
        return_data['code'] = 403
        return_data['message'] = '没有权限查询'
        return return_data


class Honor(GenericViewSet):
    authentication_classes = []
    serializer_class = HonorRecordGetSerializers

    def get_list(self, request):
        obj = honorClass(request, "get_list")
        res = obj.meth_center()
        return res

    def get_upload(self, request):
        obj = honorClass(request, "get_upload")
        res = obj.meth_center()
        return res

    def patch_data(self, request):
        obj = honorClass(request, "patch_data")
        res = obj.meth_center()
        return res

    def delete_data(self, request):
        obj = honorClass(request, "delete_data")
        res = obj.meth_center()
        return res

    def download_file(self, request):
        obj = honorClass(request, "download_file")
        res = obj.meth_center()
        return res
