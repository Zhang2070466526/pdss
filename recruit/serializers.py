# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 15:42
# @Author  : zhuang
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers
from .models import *
from general.models import center_base


class RecruitDlGetSerializers(serializers.ModelSerializer):
    base_father = serializers.SerializerMethodField()
    recruit_dl_base = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    # modify_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    recruit_dl_base_id = serializers.SerializerMethodField()
    recruit_dl_completion_rate = serializers.SerializerMethodField()
    recruit_dl_self_rate = serializers.SerializerMethodField()
    recruit_dl_date = serializers.DateField(format='%Y-%m')

    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.recruit_dl_base.base_parent_id).values()[0]['name']
        except:
            p = obj.recruit_dl_base.name
        return p

    def get_recruit_dl_base_id(self, obj):
        return obj.recruit_dl_base_id

    def get_recruit_dl_self_rate(self, obj):
        if obj.recruit_dl_self_rate is not None:
            return f'{obj.recruit_dl_self_rate * 100:.0f}%'
        return obj.recruit_dl_self_rate

    def get_recruit_dl_completion_rate(self, obj):
        if obj.recruit_dl_completion_rate is not None:
            return f'{obj.recruit_dl_completion_rate * 100:.0f}%'
        return obj.recruit_dl_completion_rate

    class Meta:
        model = RecruitDl
        # fields = "__all__"
        exclude = ["create_time", "modify_time", "creator", "modifier", "recruit_dl_status"]


class RecruitDlPutSerializers(serializers.ModelSerializer):
    recruit_dl_base_father = serializers.SerializerMethodField()
    recruit_dl_base = serializers.SerializerMethodField()
    recruit_dl_completion_rate = serializers.SerializerMethodField()
    recruit_dl_self_rate = serializers.SerializerMethodField()
    recruit_dl_date = serializers.DateField(format='%Y-%m')

    def get_recruit_dl_base_id(self, obj):
        return obj.recruit_dl_base_id

    def get_recruit_dl_self_rate(self, obj):
        if obj.recruit_dl_self_rate is not None:
            return f'{obj.recruit_dl_self_rate * 100:.0f}%'
        return obj.recruit_dl_self_rate

    def get_recruit_dl_completion_rate(self, obj):
        if obj.recruit_dl_completion_rate is not None:
            return f'{obj.recruit_dl_completion_rate * 100:.0f}%'
        return obj.recruit_dl_completion_rate

    def get_recruit_dl_base(self, obj):
        p = obj.recruit_dl_base.name
        return p

    def get_recruit_dl_base_father(self, obj):
        try:
            p = center_base.objects.get(pk=obj.recruit_dl_base.base_parent_id).name
        except:
            p = obj.recruit_dl_base.name
        return p

    class Meta:
        model = RecruitDl
        exclude = ["create_time", "modify_time", "creator", "modifier", "recruit_dl_status", "id"]


class RecruitDlDownloadSerializers(serializers.ModelSerializer):
    recruit_dl_base = serializers.SerializerMethodField()
    recruit_dl_completion_rate = serializers.SerializerMethodField()
    recruit_dl_self_rate = serializers.SerializerMethodField()

    def get_recruit_dl_base(self, obj):
        p = center_base.objects.filter(pk=obj['recruit_dl_base']).values("name")[0]["name"].split('-')[-1]
        return p

    def get_recruit_dl_completion_rate(self, obj):
        if obj['recruit_dl_demand_no']!=0:
            p = (obj['recruit_dl_entry_no'] + obj["recruit_dl_to_entry_no"]) / obj['recruit_dl_demand_no']
        else:
            p = 0
        p_percentage = p * 100
        p_formatted = '{:.0f}%'.format(p_percentage)
        return p_formatted

    def get_recruit_dl_self_rate(self, obj):
        if obj['recruit_dl_entry_no'] != 0:
            p = obj['recruit_dl_confess_no'] / obj['recruit_dl_entry_no']
        else:
            p = 0
        p_percentage = p * 100
        p_formatted = '{:.0f}%'.format(p_percentage)
        return p_formatted

    class Meta:
        model = RecruitDl
        exclude = ["create_time", "modify_time", "creator", "modifier", "recruit_dl_status", "id"]


class RecruitIdlGetSerializers(serializers.ModelSerializer):
    base_father = serializers.SerializerMethodField()
    recruit_idl_base = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    # modify_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    recruit_idl_base_id = serializers.SerializerMethodField()
    recruit_idl_completion_rate = serializers.SerializerMethodField()
    recruit_idl_date = serializers.DateField(format='%Y-%m')

    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.recruit_idl_base.base_parent_id).values()[0]['name']
        except:
            p = obj.recruit_idl_base.name
        return p

    def get_recruit_idl_base_id(self, obj):
        return obj.recruit_idl_base_id

    def get_recruit_idl_completion_rate(self, obj):
        if obj.recruit_idl_completion_rate is not None:
            return f'{obj.recruit_idl_completion_rate * 100:.0f}%'
        return obj.recruit_idl_completion_rate

    class Meta:
        model = RecruitIdl
        exclude = ["create_time", "modify_time", "creator", "modifier", "recruit_idl_status"]


