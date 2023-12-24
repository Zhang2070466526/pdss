from django.urls import path
from wx.myInfo.views import *


urlpatterns = [
    # 获取待审批列表
    path('get_approve_list', get_approve_list, name='get_approve_list'),
    path('edit_approve_list', edit_approve_list, name='edit_approve_list'),
]