from django.db import models

from employee.models import HrEmployee, HrDepartment, HrPosition, HrJobGrade, HrJobDuty, HrPayType, HrJobRank, \
    HrJobClass, HrJobSequence


class HrEmployeeMobilize(models.Model):
    employee = models.ForeignKey(to=HrEmployee, on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True,
                                 verbose_name='员工', related_name='mobilize_employee')
    mobilize_date = models.DateField(null=True, blank=True, verbose_name='调动日期')
    mobilize_reason = models.TextField(null=True, blank=True, verbose_name='调动原因')
    mobilize_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='调动类型',
                                     choices=(('1', '平调'), ('11', '用工性质调整'), ('12', '降职'), ('15', '晋升'), ('2', '晋级'),
                                              ('3', '降级')))
    old_join_date = models.DateField(null=True, blank=True, verbose_name='旧入职日期')
    new_join_date = models.DateField(null=True, blank=True, verbose_name='新入职日期')
    old_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='旧工号')
    new_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='新工号')
    old_department = models.ForeignKey(to=HrDepartment, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                       blank=True, related_name='mobilize_old_department', verbose_name='旧部门')
    new_department = models.ForeignKey(to=HrDepartment, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                       blank=True, related_name='mobilize_new_department', verbose_name='新部门')

    old_position = models.ForeignKey(to=HrPosition, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                     blank=True, related_name='mobilize_old_position', verbose_name='旧岗位')
    new_position = models.ForeignKey(to=HrPosition, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                     blank=True, related_name='mobilize_new_position', verbose_name='新岗位')

    old_job_grade = models.ForeignKey(to=HrJobGrade, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                      blank=True, related_name='mobilize_old_job_grade', verbose_name='旧职级')
    new_job_grade = models.ForeignKey(to=HrJobGrade, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                      blank=True, related_name='mobilize_new_job_grade', verbose_name='新职级')

    old_job_duty = models.ForeignKey(to=HrJobDuty, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                     blank=True, related_name='mobilize_old_job_duty', verbose_name='旧职务')
    new_job_duty = models.ForeignKey(to=HrJobDuty, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                     blank=True, related_name='mobilize_new_job_duty', verbose_name='新职务')

    old_job_class = models.ForeignKey(to=HrJobClass, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                      blank=True, related_name='mobilize_old_job_class', verbose_name='旧职等')
    new_job_class = models.ForeignKey(to=HrJobClass, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                      blank=True, related_name='mobilize_new_job_class', verbose_name='新职等')

    old_pay_type = models.ForeignKey(to=HrPayType, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                     blank=True, related_name='mobilize_old_pay_type', verbose_name='旧计薪方式')
    new_pay_type = models.ForeignKey(to=HrPayType, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                     blank=True, related_name='mobilize_new_pay_type', verbose_name='新计薪方式')

    old_job_rank = models.ForeignKey(to=HrJobRank, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                     blank=True, related_name='mobilize_old_job_rank', verbose_name='旧合同归属')
    new_job_rank = models.ForeignKey(to=HrJobRank, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                     blank=True, related_name='mobilize_new_job_rank', verbose_name='新合同归属')

    old_job_sequence = models.ForeignKey(to=HrJobSequence, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                         blank=True, related_name='mobilize_old_job_sequence', verbose_name='旧职级序列')
    new_job_sequence = models.ForeignKey(to=HrJobSequence, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                         blank=True, related_name='mobilize_new_job_sequence', verbose_name='新职级序列')
    mobilize_out_org_opinion = models.CharField(max_length=255, null=True, blank=True, verbose_name='调出组织意见')
    mobilize_in_org_opinion = models.CharField(max_length=255, null=True, blank=True, verbose_name='调入组织意见')
    hr_opinion = models.CharField(max_length=255, null=True, blank=True, verbose_name='人事意见')
    remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    term_of_labor_contract = models.CharField(max_length=255, default="固定期限",
                                              choices=(('固定期限', '固定期限'), ('无固定期限', '无固定期限'), ('已完成任务期限', '已完成任务期限'),),
                                              null=True, blank=True,
                                              verbose_name='劳动合同期期限')
    start_date_of_labor_contract = models.DateField(null=True, blank=True, verbose_name="劳动合同开始日期")
    end_date_of_labor_contract = models.DateField(null=True, blank=True, verbose_name="劳动合同结束日期")
    probation_period = models.IntegerField(null=True, blank=True, verbose_name='试用期(月)')
    workingHoursChoices = (
        ('A', '标准工时'),
        ('B', '不定时工时'),
        ('C', '综合工时'),
    )
    working_hours = models.CharField(max_length=255, default='A', choices=workingHoursChoices, null=True, blank=True,
                                     verbose_name='工时制')
    basic_salary = models.CharField(max_length=255, null=True, blank=True, verbose_name="基本工资")
    mobilize_status = models.BooleanField(default=True, null=True, blank=True, verbose_name="数据是否有效")

    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='mobilize_creator', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='mobilize_modifier', db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    contract_status_choices = (
        (0, '默认'),
        (1, '已创建、等待激活'),
        (2, '已激活'),
        (3, '合同已发起'),
        (4, '合同已签署'),
    )
    contract_status = models.IntegerField(choices=contract_status_choices, default=0, null=True, blank=True,
                                          verbose_name='合同状态')

    class Meta:
        managed = True
        ordering = ['-mobilize_date']
        db_table = 'hr_employee_mobilize'
        verbose_name_plural = '员工调动信息表'
        verbose_name = '员工调动信息表'
