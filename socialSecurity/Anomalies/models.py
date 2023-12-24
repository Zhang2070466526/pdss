from django.db import models

# Create your models here.
# python manage.py makemigrations socialSecurity
# python manage.py migrate socialSecurity


class SocialSecurityInsuranceType(models.Model):   #社保险种
    insurance_type_name = models.CharField(max_length=255, verbose_name='险种名称')
    insurance_type_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    class Meta:
        managed = True
        db_table = 'social_security_insurance_type'
        verbose_name_plural = '社保险种表'
        verbose_name = '社保险种表'


class SocialSecurityAnomalies(models.Model):   #社保异常表
    anomalies_people = models.ForeignKey(to='employee.HrEmployee', on_delete=models.DO_NOTHING, db_constraint=False,
                                       null=True, blank=True, verbose_name='员工')
    anomalies_fail_reason=models.TextField(null=True,blank=True, verbose_name='增员失败原因')   #唯一
    # anomalies_insurance_type=models.CharField(max_length=255, null=True, blank=True,  verbose_name='险种')
    anomalies_insurance_type = models.ForeignKey(to=SocialSecurityInsuranceType, on_delete=models.DO_NOTHING, db_constraint=False,
                                       null=True, blank=True, verbose_name='社保险种')
    anomalies_month = models.DateField(blank=True, null=True, verbose_name="月份")
    anomalies_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    anomalies_approval_status = models.IntegerField(null=True, blank=True,default=1, verbose_name='审批状态')    #1是未审批 2是已驳回  3是已审批
    anomalies_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    anomalies_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='创建者', related_name='anomalies_creator', db_constraint=False)
    anomalies_modifier= models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='修改者',related_name='anomalies_modifier')
    anomalies_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    anomalies_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    class Meta:
        managed = True
        db_table = 'social_security_anomalies'
        verbose_name_plural = '员工社保异常表'
        verbose_name = '员工社保异常表'


class SocialSecurityAnomaliesResults(models.Model):   #社保异常结果表
    results_people = models.ForeignKey(to='employee.HrEmployee', on_delete=models.DO_NOTHING, db_constraint=False,null=True, blank=True, verbose_name='员工')
    results_anomalies=models.ForeignKey(to=SocialSecurityAnomalies, on_delete=models.SET_NULL, null=True, blank=True,verbose_name='员工异常记录', related_name='results_anomalies', db_constraint=False)
    return_dispose=models.TextField(null=True, blank=True, verbose_name='需如何处理')
    return_cause = models.TextField(null=True, blank=True, verbose_name='增员退回原因')
    results_process = models.TextField(null=True, blank=True, verbose_name='员工处理结果')
    results_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    results_frequency = models.IntegerField(default=0,verbose_name='当前次数') #1是未驳回,一次通过,2以后就是有驳回记录了
    results_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='创建者', related_name='results_creator', db_constraint=False)
    results_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='修改者',related_name='results_modifier')
    results_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    results_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    class Meta:
        managed = True
        db_table = 'social_security_anomalies_results'
        verbose_name_plural = '员工社保异常结果表'
        verbose_name = '员工社保异常结果表'




class SocialSecurityFiles(models.Model):   #社保文件表
    file_choices = (
        (1, '员工凭证'),
    )
    file_type = models.SmallIntegerField(verbose_name='文件类型', choices=file_choices)
    file_name = models.CharField(max_length=255, default='', verbose_name='文件名')
    file_url = models.CharField(max_length=255, default='', verbose_name='文件路径')
    file_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    anomalies_file = models.ForeignKey(to=SocialSecurityAnomalies, on_delete=models.SET_NULL, null=True, blank=True,
                                      verbose_name='凭证文件', related_name='anomalies_file', db_constraint=False)
    file_create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    file_create = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                     verbose_name='创建者', related_name='file_create', db_constraint=False)
    class Meta:
        managed = True
        db_table = 'social_security_files'
        verbose_name_plural = '员工社保文件表'
        verbose_name = '员工社保文件表'

