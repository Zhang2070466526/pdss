from django.urls import path, include, re_path
from . import views
from employeeCare.views import *

urlpatterns = [
    path("ts/record", tsrecordDetailView.as_view({  # 人才补贴
        "get": "get_list",
    })),
    path("ts/data", tsrecordDetailView.as_view({
        "post": "get_upload",
        "patch": "patch_data",
        "delete": "delete_data",
        "put": "download_file",
    })),

    path("ei/record", eirecordDetailView.as_view({  # 离职访谈
        "get": "get_list",
    })),
    path("ei/data", eirecordDetailView.as_view({
        "post": "get_upload",
        "patch": "patch_data",
        "delete": "delete_data",
        "put": "download_file",
    })),

    path("cq/record", cqrecordDetailView.as_view({  # 座谈会
        "get": "get_list",
    })),
    path("cq/data", cqrecordDetailView.as_view({
        "post": "get_upload",
        "patch": "patch_data",
        "delete": "delete_data",
        "put": "download_file",
    })),

    path("ji/record", jirecordDetailView.as_view({  # 在职访谈
        "get": "get_list",
    })),
    path("ji/data", jirecordDetailView.as_view({
        "post": "get_upload",
        "patch": "patch_data",
        "delete": "delete_data",
        "put": "download_file",
    }))

]
