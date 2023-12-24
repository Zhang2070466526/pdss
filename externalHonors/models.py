from django.db import models


# Create your models here.
class ExternalHonorsList(models.Model):

    honor_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='荣誉名称')
    honor_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='honor_base',
                                   db_constraint=False, verbose_name='公司')
    honor_level = models.CharField(max_length=255, null=True, blank=True, verbose_name='荣誉级别')
    honor_issue_organize = models.CharField(max_length=255, null=True, blank=True, verbose_name='颁发单位')
    honor_date = models.DateField(null=True, blank=True, verbose_name='荣誉获得时间')
    honor_upload_declare_files = models.ManyToManyField(to='auther.UploadFiles', verbose_name='荣誉申报材料',
                                                        related_name='honor_upload_declare_files', db_constraint=False)
    honor_medal_photos = models.ManyToManyField(to='auther.UploadFiles', verbose_name='奖牌照片',
                                                related_name='honor_medal_photos', db_constraint=False)
    # honor_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    honor_remark = models.TextField(null=True,blank=True, verbose_name='备注')
    honor_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='external_honors_creator',
                                db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='external_honors_modifier',
                                 db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'external_honors_list'
        verbose_name_plural = '公司外部荣誉收集表'
        verbose_name = '公司外部荣誉收集表'
