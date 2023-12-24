from django.db import models

from auther.models import AdminUser

# python manage.py makemigrations employee
# python manage.py migrate employee



# Create your models here.
class HrJobSequence(models.Model):
    sequence_code = models.CharField(max_length=50, null=True, blank=True, verbose_name="序列编码")
    sequence_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="序列名字")
    sequence_status = models.BooleanField(default=True, verbose_name='序列状态')

    class Meta:
        managed = True
        db_table = 'hr_job_sequence'
        verbose_name_plural = '职级序列'
        verbose_name = '职级序列'


class HrDayeeSelectOptions(models.Model):
    label = models.CharField(max_length=50, blank=True, null=True, verbose_name="选择名称")
    value = models.CharField(max_length=50, blank=True, null=True, verbose_name="选择值")

    def __str__(self):
        return self.label

    class Meta:
        managed = True
        db_table = 'hr_dayee_select_options'
        verbose_name_plural = '大易下拉选择'
        verbose_name = '大易下拉选择'


class HrDepartment(models.Model):
    department_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='部门名称')
    department_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='部门编码')
    department_full_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='部门全称')
    department_full_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='部门全编码')
    department_short_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='部门简称')
    department_manage = models.CharField(max_length=255, null=True, blank=True, verbose_name='管理归属')
    department_level = models.CharField(max_length=255, null=True, blank=True, verbose_name='部门层级')
    department_parent_id = models.IntegerField(null=True, blank=True, verbose_name='上级部门id')
    department_first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='一级部门名称')
    department_second_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='二级部门名称')
    department_third_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='三级部门名称')
    department_forth_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='四级部门名称')
    department_expiry_date = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='过期时间')
    department_status = models.BooleanField(default=True, verbose_name='部门状态')

    class Meta:
        managed = True
        db_table = 'hr_department'
        verbose_name_plural = '部门表'
        verbose_name = '部门表'


class HrPosition(models.Model):
    position_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='岗位名称')
    position_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='岗位编码')
    department_status = models.BooleanField(default=True, verbose_name='岗位状态')

    class Meta:
        managed = True
        db_table = 'hr_position'
        verbose_name_plural = '岗位表'
        verbose_name = '岗位表'


class HrJobClass(models.Model):
    job_class_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='职等名称')
    job_class_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='职等编码')
    job_class_status = models.BooleanField(default=True, verbose_name='职等状态')

    class Meta:
        managed = True
        db_table = 'hr_job_class'
        verbose_name_plural = '职等表'
        verbose_name = '职等表'


class HrJobGrade(models.Model):   #职系
    job_grade_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='职级名称')
    job_grade_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='职级编码')
    job_grade_status = models.BooleanField(default=True, verbose_name='职级状态')

    class Meta:
        managed = True
        db_table = 'hr_job_grade'
        verbose_name_plural = '职级表'
        verbose_name = '职级表'


class HrJobDuty(models.Model):
    job_duty_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='职务名称')
    job_duty_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='职务编码')
    job_duty_class = models.ForeignKey(null=True, blank=True, to=HrJobClass, on_delete=models.SET_NULL,
                                       verbose_name='职等')
    job_duty_grade = models.ForeignKey(null=True, blank=True, to=HrJobGrade, on_delete=models.SET_NULL,
                                       verbose_name='职级')
    job_duty_status = models.BooleanField(default=True, verbose_name='职务状态')

    class Meta:
        managed = True
        db_table = 'hr_job_duty'
        verbose_name_plural = '职务表'
        verbose_name = '职务表'


class HrPayType(models.Model):
    pay_type_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='计薪名称')
    pay_type_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='计薪编码')
    pay_type_status = models.BooleanField(default=True, verbose_name='职务状态')

    class Meta:
        managed = True
        db_table = 'hr_pay_type'
        verbose_name_plural = '计薪方式'
        verbose_name = '计薪方式'


