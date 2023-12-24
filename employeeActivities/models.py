from django.db import models


# Create your models here.
class EmployeeActivitiesList(models.Model):
    employee_activities_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='活动名称')
    employee_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True,
                                                    blank=True,
                                                    related_name='employee_activities_company',
                                                    db_constraint=False, verbose_name='公司')
    employee_activities_date = models.DateField(verbose_name='活动时间')
    employee_activities_place = models.CharField(max_length=255, null=True, blank=True, verbose_name='活动地点')
    employee_activities_join_no = models.IntegerField(null=True, blank=True, verbose_name='参与人数')
    employee_activities_cost = models.FloatField(null=True, blank=True, verbose_name='活动费用')
    employee_activities_plans = models.ManyToManyField(to='auther.UploadFiles', verbose_name='活动方案',
                                                       related_name='employee_activities_plans', db_constraint=False)
    employee_activities_photos = models.ManyToManyField(to='auther.UploadFiles', verbose_name='活动图片',
                                                        related_name='employee_activities_photos', db_constraint=False)
    # employee_activities_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    employee_activities_remark = models.TextField(null=True,blank=True, verbose_name='备注')
    employee_activities_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='employee_activities_creator',
                                db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='employee_activities_modifier',
                                 db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'employee_activities_list'
        verbose_name_plural = '员工活动表'
        verbose_name = '员工活动表'
