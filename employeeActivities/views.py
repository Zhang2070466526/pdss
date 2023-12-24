from django.shortcuts import render
from rest_framework.authentication import BaseAuthentication
from rest_framework.viewsets import ViewSet, GenericViewSet

from utils.check_token import *
from .serializers import *
from controller.controller import Controller
from .models import *
from employeeActivities.employee.employeeClass import employeeClass


# Create your views here.
class employee(GenericViewSet):
    authentication_classes = []
    serializer_class = EmployeeActivitiesListGetSerializers

    def get_list(self, request):
        obj = employeeClass(request, "get_list")
        res = obj.meth_center()
        return res

    def get_upload(self, request):
        obj = employeeClass(request, "get_upload")
        res = obj.meth_center()
        return res

    def patch_data(self, request):
        obj = employeeClass(request, "patch_data")
        res = obj.meth_center()
        return res

    def delete_data(self, request):
        obj = employeeClass(request, "delete_data")
        res = obj.meth_center()
        return res

    def download_file(self, request):
        obj = employeeClass(request, "download_file")
        res = obj.meth_center()
        return res
