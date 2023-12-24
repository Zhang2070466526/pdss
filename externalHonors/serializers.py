# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 11:22
# @Author  : zhuang
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers

from general.models import center_base
from .models import *


class HonorRecordGetSerializers(serializers.ModelSerializer):
    base_father = serializers.SerializerMethodField()
    honor_base = serializers.SlugRelatedField(slug_field='name', read_only=True)
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    modify_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    honor_upload_declare_files = serializers.SerializerMethodField()
    honor_medal_photos = serializers.SerializerMethodField()
    honor_base_id = serializers.SerializerMethodField()
    honor_upload_declare_files_info = serializers.SerializerMethodField()
    honor_medal_photos_files_info = serializers.SerializerMethodField()

    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.honor_base.base_parent_id).values()[0]['name']
        except:
            p = obj.honor_base.name
        return p

    def get_honor_upload_declare_files(self, obj):
        return obj.honor_upload_declare_files.filter(status=1).count()

    def get_honor_medal_photos(self, obj):
        return obj.honor_medal_photos.filter(status=1).count()

    def get_honor_base_id(self, obj):
        return obj.honor_base_id

    def get_honor_upload_declare_files_info(self, obj):
        data = []
        info = obj.honor_upload_declare_files.filter(status=1).values("id", "file_name", "file_url")
        for i in info:
            p = {
                "id": i['id'],
                "name": i['file_name'],
                "url": i['file_url'],
            }
            data.append(p)
        return data

    def get_honor_medal_photos_files_info(self, obj):
        data = []
        info = obj.honor_medal_photos.filter(status=1).values("id", "file_name", "file_url")
        for i in info:
            p = {
                "id": i['id'],
                "name": i['file_name'],
                "url": i['file_url'],
            }
            data.append(p)
        return data

    class Meta:
        model = ExternalHonorsList
        fields = "__all__"


class HonorRecordPutSerializers(serializers.ModelSerializer):
    honor_base_father = serializers.SerializerMethodField()
    honor_base = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    modify_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    honor_upload_declare_files = serializers.SerializerMethodField()
    honor_medal_photos = serializers.SerializerMethodField()
    honor_base_id = serializers.SerializerMethodField()
    honor_upload_declare_files_info = serializers.SerializerMethodField()
    honor_medal_photos_files_info = serializers.SerializerMethodField()
    
    def get_honor_base(self, obj):
        p = obj.honor_base.name
        return p


    def get_honor_base_father(self, obj):
        try:
            p = center_base.objects.get(pk=obj.honor_base.base_parent_id).name
        except:
            p = obj.honor_base.name
        return p
    
    def get_honor_upload_declare_files(self, obj):
        return obj.honor_upload_declare_files.filter(status=1).count()

    def get_honor_medal_photos(self, obj):
        return obj.honor_medal_photos.filter(status=1).count()

    def get_honor_base_id(self, obj):
        return obj.honor_base_id

    def get_honor_upload_declare_files_info(self, obj):
        data = []
        info = obj.honor_upload_declare_files.filter(status=1).values("id", "file_name", "file_url")
        for i in info:
            p = {
                "id": i['id'],
                "name": i['file_name'],
                "url": i['file_url'],
            }
            data.append(p)
        return data

    def get_honor_medal_photos_files_info(self, obj):
        data = []
        info = obj.honor_medal_photos.filter(status=1).values("id", "file_name", "file_url")
        for i in info:
            p = {
                "id": i['id'],
                "name": i['file_name'],
                "url": i['file_url'],
            }
            data.append(p)
        return data

    class Meta:
        model = ExternalHonorsList
        fields = "__all__"