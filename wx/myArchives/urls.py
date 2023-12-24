from django.urls import path
from wx.myArchives.views import *

urlpatterns = [
    path('get_file_info', get_file_info, name="get_file_info"),  # 获取文件信息
    path('get_file_info_page', get_file_info_page, name="get_file_info_page"),  # 获取页面详情

]
