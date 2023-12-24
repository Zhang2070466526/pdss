# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 16:46
# @Author  : zhuang
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers

from general.models import center_base
from .models import *


class EmployeeActivitiesListGetSerializers(serializers.ModelSerializer):
    base_father = serializers.SerializerMethodField()
    employee_base = serializers.SlugRelatedField(slug_field='name', read_only=True)
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    modify_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    employee_activities_plans = serializers.SerializerMethodField()
    employee_activities_photos = serializers.SerializerMethodField()
    employee_base_id = serializers.SerializerMethodField()
    employee_activities_plans_info = serializers.SerializerMethodField()
    employee_activities_photos_info = serializers.SerializerMethodField()

    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.employee_base.base_parent_id).values()[0]['name']
        except:
            p = obj.employee_base.name
        return p

    def get_employee_activities_plans(self, obj):
        return obj.employee_activities_plans.filter(status=1).count()

    def get_employee_activities_photos(self, obj):
        return obj.employee_activities_photos.filter(status=1).count()

    def get_employee_base_id(self, obj):
        return obj.employee_base_id

    def get_employee_activities_plans_info(self, obj):
        data = []
        info = obj.employee_activities_plans.filter(status=1).values("id", "file_name", "file_url")
        for i in info:
            p = {
                "id": i['id'],
                "name": i['file_name'],
                "url": i['file_url'],
            }
            data.append(p)
        return data

    def get_employee_activities_photos_info(self, obj):
        data = []
        info = obj.employee_activities_photos.filter(status=1).values("id", "file_name", "file_url")
        for i in info:
            p = {
                "id": i['id'],
                "name": i['file_name'],
                "url": i['file_url'],
            }
            data.append(p)
        return data

    class Meta:
        model = EmployeeActivitiesList
        fields = "__all__"


class EmployeeActivitiesListPutSerializers(serializers.ModelSerializer):
    employee_base_father = serializers.SerializerMethodField()
    employee_base = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    modify_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    employee_activities_plans = serializers.SerializerMethodField()
    employee_activities_photos = serializers.SerializerMethodField()
    employee_base_id = serializers.SerializerMethodField()
    employee_activities_plans_info = serializers.SerializerMethodField()
    employee_activities_photos_info = serializers.SerializerMethodField()

    def get_employee_base(self, obj):
        p = obj.employee_base.name
        return p

    def get_employee_base_father(self, obj):

        try:
            p = center_base.objects.get(pk=obj.employee_base.base_parent_id).name
        except:
            p = obj.employee_base.name
        return p

    def get_employee_activities_plans(self, obj):
        return obj.employee_activities_plans.filter(status=1).count()

    def get_employee_activities_photos(self, obj):
        return obj.employee_activities_photos.filter(status=1).count()

    def get_employee_base_id(self, obj):
        return obj.employee_base_id

    def get_employee_activities_plans_info(self, obj):
        data = []
        info = obj.employee_activities_plans.filter(status=1).values("id", "file_name", "file_url")
        for i in info:
            p = {
                "id": i['id'],
                "name": i['file_name'],
                "url": i['file_url'],
            }
            data.append(p)
        return data

    def get_employee_activities_photos_info(self, obj):
        data = []
        info = obj.employee_activities_photos.filter(status=1).values("id", "file_name", "file_url")
        for i in info:
            p = {
                "id": i['id'],
                "name": i['file_name'],
                "url": i['file_url'],
            }
            data.append(p)
        return data

    class Meta:
        model = EmployeeActivitiesList
        fields = "__all__"
