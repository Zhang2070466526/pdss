# from django.shortcuts import render
# from rest_framework.views import APIView
# # Create your views here.
# from employeeSocialSecurity.Anomalies.anomalies import *
#
#
#
#
#
# class Anomalies_Info_Get_RecordView(APIView): # 社保增员信息查询
#     def post(self, request, **kwargs):
#         new_query = Anomalies(request, 'get_anomalies_info')
#         query = new_query.method_center()
#         return query
#
# class Anomalies_Info_Batch_RecordView(APIView): #上传
#     def post(self, request, **kwargs):
#         new_query = Anomalies(request, 'batch_anomalies_info')
#         query = new_query.method_center()
#         return query