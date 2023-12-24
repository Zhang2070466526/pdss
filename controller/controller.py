# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 13:55
# @Author  : zhuang
# @Site    : 
# @File    : controller.py
# @Software: PyCharm
import json
import os
import datetime
import time
from django.db import connection
from datetime import datetime
from rest_framework.response import Response

from auther.models import *
from externalHonors.models import *
from pdss.settings import BASE_DIR
from salarySurvey.models import *
from salarySurvey.serializers import *
from externalHonors.serializers import *
from rest_framework import status
from auther.models import *
from general.models import *
from employeeActivities.serializers import *
from recruit.serializers import *
from django.db.models import Q
from utils.check_token import CheckToken


def upload_file(file, model_file, method, fileName):
    searchTime = datetime.now().strftime("%Y-%m-%d")
    flag = 1
    if fileName == "" or fileName is None:
        flag = 0
        fileName = searchTime + "_" + "".join(list(str(time.time()))[0:10]) + "_" + file.name
    try:
        if not os.path.exists(os.path.join(os.path.join(BASE_DIR, 'static'), model_file)):
            os.mkdir(os.path.join(os.path.join(BASE_DIR, 'static'), model_file))
        if not os.path.exists(os.path.join(os.path.join(os.path.join(BASE_DIR, 'static'), model_file), method)):
            os.mkdir(os.path.join(os.path.join(os.path.join(BASE_DIR, 'static'), model_file), method))
        dirname = os.path.join(os.path.join(os.path.join(BASE_DIR, 'static'), model_file), method)
        if not os.path.exists(os.path.join(dirname, searchTime)):
            os.mkdir(os.path.join(dirname, searchTime))
        else:
            pass
        fp = open(os.path.join(os.path.join(dirname, searchTime), fileName), 'wb+')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
        if flag == 1:
            return fileName
        if flag == 0:
            return os.path.join(os.path.join(dirname, searchTime), fileName)
    except:
        pass
    return 0


def verify(request):
    return_data = {'code': '', "msg": ''}
    new_token = CheckToken()
    try:
        check_token = new_token.check_token(request.headers['Authorization'])
    except Exception as e:
        # print(e)
        return_data['code'] = 400
        return_data['msg'] = '请求参数出错啦'
        return return_data
    if check_token is None:
        return_data['code'] = 403
        return_data['msg'] = '无权限操作'
        return return_data


