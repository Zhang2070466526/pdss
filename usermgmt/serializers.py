# -*- coding: utf-8 -*-
# @Time    : 2023/5/22 9:13
# @Author  : zhuang
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from auther.models import AdminUser
from auther.models import AdminNavMenuList


class AdminUserGetSerializers(serializers.ModelSerializer):
    user_base_num = serializers.SerializerMethodField(read_only=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    modify_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    is_superuser = serializers.SerializerMethodField(read_only=True)

    def get_user_base_num(self, obj):
        return obj.user_base.count()

    def get_is_superuser(self, obj):
        return '是' if obj.is_superuser else '否'

    class Meta:
        model = AdminUser
        fields = ["username", "user", "is_superuser","user_remark", "user_remark", "create_time", "modify_time","user_base_num", "user_base", "user_menu", "password"]


class AdminUserAddSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user_base_data = validated_data.pop("user_base")
        user_menu_data = validated_data.pop("user_menu")
        validated_data['password'] = make_password(password)

        user = AdminUser.objects.create(**validated_data)
        if user_base_data:
            user.user_base.set(user_base_data)
        if user_menu_data:
            user.user_menu.set(user_menu_data)
        return user

    def update(self, instance, validated_data):
        user_base_data = validated_data.pop("user_base")
        user_menu_data = validated_data.pop("user_menu")
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', None)
        if instance.password is None:
            instance.password = instance.username
        else:
            instance.password = make_password(instance.password)
        instance.save()

        if user_base_data:
            instance.user_base.set(user_base_data)
        if user_menu_data:
            instance.user_menu.set(user_menu_data)
        return instance

    class Meta:
        model = AdminUser
        fields = "__all__"
