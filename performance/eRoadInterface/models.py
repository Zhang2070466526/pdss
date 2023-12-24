from django.db import models
# python manage.py makemigrations performance
# python manage.py migrate performance
#
# Create your models here.
class EroadInterface(models.Model):   #
    eroad_indicator_code = models.CharField(max_length=255, null=True, blank=True,  verbose_name='指标代码')
    eroad_indicator_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='指标名称')
    eroad_month = models.DateField(blank=True, null=True, verbose_name="月份")
    eroad_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='数据提供人工号')
    eroad_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='数据提供人姓名')
    eroad_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    eroad_create = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='创建者', related_name='eRoad_create', db_constraint=False)
    eroad_modifier= models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='修改者',related_name='eRoad_modifier')
    eroad_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    eroad_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'performance_eroad'
        verbose_name_plural = '绩效_易路表'
        verbose_name = '绩效_易路表'