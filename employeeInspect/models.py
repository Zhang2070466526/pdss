from django.db import models

# python manage.py makemigrations employeeInspect
# python manage.py migrate employeeInspect




# Create your models here.

class EmployeeInspect(models.Model):
    employee_inspect_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='公司', related_name='employee_inspect_base',
                                              db_constraint=False)
    # employee_inspect_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='公司', related_name='employee_inspect_base',
    #                                           db_constraint=False)
    employee_inspect_date = models.DateField(null=True, blank=True, verbose_name='日期')
    employee_inspect_day_shift_no = models.IntegerField(null=True, blank=True, verbose_name='白班稽核次数')
    employee_inspect_night_shift_no = models.IntegerField(null=True, blank=True, verbose_name='夜班稽核次数')
    employee_inspect_photos = models.ManyToManyField(to='auther.UploadFiles', verbose_name='稽查照片', related_name='employee_inspect_photos', db_constraint=False)
    # employee_inspect_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='说明')
    employee_inspect_remark = models.TextField(null=True,blank=True, verbose_name='说明')
    employee_inspect_plans = models.ManyToManyField(to='auther.UploadFiles', verbose_name='稽查方案', related_name='employee_inspect_plans', db_constraint=False)
    employee_inspect_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='创建者', related_name='project_bonus_creator',
                                db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='修改者', related_name='project_bonus_modifier',
                                 db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'employee_inspect'
        verbose_name_plural = '员工稽查'
        verbose_name = '员工稽查'
