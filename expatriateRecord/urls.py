from django.urls import path

from . import views

urlpatterns = [
    path('expatriateLedger', views.ExpatriateLedgerRecordView.as_view()),   #外派台账
    path('expatriateInfo', views.ExpatriateInfoRecordView.as_view()),   #外派信息
    path('visaLedger', views.VisaLedgerRecordView.as_view()),   #签证台账
    path('ticketLedger', views.TicketLedgerRecordView.as_view()),   #机票台账

    path('ticketLedgerTemplate',views.TicketLedgerTemplateRecordView.as_view()),  # 机票上传模版文件新增
    path('visaLedgerTemplate',views.VisatLedgerTemplateRecordView.as_view()),  # 签证台账上传模版文件新增

    path('options', views.ExpatriateOptionsView.as_view()),  #下拉菜单总接口
    path('employeeInfo', views.EmployeeInfo.as_view()),   #人员工号接口
    path('expatriateOA', views.ExpatriateOARecordView.as_view()),   #OA流程(一次性全部的)
    path('expatriateOAIncrement', views.ExpatriateOAIncrementRecordView.as_view()),   #OA流程(现在时间的两个小时之前的)
    path('expatriateAnnex', views.ExpatriateAnnexRecordView.as_view()),   #附件
    path('expatriateRemainingTime',views.ExpatriateRemainingTimeRecordView.as_view()),  #计算剩余时间 定时触发
    path('ticketrelevancyssc',views.TicketrelevancysscRecordView.as_view()),  #计算机票与信息的关联关系 定时触发



]
