from django.shortcuts import render
import datetime, json, os, random, string
from django.http import HttpResponse
from rest_framework import serializers  # 序列化器
from rest_framework.generics import GenericAPIView
from rest_framework.status import *

from memorabilia.models import *
from memorabilia.memo.memoClass import Reset
from utils.check_token import *
from rest_framework.response import Response

class MemorabiliaListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MemorabiliaList
        fields = '__all__'




class recordDetailView(GenericAPIView):
    queryset = MemorabiliaList.objects.all()
    serializer_class = MemorabiliaListSerializers

    def verify(self, request):
        return_data = {'code': '', "msg": ''}
        new_token = CheckToken()
        try:
            check_token = new_token.check_token(request.headers['Authorization'])
        except Exception as e:
            # print(e)
            return_data['code'] = HTTP_400_BAD_REQUEST
            return_data['msg'] = '请求参数出错啦'
            return return_data
        if check_token is None:
            return_data['code'] = HTTP_403_FORBIDDEN
            return_data['msg'] = '没有权限查询'
            return return_data

    def get(self, request):  # 查询
        if self.verify(self.request):
            return Response(self.verify(self.request))
        # token = request.headers['Authorization']
        new_query = Reset(request, 'resetGet')
        query = new_query.meth_center()
        return query

    def post(self, request):  # 新增
        if self.verify(self.request):
            return Response(self.verify(self.request))
        # token = request.headers['Authorization']
        new_query = Reset(request, 'resetPost')
        query = new_query.meth_center()
        return query

    def delete(self, request):  # 删除
        if self.verify(self.request):
            return Response(self.verify(self.request))
        new_query = Reset(request, 'resetDelete')
        query = new_query.meth_center()
        return query

    def patch(self, request):  # 修改
        if self.verify(self.request):
            return Response(self.verify(self.request))
        new_query = Reset(request, 'resetPatch')
        query = new_query.meth_center()
        return query
    def put(self,request):#下载数据
        if self.verify(self.request):
            return Response(self.verify(self.request))
        new_query=Reset(request,'resetPut')
        query=new_query.meth_center()
        return query

