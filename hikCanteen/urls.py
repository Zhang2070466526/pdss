# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 16:17
# @Author  : zhuang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('daliy_add_zb_dept', views.daliy_add_zb_dept, name='daliy_add_zb_dept'),
    path('daliy_add_zb_person', views.daliy_add_zb_person, name='daliy_add_zb_person'),
    path('zongbuSingleFace', views.zongbuSingleFace, name='zongbuSingleFace'),
    path('daliy_add_jheq_dept', views.daliy_add_jheq_dept, name='daliy_add_jheq_dept'),
    path('daliy_add_jheq_person', views.daliy_add_jheq_person, name='daliy_add_jheq_person'),
    path('jianhuerqiSingleFace', views.jianhuerqiSingleFace, name='jianhuerqiSingleFace'),
    path('select_expenses_record', views.select_expenses_record, name='select_expenses_record'),
    path('select_person_cards', views.select_person_cards, name='select_person_cards'),
    path('select_person', views.select_person, name='select_person'),
    path('report_loss_card', views.report_loss_card, name='report_loss_card'),
    path('report_unloss_card', views.report_unloss_card, name='report_unloss_card'),
    path('select_balance', views.select_balance, name='select_balance'),
    path('wechat', views.wechat, name='wechat'),# 企业微信
    path('daliy_entry_person_for_oa', views.daliy_entry_person_for_oa, name='daliy_entry_person_for_oa'),  # 新员工入职首充
    path('receive_oa_daliy', views.receive_oa_daliy, name='receive_oa_daliy'),  # 新员工入职首充
    path('update_face', views.update_face, name='update_face'),  # 新员工入职首充
    path('month_money_to_oa', views.month_money_to_oa, name='month_money_to_oa'),  # 新员工入职首充
    path('select_face_pic', views.get_face_pic, name='month_money_to_oa'),  # 新员工入职首充
    path('meal_card_top_up_system', views.get_card_top_up_system, name='meal_card_top_up_system'),  # 饭卡充值(平台)  查询
    path('meal_card_top_up_download', views.get_meal_card_top_up_download, name='meal_card_top_up_download'),  # 饭卡充值(平台) 下载
    path('jobrank_hik_Option', views.get_jobrank_hik_Option, name='jobrank_hik_Option'),  # 合同归属下拉菜单

]
