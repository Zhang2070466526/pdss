from rest_framework import serializers
from .models import *
from auther.models import AdminUser, UploadFiles

class ContractsInfoSerializers(serializers.ModelSerializer):  # 批量合同
    gender= serializers.SerializerMethodField(read_only=True)
    nativePlaceId = serializers.SerializerMethodField(read_only=True)
    politicsStatus = serializers.SerializerMethodField(read_only=True)
    accountNature= serializers.SerializerMethodField(read_only=True)
    nationId = serializers.SerializerMethodField(read_only=True)
    marriage = serializers.SerializerMethodField(read_only=True)
    urgentRelation= serializers.SerializerMethodField(read_only=True)
    latestDegreeId= serializers.SerializerMethodField(read_only=True)
    educateMethod= serializers.SerializerMethodField(read_only=True)
    summerSize = serializers.SerializerMethodField(read_only=True)
    jobRank= serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ContractsInfo
        fields = '__all__'
        # exclude = ['pic_file']
    def get_gender(self,obj):
        return obj.get_gender_display()
    def get_nativePlaceId(self,obj):
        return obj.get_nativePlaceId_display()
    def get_politicsStatus(self,obj):
        return obj.get_politicsStatus_display()
    def get_accountNature(self,obj):
        return obj.get_accountNature_display()
    def get_nationId(self,obj):
        return obj.get_nationId_display()
    def get_marriage(self,obj):
        return obj.get_marriage_display()
    def get_urgentRelation(self,obj):
        return obj.get_urgentRelation_display()
    def get_latestDegreeId(self,obj):
        return obj.get_latestDegreeId_display()
    def get_educateMethod(self,obj):
        return obj.get_educateMethod_display()
    def get_summerSize(self,obj):
        return obj.get_summerSize_display()
    def get_jobRank(self,obj):
        return obj.get_jobRank_display()




