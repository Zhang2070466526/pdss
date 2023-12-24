# -*- coding: utf-8 -*-
# @Time    : 2023/5/22 8:27
# @Author  : zhuang
# @Site    : 
# @File    : userClass.py
# @Software: PyCharm
import json

from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from auther.models import AdminUser
from ..serializers import *
from general.models import center_base


class userMgmt:
    def __init__(self, request, meth):
        self.return_data = None
        self.request = request
        self.token = request.check_token
        self.meth = meth
        self.method = {
            "add_user": self.add_user,
            "update_user": self.update_user,
            "get_list": self.get_list,
        }

    def center_meth(self):
        self.method[self.meth]()
        return Response(self.return_data)

    def add_user(self):
        info = json.loads(self.request.body)
        try:
            obj = AdminUser.objects.get(username=info['username'])
            self.return_data = {
                'code': 404,
                "message": "用户名重复，请重新选择"
            }
        except AdminUser.DoesNotExist:
            obj = AdminUserAddSerializers(data=info)
            if obj.is_valid():
                obj.save()
            else:
                error = obj.errors
                print(error)
                self.return_data = {
                    'code': 401,
                    "message": error
                }

    def update_user(self):
        info = json.loads(self.request.body)
        pk = AdminUser.objects.get(pk=info["id"])
        obj = AdminUserAddSerializers(instance=pk, data=info)
        if obj.is_valid():
            obj.save()
        else:
            error = obj.errors
            print(error)
            self.return_data = {
                'code': 401,
                "message": error
            }

    def get_list(self):
        columnList = [
            {"value": "序号", "label": "index", "width": "60"},
            {"value": "用户名", "label": "username", "width": "90"},
            {"value": "登录名", "label": "user", "width": "60"},
            {"value": "是否为管理员", "label": "is_superuser", "width": "180"},
            {"value": "备注", "label": "modify_time", "width": ""},
            {"value": "更新时间", "label": "create_time", "width": "120"},
            {"value": "修改时间", "label": "modify_time", "width": "120"},
            {"value": "密码", "label": "password", "width": "200"},
        ]
        tableList = []
        base_data = []
        nav_data = []
        args = ()
        searchName = self.request.GET.get("searchName", None)
        currentPage = eval(self.request.GET.get("currentPage", None)) if self.request.GET.get("currentPage",
                                                                                              None) != "" else 1
        pageSize = eval(self.request.GET.get("pageSize", None)) if self.request.GET.get("pageSize", None) != "" else 25
        if searchName is not None and searchName != "":
            args = (Q(username__contains=searchName) | Q(user__contains=searchName))
        user_obj = AdminUser.objects.filter(is_used=1, *args)
        obj = AdminUserGetSerializers(instance=user_obj[(currentPage - 1) * pageSize:currentPage * pageSize],
                                      many=True).data
        index = (currentPage - 1) * pageSize + 1
        for i in obj:
            data = dict(i)
            data['index'] = index
            tableList.append(data)
            index += 1
        base_obj = center_base.objects.filter(status=1).values()
        base_data = [{"id": i['id'], "name": i['name'], } for i in base_obj]

        nav_obj = AdminNavMenuList.objects.filter(nav_type=1, nav_parent_id=None).values()
        nav_data = [{"id": i['id'], "label": i['nav_name']} for i in nav_obj]
        for nav in nav_data:
            parent_data = AdminNavMenuList.objects.filter(nav_type=1, nav_parent_id=nav['id']).values()
            nav['child'] = [{"id": i['id'], "label": i['nav_name']} for i in parent_data]

        self.return_data = {
            "code": 200,
            "msg": "信息返回成功",
            "data": {
                'totalNumber': user_obj.count(),
                'tableList': tableList,
                'columnList': columnList,
                "navList": nav_data,
                "baseList": base_data
            },
        }

