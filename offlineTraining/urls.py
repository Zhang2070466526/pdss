from django.urls import path

from . import views
# from .views import *

urlpatterns = [
    path("get_lecturer_info", views.get_lecturer_info, name='get_lecturer_info'),  # 获取讲师库数据
    path("edit_lecturer_info", views.edit_lecturer_info, name='edit_lecturer_info'),  # 修改讲师库数据
    path("delete_lecturer_info", views.delete_lecturer_info, name='delete_lecturer_info'),  # 删除讲师库数据
    path("post_lecturer_info", views.post_lecturer_info, name='post_lecturer_info'),  # 新增讲师库数据
    path("batch_lecturer_info", views.batch_lecturer_info, name='batch_lecturer_info'),  # 批量上传讲师库数据
    path("down_lecturer_info", views.down_lecturer_info, name='down_lecturer_info'),  # 下载讲师库数据

    path("get_employee_info", views.get_employee_info, name='get_employee_info'),  # 跟据工号 获取姓名等数据
    path("summary_lecturer_info", views.summary_lecturer_info, name='summary_lecturer_info'),  # 汇总讲师数据
    path("down_summary_lecturer_info", views.down_summary_lecturer_info, name='down_summary_lecturer_info'),  # 下载汇总讲师数据

    path("get_retired_lecturer_info", views.get_retired_lecturer_info, name='get_retired_lecturer_info'),  # 获取卸任讲师的数据
    path("edit_retired_lecturer_info", views.edit_retired_lecturer_info, name='edit_retired_lecturer_info'),  # 恢复讲师任命


    path("get_content_info", views.get_content_info, name='get_content_info'),  # 获取培训报表数据
    path("post_content_info", views.post_content_info, name='post_content_info'),  # 新增培训报表数据
    path("delete_content_info", views.delete_content_info, name='delete_content_info'),  # 删除培训报表数据
    path("edit_content_info", views.edit_content_info, name='edit_content_info'),  # 修改培训报表数据批量
    path("download_content_info", views.download_content_info, name='download_content_info'),  #下载培训报表数据
    path("batch_content_info", views.batch_content_info, name='batch_content_info'),  #上传培训报表数据

    path('del_content_file', views.del_content_file, name='del_content_file'),  # 删除培训报表相关文件
    path('post_content_file', views.post_content_file, name='post_content_file'),  # 上传培训报表相关文件



    path("month_summary_analysis", views.month_summary_analysis, name='month_summary_analysis'),  #每月线下培训汇总分析
    path("download_month_summary_analysis", views.download_month_summary_analysis, name='download_month_summary_analysis'),  #每月线下培训汇总分析  下载

    path("month_Training_hours_per_person", views.month_Training_hours_per_person, name='month_Training_hours_per_person'),  #每月基地人均培训课时 查询
    path("edit_month_Training_hours_per_person", views.edit_month_Training_hours_per_person, name='edit_month_Training_hours_per_person'),  #每月基地人均培训课时 修改
    path("download_month_Training_hours_per_person", views.download_month_Training_hours_per_person, name='download_month_Training_hours_per_person'),  #每月基地人均培训课时 下载
    path('options', views.offline_training_options, name='offline_training_options'),  #下拉菜单总接口


    path("training_content_type", views.Training_Content_Type_RecordView.as_view()),  #培训类型   查询 新增
    path("edit_training_content_type", views.Edit_Training_Content_Type_RecordView.as_view()),  #培训类型   修改
    path("del_training_content_type", views.Del_Training_Content_Type_RecordView.as_view()),  #培训类型   删除


    path("training_content_type_options", views.training_content_type_options,name='training_content_type_options'),  #培训类型下拉框

    path("get_training_checkin", views.Training_Checkin_Get_RecordView.as_view()),  #培训签到 查询
    path("post_training_checkin", views.Training_Checkin_Post_RecordView.as_view()),  #培训签到 新增
    path("down_training_checkin", views.Training_Checkin_Down_RecordView.as_view()),  #培训签到 下载
    path("batch_training_checkin", views.Training_Checkin_Batch_RecordView.as_view()),  #培训签到 上传
    path("del_training_checkin", views.Training_Checkin_Del_RecordView.as_view()),  # 培训签到 删除
    path("edit_training_checkin", views.Training_Checkin_Edit_RecordView.as_view()),  # 培训签到 修改

    path('test_data',views.test_data,name='test_data'),





]
