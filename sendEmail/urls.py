# -*- coding: utf-8 -*-
# @Time    : 2023/6/6 11:16
# @Author  : zhuang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from .views import *

urlpatterns = [
    path("sbxb", sendEmail.as_view({
        "get": "get_attendance_list",
        "put": "get_attendance_data",
        "post": "add_dept",
        "delete": "del_data",
    })),
    path("sbxbData", sendEmail.as_view({
        "get": "get_attendance_data",
    }))
    ,
    path("dimissday", sendEmail.as_view({

        "get": "get_everyday_leave_data",
    })),
    path("test_send", sendEmail.as_view({
        "get": "test_send",
    })),
    path("dimissweek", sendEmail.as_view({
        "get": "get_dimissweek_list",
    })),
    path("dimissweekData", sendEmail.as_view({
            "get": "get_everyweek_leave_data",
        })),
    path("data", sendEmail.as_view({
        "get": "get_dept",
        "post": "post_person",
        "patch": "patch_data",
        "delete": "delete_one_dept_apt"
    }))
]
