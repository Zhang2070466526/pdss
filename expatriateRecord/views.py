from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.response import Response

from expatriateRecord.expatriate.expatriateInfoClass import *  # 签证信息 oa流程 下拉菜单  计算剩余时间
from expatriateRecord.expatriate.visaLedgerClass import *  # 签证台账
from expatriateRecord.expatriate.ticketLedgerClass import *  # 机票台账
from expatriateRecord.expatriate.expatriateLedgerClass import *  # 外派台账


class ExpatriateInfoRecordView(GenericAPIView):  # 外派信息
    def get(self, request):  # 查询
        new_query = ResetExpatriateInfo(request, 'resetGet')
        query = new_query.meth_center()
        return query

    def delete(self, request):  # 删除
        new_query = ResetExpatriateInfo(request, 'resetDelete')
        query = new_query.meth_center()
        return query

    def post(self, request):  # 新增
        new_query = ResetExpatriateInfo(request, 'resetPost')
        query = new_query.meth_center()
        return query

    def patch(self, request):  # 修改
        new_query = ResetExpatriateInfo(request, 'resetPatch')
        query = new_query.meth_center()
        return query
    def put(self, request):  # 下载
        new_query = ResetExpatriateInfo(request, 'resetPut')
        query = new_query.meth_center()
        return query

class VisaLedgerRecordView(GenericAPIView):  # 签证台账
    def get(self, request):  # 查询
        new_query = ResetVisaLedger(request, 'resetGet')
        query = new_query.meth_center()
        return query

    def delete(self, request):  # 删除
        new_query = ResetVisaLedger(request, 'resetDelete')
        query = new_query.meth_center()
        return query

    def post(self, request):  # 新增
        new_query = ResetVisaLedger(request, 'resetPost')
        query = new_query.meth_center()
        return query

    def patch(self, request):  # 修改
        new_query = ResetVisaLedger(request, 'resetPatch')
        query = new_query.meth_center()
        return query
    def put(self, request):  # 下载
        new_query = ResetVisaLedger(request, 'resetPut')
        query = new_query.meth_center()
        return query


class TicketLedgerRecordView(GenericAPIView):  # 机票台账
    def get(self, request):  # 查询
        new_query = ResetTicketLedger(request, 'resetGet')
        query = new_query.meth_center()
        return query

    def delete(self, request):  # 删除
        new_query = ResetTicketLedger(request, 'resetDelete')
        query = new_query.meth_center()
        return query

    def post(self, request):  # 新增
        new_query = ResetTicketLedger(request, 'resetPost')
        query = new_query.meth_center()
        return query

    def patch(self, request):  # 修改
        new_query = ResetTicketLedger(request, 'resetPatch')
        query = new_query.meth_center()
        return query

    def put(self, request):  # 下载
        new_query = ResetTicketLedger(request, 'resetPut')
        query = new_query.meth_center()
        return query

class TicketLedgerTemplateRecordView(GenericAPIView):#机票模板文件上传数据
    def post(self, request):  # 上传模板文件数据
        new_query = ResetTicketLedger(request, 'resetPostTemplate')
        query = new_query.meth_center()
        return query
class VisatLedgerTemplateRecordView(GenericAPIView):#签证台账模板文件上传数据
    def post(self, request):  # 上传模板文件数据
        new_query = ResetVisaLedger(request, 'resetPostTemplate')
        query = new_query.meth_center()
        return query

class ExpatriateLedgerRecordView(GenericAPIView):  # 外派台账
    def get(self, request):  # 查询
        new_query = ResetExpatriateLedger(request, 'resetGet')
        query = new_query.meth_center()
        return query

    def put(self, request):  # 下载
        new_query = ResetExpatriateLedger(request, 'resetPut')
        query = new_query.meth_center()
        return query


class ExpatriateOptionsView(GenericAPIView):  # 下拉菜单
    def get(self, request, **kwargs):
        new_query = ResetExpatriateInfo(request, 'optionGet')
        query = new_query.meth_center()
        return query


class EmployeeInfo(APIView):  # 人员工号查询
    def get(self, request, **kwargs):
        new_query = ResetExpatriateInfo(request, 'infoGet')  # 根据工号获取部门等数据
        query = new_query.meth_center()
        return query

    def post(self, request, **kwargs):
        new_query = ResetExpatriateInfo(request, 'infoSelete')  # 根据工号获取信息表的数据
        query = new_query.meth_center()
        return query


class ExpatriateOARecordView(APIView):
    def get(self, request, **kwargs):  # 流程数据新增
        new_query = ResetExpatriateOA(request, 'oaPost')
        query = new_query.meth_center()
        return query

class ExpatriateOAIncrementRecordView(APIView):
    def get(self, request, **kwargs):  # 流程数据新增(两个小时之前的)
        new_query = ResetExpatriateOA(request, 'oaPostIncrement')
        query = new_query.meth_center()
        return query


class ExpatriateAnnexRecordView(APIView):  # 附件管理
    def post(self, request, **kwargs):  # 手机端附件新增
        new_query = ResetExpatriateAnnex(request, 'annexPost')
        query = new_query.meth_center()
        return query


class ExpatriateRemainingTimeRecordView(APIView):  # 定时任务 计算距签证过期日剩余
    def get(self, request, **kwargs):
        new_query = ResetExpatriateRemainingTime(request, 'remainingTime')
        query = new_query.meth_center()
        return query
class TicketrelevancysscRecordView(APIView):  # 定时任务 机票与签证关联
    def get(self, request, **kwargs):
        new_query = ResetTicketrelevancyssc(request, 'ticketRelevancySSC')
        query = new_query.meth_center()
        return query

