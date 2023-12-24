# -*- coding: utf-8 -*-
# @Time    : 2023/5/22 9:13
# @Author  : zhuang
# @Site    : 
# @File    : serializers.py
# @Software: PyCharm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from rest_framework import serializers
from auther.models import AdminUser
from auther.models import AdminNavMenuList
from employee.models import HrJobRank, HrDepartment
from general.models import center_base
from hikCanteen.models import JobRank
from setup.models import *
from volumeContracts.models import *


class AdminUserGetSerializers(serializers.ModelSerializer):
    user_base = serializers.SerializerMethodField()
    user_base_num = serializers.SerializerMethodField(read_only=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    modify_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    is_superuser = serializers.SerializerMethodField(read_only=True)
    # user_jobrank_hik = serializers.SerializerMethodField(read_only=True)
    user_jobrank_employee = serializers.SerializerMethodField(read_only=True)
    user_department_employee = serializers.SerializerMethodField(read_only=True)

    def get_user_base_num(self, obj):
        return obj.user_base.count()

    def get_is_superuser(self, obj):
        return True if obj.is_superuser else False

    def get_user_base(self, obj):
        new_data = []
        userbase = obj.user_base.filter(status=1).values("id")
        userbase = [i["id"] for i in userbase]
        # print(userbase)
        # userbase=[2,8,60]
        for i in userbase:
            judge_obj = center_base.objects.filter(pk=i, base_parent_id=None)
            if judge_obj.exists():
                # print('1')
                j_o = center_base.objects.filter(base_parent_id=i)
                if j_o.exists():
                    # print(i)
                    # pass
                    new_data.append(i)

                else:
                    new_data.append(i)
            else:
                # print(i)
                new_data.append(i)
        # print(new_data)
        return new_data





    # def get_user_jobrank_hik(self, obj):
    #     new_data = []
    #     user_jobrank_hik = obj.user_jobrank_hik.filter(status=1).values("id")
    #     user_jobrank_hik = [i["id"] for i in user_jobrank_hik]
    #     return user_jobrank_hik
    def get_user_jobrank_employee(self, obj):
        new_data = []
        user_jobrank_employee = obj.user_jobrank_employee.filter(job_rank_status=1).values("id")
        user_jobrank_employee = [i["id"] for i in user_jobrank_employee]
        return user_jobrank_employee

    def get_user_department_employee(self, obj):
        new_data = []
        user_department_employee = obj.user_department_employee.filter(department_status=1).values("id")
        user_department_employee = [i["id"] for i in user_department_employee]
        return user_department_employee

    class Meta:
        model = AdminUser
        fields = ["id", "username", "user", "is_superuser", "user_remark", "user_remark", "create_time", "modify_time",
                  "user_base_num", "user_base", "user_menu", "password", "user_jobrank","user_jobrank_employee","user_department_employee"]


class AdminUserAddSerializers(serializers.ModelSerializer):
    user_menu = serializers.PrimaryKeyRelatedField(queryset=AdminNavMenuList.objects.all(), many=True, required=False)
    user_base = serializers.PrimaryKeyRelatedField(queryset=center_base.objects.all(), many=True, required=False)
    user_jobrank = serializers.PrimaryKeyRelatedField(queryset=ContractsJobrank.objects.all(), many=True,
                                                      required=False)
    # user_jobrank_hik = serializers.PrimaryKeyRelatedField(queryset=JobRank.objects.all(), many=True,
    #                                                   required=False)
    user_jobrank_employee = serializers.PrimaryKeyRelatedField(queryset=HrJobRank.objects.all(), many=True, required=False)
    user_department_employee = serializers.PrimaryKeyRelatedField(queryset=HrDepartment.objects.all(), many=True,
                                                               required=False)
    password = serializers.CharField(write_only=True)

    # print(user_menu,user_base,user_Jobrank)

    def create(self, validated_data):
        # print("1", validated_data)
        password = validated_data.pop('password')
        user_base_data = validated_data.pop("user_base")
        user_menu_data = validated_data.pop("user_menu")
        user_jobrank_data = validated_data.pop("user_jobrank")
        validated_data['password'] = make_password(password)
        is_superuser = validated_data.get("is_superuser")
        # jobrank_hik_list = validated_data.pop("user_jobrank_hik")
        jobrank_employee_list = validated_data.pop("user_jobrank_employee")
        department_employee_list = validated_data.pop("user_department_employee")

        if is_superuser:
            base_list = center_base.objects.filter(status=1).values_list("id")
            menu_list = AdminNavMenuList.objects.filter().values_list("id")
            jobrank_list = ContractsJobrank.objects.filter(jobrank_status=1).values_list("id")
            # jobrank_hik_list = JobRank.objects.filter(status=1).values_list("id")
            jobrank_employee_list = HrJobRank.objects.filter(job_rank_status=1).values_list("id")
            department_employee_list = HrDepartment.objects.filter(department_status=1).values_list("id")

            user_base_data = [i[0] for i in base_list]
            user_menu_data = [i[0] for i in menu_list]
            user_jobrank_data = [i[0] for i in jobrank_list]
            # jobrank_hik_list = [i[0] for i in jobrank_hik_list]
            jobrank_employee_list = [i[0] for i in jobrank_employee_list]
            department_employee_list = [i[0] for i in department_employee_list]


        user = AdminUser.objects.create(**validated_data)
        if user_base_data and len(user_base_data) > 0:
            user.user_base.set(user_base_data)
        if user_menu_data and len(user_menu_data) > 0:
            user.user_menu.set(user_menu_data)
        if user_jobrank_data and len(user_jobrank_data) > 0:
            user.user_jobrank.set(user_jobrank_data)
        # if jobrank_hik_list and len(jobrank_hik_list) > 0:
        #     user.user_jobrank_hik.set(jobrank_hik_list)
        if jobrank_employee_list and len(jobrank_employee_list) > 0:
            user.user_jobrank_employee.set(jobrank_employee_list)
        if department_employee_list and len(department_employee_list) > 0:
            user.user_department_employee.set(department_employee_list)
        return user

    def update(self, instance, validated_data):
        # print('修改', instance, validated_data)
        user_base_data = validated_data.pop("user_base")
        user_menu_data = validated_data.pop("user_menu")
        user_jobrank_data = validated_data.pop("user_jobrank")
        # user_jobrank_hik_data = validated_data.pop("user_jobrank_hik")
        user_jobrank_employee_data = validated_data.pop("user_jobrank_employee")
        user_department_employee_data = validated_data.pop("user_department_employee")
        instance.username = validated_data.get('username', instance.username)
        instance.user = validated_data.get('user', instance.user)
        instance.user_remark = validated_data.get('user_remark', None)
        instance.is_superuser = validated_data.get('is_superuser', None)
        if instance.password == validated_data.get("password"):
            pass
        else:
            instance.password = make_password(validated_data.get("password"))
        # print('修改',instance,validated_data)

        instance.save()

        if validated_data.get("is_superuser"):
            base_list = center_base.objects.filter(status=1).values_list("id")
            menu_list = AdminNavMenuList.objects.filter().values_list("id")
            jobrank_list = ContractsJobrank.objects.filter(jobrank_status=1).values_list("id")
            # jobrank_hik_list =JobRank.objects.filter(status=1).values_list("id")
            jobrank_employee_list = HrJobRank.objects.filter(job_rank_status=1).values_list("id")
            department_employee_list = HrDepartment.objects.filter(department_status=1).values_list("id")
            user_base_data = [i[0] for i in base_list]
            user_menu_data = [i[0] for i in menu_list]
            user_jobrank_data = [i[0] for i in jobrank_list]
            # user_jobrank_hik_data = [i[0] for i in jobrank_hik_list]
            user_jobrank_employee_data=[i[0] for i in jobrank_employee_list]
            user_department_employee_data = [i[0] for i in department_employee_list]
            instance.user_base.set(user_base_data)
            instance.user_menu.set(user_menu_data)
            instance.user_jobrank.set(user_jobrank_data)
            # for i in user_jobrank_hik_data:
            #     instance.user_jobrank_hik.add(i)
            for i in user_jobrank_employee_data:
                instance.user_jobrank_employee.add(i)
            for i in user_department_employee_data:
                instance.user_department_employee.add(i)
        else:
            instance.user_base.set(user_base_data)
            instance.user_menu.set(user_menu_data)

            instance.user_jobrank.set(user_jobrank_data)

            # user_jobrank_hik_data = [i.id for i in user_jobrank_hik_data]
            # instance.user_jobrank_hik.set(user_jobrank_hik_data)
            user_jobrank_employee_data = [i.id for i in user_jobrank_employee_data]
            instance.user_jobrank_employee.set(user_jobrank_employee_data)
            user_department_employee_data = [i.id for i in user_department_employee_data]
            instance.user_department_employee.set(user_department_employee_data)
        return instance

    class Meta:
        model = AdminUser
        fields = "__all__"


class PicManageviewsSerializers(serializers.ModelSerializer):  # 图片管理
    class Meta:
        model = PicManage
        # fields = '__all__'
        fields = ['id', 'name', 'url']


class BaseManageviewsSerializers(serializers.ModelSerializer):  # 基地管理
    base_parent_id = serializers.SerializerMethodField()

    def get_base_parent_id(self, obj):
        p = center_base.objects.filter(pk=obj.base_parent_id)
        if p.count() > 0:
            p = p[0].name
        else:
            p = ""
        return p

    class Meta:
        model = center_base
        fields = '__all__'
        # fields = ['id','name', 'url']
