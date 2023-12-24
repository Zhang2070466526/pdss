from django.urls import path,include,re_path

from employeePersonnel import views

urlpatterns = [
    # path('test/celery',views.test_celery,name='test_celery'),
    # path('history_sync/week', views.history_basic_sync_week, name='history_basic_sync_week'),  # 历史数据基本信息同步  周
    # path('history_sync/month', views.history_basic_sync_month, name='history_basic_sync_month'),  # 历史数据基本信息同步  月
    # path('test/threading/file', views.test_threading_file, name='test_threading_file'),  # 档案管理

    path('section/', include('employeePersonnel.section.urls')),  # 切片部分




    path('archive_slices/',include('employeePersonnel.archives.urls')),  # 档案切片管理
    path('incumbency_salary/',include('employeePersonnel.incumbencySalary.urls')),      #在职薪资
    path('pretaxSalary/',include('employeePersonnel.pretaxSalary.urls')),      #税前薪资
    path('adjustmentSalary/',include('employeePersonnel.adjustmentSalary.urls')),      #调薪历程
    path('adjustmentJobGrade/',include('employeePersonnel.adjustmentJobGrade.urls')),      #调职历程



]