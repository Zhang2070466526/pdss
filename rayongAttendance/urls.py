# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 16:17
# @Author  : zhuang
# @Site    :
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # 获取详细数据
    path('attendance_data', views.attendance_data, name='attendance_data'),  # 泰国罗勇考勤 get
    path('rayong_shift', views.get_rayong_shift, name='rayong_shift'),
    path('rayong_department_data', views.get_rayong_department_data, name='rayong_department_data'),
    path('generate_data_method', views.generate_data_method, name='generate_data_method'),
]
