from django.db import models


# Create your models here.
class RecruitDl(models.Model):
    recruit_dl_date = models.DateField(null=True, blank=True, verbose_name='日期')
    recruit_dl_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name='公司', related_name='dl_base', db_constraint=False)
    recruit_dl_demand_no = models.IntegerField(null=True, blank=True, verbose_name='需求人数')
    recruit_dl_interview_no = models.IntegerField(null=True, blank=True, verbose_name='面试人数')
    recruit_dl_interview_pass_no = models.IntegerField(null=True, blank=True, verbose_name='面试通过人数')
    recruit_dl_entry_no = models.IntegerField(null=True, blank=True, verbose_name='入职人数')
    recruit_dl_to_entry_no = models.IntegerField(null=True, blank=True, verbose_name='待入职人数')
    recruit_dl_completion_rate = models.FloatField(null=True, blank=True, verbose_name='完成率')
    recruit_dl_labor_no = models.IntegerField(null=True, blank=True, verbose_name='劳务人数')
    recruit_dl_confess_no = models.IntegerField(null=True, blank=True, verbose_name='自招人数')
    recruit_dl_self_rate = models.FloatField(null=True, blank=True, verbose_name='自招率')
    # recruit_dl_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注', default="")
    recruit_dl_remark = models.TextField(null=True,blank=True, verbose_name='备注', default="")
    recruit_dl_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='dl_creator',
                                db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='dl_modifier',
                                 db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'recruit_dl'
        verbose_name_plural = 'Dl招聘表'
        verbose_name = 'Dl招聘表'


class RecruitIdl(models.Model):
    recruit_idl_date = models.DateField(null=True, blank=True, verbose_name='日期')
    recruit_idl_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name='公司', related_name='idl_base', db_constraint=False)
    recruit_idl_demand_no = models.IntegerField(null=True, blank=True, verbose_name='需求人数')
    recruit_idl_interview_no = models.IntegerField(null=True, blank=True, verbose_name='面试人数')
    recruit_idl_interview_pass_no = models.IntegerField(null=True, blank=True, verbose_name='面试通过人数')
    recruit_idl_offer_no = models.IntegerField(null=True, blank=True, verbose_name='offer人数')
    recruit_idl_entry_no = models.IntegerField(null=True, blank=True, verbose_name='入职人数')
    recruit_idl_to_entry_no = models.IntegerField(null=True, blank=True, verbose_name='待入职人数')
    recruit_idl_completion_rate = models.FloatField(null=True, blank=True, verbose_name='完成率')
    # recruit_idl_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注', default="")
    recruit_idl_remark = models.TextField(null=True,blank=True, verbose_name='备注', default="")
    recruit_idl_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='idl_creator',
                                db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='idl_modifier',
                                 db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'recruit_idl'
        verbose_name_plural = 'Idl招聘表'
        verbose_name = 'Idl招聘表'


class RecruitSal(models.Model):
    recruit_sal_date = models.DateField(null=True, blank=True, verbose_name='日期')
    recruit_sal_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name='公司', related_name='sal_base', db_constraint=False)
    recruit_sal_demand_no = models.IntegerField(null=True, blank=True, verbose_name='需求人数')
    recruit_sal_interview_no = models.IntegerField(null=True, blank=True, verbose_name='面试人数')
    recruit_sal_interview_pass_no = models.IntegerField(null=True, blank=True, verbose_name='面试通过人数')
    recruit_sal_offer_no = models.IntegerField(null=True, blank=True, verbose_name='offer人数')
    recruit_sal_entry_no = models.IntegerField(null=True, blank=True, verbose_name='入职人数')
    recruit_sal_to_entry_no = models.IntegerField(null=True, blank=True, verbose_name='待入职人数')
    recruit_sal_completion_rate = models.FloatField(null=True, blank=True, verbose_name='完成率')
    # recruit_sal_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注', default="")
    recruit_sal_remark = models.TextField(null=True,blank=True, verbose_name='备注', default="")
    recruit_sal_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='sal_creator',
                                db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='sal_modifier',
                                 db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'recruit_sal'
        verbose_name_plural = 'Sal招聘表'
        verbose_name = 'Sal招聘表'
