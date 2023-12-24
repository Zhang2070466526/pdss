from django.db import models

# python manage.py makemigrations rewardsPunishments
# python manage.py migrate rewardsPunishments


# Create your models here.
class ProjectBonus(models.Model):   #项目奖金
    project_bonus_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='公司', related_name='p_b_base', db_constraint=False)
    project_bonus_date = models.DateField(null=True, blank=True, verbose_name='日期')
    project_bonus_no = models.IntegerField(null=True, blank=True, verbose_name='项目数量')
    project_bonus_reach_no = models.IntegerField(null=True, blank=True, verbose_name='达成数量')
    project_bonus_total = models.FloatField(null=True, blank=True, verbose_name='奖金总额')
    project_bonus_person_no = models.IntegerField(null=True, blank=True, verbose_name='享受人次')
    project_bonus_average = models.FloatField(null=True, blank=True, verbose_name='人均奖励')
    project_bonus_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='创建者', related_name='p_b_creator',
                                db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='修改者', related_name='p_b_modifier',
                                 db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'project_bonus'
        verbose_name_plural = '项目奖金表'
        verbose_name = '项目奖金表'


class RewardsAndPunishments(models.Model):#奖惩数据
    r_p_base= models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='公司', related_name='r_p_base', db_constraint=False)
    r_p_date = models.DateField(null=True, blank=True, verbose_name='日期')
    rewards_money = models.FloatField(null=True, blank=True, verbose_name='奖励金额')
    rewards_person_no = models.IntegerField(null=True, blank=True, verbose_name='奖励人次')
    rewards_average = models.FloatField(null=True, blank=True, verbose_name='奖励人均')
    punishments_money = models.FloatField(null=True, blank=True, verbose_name='惩处金额')
    punishments_person_no = models.IntegerField(null=True, blank=True, verbose_name='惩处人次')
    punishments_average = models.FloatField(null=True, blank=True, verbose_name='惩处人均')
    r_p_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='创建者', related_name='r_p_creator',
                                db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='修改者', related_name='r_p_modifier',
                                 db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'rewards_and_punishments'
        verbose_name_plural = '奖惩表'
        verbose_name = '奖惩表'
