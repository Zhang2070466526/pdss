from django.urls import path
from wx.me.views import *

urlpatterns = [
    path('get_me_page', get_me_page, name='get_me_page'),  # 获取个人信息主页
    path('get_notice_info', get_notice_info, name='get_notice_info'),  # 获取通知消息
    path('delete_notice_info', delete_notice_info, name='delete_notice_info'),  # 删除通知消息

]
