# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 15:40
# @Author  : zhuang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from .views import *

urlpatterns = [
    path("dl/upload", DL.as_view({
        "post": "get_upload",
    })),
    path("dl/record", DL.as_view({
        "get": "get_list",
    })),
    path("dl/data", DL.as_view({
        "patch": "patch_data",
        "delete": "delete_data",
        "post": "get_upload",
        "put": "download_file",
    })),

    path("idl/upload", IDL.as_view({
        "post": "get_upload",
    })),
    path("idl/record", IDL.as_view({
        "get": "get_list",
    })),
    path("idl/data", IDL.as_view({
        "patch": "patch_data",
        "delete": "delete_data",
        "post": "get_upload",
        "put": "download_file",
    })),

    path("sal/upload", SAL.as_view({
        "post": "get_upload",
    })),
    path("sal/record", SAL.as_view({
        "get": "get_list",
    })),
    path("sal/data", SAL.as_view({
        "patch": "patch_data",
        "delete": "delete_data",
        "post": "get_upload",
        "put": "download_file",
    })),

    # path("collect/data", Collect.as_view({
    #     "patch": "patch_data",
    #     "delete": "delete_data",
    #     "post": "get_upload",
    #     "put": "download_file",
    # })),
    path("collect/record", Collect.as_view({
        "get": "get_list",
    })),
    path("collect/data", Collect.as_view({
        "put": "download_file",
    })),
]