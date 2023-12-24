from .views import *
from django.urls import path

urlpatterns = [
    path('login_judge', login_judge, name='login_judge'),
    path('get_login_page', get_login_page, name='get_login_page'),
]