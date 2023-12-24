from django.urls import path,include,re_path
from . import views
from employeeInspect.views import *



urlpatterns = [
    path("record", recordDetailView.as_view({
        "get": "get_list",
    })),
    path("data", recordDetailView.as_view({
        "post": "get_upload",
        "patch": "patch_data",
        "delete": "delete_data",
        "put": "download_file",
    }))
]