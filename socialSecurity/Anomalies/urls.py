from django.urls import path,include,re_path
from . import views




urlpatterns = [
    path("get_anomalies_info",  views.Anomalies_Info_Get_RecordView.as_view()),  # 获取社保异常
    path("batch_anomalies_info",  views.Anomalies_Info_Batch_RecordView.as_view()),  # 上传社保增员信息
    path("post_dispose_gather",  views.Disponse_Gather_POST_RecordView.as_view()),  # 收集员工处理的结果  手机端
    path("post_dispose_overrule",  views.Disponse_Overrule_POST_RecordView.as_view()),  # 驳回员工处理的结果  电脑端
    path("down_anomalies_info",  views.Anomalies_Info_Down_RecordView.as_view()),  # 下载

    path("timing_employee_reminders", views.Anomalies_Employee_Reminders_RecordView.as_view()),  # 定时给员工提醒   7天一次
    path("social_anomalies_options", views.Social_Anomalies_Options),  # 下拉框
]