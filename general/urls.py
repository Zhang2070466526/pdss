# -*- coding: utf-8 -*-
# @Time    : 2023/5/8 13:52
# @Author  : zhuang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from .views import *

urlpatterns = [
    path("upload", general.as_view({
        "post": "upload_other_file",
        "delete": "delete_other_file"
    })),
    path("data", general.as_view({
        "patch": "patch",
        "get": "get_list",
    })),
    path("baseDrop", general.as_view({
        "get": "center_drop",
    })),
]