from django.urls import path
from .views import *

urlpatterns = [
    path('section_every_week', section_every_week, name='section_every_week'),
    path('section_every_month', section_every_month, name='section_every_month'),
]
