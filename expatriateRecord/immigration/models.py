from django.db import models


# Create your models here.


# class ImmigrationBase(models.Model):  # 派驻基地表
#     base_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='基地名称')
#     base_status = models.BooleanField(default=True, verbose_name='部门状态')
#     class Meta:
#         managed = True
#         db_table = 'immigration_base'
#         verbose_name_plural = '派驻基地表'
#         verbose_name = '派驻基地表'
#         indexes = [
#             models.Index(fields=['base_name'])
#         ]

class ImmigrationCountry(models.Model):
    country_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='派驻国名称')
    country_status = models.BooleanField(default=True, verbose_name='派驻国状态')

    class Meta:
        managed = True
        db_table = 'immigration_country'
        verbose_name = '派驻国家'
        verbose_name_plural = '派驻国家'
        indexes = [
            models.Index(fields=['country_name'])
        ]


class ImmigrationTripReason(models.Model):  # 出入境行程原因
    reason_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='派驻国名称')
    reason_status = models.BooleanField(default=True, verbose_name='派驻国状态')

    class Meta:
        managed = True
        db_table = 'immigration_trip_reason'
        verbose_name_plural = '出入境原因表'
        verbose_name = '出入境原因表'
        indexes = [
            models.Index(fields=['reason_name'])
        ]


class ImmigrationType(models.Model):  # 出入境状态
    type_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='状态名称')
    type_classify = models.ForeignKey(to=ImmigrationCountry, on_delete=models.DO_NOTHING, db_constraint=False,
                                      null=True, blank=True, verbose_name='派驻国家')
    type_status = models.BooleanField(default=True, verbose_name='状态是否有效')

    class Meta:
        managed = True
        db_table = 'immigration_type'
        verbose_name_plural = '出入境状态表'
        verbose_name = '出入境状态表'
        indexes = [
            models.Index(fields=['type_name'])
        ]


class ImmigrationRecords(models.Model):  # 出入境记录表 签证组填写
    records_people = models.ForeignKey(to='employee.HrEmployee', on_delete=models.DO_NOTHING, db_constraint=False,
                                       null=True, blank=True, verbose_name='员工')
    records_passport = models.CharField(max_length=255, null=True, blank=True, verbose_name='护照号')
    records_stationed_country = models.ForeignKey(to=ImmigrationCountry, on_delete=models.DO_NOTHING,
                                                  db_constraint=False,
                                                  null=True, blank=True, verbose_name='派驻国家')
    records_stationed_base = models.ForeignKey(to='expatriateRecord.ImmigrationBase', on_delete=models.DO_NOTHING,
                                               db_constraint=False,
                                               null=True, blank=True, verbose_name='派驻基地')
    records_begin_data = models.DateField(null=True, blank=True, verbose_name='考勤开始周期')
    records_end_data = models.DateField(null=True, blank=True, verbose_name='考勤结束周期')
    records_work_visa = models.BooleanField(default=False, verbose_name='工作签')
    records_local_bank = models.BooleanField(default=False, verbose_name='本地银行号')
    records_local_social_security = models.BooleanField(default=False, verbose_name='本地社保号')
    records_local_individual_taxes = models.BooleanField(default=False, verbose_name='本地个税号')
    records_leave_hour = models.FloatField(null=True, blank=True, verbose_name='请假小时数')
    records_absenteeism_hour = models.FloatField(null=True, blank=True, verbose_name='旷工小时数')
    # anomalies_approval_status = models.IntegerField(null=True, blank=True,default=1, verbose_name='推送状态')    #1是已经推送 2是未推送   如果是false就发，然后变为true，  或者查找一下该人, 如果没有就发，有就发放
    # records_push_status = models.BooleanField(default=False, verbose_name='推送状态')
    records_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    records_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name='创建者', related_name='records_creator', db_constraint=False)
    records_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name='修改者', related_name='records_modifier', db_constraint=False)
    # records_month = models.DateField(null=True, blank=True, verbose_name='记录月份')
    records_create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    records_modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'immigration_records'
        verbose_name_plural = '出入境记录表'
        verbose_name = '出入境记录表'


# 入泰 填写 入泰日期 行程原因 出入境记录
# 出泰 填写 出泰日期 离泰目的地 离泰天数 行程原因 出入境记录
# 未离泰 填写 出入境记录
class ImmigrationFill(models.Model):  # 出入境填写    员工填写
    fill_record = models.ForeignKey(to=ImmigrationRecords, on_delete=models.DO_NOTHING, db_constraint=False,
                                    null=True, blank=True, verbose_name='填写记录')
    fill_inout_status = models.ForeignKey(to=ImmigrationType, on_delete=models.DO_NOTHING, db_constraint=False,
                                          null=True, blank=True, verbose_name='出入境状态')
    fill_into_date = models.DateTimeField(null=True, blank=True, verbose_name='入境日期')  #入境日期
    fill_leave_date = models.DateTimeField(null=True, blank=True, verbose_name='离境日期')  #离境日期
    fill_trip_reason = models.ForeignKey(to=ImmigrationTripReason, on_delete=models.DO_NOTHING, db_constraint=False,
                                         null=True, blank=True, verbose_name='行程原因')
    fill_leave_address = models.CharField(max_length=255, null=True, blank=True, verbose_name='离境目的地')
    fill_leave_days = models.FloatField(null=True, blank=True, verbose_name='离境天数')
    # fill_leave_hour = models.FloatField(null=True, blank=True, verbose_name='请假小时数')
    # fill_absenteeism_hour = models.FloatField(null=True, blank=True, verbose_name='旷工小时数')
    fill_remark = models.TextField(null=True, blank=True, verbose_name='备注')
    fill_approval_status = models.IntegerField(null=True, blank=True, default=1,
                                               verbose_name='审批状态')  # 1是未审核 2是已审核 3是已驳回
    fill_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    fill_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                     verbose_name='创建者', related_name='fill_creator', db_constraint=False)
    fill_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                      verbose_name='修改者', related_name='fill_modifier', db_constraint=False)
    fill_create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    fill_modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'immigration_fill'
        verbose_name_plural = '出入境记录表'
        verbose_name = '出入境记录表'


class ImmigrationFiles(models.Model):  # 出入境文件
    choices = (
        (1, '附件(出境记录)'),
    )
    type = models.SmallIntegerField(verbose_name='文件类型', choices=choices)
    name = models.CharField(max_length=255, default='', verbose_name='文件名')
    url = models.CharField(max_length=255, default='', verbose_name='文件路径')
    fill_file = models.ForeignKey(to=ImmigrationFill, on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name='员工上传附件', related_name='fill_file', db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    create_user = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='创建者', related_name='create_user', db_constraint=False)
    status = models.BooleanField(default=True, verbose_name='数据是否有效')

    class Meta:
        managed = True
        db_table = 'immigration_files'
        verbose_name_plural = '出入境文件表'
        verbose_name = '出入境文件表'
