from django.urls import path
from .views import *
from .methods import *
urlpatterns = [
    path('basicInfo', basicDepartInfo.as_view()),
    path('fileInfo', fileMobilizeInfo.as_view()),
]