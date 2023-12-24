from django.db import models

# import employee.models


# Create your models here.
class IeProposalType(models.Model):
    ie_proposal_type_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='提案类型名称')
    ie_proposal_type_status = models.BooleanField(default=True, verbose_name='提案类型状态')

    class Meta:
        managed = True
        db_table = 'ie_proposal_type'
        verbose_name_plural = '提案类型'
        verbose_name = '提案类型'


# class IeProposalRecord(models.Model):
#     ie_proposal_employee = models.ForeignKey(to=employee.models.HrEmployee, on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True,
#                                              verbose_name='提案人')
#     ie_proposal_type = models.ForeignKey(to=IeProposalType, on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True,
#                                          verbose_name='提案类型')  #
#     ie_process_id=models.CharField(max_length=255, null=True, blank=True, verbose_name='单据流程id')
#     ie_proposal_feedback_on_workshop_issues = models.TextField(null=True, blank=True, verbose_name='车间异常问题反馈')#
#     ie_proposal_sane_proposal = models.TextField(null=True, blank=True, verbose_name='合理化建议')
#     ie_proposal_create_time = models.DateTimeField(auto_now=True, verbose_name='提案时间')#
#     ie_proposal_superior_examine_time = models.DateTimeField(null=True, blank=True, verbose_name='直接上级审批时间')
#     ie_proposal_ie_examine_time = models.DateTimeField(null=True, blank=True, verbose_name='IE审批时间')
#     ie_proposal_ie_superior_examine_time = models.DateTimeField(null=True, blank=True, verbose_name='IE主管审批时间')
#     ie_proposal_effect_department = models.CharField(max_length=255, null=True, blank=True, verbose_name='实施部门')
#     ie_proposal_effect_head = models.CharField(max_length=255, null=True, blank=True, verbose_name='实施负责人')
#
#     ie_proposal_feasibility_assessment = models.CharField(max_length=255, null=True, blank=True, verbose_name='实施可行性评估')
#     ie_proposal_reason = models.CharField(max_length=255, null=True, blank=True,verbose_name='原因说明')
#     ie_proposal_accept = models.BooleanField(default=False, null=True, blank=True, verbose_name='是否验收')
#
#     ie_proposal_effect_superior_examine_time = models.DateTimeField(null=True, blank=True, verbose_name='实施单位主管审批时间')
#     ie_proposal_expected_start_time = models.DateTimeField(null=True, blank=True, verbose_name='预计开始时间')
#     ie_proposal_expected_end_time = models.DateTimeField(null=True, blank=True, verbose_name='预计结束时间')
#     ie_proposal_ie_confirm_examine_time = models.DateTimeField(null=True, blank=True, verbose_name='IE效果确认审核时间')
#     ie_proposal_reality_start_time = models.DateTimeField(null=True, blank=True, verbose_name='实际开始时间')
#     ie_proposal_reality_end_time = models.DateTimeField(null=True, blank=True, verbose_name='实际结束时间')
#
#     class Meta:
#         managed = True
#         db_table = 'ie_proposal_record'
#         verbose_name_plural = 'IE提案记录表'
#         verbose_name = 'IE提案记录表'
#

class IeProposalFile(models.Model):
    # ie_proposal_employee = models.ForeignKey(to=IeProposalRecord, on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True,
    #                                          verbose_name='提案')
    ie_proposal_employee_id = models.CharField(max_length=255, null=True, blank=True, verbose_name='单据流程id')
    ie_proposal_file_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='附件名称')
    ie_proposal_file_url = models.CharField(max_length=255, null=True, blank=True, verbose_name='附件url')
    ie_proposal_type = models.CharField(max_length=2, null=True, blank=True, choices=(('1', '问题照片'), ('2', '实施完成照片')), verbose_name='附件类型')
    ie_proposal_file_create_time = models.DateTimeField(auto_now=True, verbose_name='文件创建时间')

    class Meta:
        managed = True
        db_table = 'ie_proposal_file'
        verbose_name_plural = 'IE提案相关文件'
        verbose_name = 'IE提案相关文件'
