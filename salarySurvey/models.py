from django.db import models

import auther.models


# Create your models here.
class SalarySurveyRecord(models.Model):
    name = models.CharField(max_length=50, default='', verbose_name='名称')
    salary_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='公司', related_name='salary_base', db_constraint=False)
    period = models.DateField(verbose_name="日期")
    previous_work_country = models.CharField(max_length=50, blank=True, null=True, verbose_name='原工作国家')
    previous_work_city = models.CharField(max_length=50, blank=True, null=True, verbose_name='原工作城市')
    previous_company = models.CharField(max_length=50, blank=True, null=True, verbose_name='原公司')
    previous_department = models.CharField(max_length=50, blank=True, null=True, verbose_name='原部门')
    previous_post = models.CharField(max_length=50, blank=True, null=True, verbose_name='原岗位')
    salary_calc_method = models.CharField(max_length=50, blank=True, null=True, verbose_name='计薪方式')
    monthly_income = models.FloatField(verbose_name='月度综合收入')
    base_salary = models.FloatField(verbose_name='基本工资')
    post_salary = models.FloatField(verbose_name='岗位工资')
    skill_salary = models.FloatField(verbose_name='技能工资')
    performance_salary = models.FloatField(verbose_name='绩效工资')
    seniority_subsidy = models.FloatField(verbose_name='工龄补贴')
    other_subsidy = models.FloatField(verbose_name='其他补贴')
    other_illustrate = models.CharField(max_length=255, blank=True, null=True, verbose_name='其他说明')
    overtime_hours = models.FloatField(verbose_name='加班时长')
    other_program = models.CharField(max_length=255, blank=True, null=True, verbose_name='加班处理（加班时长方案）')
    overtime_base_salary = models.FloatField(verbose_name='加班基数工资')
    description_of_leave = models.CharField(max_length=255, blank=True, null=True, verbose_name='调休说明')
    bonus_standard = models.CharField(max_length=255, blank=True, null=True, verbose_name='奖金标准')
    bonus_total = models.FloatField(verbose_name='奖金总额（海外-除12个月固薪之外的奖金，包含但不限于圣诞奖金）')
    bonus_distribute_times = models.IntegerField(verbose_name='奖金发放次数')
    bonus_distribute_way = models.CharField(max_length=255, blank=True, null=True, verbose_name='发放方式')
    social_security_cardinality = models.FloatField(verbose_name='社保基数')
    provident_fund_cardinality = models.FloatField(verbose_name='公积金基数')
    attach_business_insurance = models.CharField(max_length=255, blank=True, null=True, verbose_name='补充商业保险（如有）')
    accommodation = models.CharField(max_length=255, blank=True, null=True, verbose_name='住宿')
    meals = models.CharField(max_length=255, blank=True, null=True, verbose_name='餐费')
    transportation = models.CharField(max_length=255, blank=True, null=True, verbose_name='交通')
    spring_festival_benefits = models.FloatField(verbose_name='春节福利')
    dragon_boat_festival_benefits = models.FloatField(verbose_name='端午福利')
    mid_autumn_festival_benefits = models.FloatField(verbose_name='中秋福利')
    other_festival_benefits = models.CharField(max_length=255, blank=True, null=True, verbose_name='其他节日福利')
    residency_country = models.CharField(max_length=255, blank=True, null=True, verbose_name='派驻国家')
    residency_start_date = models.DateField(verbose_name='派驻开始时间')
    residency_end_date = models.DateField(verbose_name='派驻结束时间')
    residency_allowance = models.FloatField(verbose_name='派驻津贴')
    residency_welfare = models.CharField(max_length=255, blank=True, null=True, verbose_name='派驻福利')
    residency_allowance_distribute_way = models.CharField(max_length=255, blank=True, null=True,
                                                          verbose_name='派驻津贴发放方式')
    historical_payslip = models.ManyToManyField(to='auther.UploadFiles', verbose_name='历史薪资单',
                                                related_name='historical_payslip',
                                                db_constraint=False)
    status = models.BooleanField(default=True, verbose_name='数据是否有效')
    fix_detail_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.DO_NOTHING, null=True, blank=True,
                                           verbose_name='创建者', related_name='salary_survey_record_creator',
                                           db_constraint=False)
    fix_detail_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.DO_NOTHING, null=True, blank=True,
                                            verbose_name='修改者', related_name='salary_survey_record_modifier',
                                            db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'salary_survey_record'
        verbose_name_plural = '薪资调研记录表'
        verbose_name = '薪资调研记录表'
