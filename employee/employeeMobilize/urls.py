from .views import *
from django.urls import path

urlpatterns = [
    path('basicMobilize', basicDepartInfo.as_view()),
    path('fileMobilize', fileMobilizeInfo.as_view()),
    path('data_sync', data_sync),
]
