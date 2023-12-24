
from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('record',views.recordDetailView.as_view()),   #大事记接口
]