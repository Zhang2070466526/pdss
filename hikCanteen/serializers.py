from rest_framework import serializers
from .models import *
from auther.models import AdminUser, UploadFiles
from general.models import center_base

class MonthmoneyToOAListSerializers(serializers.ModelSerializer):
    # base_father = serializers.SerializerMethodField()
    jobRankCode = serializers.SlugRelatedField(slug_field='JobRankName', read_only=True)

    class Meta:
        model = MonthmoneyToOAList
        fields = '__all__'
        # exclude = ['pic_file']
    # def get_jobRankCode(self,obj):
    #     print(obj.jobRankCode)
        # return obj.jobRankCode
    # def get_base_father(self, obj):
    #     try:
    #         p = center_base.objects.filter(pk=obj.jobRankCode.base_parent_id).values()[0]['name']
    #     except:
    #         p=obj.jobRankCode.name
    #     return p
