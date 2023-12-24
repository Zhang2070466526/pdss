from rest_framework import serializers

from general.models import center_base
from .models import *


class CompeteRestrictionsSerializers2(serializers.ModelSerializer):  # 竞业限制   书
    # jobRank = serializers.SerializerMethodField(read_only=True)
    # jobRank = serializers.SerializerMethodField()  # 合同归属
    insured_file = serializers.SerializerMethodField()  #参保证明
    incomeTax_file = serializers.SerializerMethodField()  # 所得税缴税证明
    accumulationFund_file = serializers.SerializerMethodField()  # 公积金账户信息
    workPhotos_file = serializers.SerializerMethodField()  # 工作照片
    workVideo_file = serializers.SerializerMethodField()  # 工作视频
    dailyPhotos_file = serializers.SerializerMethodField()  # 日常照片
    dailyVideo_file = serializers.SerializerMethodField()  # 日常视频
    incumbency_file = serializers.SerializerMethodField()  # 在职证明
    noWork_file = serializers.SerializerMethodField()  # 无工作承诺函

    class Meta:
        model = CompeteRestrictions
        fields = '__all__'
        # fields=['name','idCard','phone','address','cycleData','cycleBeginData','cycleEndData','compete_remark']
        # exclude = ['insured_file']
    # def get_jobRank(self, obj):
    #     try:
    #         return obj.people.get_jobRank_display()
    #     except:
    #         return

        # return obj.get_jobRank_display()
    def get_insured_file(self, obj):
        return obj.insured_file.filter(file_status=True).count()
    def get_incomeTax_file(self, obj):
        return obj.incomeTax_file.filter(file_status=True).count()
    def get_accumulationFund_file(self, obj):
        return obj.accumulationFund_file.filter(file_status=True).count()
    def get_workPhotos_file(self, obj):
        return obj.workPhotos_file.filter(file_status=True).count()
    def get_workVideo_file(self, obj):
        return obj.workVideo_file.filter(file_status=True).count()
    def get_dailyPhotos_file(self, obj):
        return obj.dailyPhotos_file.filter(file_status=True).count()
    def get_dailyVideo_file(self, obj):
        return obj.dailyVideo_file.filter(file_status=True).count()
    def get_incumbency_file(self, obj):
        return obj.incumbency_file.filter(file_status=True).count()
    def get_noWork_file(self, obj):
        return obj.noWork_file.filter(file_status=True).count()



class CompeteRestrictionSerializers(serializers.ModelSerializer):  # 竞业限制   书
    # jobRank=serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    insured_file = serializers.SerializerMethodField()  # 参保证明
    incomeTax_file = serializers.SerializerMethodField()  # 所得税缴税证明
    accumulationFund_file = serializers.SerializerMethodField()  # 公积金账户信息
    workPhotos_file = serializers.SerializerMethodField()  # 工作照片
    workVideo_file = serializers.SerializerMethodField()  # 工作视频
    dailyPhotos_file = serializers.SerializerMethodField()  # 日常照片
    dailyVideo_file = serializers.SerializerMethodField()  # 日常视频
    incumbency_file = serializers.SerializerMethodField()  # 在职证明
    noWork_file = serializers.SerializerMethodField()  # 无工作承诺函
    photograph_file= serializers.SerializerMethodField()  # 强制拍照

    cllBack_file = serializers.SerializerMethodField()  # 电话回访
    firstlivevideo_file = serializers.SerializerMethodField()  # 实时视频(第一次)
    secondlivevideo_file= serializers.SerializerMethodField()  # 实时视频(第二次)

    # base_father = serializers.SerializerMethodField()
    # cr_base = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = CompeteRestrictions
        fields = '__all__'
    # def get_jobRank(self,obj):
    #     return obj.people.get_jobRank_display()
    # def get_base_father(self, obj):
    #
    #     try:
    #
    #         p = center_base.objects.filter(pk=obj.people.jobRank_base_id).values()[0]['name']   #一级
    #         # print("++++++++++++++++111",p)
    #     except:
    #         # print("++++")
    #         p = obj.people.jobRank_base_id  #二级
    #     print(p)
    #     return p

    # def get_base_father(self, obj):
    #     try:
    #         p = center_base.objects.filter(pk=obj.people.cr_base.base_parent_id).values()[0]['name']
    #     except:
    #         p = obj.people.cr_base.name
    #     print('p',p)
    #     return p

    def get_name(self,obj):
        return obj.people.name
    def get_insured_file(self, obj):
        return obj.insured_file.filter(file_status=True).count()

    def get_incomeTax_file(self, obj):
        return obj.incomeTax_file.filter(file_status=True).count()

    def get_accumulationFund_file(self, obj):
        return obj.accumulationFund_file.filter(file_status=True).count()

    def get_workPhotos_file(self, obj):
        return obj.workPhotos_file.filter(file_status=True).count()

    def get_workVideo_file(self, obj):
        return obj.workVideo_file.filter(file_status=True).count()

    def get_dailyPhotos_file(self, obj):
        return obj.dailyPhotos_file.filter(file_status=True).count()

    def get_dailyVideo_file(self, obj):
        return obj.dailyVideo_file.filter(file_status=True).count()

    def get_incumbency_file(self, obj):
        return obj.incumbency_file.filter(file_status=True).count()

    def get_noWork_file(self, obj):
        return obj.noWork_file.filter(file_status=True).count()
    def get_photograph_file(self, obj):
        return obj.photograph_file.filter(file_status=True).count()

    def get_cllBack_file(self, obj):
        return obj.cllBack_file.filter(file_status=True).count()

    def get_firstlivevideo_file(self, obj):
        return obj.firstlivevideo_file.filter(file_status=True).count()
    def get_secondlivevideo_file(self, obj):
        return obj.secondlivevideo_file.filter(file_status=True).count()


