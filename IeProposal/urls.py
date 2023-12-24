

from django.urls import path

from . import views
# from .views import *

urlpatterns = [
    path('phone_post_proposal', views.phone_post_proposal, name='phone_post_proposal'),#手机端提交 提案

    path('download_file', views.download_file, name='download_file'),#文件下载
    path('select_oa', views.select_oa, name='select_oa'),#oa

    path('get_detailed_proposal', views.get_detailed_proposal, name='get_detailed_proposal'),  # 查询详细的提案（第二级）  手机端
    path('get_proposal', views.get_proposal, name='get_proposal'),#电脑端查看 提案
    path('proposal_options', views.proposal_options, name='proposal_options'),#下拉菜单(提案)
    path('get_confirm_proposal',views.get_confirm_proposal, name='get_confirm_proposal'),#查询已确认
    path('down_proposal',views.down_proposal, name='down_proposal'),#电脑端 下载提案
]