from django.db import models
# from django_bulk_update_or_create import BulkUpdateOrCreateManager

# Create your models here.

# python manage.py makemigrations overdseasTrace
# python manage.py migrate overdseasTrace
class OverseasTrace(models.Model):  # 海外本土跟踪   personnelOptimization    #当前时间在12-1月，显示区间为11-3月；当前时间在2-3月，显示区间为1-5月；当前时间在4-5月，显示区间为3-7月；
    overseas_dept = models.ForeignKey(to='employee.HrDepartment', on_delete=models.DO_NOTHING, db_constraint=False,
                                       blank=True, verbose_name='培训基地部门')
    overseas_authorized_total = models.IntegerField(verbose_name='初始总编制', null=True, blank=True)
    overseas_authorized_chinese = models.IntegerField(verbose_name='初始中方外派编制', null=True, blank=True)
    overseas_initial  = models.IntegerField(verbose_name='初始在职人数', null=True, blank=True)
    overseas_expatriate_number = models.IntegerField(verbose_name='初始中方外派人数', null=True, blank=True)

    overseas_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    overseas_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name='创建者', related_name='overseas_creator', db_constraint=False)
    overseas_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                          verbose_name='修改者', related_name='overseas_modifier')
    overseas_create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    overseas_modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'Overseas_trace'
        verbose_name_plural = '人员优化跟踪表'
        verbose_name = '人员优化跟踪表'
class OverseasMonth(models.Model):  # 海外本土跟踪月份
    overseas_month_trace = models.ForeignKey(to=OverseasTrace, on_delete=models.DO_NOTHING, db_constraint=False,
                                       null=True, blank=True, verbose_name='部门跟踪')
    overseas_month_time = models.DateField(null=True, blank=True, verbose_name='记录时间')
    overseas_month_target_expatriate = models.IntegerField(verbose_name='目标外派人数', null=True, blank=True)
    overseas_month_practical_expatriate = models.IntegerField(verbose_name='实际外派人数', null=True, blank=True)

    overseas_month_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    overseas_month_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name='创建者', related_name='overseas_month_creator', db_constraint=False)
    overseas_month_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                          verbose_name='修改者', related_name='overseas_month_modifier')
    overseas_month_create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    overseas_month_modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'Overseas_month'
        verbose_name_plural = '人员优化月份表'
        verbose_name = '人员月份表'


#
# #海外本土跟踪 Overseas local tracking