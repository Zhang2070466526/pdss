from django.urls import path
from .views import *

urlpatterns = [
    # 管理员
    path("upload_info", upload_info, name='upload_info'),  # 文件上传导入
    path("get_list", get_list, name='get_list'),  # 获取人员列表
    path("edit_person", edit_person, name='edit_person'),  # 编辑人员信息
    path("delete_person", delete_person, name='delete_person'),  # 删除人员信息
    path("download_info", download_info, name='download_info'),  # 下载人员信息
    path("create_single_info", create_single_info, name='create_single_info'),  # 新增人员信息

    # 员工
    path("add_repair", add_repair, name='add_repair'),  # 新增人员信息
    path("get_my_info", get_my_info, name='get_my_info'),  # 获取人员信息
]
