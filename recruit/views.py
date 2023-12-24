from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from .models import *
from recruit.recruitClass.dlClass import dlClass
from recruit.recruitClass.idlClass import idlClass
from recruit.recruitClass.salClass import salClass
from recruit.recruitClass.collectClass import collectClass


# Create your views here.

class DL(GenericViewSet):
    def get_list(self, request):
        obj = dlClass(request, "get_list")
        res = obj.meth_center()
        return res

    def get_upload(self, request):
        obj = dlClass(request, "get_upload")
        res = obj.meth_center()
        return res

    def patch_data(self, request):
        obj = dlClass(request, "patch_data")
        res = obj.meth_center()
        return res

    def delete_data(self, request):
        obj = dlClass(request, "delete_data")
        res = obj.meth_center()
        return res

    def download_file(self, request):
        obj = dlClass(request, "download_file")
        res = obj.meth_center()
        return res


class IDL(GenericViewSet):
    def get_list(self, request):
        obj = idlClass(RecruitIdl, "get_list", request)
        res = obj.dyj_data_start()
        return res

    def get_upload(self, request):
        obj = idlClass(RecruitIdl, "get_upload", request)
        res = obj.dyj_data_start()
        return res

    def patch_data(self, request):
        obj = idlClass(RecruitIdl, "patch", request)
        res = obj.dyj_data_start()
        return res

    def delete_data(self, request):
        obj = idlClass(RecruitIdl, "delete", request)
        res = obj.dyj_data_start()
        return res

    def download_file(self, request):
        obj = idlClass(RecruitIdl, "download_file", request)
        res = obj.dyj_data_start()
        return res


class SAL(GenericViewSet):
    def get_list(self, request):
        obj = salClass(RecruitSal, "get_list", request)
        res = obj.dyj_data_start()
        return res

    def get_upload(self, request):
        obj = salClass(RecruitSal, "get_upload", request)
        res = obj.dyj_data_start()
        return res

    def patch_data(self, request):
        obj = salClass(RecruitSal, "patch", request)
        res = obj.dyj_data_start()
        return res

    def delete_data(self, request):
        obj = salClass(RecruitSal, "delete", request)
        res = obj.dyj_data_start()
        return res

    def download_file(self, request):
        obj = salClass(RecruitSal, "download_file", request)
        res = obj.dyj_data_start()
        return res


class Collect(GenericViewSet):
    def get_list(self, request):
        obj = collectClass(request, "get_list")
        res = obj.meth_center()
        return res

    def download_file(self, request):
        obj = collectClass(request, "download_file", )
        res = obj.meth_center()
        return res