class RecruitIdlPutSerializers(serializers.ModelSerializer):
    recruit_idl_base_father = serializers.SerializerMethodField()
    recruit_idl_base = serializers.SerializerMethodField()
    recruit_idl_completion_rate = serializers.SerializerMethodField()
    recruit_idl_date = serializers.DateField(format='%Y-%m')

    def get_recruit_idl_base_id(self, obj):
        return obj.recruit_idl_base_id

    def get_recruit_idl_completion_rate(self, obj):
        if obj.recruit_idl_completion_rate is not None:
            return f'{obj.recruit_idl_completion_rate * 100:.0f}%'
        return obj.recruit_idl_completion_rate

    def get_recruit_idl_base(self, obj):
        p = obj.recruit_idl_base.name
        return p

    def get_recruit_idl_base_father(self, obj):

        try:
            p = center_base.objects.get(pk=obj.recruit_idl_base.base_parent_id).name
        except:
            p = obj.recruit_idl_base.name
        return p

    class Meta:
        model = RecruitIdl
        exclude = ["create_time", "modify_time", "creator", "modifier", "recruit_idl_status"]


class RecruitIdlDownloadSerializers(serializers.ModelSerializer):
    recruit_idl_base = serializers.SerializerMethodField()
    recruit_idl_completion_rate = serializers.SerializerMethodField()

    def get_recruit_idl_base(self, obj):
        p = center_base.objects.filter(pk=obj['recruit_idl_base']).values("name")[0]["name"].split('-')[-1]
        return p

    def get_recruit_idl_completion_rate(self, obj):
        if obj['recruit_idl_demand_no'] != 0:
            p = (obj['recruit_idl_entry_no'] + obj["recruit_idl_to_entry_no"]) / obj['recruit_idl_demand_no']
        else:
            p = 0
        p_percentage = p * 100
        p_formatted = '{:.0f}%'.format(p_percentage)
        return p_formatted

    class Meta:
        model = RecruitIdl
        exclude = ["create_time", "modify_time", "creator", "modifier", "recruit_idl_status"]


class RecruitSalGetSerializers(serializers.ModelSerializer):
    base_father = serializers.SerializerMethodField()
    recruit_sal_base = serializers.SlugRelatedField(slug_field='name', read_only=True)
    # create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    # modify_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    recruit_sal_base_id = serializers.SerializerMethodField()
    recruit_sal_completion_rate = serializers.SerializerMethodField()
    recruit_sal_date = serializers.DateField(format='%Y-%m')

    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.recruit_sal_base.base_parent_id).values()[0]['name']
        except:
            p = obj.recruit_sal_base.name
        return p

    def get_recruit_sal_base_id(self, obj):
        return obj.recruit_sal_base_id

    def get_recruit_sal_completion_rate(self, obj):
        if obj.recruit_sal_completion_rate is not None:
            return f'{obj.recruit_sal_completion_rate * 100:.0f}%'
        return obj.recruit_sal_completion_rate

    class Meta:
        model = RecruitSal
        exclude = ["create_time", "modify_time", "creator", "modifier", "recruit_sal_status"]


class RecruitSalPutSerializers(serializers.ModelSerializer):
    recruit_sal_base_father = serializers.SerializerMethodField()
    recruit_sal_base = serializers.SerializerMethodField()
    recruit_sal_base_id = serializers.SerializerMethodField()
    recruit_sal_completion_rate = serializers.SerializerMethodField()
    recruit_sal_date = serializers.DateField(format='%Y-%m')

    def get_recruit_sal_base_id(self, obj):
        return obj.recruit_sal_base_id

    def get_recruit_sal_completion_rate(self, obj):
        if obj.recruit_sal_completion_rate is not None:
            return f'{obj.recruit_sal_completion_rate * 100:.0f}%'
        return obj.recruit_sal_completion_rate

    def get_recruit_sal_base(self, obj):
        p = obj.recruit_sal_base.name
        return p

    def get_recruit_sal_base_father(self, obj):
        try:
            p = center_base.objects.get(pk=obj.recruit_sal_base.base_parent_id).name
        except:
            p = obj.recruit_sal_base.name
        return p

    class Meta:
        model = RecruitSal
        fields = "__all__"


class RecruitSalDownloadSerializers(serializers.ModelSerializer):
    recruit_sal_base = serializers.SerializerMethodField()
    recruit_sal_completion_rate = serializers.SerializerMethodField()

    def get_recruit_sal_base(self, obj):
        p = center_base.objects.filter(pk=obj['recruit_sal_base']).values("name")[0]["name"].split('-')[-1]
        return p

    def get_recruit_sal_completion_rate(self, obj):
        if obj['recruit_sal_demand_no'] != 0:
            p = (obj['recruit_sal_entry_no'] + obj["recruit_sal_to_entry_no"]) / obj['recruit_sal_demand_no']
        else:
            p = 0
        p_percentage = p * 100
        p_formatted = '{:.0f}%'.format(p_percentage)
        return p_formatted

    class Meta:
        model = RecruitSal
        exclude = ["create_time", "modify_time", "creator", "modifier", "recruit_sal_status"]
