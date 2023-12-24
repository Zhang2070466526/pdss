
from rest_framework import serializers
from .models import *
from auther.models import AdminUser, UploadFiles
from general.models import *
class EmployeeInspectSerializers(serializers.ModelSerializer):  # 员工稽核
    base_father = serializers.SerializerMethodField()
    employee_inspect_base = serializers.SlugRelatedField(slug_field='name', read_only=True)
    employee_inspect_photos = serializers.SerializerMethodField()
    employee_inspect_plans=serializers.SerializerMethodField()
    class Meta:
        model =EmployeeInspect
        fields = '__all__'
    def get_employee_inspect_photos(self, obj):
        return obj.employee_inspect_photos.filter(status=True).count()
    def get_employee_inspect_plans(self, obj):
        return obj.employee_inspect_plans.filter(status=True).count()
    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.employee_inspect_base.base_parent_id).values()[0]['name']
        except:
            p = obj.employee_inspect_base.name
        return p



