from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import GenericViewSet
from volumeContracts.contracts.contractsClass import *


class ContractsView(GenericViewSet):
    def get_list(self, request):
        obj = infoMgmt(request, "get_list")
        res = obj.meth_center()

        return res

    def get_upload(self, request):
        obj = infoMgmt(request, "get_upload")
        res = obj.meth_center()
        return res

    def patch_data(self, request):
        obj = infoMgmt(request, "patch_data")
        res = obj.meth_center()
        return res

    def delete_data(self, request):
        obj = infoMgmt(request, "delete_data")
        res = obj.meth_center()
        return res

    def download_file(self, request):
        obj = infoMgmt(request, "download_file")
        res = obj.meth_center()
        return res
class jobRankView(GenericViewSet):
    def jobrank_drop(self, request):
        obj = infoMgmt(request, "jobrank_drop")
        res = obj.meth_center()
        return res
