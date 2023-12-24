from django.urls import path,include,re_path
from .views import *
# from employee.employeeClass.dataReport import *
urlpatterns = [
    path('basic_sync', basic_sync, name='basic_sync'),  # 基本信息同步
    path("get_user_field", get_user_field, name='get_user_field'),  # 获取登录用户对应的要查看的字段
    path("get_roster_info", get_roster_info, name='get_roster_info'),  # 花名册查询
    path("download_roster_info", download_roster_info, name='download_roster_info'),  # 花名册下载
    path("get_jobrank_option", get_jobrank_option, name='get_jobrank_option'),  # 合同归属下拉菜单
    path("get_department_option", get_department_option, name='get_department_option'),  # 基地归属下拉菜单
    path("get_roster_options",get_roster_options,name='get_roster_options'),#花名册下拉菜单


    path('dimissionReason_sync',dimissionReason_sync,name='dimissionReason_sync'), #报表平台 离职原因同步
    path('dimissionType_sync',dimissionType_sync,name='dimissionType_sync'), #报表平台 离职类型同步




    # path('active_employee_total',active_employee_total,name='active_employee_total'), #报表平台 汇总
    # path('active_employee_seniority',active_employee_seniority,name='active_employee_seniority'), #报表平台 司龄分布
    # path('active_employee_age',active_employee_age,name='active_employee_age'), #报表平台 年龄分布
    # path('active_employee_education', active_employee_education, name='active_employee_education'),  # 报表平台 学历分布
    # path('active_employee_nationality', active_employee_nationality, name='active_employee_nationality'),  # 报表平台 国籍分布
    # path('active_employee_sex', active_employee_sex, name='active_employee_sex'),  # 报表平台 性别分布
    # path('active_employee_promotion', active_employee_promotion, name='active_employee_promotion'),  # 报表平台 晋身情况
    # path('active_employee_job_grade', active_employee_job_grade, name='active_employee_job_grade'),  # 报表平台 职级分布
    # path('departure_employee_reason', departure_employee_reason, name='departure_employee_reason'),  # 报表平台 离职率分析 按离职原因
    # path('departure_employee_seniority', departure_employee_seniority, name='departure_employee_seniority'),  # 报表平台 离职率分析 按司龄

   # path('basic_data',basic_data,name='basic_data'),#报表平台 基础数据查询



    path('limit_get_data',limit_get_data,name='limit_get_data'),#报表平台 编制数据（查询）
    path('limit_post_data',limit_post_data,name='limit_post_data'),#报表平台 编制数据（新增）
    path('limit_batch_data',limit_batch_data,name='limit_batch_data'),#报表平台 编制数据（批量上传）
    path('limit_edit_data',limit_edit_data,name='limit_edit_data'),#报表平台 编制数据（修改）
    path('limit_down_data',limit_down_data,name='limit_down_data'),#报表平台 编制数据（下载）
    path('target_get_data',target_get_data,name='target_get_data'),#报表平台 离职率目标数据（查询）
    path('target_post_data',target_post_data,name='target_post_data'),#报表平台 离职率目标数据（新增）
    path('target_batch_data',target_batch_data,name='target_batch_data'),#报表平台 离职率目标数据（批量上传）
    path('target_edit_data',target_edit_data,name='target_edit_data'),#报表平台 离职率目标数据（修改）
    path('target_down_data',target_down_data,name='target_down_data'),#报表平台 离职率目标数据（下载）
    path('basic_data', views.Basic_Data_RecordView.as_view()),  # 报表平台 基础数据查询
    path('get_employee_options',get_employee_options,name='get_employee_options'),#报表平台 下拉框总和

    path('active_employee_total', views.Active_Employee_Total_RecordView.as_view()),   #报表平台 汇总

    path('departure_employee_seniority', views.Departure_Employee_Seniority_RecordView.as_view()),  # 报表平台 离职率分析 按司龄
    path('departure_employee_reason', views.Departure_Employee_Reason_RecordView.as_view()),  # 报表平台 离职率分析 按离职原因
    path('active_employee_job_grade', views.Active_Employee_Job_Grade_RecordView.as_view()),  # 报表平台 职级分布
    path('active_employee_seniority',views.Active_Employee_Seniority_RecordView.as_view()), #报表平台 司龄分布
    path('active_employee_age',views.Active_Employee_Age_RecordView.as_view()), #报表平台 年龄分布
    path('active_employee_education', views.Active_Employee_Education_RecordView.as_view()),  # 报表平台 学历分布
    path('active_employee_nationality', views.Active_Employee_Nationality_RecordView.as_view()),  # 报表平台 国籍分布
    path('active_employee_sex', views.Active_Employee_Sex_RecordView.as_view()),  # 报表平台 性别分布
    path('active_employee_promotion', views.Active_Employee_Promotion_RecordView.as_view()),  # 报表平台 晋升情况

    # path('history_basic_sync_week', views.history_basic_sync_week, name='history_basic_sync_week'),  # 历史数据基本信息同步  周
    # path('history_basic_sync_month', views.history_basic_sync_month, name='history_basic_sync_month'),  # 历史数据基本信息同步  月

    path('report_visualization', views.Report_Visualization_RecordView.as_view()),  # 报表可视化
    path('report_save', views.Report_Save_RecordView.as_view()),  # 报表数据存储




    # # 人事数据平台
    # path('employee_profile_slices', views.Employee_Profile_Slices.as_view()),  # 报表平台 员工档案切片
    #
    #
    # path('archives/', include('employee.archives.urls')),  # 档案管理







]