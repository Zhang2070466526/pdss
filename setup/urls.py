# -*- coding: utf-8 -*-
# @Time    : 2023/5/22 8:26
# @Author  : zhuang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from .views import *

urlpatterns = [

    path("user", AdminUserMgmt.as_view({
        "get": "get_list",
        "post": "add_user",
        "patch": "update_user",
        "delete": "delete_user",
    })),
    path("pic", PicManageView.as_view({
        "get": "get_pic",
        "post": "add_pic",
        "delete": "delete_pic",
    })),
    path("base", BaseManageView.as_view({
        "get": "get_base",
        "post": "add_base",
        "delete": "delete_base",
        "patch":'patch_base'
    })),
]