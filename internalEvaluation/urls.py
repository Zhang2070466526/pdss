from django.urls import path,include,re_path
from . import views
from internalEvaluation.views import *
# urlpatterns = [
#     path('record',views.recordDetailView.as_view()),   #内部评优
# ]



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