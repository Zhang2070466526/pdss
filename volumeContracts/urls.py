# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 16:17
# @Author  : zhuang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from .views import *

urlpatterns = [

    path("empInfoFillIn", ContractsView.as_view({
        "patch": "patch_data",
        "delete": "delete_data",
        "post": "get_upload",
        "get": "get_list",
        "put": "download_file",

    })),
    path("jobrankOption", jobRankView.as_view({
        "get": "jobrank_drop",
    })),

]