class Controller:
    def __init__(self, model, meth, request):
        self.now = None
        self.return_data = {}
        self.model = model
        self.meth = meth
        self.model_name = ''
        self.fileName = ''
        self.request = request
        self.check_token = ""
        self.model_many_obj = ''
        self.user_base = ()
        self.file_path = {
            "salarySurvey": 'salaryFile',
            "SalarySurveyRecord": 'salaryFile',
            "externalHonors": 'externalFile',
            "ExternalHonorsList": 'externalFile',
            "MemorabiliaList": 'memorabiliaFile',
            "EmployeeActivitiesList": 'employeeFile',
            'InternalEvaluationList': 'internalEvaluationFile',
            'EmployeeInspect': 'employeeInspectFile',
            'ProjectBonus': 'projectBonusFile',
            'RewardsAndPunishments': 'rewardsAndPunishmentsFile',
            'TalentSubsidies': 'talentSubsidiesFile',
            'ExitInterviews': 'exitInterviewsFile',
            'Colloquium': 'colloquiumFile',
            'JobInterviews': 'jobInterviewsFile'
        }
        # 允许方法
        self.methods = {
            "patch": self.patch,
            "delete": self.delete,
            "get_list": self.get_list,
            "delete_other_file": self.delete_other_file,
            "upload_other_file": self.upload_other_file,
            "get_upload": self.get_upload,
            "download_file": self.download_file,
        }
        # 接受每个模型的条件查找的字段
        self.model_key = {
            "SalarySurveyRecord": ["searchName", "baseNameId", "beginDate", "endDate"],
            "ExternalHonorsList": ["searchName", "beginDate", "endDate", "baseNameId"],
            "EmployeeActivitiesList": ["searchName", "beginDate", "endDate", "baseNameId"],
            "RecruitDl": ["beginDate", "baseNameId", "endDate", "searchName"],
            "RecruitIdl": ["beginDate", "baseNameId", "endDate", "searchName"],
            "RecruitSal": ["beginDate", "baseNameId", "endDate", "searchName"],
        }
        # 查找条件
        self.model_fields = {
            "ExternalHonorsList": {
                "searchName": "honor_name__contains",
                "beginDate": "honor_date__gte",
                "endDate": "honor_date__lte",
                "baseNameId": "honor_base_id",
                "user_base": "honor_base__in",
            },
            "SalarySurveyRecord": {
                "searchName": "name__contains",
                "beginDate": "period__gte",
                "endDate": "period__lte",
                "baseNameId": "salary_base_id",
                "user_base": "salary_base__in",
            },
            "EmployeeActivitiesList": {
                "searchName": "employee_activities_name__contains",
                "beginDate": "employee_activities_date__gte",
                "endDate": "employee_activities_date__lte",
                "baseNameId": "employee_base_id",
                "user_base": "employee_base__in",
            },
            "RecruitDl": {
                "beginDate": "recruit_dl_date__gte",
                "endDate": "recruit_dl_date__lte",
                "baseNameId": "recruit_dl_base_id",
                "user_base": "recruit_dl_base__in",
                "searchName": "recruit_dl_base__name__contains",
            },
            "RecruitIdl": {
                "beginDate": "recruit_idl_date__gte",
                "endDate": "recruit_idl_date__lte",
                "baseNameId": "recruit_idl_base_id",
                "user_base": "recruit_idl_base__in",
                "searchName": "recruit_idl_base__name__contains",
            },
            "RecruitSal": {
                "beginDate": "recruit_sal_date__gte",
                "endDate": "recruit_sal_date__lte",
                "baseNameId": "recruit_sal_base_id",
                "user_base": "recruit_sal_base__in",
                "searchName": "recruit_sal_base__name__contains",
            },

        }
        # 序列化模型
        self.serializers = {
            "ExternalHonorsList": HonorRecordGetSerializers,
            "SalarySurveyRecord": SalarySurveyRecordGetSerializers,
            "EmployeeActivitiesList": EmployeeActivitiesListGetSerializers,
            "RecruitDl": RecruitDlGetSerializers,
            "RecruitIdl": RecruitIdlGetSerializers,
            "RecruitSal": RecruitSalGetSerializers,
        }
        # 忽略的字段
        self.except_field = ["create_time", "modify_time", "fix_detail_creator", "fix_detail_modifier", "status",
                             "other_file_info", "honor_status", "creator", "modifier", "employee_activities_status",
                             "recruit_dl_status", "recruit_idl_status", "recruit_sal_status"]
        # 每个模型对应的状态字段
        self.model_statues = {
            "ExternalHonorsList": "honor_status",
            "SalarySurveyRecord": "status",
            "EmployeeActivitiesList": "employee_activities_status",
            "RecruitDl": "recruit_dl_status",
            "RecruitIdl": "recruit_idl_status",
            "RecruitSal": "recruit_sal_status",
        }

    # 无返回的执行
    def start(self):
        return_data = ""
        self.model_name = self.model.__name__
        self.check_token = self.request.check_token
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return_data = {'code': '', "msg": ''}
        if self.check_token is None:
            return_data['code'] = 403
            return_data['msg'] = '无权限操作'
            return return_data
        self.user_base = self.request.user_base
        self.methods[self.meth]()

    # 有返回的执行
    def data_start(self):
        return_data = {'code': '', "msg": ''}
        self.check_token = self.request.check_token
        if self.check_token is None:
            return_data['code'] = 403
            return_data['msg'] = '无权限操作'
            return return_data
        self.model_name = self.model.__name__
        self.user_base = self.request.user_base
        self.methods[self.meth]()
        return self.return_data

    def dyj_data_start(self):
        self.check_token = self.request.check_token
        return_data = {'code': '', "msg": ''}
        if self.check_token is None:
            return_data['code'] = 403
            return_data['msg'] = '无权限操作'
            return return_data
        self.user_base = self.request.user_base
        self.model_name = self.model.__name__
        self.methods[self.meth]()
        return Response(self.return_data)

    # 修改单行数据
    def patch(self):
        """
        需要添加修改的内容
        :return:
        """
        info = json.loads(self.request.body)
        pk = info['id']
        # 不修改的数据
        no_patch = ['historical_payslip', 'honor_upload_declare_files', 'honor_medal_photos',
                    "employee_activities_plans",
                    "employee_activities_photos", "employee_activities_plans", "employee_activities_photos"]
        del info['id']
        kwargs = {}
        field_list = []
        info["modifier"] = AdminUser.objects.filter(pk=self.check_token)[0]
        info['fix_detail_modifier'] = AdminUser.objects.filter(pk=self.check_token)[0]
        info['modify_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for i in self.model._meta.get_fields():
            field_list.append(i.name)
        for i in info:
            if i in field_list and i not in no_patch:
                try:
                    if "rate" in i:
                        percentage = float(info[i].strip("%"))
                        info[i] = percentage / 100
                except:
                    pass
                kwargs[i] = info[i]
        if "honor_base" in kwargs:
            kwargs["honor_base"] = info['honor_base_id']
        if "employee_base" in kwargs:
            kwargs["employee_base"] = info['employee_base_id']
        if "recruit_dl_base" in kwargs:
            kwargs["recruit_dl_base"] = info['recruit_dl_base_id']
        if "recruit_idl_base" in kwargs:
            kwargs["recruit_idl_base"] = info['recruit_idl_base_id']
        if "recruit_sal_base" in kwargs:
            kwargs["recruit_sal_base"] = info['recruit_sal_base_id']
        if "salary_base" in kwargs:
            kwargs["salary_base"] = info['salary_base_id']
        if "recruit_idl_date" in kwargs:
            kwargs["recruit_idl_date"] = datetime.strptime(info['recruit_idl_date'][0:7], "%Y-%m")
        if "recruit_dl_date" in kwargs:
            kwargs["recruit_dl_date"] = datetime.strptime(info['recruit_dl_date'][0:7], "%Y-%m")
        if "recruit_sal_date" in kwargs:
            kwargs["recruit_sal_date"] = datetime.strptime(info['recruit_sal_date'][0:7], "%Y-%m")
        try:
            self.model.objects.filter(pk=pk).update(**kwargs)
            self.return_data = {
                "code": 200,
                "msg": '修改成功'
            }
        except:
            self.return_data = {
                "code": 400,
                "msg": '修改失败'
            }

    # 删除选中数据
    def delete(self):
        infos = json.loads(self.request.body)['idList']
        # print(infos)
        kwargs = {
            self.model_statues[self.model_name]: "0"
        }
        for pk in infos:
            self.model.objects.filter(pk=int(pk)).update(**kwargs)
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "删除成功"
        }

    # 删除附件 通用
    def delete_other_file(self):
        file_id = json.loads(self.request.body)['file_id']
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "请求删除的附件为空"
        }
        if file_id != "":
            try:
                UploadFiles.objects.filter(id=file_id).update(status=0)
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

    # get获取数据
    def get_list(self):
        columnList = [{"value": "序号", "label": "index", "width": "60"}, ]
        tableList = []
        count_len = {}

        currentPage = eval(self.request.GET.get("currentPage", None)) if self.request.GET.get("currentPage",
                                                                                              None) != "" else 1
        pageSize = eval(self.request.GET.get("pageSize", None)) if self.request.GET.get("pageSize", None) != "" else 25
        kwargs = {
            self.model_statues[self.model_name]: 1
        }
        model_conditions = self.model_fields[self.model_name]
        get_obj = self.request.GET
        for key, value in get_obj.items():
            if value != "" and key in self.model_key[self.model_name]:
                kwargs[model_conditions[key]] = value
        for key, value in kwargs.items():
            if "period" in key:
                kwargs[key] = datetime.strptime(value, "%Y-%m-%d")
            if "name" in key:
                kwargs[key] = value.strip()
            if "date" in key and len(value) <= 7:
                kwargs[key] = value + "-01"

        # if self.model_name != "SalarySurveyRecord":
        kwargs[model_conditions['user_base']] = self.user_base
        # print(kwargs)
        obj = self.model.objects.filter(**kwargs).order_by("-create_time")
        database_time = time.time()
        serializer_obj = self.serializers[self.model_name](
            instance=obj[(currentPage - 1) * pageSize:currentPage * pageSize],
            many=True).data
        # print("计算tableList花费{0}s".format(time.time() - database_time))
        for field in self.model._meta.get_fields():
            if field.name not in self.except_field:
                if field.verbose_name == "公司":
                    columnList.append({
                        "value": "中心/事业部",
                        "label": "base_father",
                        "width": "180",
                    })
                field_label = {
                    "value": field.verbose_name,
                    "label": field.name,
                    "width": self.count_character(field.verbose_name),
                }
                if "period" in field_label['label']:
                    field_label['width'] = "120"
                columnList.append(field_label)

        for i in serializer_obj:
            for key, value in dict(i).items():
                count_len[key] = self.count_character(value) if key not in count_len or count_len[
                    key] < self.count_character(value) else self.count_character(value)
            tableList.append(dict(i))

        for i, item in enumerate(tableList):
            item["index"] = pageSize * (currentPage - 1) + i + 1
        else:
            pass
        del columnList[1]

        if len(count_len) > 0:
            count_len['index'] = "60"
            for i in columnList:
                i['width'] = max(int(i['width']), int(count_len[i['label'].lower()]))
        for i in columnList:
            i['width'] = 400 if int(i['width']) > 400 else int(i['width'])

        for i in columnList:
            if "honor_remark" in i['label']:
                i['width'] = ""
            if "employee_activities_remark" in i['label']:
                i['width'] = ""
            if "recruit_dl_remark" in i['label']:
                i['width'] = ""
            if "recruit_idl_remark" in i['label']:
                i['width'] = ""
            if "recruit_sal_remark" in i['label']:
                i['width'] = ""

        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "信息返回成功",
            "data": {
                'columnList': columnList,
                'tableList': tableList,
                'totalNumber': obj.count()
            }
        }

    # 附件上传

    def upload_other_file(self):
        user_id = self.request.POST.get('id', None)
        other_files = self.request.FILES.getlist("file", None)
        type_name = self.request.POST.get("type", "None")
        field_name = self.request.POST.get("field", None)
        searchTime = datetime.now().strftime("%Y-%m-%d")
        # print("===================================")

        if other_files and other_files != "":
            name = self.model.objects.filter(id=user_id).values_list()[0][1]
            for other_file in other_files:
                fileName = str(name) + "_" + searchTime + "_" + str(
                    "".join(list(str(time.time()))[0:10])) + "_" + other_file.name
                try:
                    self.fileName = upload_file(other_file, self.file_path[type_name], "other_file", fileName)
                    self.return_data = {
                        "msg": "保存附件成功",
                        "code": status.HTTP_200_OK
                    }
                    # try:
                    file_url = "static/" + self.file_path[type_name] + "/other_file/" + searchTime + "/" + fileName
                    file_name = fileName
                    file_kwargs = {
                        "file_url": file_url,
                        "file_name": file_name,
                    }
                    try:
                        obj = UploadFiles.objects.create(**file_kwargs)
                        self.return_data['data'] = {
                            "id": obj.id,
                            "name": obj.file_name,
                            "url": obj.file_url,
                        }
                        self.model_many_obj = {
                            "SalarySurveyRecord": {"historical_payslip": obj.historical_payslip},
                            "ExternalHonorsList": {
                                "honor_upload_declare_files": obj.honor_upload_declare_files,
                                "honor_medal_photos": obj.honor_medal_photos
                            }, "EmployeeActivitiesList": {
                                "employee_activities_plans": obj.employee_activities_plans,
                                "employee_activities_photos": obj.employee_activities_photos
                            },
                            "MemorabiliaList": {
                                "memorabilia_plans": obj.memorabilia_plans,
                                "memorabilia_photos": obj.memorabilia_photos

                            },
                            "InternalEvaluationList": {
                                "awards_photos": obj.awards_photos,
                            },
                            'EmployeeInspect': {
                                'employee_inspect_plans': obj.employee_inspect_plans,
                                'employee_inspect_photos': obj.employee_inspect_photos
                            },
                            'Colloquium': {
                                'colloquium_photos': obj.colloquium_photos
                            }
                        }
                        obj = self.model.objects.filter(pk=user_id)[0]
                        if field_name is None or field_name == "":
                            field_name = list(self.model_many_obj[self.model_name].keys())[0]
                        self.model_many_obj[self.model_name][field_name].add(obj.id)
                    except Exception as e:
                        self.return_data = {
                            "msg": "附件信息存储失败,格式可能出错啦",
                            "code": status.HTTP_205_RESET_CONTENT
                        }
                        # print(e)

                except Exception as e:
                    # print(e)

                    self.return_data = {
                        "msg": "保存附件错误",
                        "code": status.HTTP_400_BAD_REQUEST
                    }
        else:
            self.return_data = {
                "code": status.HTTP_200_OK,
                "msg": "空文件"
            }
        # print(self.return_data)

    # 统计字符
    def count_character(self, s):
        hanzi = 0
        num = 0
        for i in str(s):
            if u'\u4e00' <= i <= u'\u9fa5':  # \u4E00 ~ \u9FFF  中文字符
                hanzi = hanzi + 1
            else:
                num += 1

        return str(30 * hanzi + 20 * num)

    # 用于改写
    def get_upload(self):
        pass

    # 用于改写
    def download_file(self):
        pass

    def count_excel_save(self, excel_columns):

        len_list = []
        prjTuple = tuple(excel_columns)
        for idx in range(0, len(prjTuple)):
            length2 = 0
            str_list = []
            for cell in prjTuple[idx]:
                if "1" not in str(cell):
                    str_list.append(str(cell.value))
            for elem in str_list:
                elem_split = list(elem)
                length = 0
                for c in elem_split:
                    if ord(c) <= 256:
                        length += 1.5
                    else:
                        length += 2.5
                length2 = max(length, length2)
            len_list.append(length2)
        return len_list
