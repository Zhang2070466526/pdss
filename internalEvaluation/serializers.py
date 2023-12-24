
from rest_framework import serializers
from .models import *
from auther.models import AdminUser, UploadFiles
from general.models import *
class InternalEvaluationListSerializers(serializers.ModelSerializer):  # 僞造内部评优
    base_father = serializers.SerializerMethodField()
    evaluation_company = serializers.SlugRelatedField(slug_field='name', read_only=True)
    awards_photos = serializers.SerializerMethodField()
    class Meta:
        model = InternalEvaluationList
        fields = '__all__'
    def get_awards_photos(self, obj):
        return obj.awards_photos.filter(status=True).count()

    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.evaluation_company.base_parent_id).values()[0]['name']
        except:
            p = obj.evaluation_company.name
        return p

