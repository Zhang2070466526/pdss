from django.urls import path,include,re_path
from . import views
from rewardsPunishments.views import *



urlpatterns = [
    path("pb/record", pbrecordDetailView.as_view({   #  项目奖金
        "get": "get_list",
    })),
    path("pb/data", pbrecordDetailView.as_view({
        "post": "get_upload",
        "patch": "patch_data",
        "delete": "delete_data",
        "put": "download_file",
    })),


    path("rp/record", rprecordDetailView.as_view({  # 奖惩
        "get": "get_list",
    })),
    path("rp/data", rprecordDetailView.as_view({
        "post": "get_upload",
        "patch": "patch_data",
        "delete": "delete_data",
        "put": "download_file",
    }))



]