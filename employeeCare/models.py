from django.db import models
# python manage.py makemigrations employeeCare
# python manage.py migrate employeeCare


# Create your models here.
class JobInterviews(models.Model):   #在职访谈
    job_interviews_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='公司', related_name='job_interviews_base', db_constraint=False)
    job_interviews_date = models.DateField(null=True, blank=True, verbose_name='日期')
    job_interviews_number = models.IntegerField(null=True, blank=True, verbose_name='访谈人次')
    job_interviews_percentage = models.FloatField(null=True, blank=True, verbose_name='占比')
    job_interviews_outputItem = models.IntegerField(null=True, blank=True, verbose_name='产出行动项')
    job_interviews_closeItem = models.IntegerField(null=True, blank=True, verbose_name='关闭项')
    job_interviews_completionRate = models.FloatField(null=True, blank=True, verbose_name='完成率')
    # job_interviews_typical= models.CharField(max_length=255, null=True, blank=True, verbose_name='典型事项')
    # job_interviews_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    job_interviews_typical = models.TextField(null=True, blank=True, verbose_name='典型事项')
    job_interviews_remark = models.TextField(null=True,blank=True, verbose_name='备注')

    job_interviews_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='创建者', related_name='job_interviews_creator',db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='修改者', related_name='job_interviews_modifier',db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'job_interviews'
        verbose_name_plural = '在职访谈表'
        verbose_name = '在职访谈表'



class Colloquium(models.Model):   #座談會
    colloquium_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='公司', related_name='colloquium_base', db_constraint=False)
    colloquium_date = models.DateField(null=True, blank=True, verbose_name='日期')
    colloquium_numberSessions = models.IntegerField(null=True, blank=True, verbose_name='场次')
    colloquium_numberParticipants = models.IntegerField(null=True, blank=True, verbose_name='参与人次')
    colloquium_percentage = models.FloatField(null=True, blank=True, verbose_name='占比')
    colloquium_outputItems = models.IntegerField(null=True, blank=True, verbose_name='产出行动项')
    colloquium_closeItem = models.IntegerField(null=True, blank=True, verbose_name='关闭项')
    colloquium_completionRate= models.FloatField(null=True, blank=True, verbose_name='完成率')
    # colloquium_typical = models.CharField(max_length=255, null=True, blank=True, verbose_name='典型事项')
    colloquium_photos = models.ManyToManyField(to='auther.UploadFiles', verbose_name='座谈会图片',related_name='colloquium_photos', db_constraint=False)
    # colloquium_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    colloquium_remark = models.TextField(null=True,blank=True, verbose_name='备注')
    colloquium_typical= models.TextField(null=True,blank=True, verbose_name='典型事项')
    coll_interviews_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='创建者', related_name='colloquium_creator',db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='修改者', related_name='colloquium_modifier',db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'colloquium'
        verbose_name_plural = '座談会表'
        verbose_name = '座談会表'

class ExitInterviews(models.Model):   #离职访谈
    exit_interviews_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='公司', related_name='exit_interviews_base', db_constraint=False)
    exit_interviews_date = models.DateField(null=True, blank=True, verbose_name='日期')
    exit_interviews_numberInterviews = models.IntegerField(null=True, blank=True, verbose_name='访谈人次')
    exit_interviews_retentionSuccess = models.IntegerField(null=True, blank=True, verbose_name='挽留成功人次')
    exit_interviews_retentionSuccessRate = models.FloatField(null=True, blank=True, verbose_name='挽留成功率')
    # exit_interviews_typicalCase = models.CharField(max_length=255,null=True, blank=True, verbose_name='典型案例')
    # exit_interviews_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    exit_interviews_typicalCase = models.TextField(null=True,blank=True, verbose_name='典型案例')
    exit_interviews_remark = models.TextField(null=True,blank=True, verbose_name='备注')
    exit_interviews_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='创建者', related_name='exit_interviews_creator',db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='修改者', related_name='exit_interviews_modifier',db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'exit_interviews'
        verbose_name_plural = '离职访谈表'
        verbose_name = '离职访谈表'

class TalentSubsidies(models.Model):   #人才补贴
    talent_subsidies_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='公司', related_name='talent_subsidies_base', db_constraint=False)
    talent_subsidies_date = models.DateField(null=True, blank=True, verbose_name='日期')
    talent_subsidies_conditions = models.IntegerField(null=True, blank=True, verbose_name='满足条件HC')
    talent_subsidies_applied = models.IntegerField(null=True, blank=True, verbose_name='已申请HC')
    talent_subsidies_claimed = models.IntegerField(null=True, blank=True, verbose_name='已领取HC')
    # talent_subsidies_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    talent_subsidies_remark = models.TextField(null=True,blank=True, verbose_name='备注')
    talent_subsidies_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='创建者', related_name='talent_subsidies_creator',db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='修改者', related_name='talent_subsidies_modifier',db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'talent_subsidies'
        verbose_name_plural = '人才补贴表'
        verbose_name = '人才补贴表'