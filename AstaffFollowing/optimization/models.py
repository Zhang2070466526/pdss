from django.db import models
# from django_bulk_update_or_create import BulkUpdateOrCreateManager

# Create your models here.

# python manage.py makemigrations staffFollowing
# python manage.py migrate staffFollowing
class OptimizeTrace(models.Model):  # 人员优化跟踪   personnelOptimization    #当前时间在12-1月，显示区间为11-3月；当前时间在2-3月，显示区间为1-5月；当前时间在4-5月，显示区间为3-7月；
    optimize_dept = models.ForeignKey(to='employee.HrDepartment', on_delete=models.DO_NOTHING, db_constraint=False,
                                       blank=True, verbose_name='培训基地部门')
    # optimize_month = models.DateField(null=True, blank=True, verbose_name='记录时间')
    optimize_initial = models.IntegerField(verbose_name='初始在职人数', null=True, blank=True)

    # optimize_forecast = models.IntegerField(verbose_name='预测在职人数', null=True, blank=True)
    # optimize_practical = models.IntegerField(verbose_name='实际在职人数', null=True, blank=True)
    # optimize_remark= models.TextField(null=True, blank=True, verbose_name='备注')

    optimize_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    optimize_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name='创建者', related_name='optimize_creator', db_constraint=False)
    optimize_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                          verbose_name='修改者', related_name='optimize_modifier')
    optimize_create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    optimize_modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'optimize_trace'
        verbose_name_plural = '人员优化跟踪表'
        verbose_name = '人员优化跟踪表'
class OptimizeMonth(models.Model):  # 人员优化月份
    month_trace = models.ForeignKey(to=OptimizeTrace, on_delete=models.DO_NOTHING, db_constraint=False,
                                       null=True, blank=True, verbose_name='部门跟踪')
    month_time = models.DateField(null=True, blank=True, verbose_name='记录时间')
    month_forecast = models.IntegerField(verbose_name='预测在职人数', null=True, blank=True)
    month_practical = models.IntegerField(verbose_name='实际在职人数', null=True, blank=True)

    month_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    month_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name='创建者', related_name='month_creator', db_constraint=False)
    month_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                          verbose_name='修改者', related_name='month_modifier')
    month_create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    month_modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'optimize_month'
        verbose_name_plural = '人员优化月份表'
        verbose_name = '人员月份表'
