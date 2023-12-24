# from django.db import models
#
# # Create your models here.
#
# # python manage.py makemigrations staffFollowing
# # python manage.py migrate staffFollowing
# class staffOptimization(models.Model):  # 人员优化   personnelOptimization    #当前时间在12-1月，显示区间为11-3月；当前时间在2-3月，显示区间为1-5月；当前时间在4-5月，显示区间为3-7月；
#     optimize_dept = models.ForeignKey(to='employee.HrDepartment', on_delete=models.DO_NOTHING, db_constraint=False,
#                                       null=True, blank=True, verbose_name='培训基地部门')
#     optimize_month = models.DateField(null=True, blank=True, verbose_name='记录时间')
#     optimize_initial = models.IntegerField(verbose_name='初始在职人数', null=True, blank=True)
#     optimize_forecast = models.IntegerField(verbose_name='预测在职人数', null=True, blank=True)
#     optimize_practical = models.IntegerField(verbose_name='实际在职人数', null=True, blank=True)
#     optimize_title = models.TextField(null=True, blank=True, verbose_name='备注')
#
#     optimize_status = models.BooleanField(default=True, verbose_name='数据是否有效')
#     optimize_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                          verbose_name='创建者', related_name='optimize_creator', db_constraint=False)
#     optimize_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                           verbose_name='修改者', related_name='optimize_modifier')
#     optimize_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
#     optimize_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
#
#     class Meta:
#         managed = True
#         db_table = 'staff_optimization'
#         verbose_name_plural = '人员优化表'
#         verbose_name = '人员优化表'
