from django.urls import path, include
from.views import *
urlpatterns = [
    path('optimization/', include('staffFollowing.optimization.urls')),  # 人员优化 (人才发展)
    path('get_department_option_two/', get_department_option_two, name='get_department_option_two'),  # 基地归属 二级部门

    # talentDevelop
]