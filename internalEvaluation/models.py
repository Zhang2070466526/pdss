from django.db import models

#python manage.py makemigrations internalEvaluation
# python manage.py migrate internalEvaluation

# Create your models here.
class InternalEvaluationList(models.Model):
    # evaluation_company = models.CharField(max_length=255, null=True, blank=True, verbose_name='内部评优获得公司')
    awards_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='奖项名称')
    evaluation_company = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='公司', related_name='evaluation_company', db_constraint=False)
    awards_date = models.DateField(verbose_name='内部评优时间')
    awards_person_or_team = models.CharField(max_length=255, null=True, blank=True, verbose_name='获奖人员/团队')
    awards_position = models.CharField(max_length=255, null=True, blank=True, verbose_name='岗位')
    brief_story = models.TextField(null=True,blank=True, verbose_name='简要事迹')
    awards_photos = models.ManyToManyField(to='auther.UploadFiles', verbose_name='评优照片', related_name='awards_photos', db_constraint=False)
    # awards_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    awards_remark =  models.TextField(null=True,blank=True, verbose_name='备注')
    awards_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='创建者',
                                related_name='internal_evaluation_creator',db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='修改者', related_name='internal_evaluation_modifier',
                                 db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'internal_evaluation_list'
        verbose_name_plural = '内部评优表'
        verbose_name = '内部评优表'
