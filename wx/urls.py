from wx.myInfo.views import *
from wx.salary.views import *
from wx.attendance.views import *

from django.urls import path, include

urlpatterns = [
    # 获取个人信息
    path('myinfo/', include("wx.myInfo.urls")),
    # path('info/', InfoView.as_view()),
    path('get_info', get_info, name='get_info'),
    path('edit_info', edit_info, name='edit_info'),

    # 下拉菜单
    path('drop_down_menu', drop_down_menu, name='drop_down_menu'),

    path('get_index_bar', get_index_bar, name='get_index_bar'),  # 获取首页导航栏
    # 考勤查询
    path('attendance/data', Attendance.as_view()),

    # 薪资查询
    path('salary/', include("wx.salary.urls")),
    # 登录模块
    path('login/', include("wx.login.urls")),
    # 我的档案模块
    path('myArchives/', include("wx.myArchives.urls")),
    path('me/', include("wx.me.urls")),


]