class HrJobRank(models.Model):
    job_rank_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='合同归属名称')
    job_rank_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='合同归属编码')
    job_rank_region = models.CharField(max_length=10, null=True, blank=True, verbose_name='合同归属所在区域')
    job_rank_region_code = models.CharField(max_length=10, null=True, blank=True, verbose_name='合同归属所在区域代码')
    job_rank_company_code = models.CharField(max_length=10, null=True, blank=True, verbose_name='合同归属公司代码')
    job_rank_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    job_rank_status = models.BooleanField(default=True, verbose_name='职务状态')

    class Meta:
        managed = True
        db_table = 'hr_job_rank'
        verbose_name_plural = '合同归属'
        verbose_name = '合同归属'


class HrNation(models.Model):
    nation_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='民族名称')
    nation_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='民族编码')
    nation_status = models.BooleanField(default=True, verbose_name='民族状态')

    class Meta:
        managed = True
        db_table = 'hr_nation'
        verbose_name_plural = '民族'
        verbose_name = '民族'


class HrNationPlace(models.Model):
    nation_place_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='籍贯名称')
    nation_place_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='籍贯编码')
    nation_place_status = models.BooleanField(default=True, verbose_name='籍贯状态')

    class Meta:
        managed = True
        db_table = 'hr_nation_place'
        verbose_name_plural = '籍贯'
        verbose_name = '籍贯'


class HrEducationDegree(models.Model):
    edu_degree_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='学历名称')
    edu_degree_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='学历编码')
    edu_degree_status = models.BooleanField(default=True, verbose_name='学历状态')

    class Meta:
        managed = True
        db_table = 'hr_education_degree'
        verbose_name_plural = '学历'
        verbose_name = '学历'



class HrDimissionType(models.Model):
    dim_type_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='离职类型名称')
    dim_type_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='离职类型编码')
    dim_type_status= models.BooleanField(null=True, default=None, verbose_name='离职类型状态')
    class Meta:
        managed = True
        db_table = 'hr_dimission_type'
        verbose_name_plural = '离职类型'
        verbose_name = '离职类型'

class HrDimissionReason(models.Model):
    dim_reason_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='离职原因名称')
    dim_reason_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='离职原因编码')
    dim_reason_type = models.ForeignKey(null=True, blank=True, to=HrDimissionType, on_delete=models.SET_NULL,verbose_name='离职类型')
    dim_reason_status = models.BooleanField(default=True, verbose_name='离职原因状态')

    class Meta:
        managed = True
        db_table = 'hr_dimission_reason'
        verbose_name_plural = '离职原因'
        verbose_name = '离职原因'


# class HrDimissionReason(models.Model):
#     dim_reason_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='离职原因名称')
#     dim_reason_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='离职原因编码')
#     dim_reason_status = models.BooleanField(default=True, verbose_name='离职原因状态')
#
#     class Meta:
#         managed = True
#         db_table = 'hr_dimission_reason'
#         verbose_name_plural = '离职原因'
#         verbose_name = '离职原因'


class HrEmployee(models.Model):   
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
                                              db_constraint=False, related_name='employee_first_degree',
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

    class Meta:
        managed = True
        db_table = 'hr_employee'
        verbose_name_plural = '员工信息表'
        verbose_name = '员工信息表'


