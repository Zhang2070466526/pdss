from django.urls import path
from .views import *

urlpatterns = [
    # 薪资查询
    path('salaryList', SalaryList.as_view()),
    path('is_have_password', is_have_password, name='is_have_password'),  # 输入密码界面
    path('forget_password_page', forget_password_page, name='forget_password_page'),  # 忘记密码界面
    path('forget_password', forget_password, name='forget_password'),  # 修改密码接口
    path('check_password', check_password, name='check_password'),  # 验证密码接口
    path('salary_confirm', salary_confirm, name='salary_confirm'),  # 薪资确认啊
    path('salary', Salary.as_view()),
]