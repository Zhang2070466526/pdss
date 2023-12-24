from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet, GenericViewSet
from utils.check_token import *
from controller.controller import *
from general.general.generalClass import generalClass


class general(GenericViewSet):

    # 附件上传
    def upload_other_file(self, request):
        obj = generalClass(request, "upload_other_file")
        res = obj.meth_center()
        return res

    def delete_other_file(self, request):
        obj = generalClass(request, "delete_other_file")
        res = obj.meth_center()
        return res

    def patch(self, request):
        obj = generalClass(request, "patch")
        res = obj.meth_center()
        return res

    def center_drop(self, request):
        obj = generalClass(request, "center_drop")
        res = obj.meth_center()
        return res