class CompeteRestrictionsWhitelistSerializers(serializers.ModelSerializer):  # 竞业限制白名单
    people = serializers.SerializerMethodField()
    base_father = serializers.SerializerMethodField()
    cr_base = serializers.SlugRelatedField(slug_field='name', read_only=True)
    def get_people(self, competeRestrictionsWhitelist):
        people = competeRestrictionsWhitelist.people.filter(compete_status=True)

        return CompeteRestrictionSerializers(people, many=True).data

    class Meta:
        model = CompeteRestrictionsWhitelist
        fields = '__all__'
        # fields=('id','idCard')
    def get_base_father(self, obj):
        try:
            p = center_base.objects.filter(pk=obj.cr_base.base_parent_id).values()[0]['name']
        except:
            p = obj.cr_base.name
        # print(p)
        return p

#

# class CompeteRestrictionsSerializersList(serializers.ListSerializer):  # 竞业限制   书
#     class Meta:
#         model = CompeteRestrictions
#         fields = '__all__'
#
# class CompeteRestrictionsWhitelistSerializers(serializers.ModelSerializer):#竞业限制白名单表  作者
#     peoples=CompeteRestriction(many=True)
#     jobRank = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = CompeteRestrictionsWhitelist
#         fields = '__all__'
#         list_serializer_class=CompeteRestrictionsSerializersList
#     def get_jobRank(self,obj):
#         print(obj)
#         # return obj.get_jobRank_display()


# class CompeteRestrictionsWhitelistSerializers(serializers.ModelSerializer):#竞业限制白名单表  作者
#     jobRank= serializers.SerializerMethodField(read_only=True)
#     insured_file = serializers.SerializerMethodField()  #参保证明
#     # incomeTax_file = serializers.SerializerMethodField()  # 所得税缴税证明
#     # accumulationFund_file = serializers.SerializerMethodField()  # 公积金账户信息
#     # workPhotos_file = serializers.SerializerMethodField()  # 工作照片
#     # workVideo_file = serializers.SerializerMethodField()  # 工作视频
#     # dailyPhotos_file = serializers.SerializerMethodField()  # 日常照片
#     # dailyVideo_file = serializers.SerializerMethodField()  # 日常视频
#     # incumbency_file = serializers.SerializerMethodField()  # 在职证明
#     # noWork_file = serializers.SerializerMethodField()  # 无工作承诺函
#     class Meta:
#         model = CompeteRestrictionsWhitelist
#         fields = '__all__'
#
#     def get_jobRank(self,obj):
#         return obj.get_jobRank_display()
#     def get_insured_file(self, obj):
#         print("obj",obj)
#         print(obj.people_set.filter())
#         # return obj.insured_file.filter(file_status=True).count()
class CompeteRestrictionsWhitelist2SerializersList(serializers.ListSerializer):  # 竞业限制   书

    class Meta:
        model = CompeteRestrictionsWhitelist
        fields = '__all__'