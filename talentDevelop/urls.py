from django.urls import path, include
from.views import *
urlpatterns = [
    path('optimization/', include('talentDevelop.optimization.urls')),  # 人员优化 (人才发展)
    path('overseasTrace/', include('talentDevelop.overseasTrace.urls')),  # 海外本土跟踪
    path('get_department_option_two/', get_department_option_two, name='get_department_option_two'),  # 基地归属 二级部门
    # path('test_data/', test_data, name='test_data'),

]