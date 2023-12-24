from django.urls import path
from .views import *

urlpatterns = [
    path('upload_basic_info', upload_basic_info, name='upload_basic_info'),  # 导入名单
    path('get_basic_info', get_basic_info, name='get_basic_info'),  # 查询

    path('basicInfo', basicInfo.as_view()),  # 增删改查
    path('fileInfo', fileInfo.as_view()),  # 其他操作

]