class HrCandidate(models.Model):
    candidate_status = models.IntegerField(default=1,
                                           choices=((1, '待提交'), (2, '待审核'), (3, '已退回'), (4, '放弃入职'), (5, '已删除')),
                                           verbose_name='员工状态')
    candidate_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='工号')
    candidate_join_date = models.DateTimeField(null=True, blank=True, verbose_name='入职日期')
    candidate_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='姓名')
    candidate_department = models.ForeignKey(to=HrDepartment, on_delete=models.DO_NOTHING, db_constraint=False,
                                             null=True, blank=True,
                                             verbose_name='部门')
    candidate_position = models.ForeignKey(to=HrPosition, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                           blank=True,
                                           verbose_name='岗位')
    candidate_job_duty = models.ForeignKey(to=HrJobDuty, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                           blank=True,
                                           verbose_name='职务')
    candidate_job_class = models.ForeignKey(to=HrJobClass, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                            blank=True,
                                            verbose_name='职等')
    candidate_job_grade = models.ForeignKey(to=HrJobGrade, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                            blank=True,
                                            verbose_name='职级')
    candidate_job_rank = models.ForeignKey(to=HrJobRank, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                           blank=True,
                                           verbose_name='合同归属')
    candidate_job_sequence = models.ForeignKey(to=HrJobSequence, on_delete=models.DO_NOTHING,
                                               db_constraint=False, null=True,
                                               blank=True,
                                               verbose_name='职级序列')
    candidate_work_place = models.CharField(max_length=255, null=True, blank=True, verbose_name='工作地')
    candidate_identity_no = models.CharField(max_length=255, null=True, blank=True, verbose_name='证件号码')
    candidate_probation_period = models.CharField(max_length=10, null=True, blank=True, verbose_name='试用期(月)')
    candidate_on_job_status = models.CharField(max_length=100, null=True, blank=True, verbose_name='在职状态')
    remark = models.TextField(null=True, blank=True, verbose_name='备注')
    candidate_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='联系电话')
    candidate_identity_no_effective_date = models.DateField(null=True, blank=True, verbose_name='身份证生效日期')
    candidate_identity_no_failre_date = models.DateField(null=True, blank=True, verbose_name='身份证失效日期')
    candidate_pay_type = models.ForeignKey(to=HrPayType, on_delete=models.DO_NOTHING, null=True, blank=True,
                                           db_constraint=False, verbose_name='计薪方式')
    candidate_sex = models.CharField(max_length=10, null=True, blank=True, choices=(('1', '男'), ('2', '女')),
                                     verbose_name='性别')
    candidate_dl = models.CharField(max_length=10, null=True, blank=True,
                                    choices=(('DL', 'DL'), ('IDL', 'IDL'), ('SAL', 'SAL')), verbose_name='DL/IDL/SAL')
    candidate_email = models.CharField(max_length=255, null=True, blank=True, verbose_name='邮箱')
    candidate_first_degree = models.ForeignKey(to=HrEducationDegree, on_delete=models.DO_NOTHING, null=True, blank=True,
                                               db_constraint=False, related_name='candidate_first_degree',
                                               verbose_name='第一学历')
    candidate_first_degree_school = models.CharField(max_length=255, null=True, blank=True, verbose_name='第一学历学校')
    candidate_first_degree_major = models.CharField(max_length=255, null=True, blank=True, verbose_name='第一学历专业')
    candidate_first_degree_graduate_date = models.DateTimeField(null=True, blank=True, verbose_name='第一学历毕业日期')
    candidate_first_degree_type = models.CharField(max_length=10, null=True, blank=True,
                                                   choices=(('全日制', '全日制'), ('非全日制', '非全日制')), verbose_name='第一学历教育方式')
    candidate_train_degree = models.CharField(max_length=255, null=True, blank=True, verbose_name='进修学历')
    candidate_train_degree_school = models.CharField(max_length=255, null=True, blank=True, verbose_name='进修学历学校')
    candidate_train_degree_major = models.CharField(max_length=255, null=True, blank=True, verbose_name='进修学历专业')
    candidate_train_degree_graduate_date = models.DateTimeField(null=True, blank=True, verbose_name='进修学历毕业日期')
    candidate_train_degree_type = models.CharField(max_length=10, null=True, blank=True, choices=(
        ('01', '全日制'), ('02', '自考'), ('03', '远程教育'), ('04', '成人高考')),
                                                   verbose_name='进修学历教育方式')
    candidate_birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
    candidate_nationality = models.CharField(max_length=255, null=True, blank=True, verbose_name='国籍')
    candidate_nation = models.ForeignKey(to=HrNation, on_delete=models.DO_NOTHING, null=True, blank=True,
                                         db_constraint=False, verbose_name='民族')
    candidate_identity_type = models.CharField(max_length=10, null=True, blank=True, choices=(
        ('1', '身份证'), ('2', '行驶证'), ('3', '驾驶证'), ('4', '护照'), ('5', '其他')), verbose_name='证件类型')
    candidate_marriage_status = models.CharField(max_length=10, null=True, blank=True,
                                                 choices=(('0', '未婚'), ('1', '已婚'), ('2', '离异')), verbose_name='婚姻状况')
    candidate_nation_place = models.ForeignKey(to=HrNationPlace, on_delete=models.DO_NOTHING, null=True, blank=True,
                                               db_constraint=False, verbose_name='籍贯')
    candidate_political_status = models.CharField(max_length=10, null=True, blank=True,
                                                  choices=(('党员', '党员'), ('预备党员', '预备党员'), ('群众', '群众')),
                                                  verbose_name='政治面貌')
    candidate_nation_address = models.CharField(max_length=255, null=True, blank=True, verbose_name='法定送达地址（户籍地址）')
    candidate_now_address = models.CharField(max_length=255, null=True, blank=True, verbose_name='现居地址')
    candidate_emergency_contact = models.CharField(max_length=255, null=True, blank=True, verbose_name='紧急联系人')
    candidate_emergency_contact_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='紧急联系人电话')
    candidate_emergency_contact_relation = models.CharField(max_length=255, null=True, blank=True,
                                                            verbose_name='紧急联系人关系')
    candidate_emergency_contact_company = models.CharField(max_length=255, null=True, blank=True,
                                                           verbose_name='紧急联系人单位')
    candidate_emergency_contact_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name='紧急联系人2')
    candidate_emergency_contact_phone_2 = models.CharField(max_length=255, null=True, blank=True,
                                                           verbose_name='紧急联系人电话2')
    candidate_emergency_contact_relation_2 = models.CharField(max_length=255, null=True, blank=True,
                                                              verbose_name='紧急联系人关系2')
    candidate_emergency_contact_company_2 = models.CharField(max_length=255, null=True, blank=True,
                                                             verbose_name='紧急联系人单位2')
    candidate_bank_no = models.CharField(max_length=255, null=True, blank=True, verbose_name='银行卡号')
    candidate_bank_deposit = models.CharField(max_length=255, null=True, blank=True, verbose_name='开户银行')
    candidate_labor_source = models.CharField(max_length=255, null=True, blank=True, verbose_name='劳务来源')
    candidate_resume_url = models.TextField(null=True, blank=True, verbose_name='附件连接')
    e_contract_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='电子签编码')
    candidate_plan_turn_date = models.DateField(null=True, blank=True, verbose_name='预计转正时间')

    class Meta:
        managed = True
        db_table = 'hr_candidate'
        verbose_name_plural = '候选人信息表'
        verbose_name = '候选人信息表'


