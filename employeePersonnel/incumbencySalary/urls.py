from django.urls import path,include,re_path

# from employeePersonnel import views
from employeePersonnel.incumbencySalary import views
urlpatterns = [
    # 人事数据平台
    path('analyse_info', views.AnalyseInfo.as_view()),  # 在职员工职级/绩效/调薪关联分析      17
    # path('analyse_info', views.AnalyseInfo.as_view()),  # 员工历月税前工资总额     16
]