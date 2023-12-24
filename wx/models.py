from django.db import models
from employee.models import HrEmployee


# Create your models here.


class IndexBar(models.Model):
    title_field = models.CharField(max_length=255, null=True, blank=True, verbose_name="首页模板字段")
    icon = models.CharField(max_length=255, null=True, blank=True, verbose_name="图标")
    url = models.CharField(max_length=255, null=True, blank=True, verbose_name="地址")
    nav_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='菜单名')

    class Meta:
        managed = True
        db_table = 'hrssc_index_bar'
        verbose_name_plural = '首页模块表'
        verbose_name = '首页模块表'

