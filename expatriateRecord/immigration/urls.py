from django.urls import path

from . import views



urlpatterns = [


    path('record/query/thailand', views.RecordQueryThailandRecordView.as_view()),  # 出入境记录查询   泰国有签证
    path('record/query/thailand-not', views.RecordQueryThailandNotRecordView.as_view()),  # 出入境记录查询   泰国没有签证
    path('record/query/vietnam', views.RecordQueryVietnamRecordView.as_view()),  # 出入境记录查询   越南

    path('record/down/vietnam', views.RecordDownVietnamRecordView.as_view()),  # 出入境记录下载  越南

    path('record/import', views.RecordImportRecordView.as_view()),  # 出入境记录导入
    path('record/delete', views.RecordDelRecordView.as_view()),  # 出入境记录删除
    path('record/edit', views.RecordEditRecordView.as_view()),  # 出入境记录修改
    path('record/post', views.RecordPostRecordView.as_view()),  # 出入境记录新增



    path('employee/fill', views.EmployeeFillRecordView.as_view()),  #  员工填写
    path('employee/fill-verify', views.EmployeeFillRecordView.as_view()),  # 校验填写时间
    path('employee/fill-overrule', views.EmployeeFillOverruleRecordView.as_view()), # 员工填写记录驳回

    path('alert/info', views.AlertInfoRecordView.as_view()),   # 信息提醒   定时任务
    path('calculate/attendance', views.AttendanceRecordView.as_view()),   # 计算考勤   定时任务
    path('immigration/options', views.immigration_options),  #下拉框

]
