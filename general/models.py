from django.db import models


# python manage.py makemigrations general
# python manage.py migrate general

# Create your models here.
class center_base(models.Model):
    name = models.CharField(max_length=255, default='', verbose_name='基地/中心名')
    base_parent_id = models.IntegerField(verbose_name='上级id', null=True, blank=True)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    status = models.BooleanField(default=True, verbose_name='数据是否有效')

    class Meta:
        managed = True
        db_table = 'center_base'
        verbose_name_plural = '基地/中心表'
        verbose_name = '基地/中心表'


class Admin_log(models.Model):
    log_user = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='用户id', related_name='log_userId', db_constraint=False)
    log_requestMethod = models.CharField(max_length=255, default='', verbose_name='请求方式')
    log_token = models.TextField(blank=True, null=True, verbose_name='token')
    log_host = models.CharField(max_length=255, verbose_name='请求端口')
    log_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    log_requestGET = models.TextField(blank=True, null=True, verbose_name='请求发送的数据1')
    log_requestPOST = models.TextField(blank=True, null=True, verbose_name='请求发送的数据2')
    log_requestFILES = models.TextField(blank=True, null=True, verbose_name='请求发送的数据3')
    log_requestBody = models.TextField(blank=True, null=True, verbose_name='请求发送的数据4')
    # log_requestAPI = models.CharField(max_length=255, blank=True, null=True, verbose_name='请求的接口')
    log_requestAPI=models.TextField(blank=True, null=True, verbose_name='请求的接口')

    class Meta:
        managed = True
        db_table = 'admin_log'
        verbose_name_plural = '用户日志表'
        verbose_name = '用户日志表'
