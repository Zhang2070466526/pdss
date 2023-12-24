# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 16:17
# @Author  : zhuang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from .views import *

urlpatterns = [
    path("upload", Salary.as_view({
        "post": "upload_other_file",
        "delete": "delete_other_file"
    })),
    path("record", Salary.as_view({
        "get": "get_list",
    })),
    path("data", Salary.as_view({
        "patch": "patch_data",
        "delete": "delete_data",
        "post": "get_upload",
        # "post": "upload_other_file",
        "put": "download_file",
    }))
]