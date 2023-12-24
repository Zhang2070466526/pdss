from django.urls import path,include,re_path
# from . import views
# from Anomalies.urls import views



# urlpatterns = [
#     path("get_anomalies_info",  views.Anomalies_Info_Get_RecordView.as_view()),  # 获取社保异常
#     path("batch_anomalies_info",  views.Anomalies_Info_Batch_RecordView.as_view()),  # 上传社保增员信息
# ]

urlpatterns = [

    path('Anomalies/',include('socialSecurity.Anomalies.urls')),# 社保增员

]