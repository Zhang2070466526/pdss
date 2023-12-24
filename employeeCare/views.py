from django.shortcuts import render

# Create your views here.

from rest_framework import serializers  # 序列化器
from rest_framework.generics import GenericAPIView
from employeeCare.models import *
from employeeCare.serializers import *
from employeeCare.care.careClass import *
from rest_framework.viewsets import ViewSet, GenericViewSet
from utils.check_token import *




class tsrecordDetailView(GenericViewSet):   #人才补贴
    # queryset = InternalEvaluationList.objects.all()
    authentication_classes = []
    serializer_class =TalentSubsidiesSerializers


    def get_list(self, request):
        obj = Resetts(request, "get_list")
        res = obj.meth_center()
        return res

    def get_upload(self, request):  # 新增
        obj = Resetts(request, "get_upload")
        res = obj.meth_center()
        return res

    def delete_data(self, request):  # 删除
        obj = Resetts(request, "delete_data")
        res = obj.meth_center()
        return res

    def patch_data(self, request):  # 修改
        obj = Resetts(request, "patch_data")
        res = obj.meth_center()
        return res

    # 下载数据
    def download_file(self, request):
        obj = Resetts(request, "download_file")
        res = obj.meth_center()
        return res


class eirecordDetailView(GenericViewSet):  #离职访谈
    # queryset = InternalEvaluationList.objects.all()
    authentication_classes = []
    serializer_class =ExitInterviewsSerializers


    def get_list(self, request):
        obj = Resetei(request, "get_list")
        res = obj.meth_center()
        return res

    def get_upload(self, request):  # 新增
        obj = Resetei(request, "get_upload")
        res = obj.meth_center()
        return res

    def delete_data(self, request):  # 删除
        obj = Resetei(request, "delete_data")
        res = obj.meth_center()
        return res

    def patch_data(self, request):  # 修改
        obj = Resetei(request, "patch_data")
        res = obj.meth_center()
        return res

    # 下载数据
    def download_file(self, request):
        obj = Resetei(request, "download_file")
        res = obj.meth_center()
        return res


class cqrecordDetailView(GenericViewSet):  #座谈会
    # queryset = InternalEvaluationList.objects.all()
    authentication_classes = []
    serializer_class =ColloquiumSerializers


    def get_list(self, request):
        obj = Resetcq(request, "get_list")
        res = obj.meth_center()
        return res

    def get_upload(self, request):  # 新增
        obj = Resetcq(request, "get_upload")
        res = obj.meth_center()
        return res

    def delete_data(self, request):  # 删除
        obj = Resetcq(request, "delete_data")
        res = obj.meth_center()
        return res

    def patch_data(self, request):  # 修改
        obj = Resetcq(request, "patch_data")
        res = obj.meth_center()
        return res

    # 下载数据
    def download_file(self, request):
        obj = Resetcq(request, "download_file")
        res = obj.meth_center()
        return res


class jirecordDetailView(GenericViewSet):  #在职访谈
    # queryset = InternalEvaluationList.objects.all()
    authentication_classes = []
    serializer_class =JobInterviewsSerializers


    def get_list(self, request):
        obj = Resetji(request, "get_list")
        res = obj.meth_center()
        return res

    def get_upload(self, request):  # 新增
        obj = Resetji(request, "get_upload")
        res = obj.meth_center()
        return res

    def delete_data(self, request):  # 删除
        obj = Resetji(request, "delete_data")
        res = obj.meth_center()
        return res

    def patch_data(self, request):  # 修改
        obj = Resetji(request, "patch_data")
        res = obj.meth_center()
        return res

    # 下载数据
    def download_file(self, request):
        obj = Resetji(request, "download_file")
        res = obj.meth_center()
        return res
