# -*- coding: utf-8 -*-
# @Time    : 2023/6/9 14:53
# @Author  : zhuang
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers
from .models import *


class SendDepartmentSerializers(serializers.ModelSerializer):
    acceptor_name = serializers.SerializerMethodField()
    dept_acceptor_num = serializers.SerializerMethodField()
    person_list = serializers.SerializerMethodField()

    def get_acceptor_name(self, obj):
        name_list = obj.dept_acceptor.filter(status=1).values("id", "name", "email_address")
        name = ""
        for i in name_list:
            name += i['name'] + ','
        return name[0:-1]

    def get_person_list(self, obj):
        id_list = obj.dept_acceptor.filter(status=1).values("id", "name", "email_address")
        id_list = [{"id": i['id'], "name": i['name'], "email": i['email_address']} for i in id_list]
        return id_list

    def get_dept_acceptor_num(self, obj):
        return obj.dept_acceptor.filter(status=1).count()

    class Meta:
        model = SendDepartment
        fields = ["id", "dept_code", "dept_name", "dept_acceptor", "dept_acceptor_num", "person_list", "dept_id", "acceptor_name"]


class SendAcceptorSerializers(serializers.ModelSerializer):
    week_dept_num = serializers.SerializerMethodField()
    dept_id_list = serializers.SerializerMethodField()

    def get_week_dept_num(self, obj):
        return obj.week_dept.filter().count()

    def get_dept_id_list(self, obj):
        dept_list = [i.dept_id for i in obj.week_dept.filter()]
        return dept_list

    class Meta:
        model = SendAcceptor
        fields = [
            "id",
            "week_dept",
            "name",
            "week_dept_num",
            "email_address",
            "dept_id_list"
        ]