class FileType(models.Model):
    file_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="文件名称")
    field_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="文件字段名")
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    is_required = models.BooleanField(default=True, verbose_name='是否必填')

    class Meta:
        managed = True
        db_table = 'hr_employee_files_type'
        verbose_name_plural = '文件分类表'
        verbose_name = '文件分类表'


class HrEmployeeFiles(models.Model):
    employee = models.ForeignKey(to=HrEmployee, on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True,
                                 verbose_name='员工')
    candidate = models.ForeignKey(to=HrCandidate, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                  blank=True,
                                  verbose_name='候选人')
    employee_file_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='文件名称')
    employee_file_url = models.CharField(max_length=255, null=True, blank=True, verbose_name='文件地址')
    employee_file_type = models.ForeignKey(to=FileType, null=True, blank=True, on_delete=models.DO_NOTHING,
                                           db_constraint=False, verbose_name='文件名')
    employee_file_status = models.BooleanField(default=True, verbose_name='文件状态')
    creator = models.ForeignKey(AdminUser, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='创建者',
                                related_name='employee_files_creator',
                                db_constraint=False)
    modifier = models.ForeignKey(AdminUser, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='修改者',
                                 related_name='employee_files_modifier',
                                 db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'hr_employee_files'
        verbose_name_plural = '员工附件表'
        verbose_name = '员工附件表'


class HrWorkExperience(models.Model):
    employee = models.ForeignKey(to=HrEmployee, on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True,
                                 verbose_name='员工')
    candidate = models.ForeignKey(to=HrCandidate, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
                                  blank=True,
                                  verbose_name='候选人')
    work_experience_hire_date = models.DateField(null=True, blank=True, verbose_name='开始时间')
    work_experience_departure_date = models.DateField(null=True, blank=True, verbose_name='结束时间')
    work_experience_company = models.CharField(max_length=255, null=True, blank=True, verbose_name='工作单位')
    work_experience_position = models.CharField(max_length=255, null=True, blank=True, verbose_name='职务')
    work_experience_description = models.TextField(null=True, blank=True, verbose_name='工作内容描述')
    work_experience_status = models.BooleanField(default=True, verbose_name='状态')

    class Meta:
        managed = True
        db_table = 'hr_work_experience'
        verbose_name_plural = '工作经历'
        verbose_name = '工作经历'













class HrDepartmentPersonLimit(models.Model):
    department_peron_limit_department = models.ForeignKey(to=HrDepartment, on_delete=models.DO_NOTHING,
                                                          db_constraint=False, null=True, blank=True,
                                                          verbose_name='部门')
    department_peron_limit_no = models.IntegerField(null=True, blank=True, verbose_name='编制人数')
    department_peron_limit_core_no = models.IntegerField(null=True, blank=True, verbose_name='关键核心岗位定编')
    department_peron_limit_effect_date = models.DateField(null=True, blank=True, verbose_name='生效时间')
    department_peron_limit_expire_date = models.DateField(null=True, blank=True, verbose_name='失效时间')
    department_peron_limit_status = models.BooleanField(default=True, verbose_name='是否生效')

    #新增部门的生效时间是上一条部门的失效时间    失效时间是哪来的

    class Meta:
        managed = True
        db_table = 'hr_department_person_limit'
        verbose_name_plural = '部门编制人数表'
        verbose_name = '部门编制人数表'


class HrDepartmentTurnOverTarget(models.Model):
    department_turn_over_target_department = models.ForeignKey(to=HrDepartment, on_delete=models.DO_NOTHING,
                                                               db_constraint=False, null=True, blank=True,
                                                               verbose_name='部门')
    department_turn_over_target = models.FloatField(null=True, blank=True, verbose_name='离职率目标')
    department_turn_over_target_effect_date = models.DateField(null=True, blank=True, verbose_name='生效时间')
    department_turn_over_target_expire_date = models.DateField(null=True, blank=True, verbose_name='失效时间')
    department_turn_over_target_status = models.BooleanField(default=True, verbose_name='是否生效')

    class Meta:
        managed = True
        db_table = 'hr_department_turn_over_target'
        verbose_name_plural = '部门离职率目标表'
        verbose_name = '部门离职率目标表'




# class HrEmployeeHistory(models.Model):
#     employee_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='姓名')
#     employee_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='工号')
#     employee_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='联系电话')
#     employee_nationality = models.CharField(max_length=255, null=True, blank=True, verbose_name='国籍')
#     employee_email = models.CharField(max_length=255, null=True, blank=True, verbose_name='邮箱')
#     employee_department = models.ForeignKey(to=HrDepartment, on_delete=models.DO_NOTHING, db_constraint=False,
#                                             null=True, blank=True,
#                                             verbose_name='部门')
#     employee_position = models.ForeignKey(to=HrPosition, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
#                                           blank=True,
#                                           verbose_name='岗位')
#     employee_status = models.CharField(max_length=10, null=True, blank=True,
#                                        choices=(('1', '在职'), ('2', '离职'), ('99', '黑名单')), verbose_name='状态')
#     employee_dl = models.CharField(max_length=10, null=True, blank=True,
#                                    choices=(('DL', 'DL'), ('IDL', 'IDL'), ('SAL', 'SAL')), verbose_name='dl/idl/sal')
#     employee_sex = models.CharField(max_length=10, null=True, blank=True, choices=(('1', '男'), ('2', '女')),
#                                     verbose_name='性别')
#     employee_identity_type = models.CharField(max_length=10, null=True, blank=True, choices=(
#         ('1', '身份证'), ('2', '行驶证'), ('3', '驾驶证'), ('4', '护照'), ('5', '其他')), verbose_name='证件类型')
#     employee_work_place = models.CharField(max_length=255, null=True, blank=True, verbose_name='工作地')
#     employee_process= models.CharField(max_length=255, null=True, blank=True, verbose_name='工序')
#     employee_dim_reason = models.ForeignKey(to=HrDimissionReason, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
#                                           blank=True,
#                                           verbose_name='离职原因')
#     employee_dim_type = models.ForeignKey(to=HrDimissionType, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
#                                           blank=True,
#                                           verbose_name='离职类型')
#     employee_identity_no = models.CharField(max_length=255, null=True, blank=True, verbose_name='证件号码')
#     employee_job_duty = models.ForeignKey(to=HrJobDuty, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
#                                           blank=True, verbose_name='职务')
#     employee_job_class = models.ForeignKey(to=HrJobClass, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
#                                            blank=True,
#                                            verbose_name='职等')
#     employee_job_grade = models.ForeignKey(to=HrJobGrade, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
#                                            blank=True,
#                                            verbose_name='职级')
#     employee_pay_type = models.ForeignKey(to=HrPayType, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
#                                           blank=True,
#                                           verbose_name='计薪方式')
#
#     employee_job_rank = models.ForeignKey(to=HrJobRank, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
#                                           blank=True,
#                                           verbose_name='合同归属')
#
#     employee_job_sequence = models.ForeignKey(to=HrJobSequence, on_delete=models.DO_NOTHING,
#                                                    db_constraint=False, null=True,
#                                                    blank=True,
#                                                    verbose_name='职级序列')
#     employee_join_date = models.DateTimeField(null=True, blank=True, verbose_name='入职日期')
#     employee_group_join_date = models.DateTimeField(null=True, blank=True, verbose_name='集团入职日期')
#     employee_departure_date = models.DateTimeField(null=True, blank=True, verbose_name='离职结薪日期')
#     employee_departure_notice_date = models.DateTimeField(null=True, blank=True, verbose_name='离职通报日期')
#     employee_departure_handle_date = models.DateTimeField(null=True, blank=True, verbose_name='离职办理日期')
#     employee_plan_turn_date = models.DateTimeField(null=True, blank=True, verbose_name='预转正日期')
#     employee_turn_date = models.DateTimeField(null=True, blank=True, verbose_name='转正日期')
#     employee_turn_status = models.CharField(max_length=255, null=True, blank=True, verbose_name='转正状态')
#     employee_nation = models.ForeignKey(to=HrNation, on_delete=models.DO_NOTHING, db_constraint=False, null=True,
#                                         blank=True,
#                                         verbose_name='民族')
#     employee_nation_place = models.ForeignKey(to=HrNationPlace, on_delete=models.DO_NOTHING, db_constraint=False,
#                                               null=True, blank=True,
#                                               verbose_name='籍贯')
#     employee_marriage_status = models.CharField(max_length=10, null=True, blank=True,
#                                                 choices=(('0', '未婚'), ('1', '已婚'), ('2', '离异')), verbose_name='婚姻状况')
#     employee_identity_no_effective_date = models.DateField(null=True, blank=True, verbose_name='身份证生效日期')
#     employee_identity_no_failre_date = models.DateField(null=True, blank=True, verbose_name='身份证失效日期')
#     employee_birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
#     employee_nation_address = models.CharField(max_length=255, null=True, blank=True, verbose_name='户籍地址')
#     employee_work_status = models.CharField(max_length=10, null=True, blank=True,
#                                             choices=(('正式工', '正式工'), ('实习生', '实习生'), ('试用期', '试用期'), ('劳务工', '劳务工'),
#                                                      ('产线承包', '产线承包'), ('顾问', '顾问'), ('', '')), verbose_name='在职状态')
#     employee_political_status = models.CharField(max_length=10, null=True, blank=True,
#                                                  choices=(('党员', '党员'), ('预备党员', '预备党员'), ('群众', '群众')),
#                                                  verbose_name='政治面貌')
#     employee_work_experience_text = models.TextField(null=True, blank=True, verbose_name='工作经历')
#     employee_emergency_contact = models.CharField(max_length=255, null=True, blank=True, verbose_name='紧急联系人')
#     employee_emergency_contact_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='紧急联系人电话')
#     employee_emergency_contact_relation = models.CharField(max_length=255, null=True, blank=True,
#                                                            verbose_name='紧急联系人关系')
#     employee_first_degree = models.ForeignKey(to=HrEducationDegree, on_delete=models.DO_NOTHING, null=True, blank=True,
#                                               db_constraint=False,
#                                               verbose_name='第一学历')
#     employee_first_degree_school = models.CharField(max_length=255, null=True, blank=True, verbose_name='第一学历学校')
#     employee_first_degree_major = models.CharField(max_length=255, null=True, blank=True, verbose_name='第一学历专业')
#     employee_first_degree_graduate_date = models.DateTimeField(null=True, blank=True, verbose_name='第一学历毕业日期')
#     employee_first_degree_type = models.CharField(max_length=10, null=True, blank=True,
#                                                   choices=(('全日制', '全日制'), ('非全日制', '非全日制')), verbose_name='第一学历教育方式')
#     employee_train_degree = models.CharField(max_length=255, null=True, blank=True, verbose_name='进修学历')
#     employee_train_degree_school = models.CharField(max_length=255, null=True, blank=True, verbose_name='进修学历学校')
#     employee_train_degree_major = models.CharField(max_length=255, null=True, blank=True, verbose_name='进修学历专业')
#     employee_train_degree_graduate_date = models.DateTimeField(null=True, blank=True, verbose_name='进修学历毕业日期')
#     employee_train_degree_type = models.CharField(max_length=10, null=True, blank=True,
#                                                   choices=(('01', '全日制'), ('02', '自考'), ('03', '远程教育'), ('04', '成人高考')),
#                                                   verbose_name='进修学历教育方式')
#     employee_labor_source = models.CharField(max_length=255, null=True, blank=True, verbose_name='劳务来源')
#     employee_bank_no = models.CharField(max_length=255, null=True, blank=True, verbose_name='银行卡号')
#     employee_bank_deposit = models.CharField(max_length=255, null=True, blank=True, verbose_name='开户银行')
#     employee_record_begin_time= models.DateTimeField(null=True, blank=True,verbose_name='记录开始时间')
#     employee_record_end_time = models.DateTimeField(null=True, blank=True, verbose_name='记录结束时间')
#     employee_record_time = models.DateTimeField(null=True, blank=True,auto_now_add=True, verbose_name='记录时间')
#     employee_record_type=models.CharField(max_length=10, null=True, blank=True,choices=(('1', '周'), ('2', '月')), verbose_name='记录类型')
#
#
#     class Meta:
#         managed = True
#         db_table = 'hr_employee_history'
#         verbose_name_plural = '员工信息历史表'
#         verbose_name = '员工信息历史表'
#


class EditRecord(models.Model):
    employee = models.ForeignKey(to=HrEmployee, on_delete=models.DO_NOTHING, db_constraint=False,
                                 null=True, blank=True,
                                 verbose_name='员工')
    edit_type = models.CharField(max_length=100, null=True, blank=True, verbose_name="修改类型")
    old_data = models.TextField(blank=True, null=True, verbose_name="原数据")
    edit_data = models.TextField(blank=True, null=True, verbose_name="新数据")
    select_edit_data = models.TextField(blank=True, null=True, verbose_name="差异数据")
    select_edit_data_pre = models.TextField(blank=True, null=True, verbose_name="差异前数据")
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='申请时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    read_time = models.DateTimeField(blank=True, null=True, verbose_name='查看时间')
    edit_status_choices = ((1, '待审核'), (2, '已审核'), (3, '退回'))
    edit_status = models.IntegerField(default=1, choices=edit_status_choices, blank=True, null=True,
                                      verbose_name='处理状态')
    editor = models.ForeignKey(AdminUser, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='修改者',
                               related_name='editor',
                               db_constraint=False)
    remark = models.TextField(blank=True, null=True, verbose_name='备注')
    status = models.BooleanField(default=True, verbose_name="是否有效")

    class Meta:
        managed = True
        db_table = 'hr_employee_edit_record'
        verbose_name_plural = '员工编辑记录表'
        verbose_name = '员工编辑记录表'