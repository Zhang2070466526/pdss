from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from rest_framework import serializers  # 序列化器
from rest_framework.generics import GenericAPIView
from rewardsPunishments.models import *
from rewardsPunishments.serializers import *
from rewardsPunishments.punishments.punishmentsClass import Resetpb,Resetrp
from rest_framework.viewsets import ViewSet, GenericViewSet


class pbrecordDetailView(GenericViewSet):  #项目奖金
    # queryset = InternalEvaluationList.objects.all()
    authentication_classes = []
    serializer_class = ProjectBonusSerializers

    def get_list(self, request):
        obj = Resetpb(request, "get_list")
        res = obj.meth_center()
        return res

    def get_upload(self, request):  # 新增
        obj = Resetpb(request, "get_upload")
        res = obj.meth_center()
        return res

    def delete_data(self, request):  # 删除
        obj = Resetpb(request, "delete_data")
        res = obj.meth_center()
        return res

    def patch_data(self, request):  # 修改
        obj = Resetpb(request, "patch_data")
        res = obj.meth_center()
        return res

    # 下载数据
    def download_file(self, request):
        obj = Resetpb(request, "download_file")
        res = obj.meth_center()
        return res

class rprecordDetailView(GenericViewSet):   #奖惩
    # queryset = InternalEvaluationList.objects.all()
    authentication_classes = []
    serializer_class =RewardsAndPunishmentsSerializers

    def get_list(self, request):
        obj = Resetrp(request, "get_list")
        res = obj.meth_center()
        return res
    def get_upload(self, request):  #新增
        obj = Resetrp(request, "get_upload")
        res = obj.meth_center()
        return res
    def delete_data(self, request):  #删除
        obj = Resetrp(request, "delete_data")
        res = obj.meth_center()
        return res
    def patch_data(self, request):  #修改
        obj = Resetrp(request, "patch_data")
        res = obj.meth_center()
        return res
    # 下载数据
    def download_file(self, request):
        obj = Resetrp(request, "download_file")
        res = obj.meth_center()
        return res