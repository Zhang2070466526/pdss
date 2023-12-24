import calendar
import os, datetime, json, openpyxl, time, random, string, re, docx, zipfile, os,shutil
from datetime import datetime, date
# from urllib import request
import pathlib
import requests
from django.forms.models import model_to_dict
from django.http import HttpResponse
from openpyxl import Workbook
from rest_framework.response import Response
from rest_framework import status
from openpyxl.styles import Font, Side, Alignment, Border
from openpyxl.utils import get_column_letter
from rest_framework.status import *

from pdss.settings import BASE_DIR
from auther.models import *
# from ..serializers import *
from ..models import *
from django.core.exceptions import ObjectDoesNotExist
from controller.controller2 import Controller, upload_file
from general.models import *
from utils.check_token import *
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from zipfile import ZipFile

class infoMgmt:  # 竞业限制
    def __init__(self, request, meth):
        self.request = request
        self.fileName = ""
        self.return_data = {}
        self.meth = meth
        self.methods = {
            "get_upload": self.get_upload,
            "get_list": self.get_list,
            "patch_data": self.patch_data,
            "delete_data": self.delete_data,
            "download_file": self.download_file,
            'delete_other_file':self.delete_other_file,
            'get_systemUpload':self.get_systemUpload,
            'verify':self.verify,
            'get_isExpiration':self.get_isExpiration,
            'post_annex_file':self.post_annex_file,
            'delete_annex_file':self.delete_annex_file,
            # 'location':self.get_location,
            # "upload_other_file": self.upload_other_file,
        }

    def meth_center(self):
        self.methods[self.meth]()
        return Response(self.return_data)


    def get_list(self):
    #     columnList=[
    #         {
    #             "value": "序号",
    #             "label": "index",
    #             "width": 60
    #         },
    #         {
    #             "value": "中心/事业部",
    #             "label": "base_father",
    #             "width": 210
    #         },
    #         {
    #             "value": "公司",
    #             "label": "cr_base",
    #             "width": 160
    #         },
    #         {
    #             "value": "合同归属",
    #             "label": "contract",
    #             "width": 150
    #         },
    #         {
    #             "value": "是否届满",
    #             "label": "isExpiration",
    #             "width": 120
    #         },
    #         {
    #             "value": "工号",
    #             "label": "workNumber",
    #             "width": 150
    #         },
    #         {
    #             "value": "姓名",
    #             "label": "name",
    #             "width": 90
    #         },
    #         {
    #             "value": "身份证号",
    #             "label": "idCard",
    #             "width": 360
    #         },
    #         {
    #             "value": "竞业开始日期",
    #             "label": "cycleBeginData",
    #             "width": 200
    #         },
    #         {
    #             "value": "竞业结束日期",
    #             "label": "cycleEndData",
    #             "width": 200
    #         },
    #         {
    #             "value": "备注",
    #             "label": "compete_remark",
    #             "width": ""
    #         },
    #         {
    #             "value": "联系电话",
    #             "label": "phone",
    #             "width": 100
    #         },
    #         {
    #             "value": "联系地址",
    #             "label": "address",
    #             "width": 200
    #         },
    #         {
    #             "value": "竞业周期",
    #             "label": "cycleData",
    #             "width": 100
    #         },
    #         {
    #             "value": "参保证明",
    #             "label": "insured_file",
    #             "width": 300
    #         },
    #         {
    #             "value": "所得税缴税证明",
    #             "label": "incomeTax_file",
    #             "width": 300
    #         },
    #         {
    #             "value": "公积金账户信息",
    #             "label": "accumulationFund_file",
    #             "width": 300
    #         },
    #         {
    #             "value": "工作照片",
    #             "label": "workPhotos_file",
    #             "width": 300
    #         },
    #         {
    #             "value": "工作视频",
    #             "label": "workVideo_file",
    #             "width": 300
    #         },
    #         {
    #             "value": "日常照片",
    #             "label": "dailyPhotos_file",
    #             "width": 300
    #         },
    #         {
    #             "value": "日常视频",
    #             "label": "dailyVideo_file",
    #             "width": 300
    #         },
    #         {
    #             "value": "在职证明",
    #             "label": "incumbency_file",
    #             "width": 300
    #         },
    #         {
    #             "value": "无工作承诺函",
    #             "label": "noWork_file",
    #             "width": 300
    #         },
    #         {
    #             "value": "强制拍照",
    #             "label": "photograph_file",
    #             "width": 300
    #         },
    #
    #         {
    #             "value": "电话回访",
    #             "label": "cllBack_file",
    #             "width": 300
    #         },            {
    #             "value": "实时视频(第一次)",
    #             "label": "firstlivevideo_file",
    #             "width": 300
    #         },            {
    #             "value": "实时视频(第二次)",
    #             "label": "secondlivevideo_file",
    #             "width": 300
    #         },
    #         {
    #             "value": "经度",
    #             "label": "lon",
    #             "width": 100
    #         },
    #         {
    #             "value": "纬度",
    #             "label": "lat",
    #             "width": 100
    #         },
    #         {
    #             "value": "位置",
    #             "label": "location",
    #             "width": 200
    #         }
    #     ]
    #     print(self.request.GET)
    #     currentPage = eval(self.request.GET.get("currentPage", None)) if self.request.GET.get("currentPage",
    #                                                                                           None) != "" else 1
    #     pageSize = eval(self.request.GET.get("pageSize", None)) if self.request.GET.get("pageSize", None) != "" else 25
    #     kwargs = {
    #         'compete_status': True
    #     }
    #     searchName = self.request.GET.get('searchName', '')
    #     baseNameId = self.request.GET.get('baseNameId', None)
    #     deptName = self.request.GET.get("contract", None)
    #     isExpiration = self.request.GET.get("isExpiration", None)
    #     dept_list = CompeteRestrictionsWhitelist.objects.filter(Q(contract__isnull=False) & ~Q(contract=''),
    #                                                             compete_status=True).values("contract").distinct()
    #     dept_list = [{"label": i['contract'], "value": i['contract']} for i in dept_list]
    #     if searchName == '' or searchName == None or len(str(searchName)) == 0 \
    #             and baseNameId == '' or baseNameId == None or len(str(baseNameId)) == 0 \
    #             and deptName == "" or deptName == None or len(str(deptName)) == 0 \
    #             and isExpiration == "" or isExpiration == None or len(str(isExpiration)) == 0:  # 全查
    #         kwargs['cr_base__in'] = self.request.user_base
    #
    #     if len(baseNameId) == 0 or baseNameId == None:
    #         kwargs['cr_base__in'] = self.request.user_base
    #     else:
    #         kwargs['cr_base'] = baseNameId
    #     if deptName is not None and deptName != '':
    #         kwargs['contract'] = deptName  # 合同归属
    #     if isExpiration != '':
    #         kwargs['isExpiration'] = isExpiration  # 是否届满
    #
    #     base_list=center_base.objects.filter(status=True).values('id','name')
    #     # print(base_list)
    #
    #     # if CompeteRestrictionsWhitelist.objects.filter(Q(name__contains=searchName) | Q(idCard__contains=searchName) | Q(workNumber__contains=searchName),flat=True).exists():
    #
    #     totalNumber = CompeteRestrictionsWhitelist.objects.filter(Q(name__contains=searchName) | Q(idCard__contains=searchName) | Q(workNumber__contains=searchName),**kwargs).count()
    #
    #     tableList = CompeteRestrictionsWhitelist.objects.filter(
    #         Q(name__contains=searchName) | Q(idCard__contains=searchName) | Q(workNumber__contains=searchName),
    #         **kwargs).values('id','cr_base','cr_base__name','cr_base__base_parent_id','contract','isExpiration','workNumber','name','idCard','cycleBeginData','cycleEndData','compete_remark','people').order_by('-create_time')[(currentPage - 1) * pageSize:currentPage * pageSize]
    #     all_whiteid = [item['id'] for item in tableList]
    #     # CompeteRestrictions.
    #     beginDate = self.request.GET.get('beginDate', '')
    #     endDate = self.request.GET.get('endDate', '')
    #     cr_kwargs={
    #         'compete_status':True
    #     }
    #     if beginDate != "" and endDate != "":
    #         cr_kwargs['cycleData__gte'] = datetime(1901, 10, 29, 7, 17, 1, 177) if beginDate is None or len(endDate) == 0 else beginDate
    #         cr_kwargs['cycleData__lte'] = datetime(3221, 10, 29, 7, 17, 1, 177) if endDate is None or len(endDate) == 0 else endDate  #飞行日期
    #     all_crobj=CompeteRestrictions.objects.filter(people_id__in=all_whiteid,**cr_kwargs).values('id','name','idCard','phone','address','cycleData','lon','lat','location','cllBack_file').order_by('-create_time')
    #     all_crobjid = [item['id'] for item in all_crobj]
    # #     crobj_file_obj_all = CompeteRestrictions.objects.filter(
    # # Q(workPhotos_file__file_status=True,workVideo_file__file_status=True) | Q(dailyPhotos_file__file_status=True,dailyVideo_file__file_status=True),photograph_file__file_status=True,id__in=all_crobjid,compete_status=True,
    # #                                                             ).values('id',
    # #                                                                                     'photograph_file__id',
    # #                                                                                     'photograph_file__name',
    # #                                                                                     'photograph_file__url',
    # #                                                                                     'insured_file__id',
    # #                                                                                     'insured_file__name',
    # #                                                                                     "insured_file__url",
    # #                                                                                     'incomeTax_file__id',
    # #                                                                                     'incomeTax_file__name',
    # #                                                                                     "incomeTax_file__url",
    # #                                                                                     'accumulationFund_file__id',
    # #                                                                                     'accumulationFund_file__name',
    # #                                                                                     "accumulationFund_file__url",
    # #                                                                                     'workPhotos_file__id',
    # #                                                                                     'workPhotos_file__name',
    # #                                                                                     "workPhotos_file__url",
    # #                                                                                     'workVideo_file__id',
    # #                                                                                     'workVideo_file__name',
    # #                                                                                     "workVideo_file__url",
    # #                                                                                     'dailyPhotos_file__id',
    # #                                                                                     'dailyPhotos_file__name',
    # #                                                                                     "dailyPhotos_file__url",
    # #                                                                                     'dailyVideo_file__id',
    # #                                                                                     'dailyVideo_file__name',
    # #                                                                                     "dailyVideo_file__url",
    # #                                                                                     'incumbency_file__id',
    # #                                                                                     'incumbency_file__name',
    # #                                                                                     "incumbency_file__url",
    # #                                                                                     'noWork_file__id',
    # #                                                                                     'noWork_file__name',
    # #                                                                                     "noWork_file__url",
    # #                                                                                     'cllBack_file__id',
    # #                                                                                     'cllBack_file__name',
    # #                                                                                     "cllBack_file__url",
    # #                                                                                     'firstlivevideo_file__id',
    # #                                                                                     'firstlivevideo_file__name',
    # #                                                                                     "firstlivevideo_file__url",
    # #                                                                                     'secondlivevideo_file__id',
    # #                                                                                     'secondlivevideo_file__name',
    # #                                                                                     "secondlivevideo_file__url")no
    #
    #
    #
    #
    #     print(all_crobjid)
    #     all_crobjid=[67]
    #     print(all_crobjid)
    #     # work_crobj_file_obj_all = CompeteRestrictions.objects.filter(
    #     #     workPhotos_file__file_status=True, workVideo_file__file_status=True,incumbency_file__file_status=True,
    #     #     dailyPhotos_file__file_status=False,dailyVideo_file__file_status=False,noWork_file__file_status=False,
    #     #      id__in=all_crobjid, compete_status=True,
    #     # ).values('id',
    #     #          # 'photograph_file__id',
    #     #          # 'photograph_file__name',
    #     #          # 'photograph_file__url',
    #     #          # 'insured_file__id',
    #     #          # 'insured_file__name',
    #     #          # "insured_file__url",
    #     #          # 'incomeTax_file__id',
    #     #          # 'incomeTax_file__name',
    #     #          # "incomeTax_file__url",
    #     #          # 'accumulationFund_file__id',
    #     #          # 'accumulationFund_file__name',
    #     #          # "accumulationFund_file__url",
    #     #          'workPhotos_file__id',
    #     #          'workPhotos_file__name',
    #     #          "workPhotos_file__url",
    #     #          # 'workVideo_file__id',
    #     #          # 'workVideo_file__name',
    #     #          # "workVideo_file__url",
    #     #          # 'incumbency_file__id',
    #     #          # 'incumbency_file__name',
    #     #          # "incumbency_file__url",
    #     #          # 'cllBack_file__id',
    #     #          # 'cllBack_file__name',
    #     #          # "cllBack_file__url",
    #     #          # 'firstlivevideo_file__id',
    #     #          # 'firstlivevideo_file__name',
    #     #          # "firstlivevideo_file__url",
    #     #          # 'secondlivevideo_file__id',
    #     #          # 'secondlivevideo_file__name',
    #     #          # "secondlivevideo_file__url"
    #     #          )
    #     # print("work_crobj_file_obj_all",work_crobj_file_obj_all)
    #
    #     nowork_crobj_file_obj_all = CompeteRestrictions.objects.filter(
    #         # workPhotos_file__file_status=False, workVideo_file__file_status=False,incumbency_file__file_status=False,
    #         dailyPhotos_file__file_status=True,dailyVideo_file__file_status=True,noWork_file__file_status=True,
    #          id__in=all_crobjid, compete_status=True,
    #     ).values('id',
    #              # 'photograph_file__id',
    #              # 'photograph_file__name',
    #              # 'photograph_file__url',
    #              # 'insured_file__id',
    #              # 'insured_file__name',
    #              # "insured_file__url",
    #              # 'incomeTax_file__id',
    #              # 'incomeTax_file__name',
    #              # "incomeTax_file__url",
    #              # 'accumulationFund_file__id',
    #              # 'accumulationFund_file__name',
    #              # "accumulationFund_file__url",
    #
    #              'dailyPhotos_file__id',
    #              'dailyPhotos_file__name',
    #              "dailyPhotos_file__url",
    #              # 'dailyVideo_file__id',
    #              # 'dailyVideo_file__name',
    #              # "dailyVideo_file__url",
    #              # 'incumbency_file__id',
    #              # 'incumbency_file__name',
    #              # "incumbency_file__url",
    #              # 'noWork_file__id',
    #              # 'noWork_file__name',
    #              # "noWork_file__url",
    #              #
    #              # 'cllBack_file__id',
    #              # 'cllBack_file__name',
    #              # "cllBack_file__url",
    #              # 'firstlivevideo_file__id',
    #              # 'firstlivevideo_file__name',
    #              # "firstlivevideo_file__url",
    #              # 'secondlivevideo_file__id',
    #              # 'secondlivevideo_file__name',
    #              # "secondlivevideo_file__url"
    #              )
    #     print("nowork_crobj_file_obj_all",nowork_crobj_file_obj_all)
    #
    #     # print(all_crobjid)
    #     # print(all_crobj)
    #     # print(crobj_file_obj_all)
    #
    #     for index, whiteobj in enumerate(tableList):
    #         whiteobj['index']=(currentPage - 1) * pageSize + index + 1
    #         whiteobj['cr_base_id']=whiteobj['cr_base']
    #         for base in list(base_list):
    #             if base['id']==whiteobj['cr_base__base_parent_id']:
    #                 whiteobj['base_father']=base['name']
    #         if whiteobj['cr_base__base_parent_id'] is None:
    #             whiteobj['base_father'] = whiteobj['cr_base__name']
    #         whiteobj['cr_base']=whiteobj['cr_base__name']
    #         for crobj in all_crobj:
    #             if whiteobj['people']==crobj['id']:
    #                 whiteobj.update(crobj)
    #
    #     # for index, whiteobj in enumerate(tableList):
    #     #     for crobj_file_obj in crobj_file_obj_all:
    #     #         if crobj_file_obj['id']==whiteobj['id']:
    #     #             # pass
    #     #             #
    #     #             whiteobj['photograph_file_files'] = [{'id': crobj_file_obj['photograph_file__id'],
    #     #                                                   'url': crobj_file_obj['photograph_file__url'],
    #     #                                                   'name': crobj_file_obj['photograph_file__name']}]
    #     #             whiteobj['insured_file_files'] = [{'id': crobj_file_obj['insured_file__id'],
    #     #                                                    'url': crobj_file_obj['insured_file__url'],
    #     #                                                    'name': crobj_file_obj['insured_file__name']}]
    #     #             whiteobj['incomeTax_file_files'] = [{'id': crobj_file_obj['incomeTax_file__id'],
    #     #                                                   'url': crobj_file_obj['incomeTax_file__url'],
    #     #                                                   'name': crobj_file_obj['incomeTax_file__name']}]
    #     #             whiteobj['accumulationFund_file_files'] = [{'id': crobj_file_obj['accumulationFund_file__id'],
    #     #                                                    'url': crobj_file_obj['accumulationFund_file__url'],
    #     #                                                    'name': crobj_file_obj['accumulationFund_file__name']}]
    #     #             whiteobj['workPhotos_file_files'] = [{'id': crobj_file_obj['workPhotos_file__id'],
    #     #                                                   'url': crobj_file_obj['workPhotos_file__url'],
    #     #                                                   'name': crobj_file_obj['workPhotos_file__name']}]
    #     #             whiteobj['workVideo_file_files'] = [{'id': crobj_file_obj['workVideo_file__id'],
    #     #                                                    'url': crobj_file_obj['workVideo_file__url'],
    #     #                                                    'name': crobj_file_obj['workVideo_file__name']}]
    #     #             whiteobj['dailyPhotos_file_files'] = [{'id': crobj_file_obj['dailyPhotos_file__id'],
    #     #                                                   'url': crobj_file_obj['dailyPhotos_file__url'],
    #     #                                                   'name': crobj_file_obj['dailyPhotos_file__name']}]
    #     #             whiteobj['dailyVideo_file_files'] = [{'id': crobj_file_obj['dailyVideo_file__id'],
    #     #                                                    'url': crobj_file_obj['dailyVideo_file__url'],
    #     #                                                    'name': crobj_file_obj['dailyVideo_file__name']}]
    #     #             whiteobj['incumbency_file_files'] = [{'id': crobj_file_obj['incumbency_file__id'],
    #     #                                                   'url': crobj_file_obj['incumbency_file__url'],
    #     #                                                   'name': crobj_file_obj['incumbency_file__name']}]
    #     #             whiteobj['noWork_file_files'] = [{'id': crobj_file_obj['noWork_file__id'],
    #     #                                                    'url': crobj_file_obj['noWork_file__url'],
    #     #                                                    'name': crobj_file_obj['noWork_file__name']}]
    #     #             whiteobj['cllBack_file_files'] = [{'id': crobj_file_obj['cllBack_file__id'],
    #     #                                                    'url': crobj_file_obj['cllBack_file__url'],
    #     #                                                    'name': crobj_file_obj['cllBack_file__name']}]
    #     #             whiteobj['firstlivevideo_file_files'] = [{'id': crobj_file_obj['firstlivevideo_file__id'],
    #     #                                                   'url': crobj_file_obj['firstlivevideo_file__url'],
    #     #                                                   'name': crobj_file_obj['firstlivevideo_file__name']}]
    #     #             whiteobj['secondlivevideo_file_files'] = [{'id': crobj_file_obj['secondlivevideo_file__id'],
    #     #                                                    'url': crobj_file_obj['secondlivevideo_file__url'],
    #     #                                                    'name': crobj_file_obj['secondlivevideo_file__name']}]
    #     #
    #     #             whiteobj['photograph_file']=crobj_file_obj['photograph_file__name']
    #     #             whiteobj['insured_file']=crobj_file_obj['insured_file__name']
    #     #             whiteobj['incomeTax_file']=crobj_file_obj['incomeTax_file__name']
    #     #             whiteobj['accumulationFund_file']=crobj_file_obj['accumulationFund_file__name']
    #     #             whiteobj['workPhotos_file']=crobj_file_obj['workPhotos_file__name']
    #     #             whiteobj['workVideo_file']=crobj_file_obj['workVideo_file__name']
    #     #             whiteobj['dailyPhotos_file']=crobj_file_obj['dailyPhotos_file__name']
    #     #             whiteobj['dailyVideo_file']=crobj_file_obj['dailyVideo_file__name']
    #     #             whiteobj['incumbency_file']=crobj_file_obj['incumbency_file__name']
    #     #             whiteobj['noWork_file']=crobj_file_obj['noWork_file__name']
    #     #             whiteobj['cllBack_file']=crobj_file_obj['cllBack_file__name']
    #     #             whiteobj['firstlivevideo_file']=crobj_file_obj['firstlivevideo_file__name']
    #     #             whiteobj['secondlivevideo_file']=crobj_file_obj['secondlivevideo_file__name']
    #     ret_data=[]
    #
    #
    #
    #
    #     if beginDate != "" and endDate != "":
    #         for index, line in enumerate(tableList):
    #                 if 'cycleData' in line.keys():
    #                     ret_data.append(line)
    #         totalNumber=len(ret_data)
    #     else:
    #         ret_data=tableList
    #     # for line in ret_data:
    #     #     line = {key: value for key, value in line.items() if value is not None}
    #     # for line in ret_data:
    #     #     print(line)
    #
    #
    #
    #     self.return_data = {
    #         "code": status.HTTP_200_OK,
    #         "msg": "信息返回成功",
    #         "data": {
    #             'columnList': columnList,
    #             'tableList': ret_data,
    #             'totalNumber': totalNumber,
    #         }
    #     }
    #     # print(self.return_data)




        # obj = Controller(CompeteRestrictions, "get_list", self.request)
        # self.return_data = obj.data_start()

        obj = Controller(CompeteRestrictionsWhitelist, "get_list", self.request)
        self.return_data = obj.data_start()

    def get_systemUpload(self):
        if self.request.check_token!=None:
            info = eval(self.request.POST.get('createData', None))
            # cllBack_file = self.request.FILES.get("cllBack_file", None)  # 电话回访
            # firstlivevideo_file = self.request.FILES.get("firstlivevideo_file", None)  # 实时视频(第一次)
            # secondlivevideo_file=self.request.FILES.get("secondlivevideo_file", None)  # 实时视频(第二次)
            # print(cllBack_file,firstlivevideo_file,secondlivevideo_file)
            # print(info)
            if self.is_valid_id_card(info['idCard']):
                # info['cr_base_id']=info['cr_base_id']
                try:
                    info['cr_base_id'] = info['cr_base_id'][1] if len(info['cr_base_id']) == 2 else info['cr_base_id'][
                        0]
                except:
                    info['cr_base_id'] = info['cr_base_id']

                info['creator_id']=self.request.check_token

                info['idCard'] = info['idCard'].strip()
                info['compete_status']=1
                # print(info)
                obj=CompeteRestrictionsWhitelist.objects.update_or_create(defaults=info, idCard=info['idCard'],compete_status=info['compete_status'])
                # print(obj)
                self.return_data = {
                    "code": HTTP_200_OK,
                    "msg": "新增成功"
                }
            else:
                self.return_data = {
                    "code": status.HTTP_400_BAD_REQUEST,
                    "msg": "请填写正确的身份证！"
                }
        else:
            self.return_data = {
                "code": HTTP_403_FORBIDDEN,
                "msg": "没有权限访问"
            }
        # print(self.return_data)

    def get_upload(self):
        import arrow
        utc1 = arrow.utcnow()

        # print(self.request.POST)
        # print(self.request.FILES)
        # info=eval(self.request.POST.get('createData',None))
        # print(info)
        info =self.request.POST.dict()
        # print(info)
        # info={'lat': '', 'lon': '', 'location': '', 'idCard': '320924198611062130', 'phone': '1231231321', 'address': 'ASDASDSA', 'cycleData': '2023-08', 'name': '李以权', 'insured_file': '', 'incomeTax_file': '', 'accumulationFund_file': '', 'cllBack_file': '', 'incumbency_file': '', 'workVideo_file': '', 'firstlivevideo_file': '', 'secondlivevideo_file': '', 'workPhotos_file': '', 'noWork_file': '', 'dailyPhotos_file': '', 'dailyVideo_file': ''}

        info['idCard']= info['idCard']
        # print(len(info['idCard']))
        if self.is_valid_id_card(info['idCard']):
            whiteList_obj = CompeteRestrictionsWhitelist.objects.filter(idCard=info['idCard'], compete_status=True)

            if whiteList_obj:
                beginData,endData,name,id=whiteList_obj.values_list('cycleBeginData','cycleEndData','name','id').first()
                if name==info['name']:
                    # try:
                        if self.is_year_month_in_range(info['cycleData'],beginData,endData):
                            if type(info['cycleData'])==str:
                                cycleData=self.get_first_last(datetime.strptime(info['cycleData'],'%Y-%m'))[4]
                            else:
                                cycleData=self.get_first_last(info['cycleData'])[4] #该月第一天

                            info['cycleData']=cycleData
                            # print(cycleData)
                            try:
                                del info['insured_file']
                            except:
                                pass
                            try:
                                del info['incomeTax_file']
                            except:
                                pass
                            try:
                                del info['accumulationFund_file']
                            except:
                                pass
                            try:
                                del info['noWork_file']
                            except:
                                pass
                            try:
                                del info['dailyVideo_file']
                            except:
                                pass
                            try:
                                del info['dailyPhotos_file']
                            except:
                                pass
                            try:
                                del info['incumbency_file']
                            except:
                                pass
                            try:
                                del info['workPhotos_file']
                            except:
                                pass
                            try:
                                del info['workVideo_file']
                            except:
                                pass
                            try:
                                del info['cllBack_file']
                            except:
                                pass
                            try:
                                del info['secondlivevideo_file']
                            except:
                                pass
                            try:
                                del info['firstlivevideo_file']
                            except:
                                pass
                            # print("info",info)
                            info['people_id']=id
                            info['idCard']=info['idCard'].strip()
                            # print(info['idCard'])
                            # print(info)
                            obj=CompeteRestrictions.objects.update_or_create(defaults=info,cycleData=cycleData,idCard=info['idCard'])
                            utc2 = arrow.utcnow()


                            infoId=obj[0].id

                            # print(self.request.FILES)
                            insured_file=self.request.FILES.get("insured_file", None)#参保证明
                            incomeTax_file = self.request.FILES.get("incomeTax_file", None)  # 所得税缴税证明
                            accumulationFund_file = self.request.FILES.get("accumulationFund_file", None)  # 公积金账户信息
                            workPhotos_file = self.request.FILES.get("workPhotos_file", None)  # 工作照片
                            workVideo_file = self.request.FILES.get("workVideo_file", None)  # 工作视频
                            dailyPhotos_file = self.request.FILES.get("dailyPhotos_file", None)  # 日常照片
                            dailyVideo_file = self.request.FILES.get("dailyVideo_file", None)  # 日常视频
                            incumbency_file = self.request.FILES.get("incumbency_file", None)  # 在职证明
                            noWork_file = self.request.FILES.get("noWork_file", None)  # 无工作承诺函
                            photograph_file=self.request.FILES.get("photograph_file", None)  # 强制拍照

                            # cllBack_file = self.request.FILES.get("cllBack_file", None)  # 电话回访
                            # firstlivevideo_file = self.request.FILES.get("firstlivevideo_file", None)  # 实时视频(第一次)
                            # secondlivevideo_file=self.request.FILES.get("secondlivevideo_file", None)  # 实时视频(第二次)

                            utc3 = arrow.utcnow()
                            # print(incomeTax_file,accumulationFund_file,workVideo_file)

                            t = time.strftime('%Y-%m-%d')
                            dummy_path = os.path.join(BASE_DIR, 'static', 'competeRestrictionsFile', 'upload_file', t,str(info['name']) +'_'+ str(info['idCard']))  # 创建文件夹
                            self.mkdir(dummy_path)
                            try:

                                if insured_file!=None:
                                    # print('insured_file')
                                    insured_url, insured_name, insured_suffix = self.createPath(insured_file, str(info['name']) + '_' + str(
                                                    info['idCard']), str(info['name']) +str(info['cycleData'])+'_参保证明')
                                    self.saveFile(insured_url, insured_file)  # 保存文件
                                    utc4 = arrow.utcnow()
                                    insured_kwargs = {
                                        "url": insured_url,
                                        "name": insured_name,
                                    }
                                    # insuredFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=insured_kwargs, id=infoId)[0]
                                    # insuredFile_obj.insured_file.add(infoId)
                                    insuredFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('insured_file__id',flat=True))[-1]  #参保证明
                                    if insuredFile_id==None:
                                        insuredFile_obj=CompeteRestrictionsFile.objects.create(**insured_kwargs)
                                        insuredFile_obj.insured_file.add(infoId)
                                    else:
                                        insuredFile_obj = CompeteRestrictionsFile.objects.filter(id=insuredFile_id).update(**insured_kwargs)
                                    self.return_data = {
                                        "code": status.HTTP_200_OK,
                                        "msg": "参保证明上传成功！"
                                    }
                                    utc5 = arrow.utcnow()
                                    # print(utc2 - utc1, utc3 - utc2, utc4 - utc3, utc5 - utc4,utc5-utc1)
                                if photograph_file!=None:
                                    # print('photograph_file')
                                    photograph_url, photograph_name, photograph_suffix = self.createPath(photograph_file,
                                                                                                         str(info[
                                                                                                                 'name']) + '_' + str(
                                                                                                             info[
                                                                                                                 'idCard']),
                                                                                                         str(info[
                                                                                                                 'name']) + str(
                                                                                                             info[
                                                                                                                 'cycleData']) + '_照片')
                                    self.saveFile(photograph_url, photograph_file)
                                    photograph_kwargs = {
                                        "url": photograph_url,
                                        "name": photograph_name,
                                    }

                                    photographFile_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list('photograph_file__id',
                                                                                                  flat=True))[-1]
                                    if photographFile_id == None:
                                        photographFile_obj = CompeteRestrictionsFile.objects.create(**photograph_kwargs)
                                        photographFile_obj.photograph_file.add(infoId)
                                    else:
                                        photographFile_obj = CompeteRestrictionsFile.objects.filter(
                                            id=photographFile_id).update(**photograph_kwargs)

                                    self.return_data = {
                                        "code": status.HTTP_200_OK,
                                        "msg": "拍照信息上传成功！"
                                    }
                                if incumbency_file!=None:
                                    incumbency_url,incumbency_name,incumbency_suffix=self.createPath(incumbency_file, str(info['name']) + '_' + str(info['idCard']), str(info['name'])+str(info['cycleData'])+'_在职证明')
                                    self.saveFile(incumbency_url, incumbency_file)
                                    incumbency_kwargs={
                                        "url": incumbency_url,
                                        "name":incumbency_name,
                                        "file_status": 1,
                                    }
                                    # incumbencyFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=incumbency_kwargs, id=infoId)[0]
                                    # incumbencyFile_obj.incumbency_file.add(infoId)
                                    incumbencyFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('incumbency_file__id',flat=True))[-1]   #在职证明
                                    noWorkFile_id = list(CompeteRestrictions.objects.filter(id=infoId).values_list('noWork_file__id', flat=True))[-1]#无工作承诺函
                                    if incumbencyFile_id==None:
                                        incumbencyFile_obj=CompeteRestrictionsFile.objects.create(**incumbency_kwargs)
                                        incumbencyFile_obj.incumbency_file.add(infoId)
                                    else:
                                        incumbencyFile_obj = CompeteRestrictionsFile.objects.filter(id=incumbencyFile_id).update(**incumbency_kwargs)
                                    if noWorkFile_id==None:
                                        pass
                                    else:
                                        noWorkFile_obj = CompeteRestrictionsFile.objects.filter(id=noWorkFile_id).update(file_status=False)
                                    self.return_data = {
                                        "code": status.HTTP_200_OK,
                                        "msg": "在职证明上传成功！"
                                    }
                                if workVideo_file!=None:
                                    # print('workVideo_file')
                                    workVideo_url, workVideo_name, workVideo_suffix = self.createPath(workVideo_file, str(
                                        info['name']) + '_' + str(info['idCard']), str(info['name']) + str(
                                        info['cycleData']) + '_工作视频')
                                    self.saveFile(workVideo_url, workVideo_file)
                                    workVideo_kwargs = {
                                        "url": workVideo_url,
                                        "name": workVideo_name,
                                        "file_status": 1,
                                    }
                                    workVideoFile_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list('workVideo_file__id',
                                                                                                  flat=True))[-1]  # 工作视频
                                    dailyVideoFile_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list('dailyVideo_file__id',
                                                                                                  flat=True))[-1]  # 日常视频
                                    if workVideoFile_id == None:
                                        workVideoFile_obj = CompeteRestrictionsFile.objects.create(**workVideo_kwargs)
                                        workVideoFile_obj.workVideo_file.add(infoId)
                                    else:
                                        workVideoFile_obj = CompeteRestrictionsFile.objects.filter(
                                            id=workVideoFile_id).update(**workVideo_kwargs)
                                    if dailyVideoFile_id == None:
                                        pass
                                    else:
                                        dailyVideoFile_obj = CompeteRestrictionsFile.objects.filter(
                                            id=dailyVideoFile_id).update(file_status=False)
                                    self.return_data = {
                                        "code": status.HTTP_200_OK,
                                        "msg": "工作视频上传成功！"
                                    }
                                if workPhotos_file!=None:
                                    workPhotos_url, workPhotos_name, workPhotos_suffix = self.createPath(workPhotos_file,
                                                                                                         str(info[
                                                                                                                 'name']) + '_' + str(
                                                                                                             info[
                                                                                                                 'idCard']),
                                                                                                         str(info[
                                                                                                                 'name']) + str(
                                                                                                             info[
                                                                                                                 'cycleData']) + '_工作照片')
                                    self.saveFile(workPhotos_url, workPhotos_file)
                                    workPhotos_kwargs = {
                                        "url": workPhotos_url,
                                        "name": workPhotos_name,
                                        "file_status": 1,
                                    }
                                    # if flag==0:#更新
                                    #     workPhotosFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('workPhotos_file__id',flat=True))[-1]
                                    #     workPhotosFile_obj=CompeteRestrictionsFile.objects.filter(id=workPhotosFile_id).update(**workPhotos_kwargs)
                                    # else:  #创建
                                    #     workPhotosFile_obj=CompeteRestrictionsFile.objects.create(**workPhotos_kwargs)
                                    #     workPhotosFile_obj.workPhotos_file.add(infoId)
                                    workPhotosFile_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list('workPhotos_file__id',
                                                                                                  flat=True))[-1]  # 工作照片
                                    dailyPhotosFile_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list('dailyPhotos_file__id',
                                                                                                  flat=True))[-1]  # 日常照片
                                    # print(workPhotosFile_id,dailyPhotosFile_id)
                                    if workPhotosFile_id == None:
                                        workPhotosFile_obj = CompeteRestrictionsFile.objects.create(**workPhotos_kwargs)
                                        workPhotosFile_obj.workPhotos_file.add(infoId)
                                    else:
                                        workPhotosFile_obj = CompeteRestrictionsFile.objects.filter(
                                            id=workPhotosFile_id).update(**workPhotos_kwargs)

                                    if dailyPhotosFile_id == None:
                                        pass
                                    else:
                                        dailyPhotosFile_obj = CompeteRestrictionsFile.objects.filter(
                                            id=dailyPhotosFile_id).update(file_status=False)
                                    self.return_data = {
                                        "code": status.HTTP_200_OK,
                                        "msg": "工作照片上传成功！"
                                    }
                                if incomeTax_file!=None:
                                    incomeTax_url, incomeTax_name, incomeTax_suffix = self.createPath(incomeTax_file, str(
                                        info['name']) + '_' + str(info['idCard']), str(info['name']) + str(
                                        info['cycleData']) + '_所得税缴税证明')
                                    self.saveFile(incomeTax_url, incomeTax_file)
                                    incomeTax_kwargs = {
                                        "url": incomeTax_url,
                                        "name": incomeTax_name,
                                    }
                                    # incomeTaxFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=incomeTax_kwargs, id=infoId)[0]
                                    # incomeTaxFile_obj.incomeTax_file.add(infoId)
                                    incomeTaxFile_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list('incomeTax_file__id',
                                                                                                  flat=True))[-1]  # 所得税缴税证明
                                    if incomeTaxFile_id == None:
                                        incomeTaxFile_obj = CompeteRestrictionsFile.objects.create(**incomeTax_kwargs)
                                        incomeTaxFile_obj.incomeTax_file.add(infoId)
                                    else:
                                        incomeTaxFile_obj = CompeteRestrictionsFile.objects.filter(
                                            id=incomeTaxFile_id).update(**incomeTax_kwargs)
                                    self.return_data = {
                                        "code": status.HTTP_200_OK,
                                        "msg": "所得税缴税证明上传成功！"
                                    }
                                if accumulationFund_file!=None:
                                    accumulationFund_url, accumulationFund_name, accumulationFund_suffix = self.createPath(
                                        accumulationFund_file, str(info['name']) + '_' + str(info['idCard']),
                                        str(info['name']) + str(info['cycleData']) + '_公积金账户信息')
                                    self.saveFile(accumulationFund_url, accumulationFund_file)
                                    accumulationFund_kwargs = {
                                        "url": accumulationFund_url,
                                        "name": accumulationFund_name,
                                    }
                                    # accumulationFundFile_obj =CompeteRestrictionsFile.objects.update_or_create(defaults=accumulationFund_kwargs, id=infoId)[0]
                                    # accumulationFundFile_obj.accumulationFund_file.add(infoId)
                                    accumulationFundFile_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list(
                                            'accumulationFund_file__id', flat=True))[-1]  # 公积金账户信息
                                    if accumulationFundFile_id == None:
                                        accumulationFundFile_obj = CompeteRestrictionsFile.objects.create(
                                            **accumulationFund_kwargs)
                                        accumulationFundFile_obj.accumulationFund_file.add(infoId)
                                    else:
                                        accumulationFundFile_obj = CompeteRestrictionsFile.objects.filter(
                                            id=accumulationFundFile_id).update(**accumulationFund_kwargs)
                                    self.return_data = {
                                        "code": status.HTTP_200_OK,
                                        "msg": "公积金账户信息上传成功！"
                                    }
                                if dailyVideo_file!=None:
                                    dailyVideo_url, dailyVideo_name, dailyVideo_suffix = self.createPath(dailyVideo_file,
                                                                                                         str(info[
                                                                                                                 'name']) + '_' + str(
                                                                                                             info[
                                                                                                                 'idCard']),
                                                                                                         str(info[
                                                                                                                 'name']) + str(
                                                                                                             info[
                                                                                                                 'cycleData']) + '_日常视频')
                                    self.saveFile(dailyVideo_url, dailyVideo_file)
                                    dailyVideo_kwargs = {
                                        "url": dailyVideo_url,
                                        "name": dailyVideo_name,
                                        "file_status": 1,
                                    }
                                    # dailyVideoFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=dailyVideo_kwargs, id=infoId)[0]
                                    # dailyVideoFile_obj.dailyVideo_file.add(infoId)
                                    dailyVideoFile_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list('dailyVideo_file__id',
                                                                                                  flat=True))[-1]  # 日常视频
                                    workVideosFile_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list('workVideo_file__id',
                                                                                                  flat=True))[-1]  # 工作视频
                                    if dailyVideoFile_id == None:
                                        dailyVideoFile_obj = CompeteRestrictionsFile.objects.create(**dailyVideo_kwargs)
                                        dailyVideoFile_obj.dailyVideo_file.add(infoId)
                                    else:
                                        dailyVideoFile_obj = CompeteRestrictionsFile.objects.filter(
                                            id=dailyVideoFile_id).update(**dailyVideo_kwargs)
                                    if workVideosFile_id == None:
                                        pass
                                    else:  # 存在工作照片   删掉
                                        workVideoFile_obj = CompeteRestrictionsFile.objects.filter(
                                            id=workVideosFile_id).update(file_status=False)
                                    self.return_data = {
                                        "code": status.HTTP_200_OK,
                                        "msg": "日常视频上传成功！"
                                    }
                                if dailyPhotos_file!=None:
                                    dailyPhotos_url, dailyPhotos_name, dailyPhotos_suffix = self.createPath(
                                        dailyPhotos_file, str(info['name']) + '_' + str(info['idCard']),
                                        str(info['name']) + str(info['cycleData']) + '_日常照片')
                                    self.saveFile(dailyPhotos_url, dailyPhotos_file)
                                    dailyPhotos_kwargs = {
                                        "url": dailyPhotos_url,
                                        "name": dailyPhotos_name,
                                        "file_status": 1,
                                    }
                                    # dailyPhotosFile_obj =CompeteRestrictionsFile.objects.update_or_create(defaults=dailyPhotos_kwargs, id=infoId)[0]
                                    # dailyPhotosFile_obj.dailyPhotos_file.add(infoId)
                                    dailyPhotosFile_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list('dailyPhotos_file__id',
                                                                                                  flat=True))[-1]  # 日常照片
                                    # print(dailyPhotosFile_id)
                                    workPhotosFile_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list('workPhotos_file__id',
                                                                                                  flat=True))[-1]  # 工作照片
                                    # print(workPhotosFile_id)
                                    if dailyPhotosFile_id == None:
                                        dailyPhotosFile_obj = CompeteRestrictionsFile.objects.create(**dailyPhotos_kwargs)
                                        # print('11',dailyPhotosFile_obj)
                                        dailyPhotosFile_obj.dailyPhotos_file.add(infoId)
                                    else:
                                        dailyPhotosFile_obj = CompeteRestrictionsFile.objects.filter(
                                            id=dailyPhotosFile_id).update(**dailyPhotos_kwargs)
                                        # print('22', dailyPhotosFile_obj)
                                    if workPhotosFile_id == None:
                                        pass
                                    else:  # 存在工作照片   删掉
                                        workPhotosFile_obj = CompeteRestrictionsFile.objects.filter(
                                            id=workPhotosFile_id).update(file_status=False)
                                    self.return_data = {
                                        "code": status.HTTP_200_OK,
                                        "msg": "日常照片上传成功！"
                                    }
                                if noWork_file!=None:
                                    noWork_url, noWork_name, noWork_suffix = self.createPath(noWork_file,
                                                                                             str(info['name']) + '_' + str(
                                                                                                 info['idCard']),
                                                                                             str(info['name']) + str(info[
                                                                                                                         'cycleData']) + '_无工作承诺函')
                                    self.saveFile(noWork_url, noWork_file)
                                    noWork_kwargs = {
                                        "url": noWork_url,
                                        "name": noWork_name,
                                        "file_status": 1,
                                    }
                                    # noWorkFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=noWork_kwargs, id=infoId)[0]
                                    # noWorkFile_obj.noWork_file.add(infoId)
                                    noWorkFile_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list('noWork_file__id',
                                                                                                  flat=True))[-1]
                                    incumbency_file_id = list(
                                        CompeteRestrictions.objects.filter(id=infoId).values_list('incumbency_file__id',
                                                                                                  flat=True))[-1]  # 在职证明
                                    if noWorkFile_id == None:
                                        noWorkFile_obj = CompeteRestrictionsFile.objects.create(**noWork_kwargs)
                                        noWorkFile_obj.noWork_file.add(infoId)
                                    else:
                                        noWorkFile_obj = CompeteRestrictionsFile.objects.filter(id=noWorkFile_id).update(
                                            **noWork_kwargs)
                                    if incumbency_file_id == None:
                                        pass
                                    else:  # 存在工作照片   删掉
                                        incumbencyFile_obj = CompeteRestrictionsFile.objects.filter(
                                            id=incumbency_file_id).update(file_status=False)
                                    self.return_data = {
                                        "code": status.HTTP_200_OK,
                                        "msg": "无工作承诺函上传成功！"
                                    }

                                # if cllBack_file!=None:
                                #     # print('cllBack_file')
                                #     cllBack_url, cllBack_name, cllBack_suffix = self.createPath(
                                #         cllBack_file,
                                #         str(info['name']) + '_' + str(info['idCard']),
                                #         str(info['name']) + str(info['cycleData']) + '_电话回访录音')
                                #     self.saveFile(cllBack_url, cllBack_file)
                                #     cellBack_kwargs = {
                                #         "url": cllBack_url,
                                #         "name": cllBack_name,
                                #     }
                                #     cllBackFile_id = list(
                                #         CompeteRestrictions.objects.filter(id=infoId).values_list('cllBack_file__id',flat=True))[-1]
                                #     if cllBackFile_id == None:
                                #         cllBackFile_obj = CompeteRestrictionsFile.objects.create(**cellBack_kwargs)
                                #         cllBackFile_obj.cllBack_file.add(infoId)
                                #     else:
                                #         cllBackFile_obj = CompeteRestrictionsFile.objects.filter(
                                #             id=cllBackFile_id).update(**cellBack_kwargs)
                                #     self.return_data = {
                                #         "code": status.HTTP_200_OK,
                                #         "msg": "电话回访录音上传成功！"
                                #     }
                                # if firstlivevideo_file!=None:
                                #     # print('firstlivevideo_file')
                                #     firstlivevideo_url,firstlivevideo_name,firstlivevideo_suffix = self.createPath(
                                #         firstlivevideo_file,
                                #         str(info['name']) + '_' + str(info['idCard']),
                                #         str(info['name']) + str(info['cycleData']) + '_实时视频(第一次)')
                                #     self.saveFile(firstlivevideo_url,firstlivevideo_file)
                                #     firstlivevideoFile_kwargs = {
                                #         "url": firstlivevideo_url,
                                #         "name": firstlivevideo_name,
                                #     }
                                #     firstlivevideoFile_id = list(
                                #         CompeteRestrictions.objects.filter(id=infoId).values_list('firstlivevideo_file__id',flat=True))[-1]
                                #     if firstlivevideoFile_id == None:
                                #         firstlivevideoFile_obj = CompeteRestrictionsFile.objects.create(**firstlivevideoFile_kwargs)
                                #         firstlivevideoFile_obj.firstlivevideo_file.add(infoId)
                                #     else:
                                #         firstlivevideoFile_obj = CompeteRestrictionsFile.objects.filter(
                                #             id=firstlivevideoFile_id).update(**firstlivevideoFile_kwargs)
                                #     self.return_data = {
                                #         "code": status.HTTP_200_OK,
                                #         "msg": "实时视频(第一次)上传成功！"
                                #     }
                                # if secondlivevideo_file!=None:
                                #     # print('secondlivevideo_file')
                                #     secondlivevideo_url,secondlivevideo_name,secondlivevideo_suffix = self.createPath(
                                #         secondlivevideo_file,
                                #         str(info['name']) + '_' + str(info['idCard']),
                                #         str(info['name']) + str(info['cycleData']) + '_实时视频(第二次)')
                                #     self.saveFile(secondlivevideo_url,secondlivevideo_file)
                                #     secondlivevideoFile_kwargs = {
                                #         "url": secondlivevideo_url,
                                #         "name": secondlivevideo_name,
                                #     }
                                #     secondlivevideoFile_id = list(
                                #         CompeteRestrictions.objects.filter(id=infoId).values_list('secondlivevideo_file__id',flat=True))[-1]
                                #     if secondlivevideoFile_id == None:
                                #         secondlivevideoFile_obj = CompeteRestrictionsFile.objects.create(**secondlivevideoFile_kwargs)
                                #         secondlivevideoFile_obj.secondlivevideo_file.add(infoId)
                                #     else:
                                #         secondlivevideoFile_obj = CompeteRestrictionsFile.objects.filter(
                                #             id=secondlivevideoFile_id).update(**secondlivevideoFile_kwargs)
                                #     self.return_data = {
                                #         "code": status.HTTP_200_OK,
                                #         "msg": "实时视频(第二次)上传成功！"
                                #     }

                                self.return_data = {
                                    "code": status.HTTP_200_OK,
                                    "msg": "上传成功！"
                                }

                            except:
                                self.return_data = {
                                    "code": status.HTTP_401_UNAUTHORIZED,
                                    "msg": "上传失败！"
                                }

                            # try:
                            #     if photograph_file!=None:
                            #         if incumbency_file!=None and noWork_file==None:  #  在职证明 工作照片 工作视频
                            #             workPhotos_url, workPhotos_name, workPhotos_suffix = self.createPath(workPhotos_file,str(info['name']) + '_' + str(info['idCard']),str(info['name'])+str(info['cycleData'])+'_工作照片')
                            #             self.saveFile(workPhotos_url, workPhotos_file)
                            #             workPhotos_kwargs = {
                            #                 "url": workPhotos_url,
                            #                 "name": workPhotos_name,
                            #                 "file_status":1,
                            #             }
                            #             # if flag==0:#更新
                            #             #     workPhotosFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('workPhotos_file__id',flat=True))[-1]
                            #             #     workPhotosFile_obj=CompeteRestrictionsFile.objects.filter(id=workPhotosFile_id).update(**workPhotos_kwargs)
                            #             # else:  #创建
                            #             #     workPhotosFile_obj=CompeteRestrictionsFile.objects.create(**workPhotos_kwargs)
                            #             #     workPhotosFile_obj.workPhotos_file.add(infoId)
                            #             workPhotosFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('workPhotos_file__id',flat=True))[-1]   #工作照片
                            #             dailyPhotosFile_id = list(CompeteRestrictions.objects.filter(id=infoId).values_list('dailyPhotos_file__id', flat=True))[-1]  # 日常照片
                            #             # print(workPhotosFile_id,dailyPhotosFile_id)
                            #             if workPhotosFile_id==None:
                            #                 workPhotosFile_obj=CompeteRestrictionsFile.objects.create(**workPhotos_kwargs)
                            #                 workPhotosFile_obj.workPhotos_file.add(infoId)
                            #             else:
                            #                 workPhotosFile_obj = CompeteRestrictionsFile.objects.filter(id=workPhotosFile_id).update(**workPhotos_kwargs)
                            #
                            #             if dailyPhotosFile_id==None:
                            #                 pass
                            #             else:
                            #                 dailyPhotosFile_obj= CompeteRestrictionsFile.objects.filter(id=dailyPhotosFile_id).update(file_status=False)
                            #
                            #
                            #
                            #             workVideo_url, workVideo_name, workVideo_suffix = self.createPath(workVideo_file,str(info['name']) + '_' + str(info['idCard']),str(info['name'])+str(info['cycleData'])+ '_工作视频')
                            #             self.saveFile(workVideo_url, workVideo_file)
                            #             workVideo_kwargs = {
                            #                 "url": workVideo_url,
                            #                 "name": workVideo_name,
                            #                 "file_status": 1,
                            #             }
                            #             workVideoFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('workVideo_file__id',flat=True))[-1]  #工作视频
                            #             dailyVideoFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('dailyVideo_file__id',flat=True))[-1]  #日常视频
                            #             if workVideoFile_id==None:
                            #                 workVideoFile_obj=CompeteRestrictionsFile.objects.create(**workVideo_kwargs)
                            #                 workVideoFile_obj.workVideo_file.add(infoId)
                            #             else:
                            #                 workVideoFile_obj = CompeteRestrictionsFile.objects.filter(id=workVideoFile_id).update(**workVideo_kwargs)
                            #             if dailyVideoFile_id==None:
                            #                 pass
                            #             else:
                            #                 dailyVideoFile_obj = CompeteRestrictionsFile.objects.filter(id=dailyVideoFile_id).update(file_status=False)
                            #
                            #
                            #
                            #
                            #             incumbency_url,incumbency_name,incumbency_suffix=self.createPath(incumbency_file, str(info['name']) + '_' + str(info['idCard']), str(info['name'])+str(info['cycleData'])+'_在职证明')
                            #             self.saveFile(incumbency_url, incumbency_file)
                            #             incumbency_kwargs={
                            #                 "url": incumbency_url,
                            #                 "name":incumbency_name,
                            #                 "file_status": 1,
                            #             }
                            #             # incumbencyFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=incumbency_kwargs, id=infoId)[0]
                            #             # incumbencyFile_obj.incumbency_file.add(infoId)
                            #             incumbencyFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('incumbency_file__id',flat=True))[-1]   #在职证明
                            #             noWorkFile_id = list(CompeteRestrictions.objects.filter(id=infoId).values_list('noWork_file__id', flat=True))[-1]#无工作承诺函
                            #             if incumbencyFile_id==None:
                            #                 incumbencyFile_obj=CompeteRestrictionsFile.objects.create(**incumbency_kwargs)
                            #                 incumbencyFile_obj.incumbency_file.add(infoId)
                            #             else:
                            #                 incumbencyFile_obj = CompeteRestrictionsFile.objects.filter(id=incumbencyFile_id).update(**incumbency_kwargs)
                            #             if noWorkFile_id==None:
                            #                 pass
                            #             else:
                            #                 noWorkFile_obj = CompeteRestrictionsFile.objects.filter(id=noWorkFile_id).update(file_status=False)
                            #
                            #             insured_url, insured_name, insured_suffix = self.createPath(insured_file, str(info['name']) + '_' + str(
                            #                 info['idCard']), str(info['name']) +str(info['cycleData'])+'_参保证明')
                            #             self.saveFile(insured_url, insured_file)  # 保存文件
                            #             insured_kwargs = {
                            #                 "url": insured_url,
                            #                 "name": insured_name,
                            #             }
                            #             # insuredFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=insured_kwargs, id=infoId)[0]
                            #             # insuredFile_obj.insured_file.add(infoId)
                            #             insuredFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('insured_file__id',flat=True))[-1]  #参保证明
                            #             if insuredFile_id==None:
                            #                 insuredFile_obj=CompeteRestrictionsFile.objects.create(**insured_kwargs)
                            #                 insuredFile_obj.insured_file.add(infoId)
                            #             else:
                            #                 insuredFile_obj = CompeteRestrictionsFile.objects.filter(id=insuredFile_id).update(**insured_kwargs)
                            #
                            #
                            #             incomeTax_url, incomeTax_name, incomeTax_suffix = self.createPath(incomeTax_file,str(info['name']) + '_' + str(info['idCard']),str(info['name'])+str(info['cycleData'])+'_所得税缴税证明')
                            #             self.saveFile(incomeTax_url, incomeTax_file)
                            #             incomeTax_kwargs = {
                            #                 "url": incomeTax_url,
                            #                 "name": incomeTax_name,
                            #             }
                            #             # incomeTaxFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=incomeTax_kwargs, id=infoId)[0]
                            #             # incomeTaxFile_obj.incomeTax_file.add(infoId)
                            #             incomeTaxFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('incomeTax_file__id',flat=True))[-1]   #所得税缴税证明
                            #             if incomeTaxFile_id==None:
                            #                 incomeTaxFile_obj=CompeteRestrictionsFile.objects.create(**incomeTax_kwargs)
                            #                 incomeTaxFile_obj.incomeTax_file.add(infoId)
                            #             else:
                            #                 incomeTaxFile_obj = CompeteRestrictionsFile.objects.filter(id=incomeTaxFile_id).update(**incomeTax_kwargs)
                            #
                            #
                            #             accumulationFund_url, accumulationFund_name, accumulationFund_suffix = self.createPath(accumulationFund_file, str(info['name']) + '_' + str(info['idCard']),str(info['name'])+str(info['cycleData'])+ '_公积金账户信息')
                            #             self.saveFile(accumulationFund_url, accumulationFund_file)
                            #             accumulationFund_kwargs = {
                            #                 "url": accumulationFund_url,
                            #                 "name": accumulationFund_name,
                            #             }
                            #             # accumulationFundFile_obj =CompeteRestrictionsFile.objects.update_or_create(defaults=accumulationFund_kwargs, id=infoId)[0]
                            #             # accumulationFundFile_obj.accumulationFund_file.add(infoId)
                            #             accumulationFundFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('accumulationFund_file__id',flat=True))[-1]  #公积金账户信息
                            #             if accumulationFundFile_id==None:
                            #                 accumulationFundFile_obj=CompeteRestrictionsFile.objects.create(**accumulationFund_kwargs)
                            #                 accumulationFundFile_obj.accumulationFund_file.add(infoId)
                            #             else:
                            #                 accumulationFundFile_obj = CompeteRestrictionsFile.objects.filter(id=accumulationFundFile_id).update(**accumulationFund_kwargs)
                            #
                            #
                            #
                            #             photograph_url, photograph_name,photograph_suffix = self.createPath(photograph_file, str(info['name']) + '_' + str(info['idCard']),str(info['name'])+str(info['cycleData'])+ '_照片')
                            #             self.saveFile(photograph_url, photograph_file)
                            #             photograph_kwargs = {
                            #                 "url": photograph_url,
                            #                 "name": photograph_name,
                            #             }
                            #
                            #             photographFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('photograph_file__id',flat=True))[-1]  #公积金账户信息
                            #             if photographFile_id==None:
                            #                 photographFile_obj=CompeteRestrictionsFile.objects.create(**photograph_kwargs)
                            #                 photographFile_obj.photograph_file.add(infoId)
                            #             else:
                            #                 photographFile_obj = CompeteRestrictionsFile.objects.filter(id=photographFile_id).update(**photograph_kwargs)
                            #
                            #             self.return_data = {
                            #                 "code": HTTP_200_OK,
                            #                 "msg": "添加成功"
                            #             }
                            #
                            #         elif noWork_file!=None and incumbency_file==None:#无工作承诺函 日常照片 日常视频
                            #             dailyPhotos_url, dailyPhotos_name, dailyPhotos_suffix = self.createPath(dailyPhotos_file,str(info['name']) + '_' + str(info['idCard']),str(info['name'])+str(info['cycleData'])+ '_日常照片')
                            #             self.saveFile(dailyPhotos_url, dailyPhotos_file)
                            #             dailyPhotos_kwargs = {
                            #                 "url": dailyPhotos_url,
                            #                 "name": dailyPhotos_name,
                            #                 "file_status":1,
                            #             }
                            #             # dailyPhotosFile_obj =CompeteRestrictionsFile.objects.update_or_create(defaults=dailyPhotos_kwargs, id=infoId)[0]
                            #             # dailyPhotosFile_obj.dailyPhotos_file.add(infoId)
                            #             dailyPhotosFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('dailyPhotos_file__id',flat=True))[-1]   #日常照片
                            #             # print(dailyPhotosFile_id)
                            #             workPhotosFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('workPhotos_file__id',flat=True))[-1]   #工作照片
                            #             # print(workPhotosFile_id)
                            #             if dailyPhotosFile_id==None:
                            #                 dailyPhotosFile_obj=CompeteRestrictionsFile.objects.create(**dailyPhotos_kwargs)
                            #                 # print('11',dailyPhotosFile_obj)
                            #                 dailyPhotosFile_obj.dailyPhotos_file.add(infoId)
                            #             else:
                            #                 dailyPhotosFile_obj = CompeteRestrictionsFile.objects.filter(id=dailyPhotosFile_id).update(**dailyPhotos_kwargs)
                            #                 # print('22', dailyPhotosFile_obj)
                            #             if workPhotosFile_id==None:
                            #                 pass
                            #             else:   #存在工作照片   删掉
                            #                 workPhotosFile_obj= CompeteRestrictionsFile.objects.filter(id=workPhotosFile_id).update(file_status=False)
                            #
                            #             dailyVideo_url, dailyVideo_name, dailyVideo_suffix = self.createPath(dailyVideo_file,str(info['name']) + '_' + str(info['idCard']),str(info['name']) +str(info['cycleData'])+ '_日常视频')
                            #             self.saveFile(dailyVideo_url, dailyVideo_file)
                            #             dailyVideo_kwargs = {
                            #                 "url": dailyVideo_url,
                            #                 "name": dailyVideo_name,
                            #                 "file_status":1,
                            #             }
                            #             # dailyVideoFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=dailyVideo_kwargs, id=infoId)[0]
                            #             # dailyVideoFile_obj.dailyVideo_file.add(infoId)
                            #             dailyVideoFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('dailyVideo_file__id',flat=True))[-1]  #日常视频
                            #             workVideosFile_id = list(CompeteRestrictions.objects.filter(id=infoId).values_list('workVideo_file__id', flat=True))[-1]  # 工作视频
                            #             if dailyVideoFile_id==None:
                            #                 dailyVideoFile_obj=CompeteRestrictionsFile.objects.create(**dailyVideo_kwargs)
                            #                 dailyVideoFile_obj.dailyVideo_file.add(infoId)
                            #             else:
                            #                 dailyVideoFile_obj = CompeteRestrictionsFile.objects.filter(id=dailyVideoFile_id).update(**dailyVideo_kwargs)
                            #             if workVideosFile_id==None:
                            #                 pass
                            #             else:   #存在工作照片   删掉
                            #                 workVideoFile_obj= CompeteRestrictionsFile.objects.filter(id=workVideosFile_id).update(file_status=False)
                            #
                            #
                            #             noWork_url, noWork_name, noWork_suffix = self.createPath(noWork_file,str(info['name']) + '_' + str(info['idCard']),str(info['name']) +str(info['cycleData'])+ '_无工作承诺函')
                            #             self.saveFile(noWork_url, noWork_file)
                            #             noWork_kwargs = {
                            #                 "url": noWork_url,
                            #                 "name": noWork_name,
                            #                 "file_status":1,
                            #             }
                            #             # noWorkFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=noWork_kwargs, id=infoId)[0]
                            #             # noWorkFile_obj.noWork_file.add(infoId)
                            #             noWorkFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('noWork_file__id',flat=True))[-1]
                            #             incumbency_file_id = list(CompeteRestrictions.objects.filter(id=infoId).values_list('incumbency_file__id', flat=True))[-1]  #在职证明
                            #             if noWorkFile_id==None:
                            #                 noWorkFile_obj=CompeteRestrictionsFile.objects.create(**noWork_kwargs)
                            #                 noWorkFile_obj.noWork_file.add(infoId)
                            #             else:
                            #                 noWorkFile_obj = CompeteRestrictionsFile.objects.filter(id=noWorkFile_id).update(**noWork_kwargs)
                            #             if incumbency_file_id==None:
                            #                 pass
                            #             else:   #存在工作照片   删掉
                            #                 incumbencyFile_obj= CompeteRestrictionsFile.objects.filter(id=incumbency_file_id).update(file_status=False)
                            #
                            #             insured_url, insured_name, insured_suffix = self.createPath(insured_file, str(info['name']) + '_' + str(
                            #                 info['idCard']), str(info['name']) +str(info['cycleData'])+ '_参保证明')
                            #             self.saveFile(insured_url, insured_file)  # 保存文件
                            #             insured_kwargs = {
                            #                 "url": insured_url,
                            #                 "name": insured_name,
                            #             }
                            #             # insuredFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=insured_kwargs, id=infoId)[0]
                            #             # # insuredFile_obj = CompeteRestrictionsFile.objects.update_or_create(**insured_kwargs)[0]
                            #             # obj.insured_file.add(insuredFile_obj.id)
                            #             insured_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('insured_file__id',flat=True))[-1]
                            #             if insured_id==None:
                            #                 insuredFile_obj=CompeteRestrictionsFile.objects.create(**insured_kwargs)
                            #                 insuredFile_obj.insured_file.add(infoId)
                            #             else:
                            #                 insuredFile_obj = CompeteRestrictionsFile.objects.filter(id=insured_id).update(**insured_kwargs)
                            #
                            #             incomeTax_url, incomeTax_name, incomeTax_suffix = self.createPath(incomeTax_file,str(info['name']) + '_' + str(info['idCard']),str(info['name'])+str(info['cycleData'])+ '_所得税缴税证明')
                            #             self.saveFile(incomeTax_url, incomeTax_file)
                            #             incomeTax_kwargs = {
                            #                 "url": incomeTax_url,
                            #                 "name": incomeTax_name,
                            #             }
                            #             # incomeTaxFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=incomeTax_kwargs, id=infoId)[0]
                            #             # # incomeTaxFile_obj = CompeteRestrictionsFile.objects.update_or_create(**incomeTax_kwargs)[0]
                            #             # obj.incomeTax_file.add(incomeTaxFile_obj.id)
                            #             incomeTax_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('incomeTax_file__id',flat=True))[-1]
                            #             if incomeTax_id==None:
                            #                 incomeTaxFile_obj=CompeteRestrictionsFile.objects.create(**incomeTax_kwargs)
                            #                 incomeTaxFile_obj.incomeTax_file.add(infoId)
                            #             else:
                            #                 incomeTaxFile_obj = CompeteRestrictionsFile.objects.filter(id=incomeTax_id).update(**incomeTax_kwargs)
                            #
                            #             #
                            #             accumulationFund_url, accumulationFund_name, accumulationFund_suffix = self.createPath(accumulationFund_file, str(info['name']) + '_' + str(info['idCard']),str(info['name']) +str(info['cycleData'])+ '_公积金账户信息')
                            #             self.saveFile(accumulationFund_url, accumulationFund_file)
                            #             accumulationFund_kwargs = {
                            #                 "url": accumulationFund_url,
                            #                 "name": accumulationFund_name,
                            #             }
                            #             # accumulationFundFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=accumulationFund_kwargs, id=infoId)[0]
                            #             # obj.accumulationFund_file.add(accumulationFundFile_obj.id)
                            #             accumulationFundFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('accumulationFund_file__id',flat=True))[-1]
                            #             if accumulationFundFile_id==None:
                            #                 accumulationFundFile_obj=CompeteRestrictionsFile.objects.create(**accumulationFund_kwargs)
                            #                 accumulationFundFile_obj.accumulationFund_file.add(infoId)
                            #             else:
                            #                 accumulationFundFile_obj = CompeteRestrictionsFile.objects.filter(id=accumulationFundFile_id).update(**accumulationFund_kwargs)
                            #
                            #             photograph_url, photograph_name, photograph_suffix = self.createPath(photograph_file,str(info['name']) + '_' + str(info['idCard']),str(info['name']) + str(info['cycleData']) + '_照片')
                            #             self.saveFile(photograph_url, photograph_file)
                            #             photograph_kwargs = {
                            #                 "url": photograph_url,
                            #                 "name": photograph_name,
                            #             }
                            #             # print(photograph_kwargs)
                            #
                            #             photographFile_id = list(CompeteRestrictions.objects.filter(id=infoId).values_list('photograph_file__id',flat=True))[-1]  # 强制拍照
                            #             # print(photographFile_id)
                            #             if photographFile_id == None:
                            #                 photographFile_obj = CompeteRestrictionsFile.objects.create(**photograph_kwargs)
                            #                 photographFile_obj.photograph_file.add(infoId)
                            #             else:
                            #                 photographFile_obj = CompeteRestrictionsFile.objects.filter(id=photographFile_id).update(**photograph_kwargs)
                            #
                            #             self.return_data = {
                            #                 "code": HTTP_200_OK,
                            #                 "msg": "添加成功"
                            #             }
                            #
                            #
                            #         elif noWork_file!=None and incumbency_file!=None:
                            #             self.return_data = {
                            #                     "code": status.HTTP_401_UNAUTHORIZED,
                            #                     "msg": "在职证明和无工作承诺函只能选择一个！"
                            #                 }
                            #         elif noWork_file==None and incumbency_file==None:
                            #             self.return_data = {
                            #                     "code": status.HTTP_401_UNAUTHORIZED,
                            #                     "msg": "在职证明和无工作承诺函必须选择一个！"
                            #                 }
                            #     else:
                            #         self.return_data = {
                            #             "code": status.HTTP_401_UNAUTHORIZED,
                            #             "msg": "抱歉，请必须拍照，否则无法上传！"
                            #         }
                            # except:
                            #     self.return_data = {
                            #         "code": status.HTTP_401_UNAUTHORIZED,
                            #         "msg": "上传失败！"
                            #     }
                        else:
                            self.return_data = {
                                "code": status.HTTP_401_UNAUTHORIZED,
                                "msg": "日期不在竞业周期范围内，无法添加！"
                            }
                    # except:
                    #     self.return_data = {
                    #         "code": status.HTTP_401_UNAUTHORIZED,
                    #         "msg": "有错误,无法添加！"
                    #     }
                else:
                    self.return_data = {
                        "code": status.HTTP_401_UNAUTHORIZED,
                        "msg": "身份证号与姓名无法匹配,无法添加！"
                    }
            else:
                self.return_data = {
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "msg": "您不是竞业限制人员，无法添加！"
                }
        else:
            self.return_data = {
                "code": status.HTTP_400_BAD_REQUEST,
                "msg": "请填写正确的身份证！"
            }



        # print(info)

    def get_isExpiration(self):
        try:
            workLs=CompeteRestrictionsWhitelist.objects.filter(compete_status=True).values_list('workNumber')
            for i in workLs:
                workNumber=i[0]
                id,beginData,endData=CompeteRestrictionsWhitelist.objects.filter(workNumber=workNumber,compete_status=True).values_list('id','cycleBeginData','cycleEndData')[0]
                if endData.year == beginData.year and endData.month== beginData.month:
                    months_difference=1
                else:
                    months_difference = (endData.year - beginData.year) * 12 + (endData.month - beginData.month)+1
                end = endData.replace(day=28)
                begin = beginData.replace(day=1)
                num_count = CompeteRestrictions.objects.filter(compete_status=True,people_id=id,cycleData__range=(begin,end)).values('cycleData').distinct().count() #数据库有几条数据
                # print(workNumber,num_count,months_difference,beginData,endData,begin,end)
                if eval(str(num_count))>=eval(str(months_difference)):
                    CompeteRestrictionsWhitelist.objects.filter(workNumber=workNumber, compete_status=True).update(isExpiration=True)
                elif eval(str(num_count))<eval(str(months_difference)):
                    CompeteRestrictionsWhitelist.objects.filter(workNumber=workNumber, compete_status=True).update(isExpiration=False)
                    # self.return_data = {
                    #     "msg": workNumber+"已届满",
                    #     'isExpiration': True
                    # }
                # else:
                #     self.return_data = {
                #         "msg": workNumber + "未届满",
                #         'isExpiration': False
                #     }

            self.return_data = {
                "code": HTTP_200_OK,
                "msg": "届满已校验成功"
            }
        except:
            self.return_data = {
                "code": HTTP_401_UNAUTHORIZED,
                "msg": "未知错误！"
            }




    #     if self.judgeDate(info['cycleData'],info['cycleBeginData'],info['cycleEndData']):
    #         if type(info['cycleData'])==str:
    #             cycleData=self.get_first_last(datetime.strptime(info['cycleData'],'%Y-%m-%d'))[0]
    #         else:
    #             cycleData=self.get_first_last(info['cycleData'])[0] #该月第一天
    #         info['cycleData']=cycleData
    #         # print(info)
    #         try:
    #             del info['insured_file']
    #         except:
    #             pass
    #         try:
    #             del info['incomeTax_file']
    #         except:
    #             pass
    #         try:
    #             del info['accumulationFund_file']
    #         except:
    #             pass
    #         try:
    #             del info['noWork_file']
    #         except:
    #             pass
    #         try:
    #             del info['dailyVideo_file']
    #         except:
    #             pass
    #         try:
    #             del info['dailyPhotos_file']
    #         except:
    #             pass
    #         try:
    #             del info['incumbency_file']
    #         except:
    #             pass
    #         try:
    #             del info['workPhotos_file']
    #         except:
    #             pass
    #         try:
    #             del info['workVideo_file']
    #         except:
    #             pass
    #
    #         obj=CompeteRestrictions.objects.update_or_create(defaults=info,cycleData=cycleData,idCard=info['idCard'])
    #         if obj[1]==True:
    #             flag=1 #创建
    #         else:
    #             flag=0#更新
    #         # print(obj,flag)
    #         infoId=obj[0].id
    #
    #
    #
    #         insured_file=self.request.FILES.get("insured_file", None)#参保证明
    #         incomeTax_file = self.request.FILES.get("incomeTax_file", None)  # 所得税缴税证明
    #         accumulationFund_file = self.request.FILES.get("accumulationFund_file", None)  # 公积金账户信息
    #         workPhotos_file = self.request.FILES.get("workPhotos_file", None)  # 工作照片
    #         workVideo_file = self.request.FILES.get("workVideo_file", None)  # 工作视频
    #         dailyPhotos_file = self.request.FILES.get("dailyPhotos_file", None)  # 日常照片
    #         dailyVideo_file = self.request.FILES.get("dailyVideo_file", None)  # 日常视频
    #         incumbency_file = self.request.FILES.get("incumbency_file", None)  # 在职证明
    #         noWork_file = self.request.FILES.get("noWork_file", None)  # 无工作承诺函
    #         t = time.strftime('%Y-%m-%d')
    #         dummy_path = os.path.join(BASE_DIR, 'static', 'competeRestrictionsFile', 'upload_file', t,str(info['name']) +'_'+ str(info['idCard']))  # 创建文件夹
    #         self.mkdir(dummy_path)
    #         try:
    #             if incumbency_file!=None and noWork_file==None:  #  在职证明 工作照片 工作视频
    #                 workPhotos_url, workPhotos_name, workPhotos_suffix = self.createPath(workPhotos_file,str(info['name']) + '_' + str(info['idCard']),str(info['name']) + '_工作照片')
    #                 self.saveFile(workPhotos_url, workPhotos_file)
    #                 workPhotos_kwargs = {
    #                     "url": workPhotos_url,
    #                     "name": workPhotos_name,
    #                     "file_status":1,
    #                 }
    #                 # if flag==0:#更新
    #                 #     workPhotosFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('workPhotos_file__id',flat=True))[-1]
    #                 #     workPhotosFile_obj=CompeteRestrictionsFile.objects.filter(id=workPhotosFile_id).update(**workPhotos_kwargs)
    #                 # else:  #创建
    #                 #     workPhotosFile_obj=CompeteRestrictionsFile.objects.create(**workPhotos_kwargs)
    #                 #     workPhotosFile_obj.workPhotos_file.add(infoId)
    #                 workPhotosFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('workPhotos_file__id',flat=True))[-1]   #工作照片
    #                 dailyPhotosFile_id = list(CompeteRestrictions.objects.filter(id=infoId).values_list('dailyPhotos_file__id', flat=True))[-1]  # 日常照片
    #                 # print(workPhotosFile_id,dailyPhotosFile_id)
    #                 if workPhotosFile_id==None:
    #                     workPhotosFile_obj=CompeteRestrictionsFile.objects.create(**workPhotos_kwargs)
    #                     workPhotosFile_obj.workPhotos_file.add(infoId)
    #                 else:
    #                     workPhotosFile_obj = CompeteRestrictionsFile.objects.filter(id=workPhotosFile_id).update(**workPhotos_kwargs)
    #
    #                 if dailyPhotosFile_id==None:
    #                     pass
    #                 else:
    #                     dailyPhotosFile_obj= CompeteRestrictionsFile.objects.filter(id=dailyPhotosFile_id).update(file_status=False)
    #
    #
    #
    #                 workVideo_url, workVideo_name, workVideo_suffix = self.createPath(workVideo_file,str(info['name']) + '_' + str(info['idCard']),str(info['name']) + '_工作视频')
    #                 self.saveFile(workVideo_url, workVideo_file)
    #                 workVideo_kwargs = {
    #                     "url": workVideo_url,
    #                     "name": workVideo_name,
    #                     "file_status": 1,
    #                 }
    #                 workVideoFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('workVideo_file__id',flat=True))[-1]  #工作视频
    #                 dailyVideoFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('dailyVideo_file__id',flat=True))[-1]  #日常视频
    #                 if workVideoFile_id==None:
    #                     workVideoFile_obj=CompeteRestrictionsFile.objects.create(**workVideo_kwargs)
    #                     workVideoFile_obj.workVideo_file.add(infoId)
    #                 else:
    #                     workVideoFile_obj = CompeteRestrictionsFile.objects.filter(id=workVideoFile_id).update(**workVideo_kwargs)
    #                 if dailyVideoFile_id==None:
    #                     pass
    #                 else:
    #                     dailyVideoFile_obj = CompeteRestrictionsFile.objects.filter(id=dailyVideoFile_id).update(file_status=False)
    #
    #
    #
    #
    #                 incumbency_url,incumbency_name,incumbency_suffix=self.createPath(incumbency_file, str(info['name']) + '_' + str(info['idCard']), str(info['name']) + '_在职证明')
    #                 self.saveFile(incumbency_url, incumbency_file)
    #                 incumbency_kwargs={
    #                     "url": incumbency_url,
    #                     "name":incumbency_name,
    #                     "file_status": 1,
    #                 }
    #                 # incumbencyFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=incumbency_kwargs, id=infoId)[0]
    #                 # incumbencyFile_obj.incumbency_file.add(infoId)
    #                 incumbencyFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('incumbency_file__id',flat=True))[-1]   #在职证明
    #                 noWorkFile_id = list(CompeteRestrictions.objects.filter(id=infoId).values_list('noWork_file__id', flat=True))[-1]#无工作承诺函
    #                 if incumbencyFile_id==None:
    #                     incumbencyFile_obj=CompeteRestrictionsFile.objects.create(**incumbency_kwargs)
    #                     incumbencyFile_obj.incumbency_file.add(infoId)
    #                 else:
    #                     incumbencyFile_obj = CompeteRestrictionsFile.objects.filter(id=incumbencyFile_id).update(**incumbency_kwargs)
    #                 if noWorkFile_id==None:
    #                     pass
    #                 else:
    #                     noWorkFile_obj = CompeteRestrictionsFile.objects.filter(id=noWorkFile_id).update(file_status=False)
    #
    #                 insured_url, insured_name, insured_suffix = self.createPath(insured_file, str(info['name']) + '_' + str(
    #                     info['idCard']), str(info['name']) + '_''参保证明')
    #                 self.saveFile(insured_url, insured_file)  # 保存文件
    #                 insured_kwargs = {
    #                     "url": insured_url,
    #                     "name": insured_name,
    #                 }
    #                 # insuredFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=insured_kwargs, id=infoId)[0]
    #                 # insuredFile_obj.insured_file.add(infoId)
    #                 insuredFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('insured_file__id',flat=True))[-1]  #参保证明
    #                 if insuredFile_id==None:
    #                     insuredFile_obj=CompeteRestrictionsFile.objects.create(**insured_kwargs)
    #                     insuredFile_obj.insured_file.add(infoId)
    #                 else:
    #                     insuredFile_obj = CompeteRestrictionsFile.objects.filter(id=insuredFile_id).update(**insured_kwargs)
    #
    #
    #                 incomeTax_url, incomeTax_name, incomeTax_suffix = self.createPath(incomeTax_file,str(info['name']) + '_' + str(info['idCard']),str(info['name']) + '_所得税缴税证明')
    #                 self.saveFile(incomeTax_url, incomeTax_file)
    #                 incomeTax_kwargs = {
    #                     "url": incomeTax_url,
    #                     "name": incomeTax_name,
    #                 }
    #                 # incomeTaxFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=incomeTax_kwargs, id=infoId)[0]
    #                 # incomeTaxFile_obj.incomeTax_file.add(infoId)
    #                 incomeTaxFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('incomeTax_file__id',flat=True))[-1]   #所得税缴税证明
    #                 if incomeTaxFile_id==None:
    #                     incomeTaxFile_obj=CompeteRestrictionsFile.objects.create(**incomeTax_kwargs)
    #                     incomeTaxFile_obj.incomeTax_file.add(infoId)
    #                 else:
    #                     incomeTaxFile_obj = CompeteRestrictionsFile.objects.filter(id=incomeTaxFile_id).update(**incomeTax_kwargs)
    #
    #
    #                 accumulationFund_url, accumulationFund_name, accumulationFund_suffix = self.createPath(accumulationFund_file, str(info['name']) + '_' + str(info['idCard']),str(info['name']) + '_公积金账户信息')
    #                 self.saveFile(accumulationFund_url, accumulationFund_file)
    #                 accumulationFund_kwargs = {
    #                     "url": accumulationFund_url,
    #                     "name": accumulationFund_name,
    #                 }
    #                 # accumulationFundFile_obj =CompeteRestrictionsFile.objects.update_or_create(defaults=accumulationFund_kwargs, id=infoId)[0]
    #                 # accumulationFundFile_obj.accumulationFund_file.add(infoId)
    #                 accumulationFundFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('accumulationFund_file__id',flat=True))[-1]  #公积金账户信息
    #                 if accumulationFundFile_id==None:
    #                     accumulationFundFile_obj=CompeteRestrictionsFile.objects.create(**accumulationFund_kwargs)
    #                     accumulationFundFile_obj.accumulationFund_file.add(infoId)
    #                 else:
    #                     accumulationFundFile_obj = CompeteRestrictionsFile.objects.filter(id=accumulationFundFile_id).update(**accumulationFund_kwargs)
    #
    #                 self.return_data = {
    #                     "code": HTTP_200_OK,
    #                     "msg": "添加成功"
    #                 }
    #
    #             elif noWork_file!=None and incumbency_file==None:#无工作承诺函 日常照片 日常视频
    #                 dailyPhotos_url, dailyPhotos_name, dailyPhotos_suffix = self.createPath(dailyPhotos_file,str(info['name']) + '_' + str(info['idCard']),str(info['name']) + '_日常照片')
    #                 self.saveFile(dailyPhotos_url, dailyPhotos_file)
    #                 dailyPhotos_kwargs = {
    #                     "url": dailyPhotos_url,
    #                     "name": dailyPhotos_name,
    #                     "file_status":1,
    #                 }
    #                 # dailyPhotosFile_obj =CompeteRestrictionsFile.objects.update_or_create(defaults=dailyPhotos_kwargs, id=infoId)[0]
    #                 # dailyPhotosFile_obj.dailyPhotos_file.add(infoId)
    #                 dailyPhotosFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('dailyPhotos_file__id',flat=True))[-1]   #日常照片
    #                 # print(dailyPhotosFile_id)
    #                 workPhotosFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('workPhotos_file__id',flat=True))[-1]   #工作照片
    #                 # print(workPhotosFile_id)
    #                 if dailyPhotosFile_id==None:
    #                     dailyPhotosFile_obj=CompeteRestrictionsFile.objects.create(**dailyPhotos_kwargs)
    #                     # print('11',dailyPhotosFile_obj)
    #                     dailyPhotosFile_obj.dailyPhotos_file.add(infoId)
    #                 else:
    #                     dailyPhotosFile_obj = CompeteRestrictionsFile.objects.filter(id=dailyPhotosFile_id).update(**dailyPhotos_kwargs)
    #                     # print('22', dailyPhotosFile_obj)
    #                 if workPhotosFile_id==None:
    #                     pass
    #                 else:   #存在工作照片   删掉
    #                     workPhotosFile_obj= CompeteRestrictionsFile.objects.filter(id=workPhotosFile_id).update(file_status=False)
    #
    #                 dailyVideo_url, dailyVideo_name, dailyVideo_suffix = self.createPath(dailyVideo_file,str(info['name']) + '_' + str(info['idCard']),str(info['name']) + '_日常视频')
    #                 self.saveFile(dailyVideo_url, dailyVideo_file)
    #                 dailyVideo_kwargs = {
    #                     "url": dailyVideo_url,
    #                     "name": dailyVideo_name,
    #                     "file_status":1,
    #                 }
    #                 # dailyVideoFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=dailyVideo_kwargs, id=infoId)[0]
    #                 # dailyVideoFile_obj.dailyVideo_file.add(infoId)
    #                 dailyVideoFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('dailyVideo_file__id',flat=True))[-1]  #日常视频
    #                 workVideosFile_id = list(CompeteRestrictions.objects.filter(id=infoId).values_list('workVideo_file__id', flat=True))[-1]  # 工作视频
    #                 if dailyVideoFile_id==None:
    #                     dailyVideoFile_obj=CompeteRestrictionsFile.objects.create(**dailyVideo_kwargs)
    #                     dailyVideoFile_obj.dailyVideo_file.add(infoId)
    #                 else:
    #                     dailyVideoFile_obj = CompeteRestrictionsFile.objects.filter(id=dailyVideoFile_id).update(**dailyVideo_kwargs)
    #                 if workVideosFile_id==None:
    #                     pass
    #                 else:   #存在工作照片   删掉
    #                     workVideoFile_obj= CompeteRestrictionsFile.objects.filter(id=workVideosFile_id).update(file_status=False)
    #
    #
    #                 noWork_url, noWork_name, noWork_suffix = self.createPath(noWork_file,str(info['name']) + '_' + str(info['idCard']),str(info['name']) + '_无工作承诺函')
    #                 self.saveFile(noWork_url, noWork_file)
    #                 noWork_kwargs = {
    #                     "url": noWork_url,
    #                     "name": noWork_name,
    #                     "file_status":1,
    #                 }
    #                 # noWorkFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=noWork_kwargs, id=infoId)[0]
    #                 # noWorkFile_obj.noWork_file.add(infoId)
    #                 noWorkFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('noWork_file__id',flat=True))[-1]
    #                 incumbency_file_id = list(CompeteRestrictions.objects.filter(id=infoId).values_list('incumbency_file__id', flat=True))[-1]  #在职证明
    #                 if noWorkFile_id==None:
    #                     noWorkFile_obj=CompeteRestrictionsFile.objects.create(**noWork_kwargs)
    #                     noWorkFile_obj.noWork_file.add(infoId)
    #                 else:
    #                     noWorkFile_obj = CompeteRestrictionsFile.objects.filter(id=noWorkFile_id).update(**noWork_kwargs)
    #                 if incumbency_file_id==None:
    #                     pass
    #                 else:   #存在工作照片   删掉
    #                     incumbencyFile_obj= CompeteRestrictionsFile.objects.filter(id=incumbency_file_id).update(file_status=False)
    #
    #                 insured_url, insured_name, insured_suffix = self.createPath(insured_file, str(info['name']) + '_' + str(
    #                     info['idCard']), str(info['name']) + '_''参保证明')
    #                 self.saveFile(insured_url, insured_file)  # 保存文件
    #                 insured_kwargs = {
    #                     "url": insured_url,
    #                     "name": insured_name,
    #                 }
    #                 # insuredFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=insured_kwargs, id=infoId)[0]
    #                 # # insuredFile_obj = CompeteRestrictionsFile.objects.update_or_create(**insured_kwargs)[0]
    #                 # obj.insured_file.add(insuredFile_obj.id)
    #                 insured_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('insured_file__id',flat=True))[-1]
    #                 if insured_id==None:
    #                     insuredFile_obj=CompeteRestrictionsFile.objects.create(**insured_kwargs)
    #                     insuredFile_obj.insured_file.add(infoId)
    #                 else:
    #                     insuredFile_obj = CompeteRestrictionsFile.objects.filter(id=insured_id).update(**insured_kwargs)
    #
    #                 incomeTax_url, incomeTax_name, incomeTax_suffix = self.createPath(incomeTax_file,str(info['name']) + '_' + str(info['idCard']),str(info['name']) + '_所得税缴税证明')
    #                 self.saveFile(incomeTax_url, incomeTax_file)
    #                 incomeTax_kwargs = {
    #                     "url": incomeTax_url,
    #                     "name": incomeTax_name,
    #                 }
    #                 # incomeTaxFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=incomeTax_kwargs, id=infoId)[0]
    #                 # # incomeTaxFile_obj = CompeteRestrictionsFile.objects.update_or_create(**incomeTax_kwargs)[0]
    #                 # obj.incomeTax_file.add(incomeTaxFile_obj.id)
    #                 incomeTax_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('incomeTax_file__id',flat=True))[-1]
    #                 if incomeTax_id==None:
    #                     incomeTaxFile_obj=CompeteRestrictionsFile.objects.create(**incomeTax_kwargs)
    #                     incomeTaxFile_obj.incomeTax_file.add(infoId)
    #                 else:
    #                     incomeTaxFile_obj = CompeteRestrictionsFile.objects.filter(id=incomeTax_id).update(**incomeTax_kwargs)
    #
    #                 #
    #                 accumulationFund_url, accumulationFund_name, accumulationFund_suffix = self.createPath(accumulationFund_file, str(info['name']) + '_' + str(info['idCard']),str(info['name']) + '_公积金账户信息')
    #                 self.saveFile(accumulationFund_url, accumulationFund_file)
    #                 accumulationFund_kwargs = {
    #                     "url": accumulationFund_url,
    #                     "name": accumulationFund_name,
    #                 }
    #                 # accumulationFundFile_obj = CompeteRestrictionsFile.objects.update_or_create(defaults=accumulationFund_kwargs, id=infoId)[0]
    #                 # obj.accumulationFund_file.add(accumulationFundFile_obj.id)
    #                 accumulationFundFile_id=list(CompeteRestrictions.objects.filter(id=infoId).values_list('accumulationFund_file__id',flat=True))[-1]
    #                 if accumulationFundFile_id==None:
    #                     accumulationFundFile_obj=CompeteRestrictionsFile.objects.create(**accumulationFund_kwargs)
    #                     accumulationFundFile_obj.accumulationFund_file.add(infoId)
    #                 else:
    #                     accumulationFundFile_obj = CompeteRestrictionsFile.objects.filter(id=accumulationFundFile_id).update(**accumulationFund_kwargs)
    #
    #
    #                 self.return_data = {
    #                     "code": HTTP_200_OK,
    #                     "msg": "添加成功"
    #                 }
    #
    #
    #             elif noWork_file!=None and incumbency_file!=None:
    #                 self.return_data = {
    #                         "code": status.HTTP_401_UNAUTHORIZED,
    #                         "msg": "在职证明和无工作承诺函只能选择一个！"
    #                     }
    #             elif noWork_file==None and incumbency_file==None:
    #                 self.return_data = {
    #                         "code": status.HTTP_401_UNAUTHORIZED,
    #                         "msg": "在职证明和无工作承诺函必须选择一个！"
    #                     }
    #         except:
    #             self.return_data = {
    #                 "code": status.HTTP_401_UNAUTHORIZED,
    #                 "msg": "上传失败！"
    #             }
    #     else:
    #         self.return_data = {
    #             "code": status.HTTP_401_UNAUTHORIZED,
    #             "msg": "日期不在竞业周期范围内，无法添加！"
    #         }
    # #





        # if pic_suffix in ['jpg', 'jpeg', 'png']:
        #     with open('static/volumeContractsFile/upload_file/' + t + '/' + path+'/' +pic_name, 'wb') as f:
        #         for dot in pic_obj.chunks():
        #             f.write(dot)
        # elif pic_suffix in ['doc', 'docx', 'xls', 'xlsx', 'txt']:
        #     with open('static/volumeContractsFile/upload_file/' + t + '/' + path+'/'+pic_name, 'wb+') as f:
        #         for dot in pic_obj.chunks():
        #             f.write(dot)

    def patch_data(self):   #只修改白名单
        # isPatch = self.request.GET.get('isPatch', 'None')
        info = self.request.data
        # print(info)
        # info1={
        #     "phone": info['phone'],
        #     "address":info['address'],
        #     "cycleData": info['cycleData'],
        #     "name": info['name'],
        #     'id':info['id'],
        # }
        info2={
            "idCard": info['idCard'],
            "cycleBeginData": info['cycleBeginData'],
            "cycleEndData":info['cycleEndData'],
            # "cr_base_id":info['cr_base_id'][1] if len(info['cr_base_id'])==2 else info['cr_base_id'][0],
            'id':info['id'],   #白名单id
            'compete_remark':info['compete_remark'],
            'name':info['name'],
            'contract':info['contract'],
            'workNumber':info['workNumber'],
            # 'isExpiration':info['isExpiration'],
            'modifier_id': self.request.check_token
        }
        # print(info2)
        try:
            info2['cr_base_id']=info['cr_base_id'][1] if len(info['cr_base_id'])==2 else info['cr_base_id'][0]
        except:
            info2['cr_base_id']=info['cr_base_id']


        if self.request.check_token!=None:
            CompeteRestrictionsWhitelist.objects.filter(id=info2['id'], compete_status=True).update(**info2)
            CompeteRestrictions.objects.filter(people_id=info2['id'],compete_status=True).update(idCard=info2['idCard'],name=info2['name'])


            # if self.judgeDate(info['cycleData'], info['cycleBeginData'], info['cycleEndData']):
            #     # CompeteRestrictions.objects.filter(id=info1['id'], compete_status=True).update(**info1)
            #     # CompeteRestrictionsWhitelist.objects.filter(id=info2['id'], compete_status=True).update(**info2)
            # else:
            #     self.return_data = {
            #         "code": status.HTTP_401_UNAUTHORIZED,
            #         "msg": "周期不在竞业周期范围内，无法修改！"
            #     }
        else:
            self.return_data = {
                "code": HTTP_403_FORBIDDEN,
                "msg": "没有权限访问"
            }

    # def get_location(self,request):
    #     longitude = request.GET.get("longitude", None)  # 经度
    #     latitude = request.GET.get("latitude", None)  # 纬度
    #     if longitude is None or latitude is None:
    #         return HttpResponse('')
    #     url = "https://restapi.amap.com/v3/geocode/regeo?output=json&location={0},{1}&key=5ac9f355f8489931303f20f73fd05ed7&radius=50&extensions=all&batch=false&extensions=base".format(
    #         longitude, latitude)
    #     resp = requests.get(url).content
    #     resp = json.loads(resp)
    #     return HttpResponse(json.dumps(resp))
    def verify(self):
        info=self.request.GET
        try:
            if self.is_valid_id_card(info['idCard']):
                self.return_data = {
                    "code": status.HTTP_200_OK,
                    "msg": "是身份证！"
                }
            else:
                self.return_data = {
                    "code": status.HTTP_400_BAD_REQUEST,
                    "msg": "请填写正确的身份证！"
                }
        except:
            self.return_data = {
                "code": status.HTTP_400_BAD_REQUEST,
                "msg": "数据错误！"
            }


    def delete_data(self):  # 删除数据   只改白名单
        if self.request.check_token != None:
            self.return_data = {
                "code": status.HTTP_200_OK,
                "msg": "删除成功！"
            }
            try:
                # print(json.loads(self.request.body))
                idList= json.loads(self.request.body)['idList']
                for item in idList:
                    if item['pId']=='':   #白名单
                        CompeteRestrictionsWhitelist.objects.filter(id=item['id']).update(compete_status=False)
                    else:  #限制
                        self.return_data = {
                            "code": status.HTTP_400_BAD_REQUEST,
                            "msg": "该行存在竞业数据，无法删除！"
                        }
                        # CompeteRestrictions.objects.filter(id=item['pId']).update(compete_status=False)

            except Exception as e:
                self.return_data = {
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "msg": "删除失败！"
                }

        else:
            self.return_data = {
                "code": HTTP_403_FORBIDDEN,
                "msg": "没有权限访问"
            }




    def post_annex_file(self):
        # print(self.request.FILES)
        # print(self.request.POST.dict())
        info = eval(self.request.POST.dict().get('createData'))
        if len(info['cycleData'])==7:
            info['cycleData']=info['cycleData']+'-01'
        #
        # print(len(info['cycleData']),info['cycleData'],type(info['cycleData']))
        file = self.request.FILES.get("file", None)  # 电话回访

        import arrow
        now = arrow.now()
        t1 = now.format('YYYY-MM-DD')
        t2 = now.timestamp()

        t = time.strftime('%Y-%m-%d')
        dummy_path = os.path.join(BASE_DIR, 'static', 'competeRestrictionsFile', 'upload_file', t,
                                  str(info['name']) + '_' + str(info['cycleData']+'_附件'))  # 创建文件夹
        self.mkdir(dummy_path)

        if info['pId']!='':
            if info['type']=='cllBack_file':#可以多次上传
                # for f in filels:
                cllBack_url, cllBack_name, cllBack_suffix = self.createPath(
                    file,
                    str(info['name']) + '_' + str(info['cycleData']+'_附件'),
                    str(info['name']) + str(info['cycleData'])+'_'+str(t2)[-5:]+ '_电话回访录音')
                self.saveFile(cllBack_url, file)
                cellBack_kwargs = {
                    "url": cllBack_url,
                    "name": cllBack_name,
                }
                cllBackFile_obj = CompeteRestrictionsFile.objects.create(**cellBack_kwargs)
                cllBackFile_obj.cllBack_file.add(info['pId'])
                self.return_data = {
                    "code": status.HTTP_200_OK,
                    "msg": "电话回访录音上传成功！"
                }
            elif info['type']=='firstlivevideo_file':
                firstlivevideo_url, firstlivevideo_name, firstlivevideo_suffix = self.createPath(
                        file,
                        str(info['name']) + '_' + str(info['cycleData']+'_附件'),
                        str(info['name']) + str(info['cycleData']) +'_'+str(t2)[-5:]+ '_实时视频(第一次)')
                self.saveFile(firstlivevideo_url,file)
                firstlivevideoFile_kwargs = {
                    "url": firstlivevideo_url,
                    "name": firstlivevideo_name,
                }
                firstlivevideoFile_obj = CompeteRestrictionsFile.objects.create(**firstlivevideoFile_kwargs)
                firstlivevideoFile_obj.firstlivevideo_file.add(info['pId'])
                self.return_data = {
                    "code": status.HTTP_200_OK,
                    "msg": "实时视频(第一次)上传成功！"
                }
            elif info['type']=="secondlivevideo_file":
                #     # print('secondlivevideo_file')
                secondlivevideo_url,secondlivevideo_name,secondlivevideo_suffix = self.createPath(
                    file,
                    str(info['name']) + '_' + str(info['cycleData']+'_附件'),
                    str(info['name']) + str(info['cycleData']) +'_'+str(t2)[-5:]+ '_实时视频(第二次)')
                self.saveFile(secondlivevideo_url,file)
                secondlivevideoFile_kwargs = {
                    "url": secondlivevideo_url,
                    "name": secondlivevideo_name,
                }
                # print(secondlivevideoFile_kwargs)
                secondlivevideoFile_obj = CompeteRestrictionsFile.objects.create(**secondlivevideoFile_kwargs)
                secondlivevideoFile_obj.secondlivevideo_file.add(info['pId'])

                self.return_data = {
                    "code": status.HTTP_200_OK,
                    "msg": "实时视频(第二次)上传成功！"
                }
                # print('3')



        else:
            self.return_data = {
                "code": status.HTTP_401_UNAUTHORIZED,
                "msg": "请选择正确的竞业人员"
            }


        # if info['pId']=='':

        #
        # pass
    def delete_annex_file(self):
        # print(json.loads(self.request.body))
        pId=json.loads(self.request.body)['pId']
        type = json.loads(self.request.body)['type']
        # print(type,pId)   #{'pId': 67, 'type': 'firstlivevideo_file'}

        if pId != "":
            try:
                compete_restrictions = CompeteRestrictions.objects.get(pk=pId)
                # CompeteRestrictionsFile.objects.filter(id=file_id).update(file_status=0)
                # print(CompeteRestrictions.objects.filter(pk=pId).values('cllBack_file__file_status'))
                if type=='cllBack_file':#可以多次上传
                    compete_restrictions.cllBack_file.update(file_status=False)

                elif type=='firstlivevideo_file':#可以多次上传
                    compete_restrictions.firstlivevideo_file.update(file_status=False)
                elif type=='secondlivevideo_file':#可以多次上传
                    compete_restrictions.secondlivevideo_file.update(file_status=False)
                self.return_data = {
                    "code": 200,
                    "msg": "附件删除成功"
                }
            except Exception as e:
                # print(e)
                self.return_data = {
                    "code": 400,
                    "msg": "附件删除异常"
                }

        return self.return_data


    def delete_other_file(self):#删除文件
        file_id = json.loads(self.request.body)['file_id']
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "请求删除的附件为空"
        }
        if file_id != "":
            try:
                CompeteRestrictionsFile.objects.filter(id=file_id).update(file_status=0)
                self.return_data = {
                    "code": 200,
                    "msg": "附件删除成功"
                }
            except Exception as e:
                # print(e)
                self.return_data = {
                    "code": 400,
                    "msg": "附件删除失败"
                }

        return self.return_data



    def download_file(self):
        if self.request.check_token != None:
            id_list = self.request.data.get('idList')
            downloadAll = self.request.data.get('downloadAll')

            # print(id_list,downloadAll)   #[{'id': 9, 'pId': ''}, {'id': 8, 'pId': 32}, {'id': 7, 'pId': 34}, {'id': 7, 'pId': 35}] True
            t = time.strftime('%Y-%m-%d')
            t1 = str(time.time())
            # dummy_path = os.path.join(BASE_DIR, 'static', 'competeRestrictionsFile', 'zip_file', t, t1,'文件')  # 创建文件夹
            dummy_path = os.path.join(BASE_DIR, 'static', 'competeRestrictionsFile', 'zip_file', t, t1)  # 创建文件夹
            self.mkdir(dummy_path)
            box = os.path.join(BASE_DIR, 'static', 'competeRestrictionsFile', 'zip_file', t, '压缩文件夹',t1)  # 创建文件夹
            self.mkdir(box)
            zip_path = os.path.join('static', 'competeRestrictionsFile', 'zip_file', t,'压缩文件夹', t1, '竞业下载.zip')  # 压缩后文件存放的路径
            zip_path = zip_path.replace('\\', '/')
            # delete_path=[]
            if downloadAll == True:  # 是下载全部   有条件
                kwargs = {'compete_status': True}
                searchName = self.request.GET.get('searchName',None)
                baseNameId = self.request.GET.get('baseNameId', None)
                deptName = self.request.GET.get("contract", None)
                isExpiration = self.request.GET.get("isExpiration", None)
                beginDate = self.request.GET.get('beginDate', None)
                endDate = self.request.GET.get('endDate',None)
                dept_list = CompeteRestrictionsWhitelist.objects.filter(Q(contract__isnull=False) & ~Q(contract=''),
                                                                        compete_status=True).values(
                    "contract").distinct()
                dept_list = [{"label": i['contract'], "value": i['contract']} for i in dept_list]
                # if jobRankId == '' and beginDate == "" and endDate == "":  # 全查
                #     kwargs['compete_status'] = True
                #     kwargs['people__cr_base__in'] = self.request.user_base
                # if jobRankId != '':
                #     kwargs['people__cr_base'] =jobRankId
                # # if len(baseNameId) == 0 or baseNameId == None:
                # #     kwargs['cr_base__in'] = self.user_base
                # #     # kwargs['jobRank__in'] =[1,2,3,4,5,6,7,8,9,10,11]
                # # else:
                # #     kwargs['cr_base'] = baseNameId
                # # print(kwargs)
                # if beginDate != "" and endDate != "":
                #     kwargs['cycleData__gte'] = datetime(1901, 10, 29, 7, 17, 1,
                #                                         177) if beginDate == None else beginDate
                #     kwargs['cycleData__lte'] = datetime(2521, 10, 29, 7, 17, 1,
                #                                         177) if endDate == None else endDate
                if searchName == '' or searchName == None or len(str(searchName)) == 0 \
                        and baseNameId == '' or baseNameId == None or len(str(baseNameId)) == 0 \
                        and deptName == "" or deptName == None or len(str(deptName)) == 0 \
                        and isExpiration == "" or isExpiration == None or len(str(isExpiration)) == 0\
                        and beginDate == "" or beginDate == None or len(str(beginDate)) == 0\
                        and endDate == "" or endDate == None or len(str(endDate)) == 0:  # 全查
                    kwargs['people__cr_base__in'] = self.request.user_base

                if len(baseNameId) == 0 or baseNameId == None:
                    kwargs['people__cr_base__in'] =self.request.user_base
                else:
                    kwargs['people__cr_base'] = baseNameId

                if deptName is not None and deptName != '':
                    kwargs['people__contract'] = deptName  # 合同归属
                if isExpiration != '':
                    kwargs['people__isExpiration'] = isExpiration  # 是否离职

                if len(str(beginDate))!=0 and len(str(endDate))!=0:
                    from datetime import datetime
                    original_date1 = datetime.strptime(endDate, "%Y-%m-%d")
                    endDate = original_date1.replace(day=1)
                    original_date2 = datetime.strptime(beginDate, "%Y-%m-%d")
                    beginDate = original_date2.replace(day=1)
                    kwargs['cycleData__gte'] =beginDate
                    kwargs['cycleData__lte'] =endDate

                elif beginDate == "" or beginDate is None or len(str(beginDate))==0 and endDate == "" or endDate is None or len(str(endDate))==0:
                    from datetime import datetime
                    kwargs['cycleData__gte'] = datetime(1901, 10, 29, 7, 17, 1,177)
                    kwargs['cycleData__lte'] =datetime(2521, 10, 29, 7, 17, 1,177)
                else:
                    print('日期错误')

                # print(kwargs)
                allList = list(CompeteRestrictions.objects.filter(Q(people__name__contains=searchName) | Q(people__idCard__contains=searchName)|Q(people__workNumber__contains=searchName),
                                                        **kwargs).all().values_list('id', flat=True))

                for id in allList:
                    # print(id)
                    # print(list(CompeteRestrictions.objects.filter(pk=id, compete_status=True,cllBack_file__file_status=True,firstlivevideo_file__file_status=True,secondlivevideo_file__file_status=True).values_list('insured_file',
                    #                                                                                'incomeTax_file',
                    #                                                                                'accumulationFund_file',
                    #                                                                                'workPhotos_file',
                    #                                                                                'workVideo_file',
                    #                                                                                'dailyPhotos_file',
                    #                                                                                'dailyVideo_file',
                    #                                                                                'incumbency_file',
                    #                                                                                'noWork_file',
                    #                                                                                'photograph_file',
                    #                                                                               'cllBack_file',
                    #                                                                               'firstlivevideo_file',
                    #                                                                               'secondlivevideo_file')))

                    fileId_list = list(
                        CompeteRestrictions.objects.filter(id=id, compete_status=True).values_list('insured_file',
                                                                                                   'incomeTax_file',
                                                                                                   'accumulationFund_file',
                                                                                                   'workPhotos_file',
                                                                                                   'workVideo_file',
                                                                                                   'dailyPhotos_file',
                                                                                                   'dailyVideo_file',
                                                                                                   'incumbency_file',
                                                                                                   'noWork_file',
                                                                                                   'photograph_file',
                                                                                                   'cllBack_file','firstlivevideo_file','secondlivevideo_file'))
                    cllBack_file_id = list(
                        CompeteRestrictions.objects.filter(cllBack_file__file_status=True, id=id,
                                                           compete_status=True).values_list('cllBack_file', flat=True))
                    firstlivevideo_file_id = list(
                        CompeteRestrictions.objects.filter(firstlivevideo_file__file_status=True, id=id,
                                                           compete_status=True).values_list('firstlivevideo_file',
                                                                                            flat=True))
                    secondlivevideo_file_id = list(
                        CompeteRestrictions.objects.filter(secondlivevideo_file__file_status=True, id=id,
                                                           compete_status=True).values_list('secondlivevideo_file',
                                                                                            flat=True))

                    if len(fileId_list) > 0:
                        fileId_list = list(fileId_list[-1])
                    try:
                        fileId_list.append(cllBack_file_id[0])
                    except:
                        pass
                    try:
                        fileId_list.append(firstlivevideo_file_id[0])
                    except:
                        pass
                    try:
                        fileId_list.append(secondlivevideo_file_id[0])
                    except:
                        pass


                    for i in fileId_list:
                        if len(CompeteRestrictionsFile.objects.filter(id=i, file_status=True).values_list('url',
                                                                                                          flat=True)) != 0:
                            file_path = CompeteRestrictionsFile.objects.filter(id=i, file_status=True).values_list('url',
                                                                                                       flat=True)[0]
                            dls = CompeteRestrictions.objects.filter(id=id, compete_status=True).values('name','idCard','cycleData')[0]
                            fname = dls['name'] + "_" + dls['idCard']
                            dummy_path2 = os.path.join(BASE_DIR, 'static', 'competeRestrictionsFile', 'zip_file', t,
                                                       t1, str(fname), str(dls['cycleData']))  # 创建文件夹
                            self.mkdir(dummy_path2)
                            path = pathlib.Path(file_path)
                            if path.is_file():
                                file_path = file_path
                            else:
                                continue
                            shutil.copy(file_path, dummy_path2)
                        else:
                            pass
                self.folder_to_zip(dummy_path, zip_path)
            else:
                # path_list = []
                for item in id_list:
                    if item['pId']=='':#只有白名单有 没有文件
                        pass
                    else:   #全删后在下载就没有了
                        cllBack_file_id=list(CompeteRestrictions.objects.filter(cllBack_file__file_status=True,id=item['pId'],compete_status=True).values_list('cllBack_file',flat=True))
                        firstlivevideo_file_id = list(CompeteRestrictions.objects.filter(firstlivevideo_file__file_status=True,id=item['pId'],compete_status=True).values_list('firstlivevideo_file', flat=True))
                        secondlivevideo_file_id = list(CompeteRestrictions.objects.filter(secondlivevideo_file__file_status=True,id=item['pId'],compete_status=True).values_list('secondlivevideo_file', flat=True))

                        # fileId_list=list(CompeteRestrictions.objects.filter(Q(cllBack_file__file_status=True)|Q(cllBack_file__file_status__isnull=True),Q(firstlivevideo_file__file_status=True)|Q(firstlivevideo_file__file_status__isnull=True),Q(secondlivevideo_file__file_status=True)|Q(secondlivevideo_file__file_status__isnull=True),id=item['pId'], compete_status=True).values_list('insured_file','incomeTax_file','accumulationFund_file','workPhotos_file','workVideo_file','dailyPhotos_file','dailyVideo_file','incumbency_file','noWork_file','photograph_file','cllBack_file','firstlivevideo_file','secondlivevideo_file'))
                        fileId_list = list(CompeteRestrictions.objects.filter(
                            id=item['pId'],
                            compete_status=True).values_list('insured_file', 'incomeTax_file', 'accumulationFund_file',
                                                             'workPhotos_file', 'workVideo_file', 'dailyPhotos_file',
                                                             'dailyVideo_file', 'incumbency_file', 'noWork_file',
                                                             'photograph_file'))
                        # print('fileId_list',fileId_list)   #[(640, 642, 643, None, None, 645, 644, None, 646, 641)]
                        if len(fileId_list) > 0:
                            fileId_list = list(fileId_list[-1])
                        try:
                            fileId_list.append(cllBack_file_id[0])
                        except:
                            pass
                        try:
                            fileId_list.append(firstlivevideo_file_id[0])
                        except:
                            pass
                        try:
                            fileId_list.append(secondlivevideo_file_id[0])
                        except:
                            pass
                        for i in fileId_list:
                            if len(CompeteRestrictionsFile.objects.filter(id=i,file_status=True).values_list('url',flat=True))!=0:
                                file_path=CompeteRestrictionsFile.objects.filter(id=i,file_status=True).values_list('url',flat=True)[0]
                                # print(file_path)
                                dls=CompeteRestrictions.objects.filter(id=item['pId'], compete_status=True).values('name','idCard','cycleData')[0]
                                fname=dls['name']+"_"+dls['idCard']
                                dummy_path2 = os.path.join(BASE_DIR, 'static', 'competeRestrictionsFile', 'zip_file', t,
                                                          t1,str(fname),str(dls['cycleData']))  # 创建文件夹
                                self.mkdir(dummy_path2)
                                path=pathlib.Path(file_path)
                                # print(path)
                                if path.is_file():
                                    file_path=file_path
                                else:
                                    # print("continue:",file_path)
                                    continue
                                # delete_path.append(os.path.join(BASE_DIR, 'static', 'competeRestrictionsFile', 'zip_file', t,t1,str(fname)))
                                # delete_path.append(fname)
                                # path = pathlib.Path(file_path)
                                # if path.is_file():
                                #     file_path=file_path
                                # else:
                                #     continue
                                # print(file_path)
                                shutil.copy(file_path,dummy_path2)
                            else:
                                pass

                    self.folder_to_zip(dummy_path, zip_path)

            # path = pathlib.Path(zip_path)
            # print('1',path,path.is_file())
            # if path.is_file():
            self.return_data = {
                "code": status.HTTP_200_OK,
                "msg": '下载成功！',
                'downloadUrl': zip_path
            }
            # print(self.return_data)
            shutil.rmtree(dummy_path)


            # for path in delete_path:
            #     # print(path)
            #     shutil.rmtree(os.path.join(BASE_DIR, 'static', 'competeRestrictionsFile', 'zip_file', t,'1688012926.8668625',str(path)))

        else:
            self.return_data = {
                "code": HTTP_403_FORBIDDEN,
                "msg": "没有权限访问"
            }



    def mkdir(self, path):
        folder = os.path.exists(path)
        # 判断是否存在文件夹如果不存在则创建为文件夹
        if not folder:
            # os.makedirs 传入一个path路径，生成一个递归的文件夹；如果文件夹存在，就会报错,因此创建文件夹之前，需要使用os.path.exists(path)函数判断文件夹是否存在；
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            # print('文件夹创建成功：', path)
        else:
            pass
            # print('文件夹已经存在：', path)



    # 定义压缩文件夹的方法
    def folder_to_zip(self, folderpath, zipath):
        """
        folderpath : 待压缩文件夹的路径
        zipath     ：压缩后文件存放的路径
        """

        zip = zipfile.ZipFile(zipath, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(folderpath):
            # 将待压缩文件夹下的所有文件逐一添加到压缩文件
            fpath = path.replace(os.path.dirname(folderpath), '')
            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath, filename))

        zip.close()



        # old_path = r'F:\1'  # 要复制的文件所在目录
        # new_path = r'F:\2'  # 新路径

    def FindFile(self,path,new_path):   #把一个文件夹内(包含子文件夹)的所有文件复制到另一个文件夹下
        for ipath in os.listdir(path):
            fulldir = os.path.join(path, ipath)  # 拼接成绝对路径
            # print(fulldir)  # 打印相关后缀的文件路径及名称
            if os.path.isfile(fulldir):  # 文件，匹配->打印
                shutil.copy(fulldir, new_path)
            if os.path.isdir(fulldir):  # 目录，递归
                self.FindFile(fulldir)

    def createPath(self, pic,path,fileName):  # 生成路径     文件对象  文件上一级目录名称 文件名称
        t = time.strftime('%Y-%m-%d')
        file_suffix = str(pic).split(".")[-1]  #文件后缀

        file_name = f"{fileName}.{file_suffix}"    #文件名称

        file_path = os.path.join('static', 'competeRestrictionsFile', 'upload_file', t,path,file_name)  # 文件路径
        file_path = file_path.replace('\\', '/')
        return (file_path,file_name,file_suffix)  # 文件路径   文件名字  文件后缀

    def saveFile(self,file_path,file_obj):  # 文件名,图像对象   文件保存
        with open(str(file_path),'wb+') as f:
            for dot in file_obj.chunks():
                f.write(dot)

    def zip_files(self,*files_i: list, file_o: str) -> None:
        with ZipFile(file_o, 'w') as z:
            for i in files_i:
                for f in i:
                    z.write(f, arcname=(n := os.path.basename(f)))
                    # print('zip_files:', n)
    def get_first_last(self, date):
        import calendar
        import datetime
        year, month = int(date.year), int(date.month)
        weekDay, monthCountDay = calendar.monthrange(year, month)
        first_day = datetime.date(year, month, 1)
        #
        # range_day = str(datetime.date(year, month, day=1)) + "至" + str(datetime.date(year, month, day=monthCountDay))
        first_month = datetime.date(year, month, day=1)
        last_month = datetime.date(year, month, day=monthCountDay)
        first_year = datetime.date(year, 1, 1)
        last_year = datetime.date(year, 12, 31)
        return first_month, last_month, first_year, last_year,first_day

    def judgeDate(self,date,beginDate,endDate):
        if type(beginDate) == str:
            beginDate =datetime.strptime(beginDate, '%Y-%m-%d')
        if type(endDate)==str:
            endDate=datetime.strptime(endDate, '%Y-%m-%d')
        if type(date)==str:
            date=datetime.strptime(date, '%Y-%m-%d').date()
        if beginDate <= date <= endDate:
            return True
        else:
            return False

    def is_valid_id_card(self,id_card):
        pattern = r'^[1-9]\d{5}(?:18|19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[1-2]\d|3[0-1])\d{3}[0-9Xx]$'
        return re.match(pattern, id_card) is not None
    def convert_to_last_day(self,date_str):
        year = int(date_str[:4])
        month = int(date_str[-2:])
        num_days = calendar.monthrange(year, month)[1]
        last_day = date(year, month, num_days)
        return last_day.strftime("%Y-%m-%d")

    # def is_year_month_in_range(self,year_month, start_date, end_date):
    #     # print(year_month,start_date,end_date,type(start_date))
    #     year_month_date = datetime.strptime(year_month, "%Y-%m")
    #     # start_date = datetime.strptime(start_date, "%Y-%m-%d")
    #     # end_date = datetime.strptime(end_date, "%Y-%m-%d")
    #
    #     if start_date.year <= year_month_date.year <= end_date.year:
    #         if start_date.month <= year_month_date.month <= end_date.month:
    #             return True
    #     return False


    def is_year_month_in_range(self, year_month, start_date, end_date):
        if type(start_date) != str:
            start_date = datetime.strptime(str(start_date)[:7], "%Y-%m")
        else:
            start_date = datetime.strptime(start_date[:7], "%Y-%m")
        if type(end_date) != str:
            end_date = datetime.strptime(str(end_date)[:7], "%Y-%m")
        else:
            end_date = datetime.strptime(end_date[:7], "%Y-%m")
        year_month = datetime.strptime(year_month[:7], "%Y-%m")
        if start_date <= year_month <= end_date:
            return True
        return False
