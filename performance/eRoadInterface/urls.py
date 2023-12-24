from django.urls import path,include,re_path
from . import views




urlpatterns = [
    path("get_token",  views.Create_Token_POST_RecordView.as_view()),  # 创建 token

    path("push_performance_data",  views.Push_Performance_Data_POST_RecordView.as_view()),  # 推送数据
]