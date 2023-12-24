from django.shortcuts import render

# Create your views here.

from rest_framework import serializers  # 序列化器
from rest_framework.generics import GenericAPIView
from employeeInspect.models import *
from employeeInspect.serializers import *
from employeeInspect.inspect.inspectClass import Reset
from rest_framework.viewsets import ViewSet, GenericViewSet




class recordDetailView(GenericViewSet):
    # queryset = InternalEvaluationList.objects.all()
    authentication_classes = []
    serializer_class =EmployeeInspectSerializers


    def get_list(self, request):
        obj = Reset(request, "get_list")
        res = obj.meth_center()
        return res
    def get_upload(self, request):  #新增
        obj = Reset(request, "get_upload")
        res = obj.meth_center()
        return res
    def delete_data(self, request):  #删除
        obj = Reset(request, "delete_data")
        res = obj.meth_center()
        return res
    def patch_data(self, request):  #修改
        obj = Reset(request, "patch_data")
        res = obj.meth_center()
        return res
    # 下载数据
    def download_file(self, request):
        obj = Reset(request, "download_file")
        res = obj.meth_center()
        return res