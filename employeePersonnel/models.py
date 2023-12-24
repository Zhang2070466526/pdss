from django.db import models

from employee.models import *


# Create your models here.
class HrEmployeeHistory(models.Model):
    employee_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='姓名')
    employee_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='工号')
    employee_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='联系电话')
    employee_nationality = models.CharField(max_length=255, null=True, blank=True, verbose_name='国籍')
    employee_email = models.CharField(max_length=255, null=True, blank=True, verbose_name='邮箱')
    employee_department = models.ForeignKey(to=HrDepartment, on_delete=models.DO_NOTHING, db_constraint=False,
                                            null=True, blank=True,
                                            verbose_name='部门')
    employee_position = models.ForeignKey(to=HrPosition, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                          blank=True,
                                          verbose_name='岗位')
    employee_status = models.CharField(max_length=10, null=True, blank=True,
                                       choices=(('1', '在职'), ('2', '离职'), ('99', '黑名单')), verbose_name='状态')
    employee_dl = models.CharField(max_length=10, null=True, blank=True,
                                   choices=(('DL', 'DL'), ('IDL', 'IDL'), ('SAL', 'SAL')), verbose_name='dl/idl/sal')
    employee_sex = models.CharField(max_length=10, null=True, blank=True, choices=(('1', '男'), ('2', '女')),
                                    verbose_name='性别')
    employee_identity_type = models.CharField(max_length=10, null=True, blank=True, choices=(
        ('1', '身份证'), ('2', '行驶证'), ('3', '驾驶证'), ('4', '护照'), ('5', '其他')), verbose_name='证件类型')
    employee_work_place = models.CharField(max_length=255, null=True, blank=True, verbose_name='工作地')
    employee_process= models.CharField(max_length=255, null=True, blank=True, verbose_name='工序')
    employee_dim_reason = models.ForeignKey(to=HrDimissionReason, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                          blank=True,
                                          verbose_name='离职原因')
    employee_dim_type = models.ForeignKey(to=HrDimissionType, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                          blank=True,
                                          verbose_name='离职类型')
    employee_identity_no = models.CharField(max_length=255, null=True, blank=True, verbose_name='证件号码')
    employee_job_duty = models.ForeignKey(to=HrJobDuty, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                          blank=True, verbose_name='职务')
    employee_job_class = models.ForeignKey(to=HrJobClass, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                           blank=True,
                                           verbose_name='职等')
    employee_job_grade = models.ForeignKey(to=HrJobGrade, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                           blank=True,
                                           verbose_name='职级')
    employee_pay_type = models.ForeignKey(to=HrPayType, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                          blank=True,
                                          verbose_name='计薪方式')

    employee_job_rank = models.ForeignKey(to=HrJobRank, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                          blank=True,
                                          verbose_name='合同归属')

    employee_job_sequence = models.ForeignKey(to=HrJobSequence, on_delete=models.DO_NOTHING,
                                                   db_constraint=False, null=True,
                                                   blank=True,
                                                   verbose_name='职级序列')
    employee_join_date = models.DateTimeField(null=True, blank=True, verbose_name='入职日期')
    employee_group_join_date = models.DateTimeField(null=True, blank=True, verbose_name='集团入职日期')
    employee_departure_date = models.DateTimeField(null=True, blank=True, verbose_name='离职结薪日期')
    employee_departure_notice_date = models.DateTimeField(null=True, blank=True, verbose_name='离职通报日期')
    employee_departure_handle_date = models.DateTimeField(null=True, blank=True, verbose_name='离职办理日期')
    employee_plan_turn_date = models.DateTimeField(null=True, blank=True, verbose_name='预转正日期')
    employee_turn_date = models.DateTimeField(null=True, blank=True, verbose_name='转正日期')
    employee_turn_status = models.CharField(max_length=255, null=True, blank=True, verbose_name='转正状态')
    employee_nation = models.ForeignKey(to=HrNation, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                        blank=True,
                                        verbose_name='民族')
    employee_nation_place = models.ForeignKey(to=HrNationPlace, on_delete=models.DO_NOTHING, db_constraint=False,
                                              null=True, blank=True,
                                              verbose_name='籍贯')
    employee_marriage_status = models.CharField(max_length=10, null=True, blank=True,
                                                choices=(('0', '未婚'), ('1', '已婚'), ('2', '离异')), verbose_name='婚姻状况')
    employee_identity_no_effective_date = models.DateField(null=True, blank=True, verbose_name='身份证生效日期')
    employee_identity_no_failre_date = models.DateField(null=True, blank=True, verbose_name='身份证失效日期')
    employee_birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
    employee_nation_address = models.CharField(max_length=255, null=True, blank=True, verbose_name='户籍地址')
    employee_work_status = models.CharField(max_length=10, null=True, blank=True,
                                            choices=(('正式工', '正式工'), ('实习生', '实习生'), ('试用期', '试用期'), ('劳务工', '劳务工'),
                                                     ('产线承包', '产线承包'), ('顾问', '顾问'), ('', '')), verbose_name='在职状态')
    employee_political_status = models.CharField(max_length=10, null=True, blank=True,
                                                 choices=(('党员', '党员'), ('预备党员', '预备党员'), ('群众', '群众')),
                                                 verbose_name='政治面貌')
    employee_work_experience_text = models.TextField(null=True, blank=True, verbose_name='工作经历')
    employee_emergency_contact = models.CharField(max_length=255, null=True, blank=True, verbose_name='紧急联系人')
    employee_emergency_contact_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='紧急联系人电话')
    employee_emergency_contact_relation = models.CharField(max_length=255, null=True, blank=True,
                                                           verbose_name='紧急联系人关系')
    employee_first_degree = models.ForeignKey(to=HrEducationDegree, on_delete=models.DO_NOTHING, null=True, blank=True,
                                              db_constraint=False,
                                              verbose_name='第一学历')
    employee_first_degree_school = models.CharField(max_length=255, null=True, blank=True, verbose_name='第一学历学校')
    employee_first_degree_major = models.CharField(max_length=255, null=True, blank=True, verbose_name='第一学历专业')
    employee_first_degree_graduate_date = models.DateTimeField(null=True, blank=True, verbose_name='第一学历毕业日期')
    employee_first_degree_type = models.CharField(max_length=10, null=True, blank=True,
                                                  choices=(('全日制', '全日制'), ('非全日制', '非全日制')), verbose_name='第一学历教育方式')
    employee_train_degree = models.CharField(max_length=255, null=True, blank=True, verbose_name='进修学历')
    employee_train_degree_school = models.CharField(max_length=255, null=True, blank=True, verbose_name='进修学历学校')
    employee_train_degree_major = models.CharField(max_length=255, null=True, blank=True, verbose_name='进修学历专业')
    employee_train_degree_graduate_date = models.DateTimeField(null=True, blank=True, verbose_name='进修学历毕业日期')
    employee_train_degree_type = models.CharField(max_length=10, null=True, blank=True,
                                                  choices=(('01', '全日制'), ('02', '自考'), ('03', '远程教育'), ('04', '成人高考')),
                                                  verbose_name='进修学历教育方式')
    employee_labor_source = models.CharField(max_length=255, null=True, blank=True, verbose_name='劳务来源')
    employee_bank_no = models.CharField(max_length=255, null=True, blank=True, verbose_name='银行卡号')
    employee_bank_deposit = models.CharField(max_length=255, null=True, blank=True, verbose_name='开户银行')
    employee_record_begin_time= models.DateTimeField(null=True, blank=True,verbose_name='记录开始时间')
    employee_record_end_time = models.DateTimeField(null=True, blank=True, verbose_name='记录结束时间')
    employee_record_time = models.DateTimeField(null=True, blank=True,auto_now_add=True, verbose_name='记录时间')
    employee_record_type=models.CharField(max_length=10, null=True, blank=True,choices=(('1', '周'), ('2', '月')), verbose_name='记录类型')


    class Meta:
        managed = True
        db_table = 'hr_employee_history'
        verbose_name_plural = '员工信息历史表'
        verbose_name = '员工信息历史表'


