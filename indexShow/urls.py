from django.urls import path
from .views import *

urlpatterns = [
    path("get_index_data/", get_index_data)
]