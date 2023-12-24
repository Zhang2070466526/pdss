from django.urls import path, include

urlpatterns = [
    path('intern/', include('monthReport.intern.urls')),  # 追光者模块
]