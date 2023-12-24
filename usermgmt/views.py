import json

from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from auther.models import AdminUser
from .serializers import *
from usermgmt.userClass.userClass import userMgmt


# Create your views here.

class AdminUserMgmt(GenericViewSet):

    def add_user(self, request):
        obj = userMgmt(request, "add_user")
        res = obj.center_meth()
        return res

    def update_user(self, request):
        obj = userMgmt(request, "update_user")
        res = obj.center_meth()
        return res

    def get_list(self, request):
        obj = userMgmt(request, "get_list")
        res = obj.center_meth()
        return res
