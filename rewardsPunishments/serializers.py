
from rest_framework import serializers
from .models import *
from auther.models import AdminUser, UploadFiles
from general.models import *
class ProjectBonusSerializers(serializers.ModelSerializer):  # 項目獎金
    base_father = serializers.SerializerMethodField()
    project_bonus_base = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = ProjectBonus
        fields = '__all__'
    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.project_bonus_base.base_parent_id).values()[0]['name']
        except:
            p = obj.project_bonus_base.name
        return p


class RewardsAndPunishmentsSerializers(serializers.ModelSerializer):  # 奖惩
    base_father = serializers.SerializerMethodField()
    r_p_base = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = RewardsAndPunishments
        fields = '__all__'
    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.r_p_base.base_parent_id).values()[0]['name']
        except:
            p = obj.r_p_base.name
        return p
