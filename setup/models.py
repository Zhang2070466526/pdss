from django.db import models


# Create your models here.
# python manage.py makemigrations setup
# python manage.py migrate setup

class PicManage(models.Model):
    pic_status = models.BooleanField(default=True, verbose_name='轮播图是否有效')
    name = models.CharField(blank=True, null=True, max_length=250, verbose_name='图片名称')
    url = models.CharField(blank=True, null=True, max_length=250, verbose_name='图片路径')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='pic_creator', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='pic_modifier', db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'PicManage'
        verbose_name_plural = '图片管理表'
        verbose_name = '图片管理表'
