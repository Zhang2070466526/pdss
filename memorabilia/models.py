from django.db import models




# python manage.py makemigrations memorabilia
# python manage.py migrate memorabilia


# Create your models here.
class MemorabiliaList(models.Model):
    memorabilia_base = models.ForeignKey(to='general.center_base',on_delete=models.SET_NULL, null=True, blank=True,verbose_name='公司',related_name='memorabilia_base',db_constraint=False)
    # memorabilia_base = models.CharField(max_length=50, null=True, blank=True, verbose_name='中心/基地')
    memorabilia_date = models.DateField(null=True, blank=True, verbose_name='日期')
    memorabilia_key_events_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='关键事件名称')
    memorabilia_main_attending_leaders = models.CharField(max_length=50, null=True, blank=True, verbose_name='主要出席领导（内外部）')
    memorabilia_location = models.CharField(max_length=50, null=True, blank=True, verbose_name='地点')
    # memorabilia_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    memorabilia_remark =models.TextField(null=True,blank=True, verbose_name='备注')
    memorabilia_photos = models.ManyToManyField(to='auther.UploadFiles', verbose_name='照片', related_name='memorabilia_photos', db_constraint=False)
    memorabilia_plans = models.ManyToManyField(to='auther.UploadFiles', verbose_name='方案', related_name='memorabilia_plans', db_constraint=False)
    memorabilia_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='创建者', related_name='memorabilia_creator',
                                db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='修改者', related_name='memorabilia_modifier',
                                 db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'memorabilia_list'
        verbose_name_plural = '公司大事记收集表'
        verbose_name = '公司大事记收集表'
