from django.urls import path
from .views import *

urlpatterns = [
    path('basicDepartInfo', basicDepartInfo.as_view()),
    path('fileDepartInfo', fileDepartInfo.as_view()),
]