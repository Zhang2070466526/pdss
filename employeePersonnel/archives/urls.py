from django.urls import path,include,re_path

# from employeePersonnel import views
from employeePersonnel.archives import views
urlpatterns = [
    # 人事数据平台
    # path('week_info', views.ArchiveSlicesWeekInfo.as_view()),  # 报表平台 员工档案切片 周
    # path('month_info', views.ArchiveSlicesMonthInfo.as_view()),  # 报表平台 员工档案切片 月
    #
    # path('week_down', views.ArchiveSlicesWeekDown.as_view()),  # 报表平台 员工档案切片 周
    # path('month_down', views.ArchiveSlicesMonthDown.as_view()),  # 报表平台 员工档案切片 月

    path('slice_info_select', views.ArchiveSlicesInfoSelect.as_view()),  # 报表平台 员工档案切片
    path('slice_info_down', views.ArchiveSlicesInfoDown.as_view()),  # 报表平台 员工档案切片
    path("slice_info_options",views.slice_info_options,name='slice_info_options'),# 员工档案 下拉菜单


]