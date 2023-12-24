from django.db import models


class internLeaveInfo(models.Model):
    intern_leave_center_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True,
                                                 blank=True,
                                                 verbose_name='中心/事业部', related_name='intern_leave_center_base',
                                                 db_constraint=False)
    intern_employee = models.ForeignKey(to='employee.HrEmployee', on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name='离职人', related_name='intern_employee', db_constraint=False)
    intern_leave_date = models.DateField(null=True, blank=True, verbose_name="离职日期")
    intern_term = models.CharField(max_length=255, null=True, blank=True, verbose_name="届别")
    intern_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="类别")
    performance_one = models.FloatField(null=True, blank=True, verbose_name="绩效1")
    performance_two = models.FloatField(null=True, blank=True, verbose_name="绩效2")
    performance_three = models.FloatField(null=True, blank=True, verbose_name="绩效3")
    intern_leave_reason = models.TextField(null=True, blank=True, verbose_name="离职原因")
    intern_status = models.BooleanField(default=True, null=True, blank=True, verbose_name="数据是否有效")
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='intern_leave_creator', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='intern_leave_modifier', db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        ordering = ['-create_time']
        verbose_name = '追光者离职信息表'
        verbose_name_plural = '追光者离职信息表'
        db_table = 'intern_leave_info'


class internBasicInfo(models.Model):
    intern_center_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True,
                                           verbose_name='中心/事业部', related_name='intern_center_base',
                                           db_constraint=False)
    intern_month = models.DateField(null=True, blank=True, verbose_name="月份")
    intern_organization = models.CharField(max_length=255, null=True, blank=True, verbose_name="组织归属")
    intern_term = models.CharField(max_length=255, null=True, blank=True, verbose_name="届别")
    intern_type = models.CharField(max_length=255, null=True, blank=True, verbose_name="类别")
    # 基本信息
    intern_num_at_begin = models.IntegerField(null=True, blank=True, verbose_name="期初人数")
    intern_num_join_in = models.IntegerField(null=True, blank=True, verbose_name="入职人数")
    intern_num_call_in = models.IntegerField(null=True, blank=True, verbose_name="调入人数")
    intern_num_call_out = models.IntegerField(null=True, blank=True, verbose_name="调出人数")
    intern_num_leave_out = models.IntegerField(null=True, blank=True, verbose_name="离职人数")
    intern_num_at_end = models.IntegerField(null=True, blank=True, verbose_name="期末人数")
    # 在职职等情况
    intern_job_one = models.IntegerField(null=True, blank=True, verbose_name="职等1")
    intern_job_tow = models.IntegerField(null=True, blank=True, verbose_name="职等2")
    intern_job_three = models.IntegerField(null=True, blank=True, verbose_name="职等3")
    intern_job_four = models.IntegerField(null=True, blank=True, verbose_name="职等4")
    intern_job_five = models.IntegerField(null=True, blank=True, verbose_name="职等5")

    # 情况说明
    intern_yd_detail = models.TextField(null=True, blank=True, verbose_name="本月新晋升/定岗说明")
    intern_yd_over_four_detail = models.TextField(null=True, blank=True, verbose_name="职级4及以上说明(岗位、职级、姓名)")

    intern_status = models.BooleanField(default=True, null=True, blank=True, verbose_name="数据是否有效")
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='intern_basic_creator', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='intern_basic_modifier', db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        ordering = ['intern_center_base', 'intern_month', '-create_time']
        verbose_name = '追光者月度统计基本信息表'
        verbose_name_plural = '追光者月度统计基本信息表'
        db_table = 'intern_basic_info'
