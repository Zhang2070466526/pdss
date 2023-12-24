from django.urls import path
from .views import *

urlpatterns = [

    path("data", RestrictionsView.as_view({
        "patch": "patch_data",
        "delete": "delete_data",
        "post": "get_upload",
        "get": "get_list",
        "put": "download_file",

    })),
    path("file", RestrictionsView.as_view({
        "delete": "delete_other_file",
    })),
    path("annexfile", RestrictionsView.as_view({
        "delete": "delete_annex_file",
        'post':'post_annex_file'
    })),
    path("dataSystem", RestrictionsView.as_view({
        "post": "get_systemUpload",
    })),
    path("verify", RestrictionsView.as_view({
        "get": "verify",
    })),
    path("location", RestrictionsView.as_view({
        "get": "get_location",
    })),
    path("isExpiration", RestrictionsView.as_view({
        "get": "get_isExpiration",
    })),

]
#
# from django.conf import settings
# from django.urls import path, include
#
# # 判断当前是否为调试模式  所以在settings.py 中一定要配置Debug = True 才能调用debug_toolbar
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))
