# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 11:18
# @Author  : zhuang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from .views import *

urlpatterns = [
    path("upload", Honor.as_view({

        "post": "get_upload",
    })),
    path("record", Honor.as_view({
        "get": "get_list",
    })),
    path("data", Honor.as_view({
        "patch": "patch_data",
        "delete": "delete_data",
        "post": "get_upload",
        "put": "download_file",
    }))
]