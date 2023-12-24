from rest_framework import serializers
from .models import *
from auther.models import AdminUser, UploadFiles
from general.models import *


class TalentSubsidiesSerializers(serializers.ModelSerializer):  # 人才补贴
    base_father = serializers.SerializerMethodField()
    talent_subsidies_base = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = TalentSubsidies
        fields = '__all__'

    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.talent_subsidies_base.base_parent_id).values()[0]['name']
        except:
            p = obj.talent_subsidies_base.name
        return p


class ExitInterviewsSerializers(serializers.ModelSerializer):  # 离职访谈
    base_father = serializers.SerializerMethodField()
    exit_interviews_base = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = ExitInterviews
        fields = '__all__'

    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.exit_interviews_base.base_parent_id).values()[0]['name']
        except:
            p = obj.exit_interviews_base.name
        return p


class ColloquiumSerializers(serializers.ModelSerializer):  # 座谈会
    base_father = serializers.SerializerMethodField()
    colloquium_base = serializers.SlugRelatedField(slug_field='name', read_only=True)
    colloquium_photos = serializers.SerializerMethodField()

    class Meta:
        model = Colloquium
        fields = '__all__'

    def get_colloquium_photos(self, obj):
        return obj.colloquium_photos.filter(status=True).count()

    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.colloquium_base.base_parent_id).values()[0]['name']
        except:
            p = obj.colloquium_base.name
        return p


class JobInterviewsSerializers(serializers.ModelSerializer):  # 在职访谈
    base_father = serializers.SerializerMethodField()
    job_interviews_base = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = JobInterviews
        fields = '__all__'

    def get_base_father(self, obj):

        try:
            p = center_base.objects.filter(pk=obj.job_interviews_base.base_parent_id).values()[0]['name']
        except:
            p = obj.job_interviews_base.name
        return p
