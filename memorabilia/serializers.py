from rest_framework import serializers
from .models import *
from auther.models import AdminUser, UploadFiles
from general.models import *

class MemorabiliaListSerializersForge(serializers.ModelSerializer):  # 僞造
    base_father = serializers.SerializerMethodField()
    memorabilia_base= serializers.SlugRelatedField(slug_field='name', read_only=True)
    memorabilia_plans = serializers.SerializerMethodField()
    memorabilia_photos = serializers.SerializerMethodField()


    class Meta:
        model = MemorabiliaList
        fields = '__all__'

    def get_memorabilia_plans(self, obj):
        return obj.memorabilia_plans.filter(status=True).count()

    def get_memorabilia_photos(self, obj):
        return obj.memorabilia_photos.filter(status=True).count()

    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.memorabilia_base.base_parent_id).values()[0]['name']
        except:
            p = obj.memorabilia_base.name
        return p




class UploadFilesSerializers(serializers.ModelSerializer):
    class Meta:
        model = UploadFiles
        fields = '__all__'


class MemorabiliaListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MemorabiliaList
        fields = '__all__'


class MemorabiliaListSerializersPart(serializers.ModelSerializer):  # 部分
    class Meta:
        model = MemorabiliaList
        # 指定这些字段，除了这些字段其他全部生成
        exclude = ['memorabilia_plans', 'memorabilia_photos']
