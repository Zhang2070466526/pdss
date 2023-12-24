from django.urls import include, path

urlpatterns = [
    path('basicInfo/', include('monthReport.intern.basicInfo.urls')),  # 追光者基本信息
    path('leaveInfo/', include('monthReport.intern.departInfo.urls')),  # 追光者基本信息

]
