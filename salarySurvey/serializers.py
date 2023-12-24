# -*- coding: utf-8 -*-
# @Time    : 2023/4/25 16:29
# @Author  : zhuang
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
from django.forms import model_to_dict
from rest_framework import serializers

from general.models import center_base
from .models import *


class SalarySurveyRecordGetSerializers(serializers.ModelSerializer):
    base_father = serializers.SerializerMethodField()
    salary_base = serializers.SlugRelatedField(slug_field="name", read_only=True)
    salary_base_id = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    modify_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    historical_payslip = serializers.SerializerMethodField()
    other_file_info = serializers.SerializerMethodField()

    class Meta:
        model = SalarySurveyRecord
        fields = "__all__"

    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.salary_base.base_parent_id).values()[0]['name']
        except:
            p = obj.salary_base.name
        return p

    def get_salary_base_id(self, obj):
        return obj.salary_base_id

    def get_historical_payslip(self, obj):
        return obj.historical_payslip.filter(status=1).count()

    def get_other_file_info(self, obj):
        data = []
        info = obj.historical_payslip.filter(status=1).values("id", "file_name", "file_url")
        for i in info:
            p = {
                "id": i['id'],
                "name": i['file_name'],
                "url": i['file_url'],
            }
            data.append(p)
        return data


class SalarySurveyRecordPutSerializers(serializers.ModelSerializer):
    salary_base_father = serializers.SerializerMethodField()
    salary_base = serializers.SerializerMethodField()
    salary_base_id = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    modify_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    historical_payslip = serializers.SerializerMethodField()
    other_file_info = serializers.SerializerMethodField()

    class Meta:
        model = SalarySurveyRecord
        fields = "__all__"

    def get_salary_base_father(self, obj):
        try:
            p = center_base.objects.get(pk=obj.salary_base.base_parent_id).name
        except:
            p = obj.salary_base.name
        return p

    def get_salary_base_id(self, obj):
        return obj.salary_base_id

    def get_historical_payslip(self, obj):
        return obj.historical_payslip.filter(status=1).count()

    def get_other_file_info(self, obj):
        data = []
        info = obj.historical_payslip.filter(status=1).values("id", "file_name", "file_url")
        for i in info:
            p = {
                "id": i['id'],
                "name": i['file_name'],
                "url": i['file_url'],
            }
            data.append(p)
        return data

    def get_salary_base(self, obj):

        p = obj.salary_base.name
        return p