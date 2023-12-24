from django.db import models


# python manage.py makemigrations expatriateRecord
# python manage.py migrate expatriateRecord

# Create your models here.

class ExpatriateInfoList(models.Model):  # 外派信息
    code = models.CharField(max_length=255, null=True, blank=True, verbose_name='工号')
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='姓名')
    abbreviation_Dept = models.CharField(max_length=255, null=True, blank=True, verbose_name='部门简称')
    passport = models.CharField(max_length=255, null=True, blank=True, verbose_name='护照号')
    idCard = models.CharField(max_length=255, null=True, blank=True, verbose_name='身份证号码')
    # base_Attribution = models.CharField(max_length=255, null=True, blank=True, verbose_name='基地归属')
    post = models.CharField(max_length=255, null=True, blank=True, verbose_name='岗位名称')
    date_Of_Entry = models.DateTimeField(blank=True, null=True, verbose_name="入职日期")
    expatriate_Dept = models.CharField(max_length=255, null=True, blank=True, verbose_name="外派部门")  #部门名称


    expatriate_jobClass = models.CharField(max_length=255, null=True, blank=True, verbose_name="职等")
    expatriate_country = models.CharField(max_length=255, null=True, blank=True, verbose_name="外派国家")
    expatriate_several_frequency= models.IntegerField(null=True, blank=True, verbose_name="第几次外派")
    expatriate_hardship = models.CharField(max_length=255, null=True, blank=True, verbose_name="艰苦补贴")
    expatriate_life = models.CharField(max_length=255, null=True, blank=True, verbose_name="生活补贴")
    expatriate_other = models.CharField(max_length=255, null=True, blank=True, verbose_name="其他")
    expatriate_allowance_currency= models.CharField(max_length=255, null=True, blank=True, verbose_name="津贴币种")


    expatriate_jobRank = models.CharField(max_length=255, null=True, blank=True, verbose_name="合同归属")
    expatriate_Before_Base = models.CharField(max_length=255, null=True, blank=True, verbose_name="外派前中心/事业部")
    expatriate_Before_Manage = models.CharField(max_length=255, null=True, blank=True, verbose_name="外派前管理归属")    #基地归属
    expatriate_Before_Factory = models.CharField(max_length=255, null=True, blank=True, verbose_name="外派前厂区")
    resident_Dept = models.CharField(max_length=255, null=True, blank=True, verbose_name="派驻部门")
    expatriate_Cycle = models.CharField(max_length=255, null=True, blank=True, verbose_name="外派周期")
    expatriate_Begin = models.DateField(blank=True, null=True, verbose_name="外派起始时间")
    expatriate_End = models.DateField(blank=True, null=True, verbose_name="外派结束时间")
    isCross_Division = models.BooleanField(default=False, verbose_name='是否跨事业部')
    expatriate_After_Base = models.CharField(max_length=255, null=True, blank=True, verbose_name="外派后中心/事业部")
    expatriate_After_Manage = models.CharField(max_length=255, null=True, blank=True, verbose_name="外派后管理归属")
    expatriate_After_Factory = models.CharField(max_length=255, null=True, blank=True, verbose_name="外派后厂区")
    expatriate_Reason = models.TextField(null=True, blank=True, verbose_name='外派缘由说明')
    expatriate_Target = models.TextField(null=True, blank=True, verbose_name='外派工作目标')
    expatriate_Allowance = models.CharField(max_length=255, null=True, blank=True, verbose_name="外派津贴")
    description_Allowance = models.CharField(max_length=255, null=True, blank=True, verbose_name='津贴说明')
    expatriate_Type = models.CharField(max_length=255, null=True, blank=True, verbose_name='外派类型')
    expatriate_After_Cost = models.CharField(max_length=255, null=True, blank=True, verbose_name='外派后成本归属')
    first_Expatriate = models.CharField(max_length=255, null=True, blank=True, verbose_name='首次外派时间')
    last_Expatriate_Begin = models.DateField(blank=True, null=True, verbose_name='上次外派开始时间')
    last_Expatriate_End = models.DateField(blank=True, null=True, verbose_name='上次外派结束时间')
    number_Of_Expatriate = models.IntegerField(null=True, blank=True, verbose_name='外派次数')
    rank = models.CharField(max_length=255, null=True, blank=True, verbose_name='职级')
    isSigned_Expatriate = models.BooleanField(default=False, verbose_name='是否签订外派')
    expatriate_Quality = models.CharField(max_length=255, null=True, blank=True, verbose_name="外派性质")   #长短期
    expatriate_Place = models.CharField(max_length=255, null=True, blank=True, verbose_name="外派地")

    #
    # first_Docking = models.DateField(null=True, blank=True, verbose_name='首次对接日期')
    # application_Approval = models.DateField(null=True, blank=True, verbose_name='BOI申请批文日期')
    # invitation_Letter_Provided = models.DateField(null=True, blank=True, verbose_name='批文_邀请函提供日期')
    # collectInfo = models.DateField(null=True, blank=True, verbose_name='收齐资料日期')
    # submit_Embassy = models.DateField(null=True, blank=True, verbose_name='提交使馆日期')
    # last_SupplementaryInfo = models.DateField(null=True, blank=True, verbose_name='末次补资料日期')
    # signed = models.DateField(null=True, blank=True, verbose_name='出签日期')
    # arrival_Thailand = models.DateField(null=True, blank=True, verbose_name='抵派驻地日期')
    # visa_Application_Remarks = models.CharField(max_length=255, null=True, blank=True, verbose_name='签证申请备注')
    # current_Progress = models.CharField(max_length=255, null=True, blank=True, verbose_name='当前进度')
    # sending_Embassy = models.CharField(max_length=255, null=True, blank=True, verbose_name='送签使馆')
    # system_Post = models.CharField(max_length=255, null=True, blank=True, verbose_name='系统岗位名称')
    # visa_Type = models.CharField(max_length=255, null=True, blank=True, verbose_name='签证类型')
    # visa_Validity_Period_Begin = models.DateField(null=True, blank=True, verbose_name='签证有效期开始时间')
    # visa_Validity_Period_End = models.DateField(null=True, blank=True, verbose_name='签证有效期到期时间')
    # backSign = models.CharField(max_length=255, null=True, blank=True, verbose_name='回头签')
    # visa_Expiration_Date = models.IntegerField(null=True, blank=True, verbose_name='距签证过期日剩余')
    # arrival_Thailand_First = models.DateField(null=True, blank=True, verbose_name='首次抵派驻地日期')
    # report_90 = models.DateField(null=True, blank=True, verbose_name='90天报道申报日')
    # filing_Dead_90 = models.DateField(null=True, blank=True, verbose_name='90天申报截止日')
    # expiration_Article = models.IntegerField(null=True, blank=True, verbose_name='距报道过期日剩余')
    # isAssignOver = models.BooleanField(default=True, verbose_name='外派是否结束_签证是否注销')
    visaledger_info=models.ManyToManyField(to='VisaLedgerInfoList', verbose_name='签证台账',related_name='visaledger_info', db_constraint=False)

    expatriate_passport = models.ManyToManyField(to='ExpatriateFile', verbose_name='护照首页',related_name='expatriate_passport', db_constraint=False)
    expatriate_agreement = models.ManyToManyField(to='ExpatriateFile', verbose_name='外派协议', related_name='expatriate_agreement',db_constraint=False)
    expatriate_remark = models.TextField(null=True, blank=True, verbose_name='信息备注')
    # visaLedger_remark = models.TextField(null=True, blank=True, verbose_name='签证备注')




    status = models.BooleanField(default=True, verbose_name='数据是否有效')
    expatriate_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='expatriate_creator', db_constraint=False)
    expatriate_modifier= models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='expatriate_modifier', db_constraint=False)

    expatriate_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    expatriate_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'expatriateInfoList'
        verbose_name_plural = '外派信息表'
        verbose_name = '外派信息表'


class VisaLedgerInfoList(models.Model):  # 签证台账
    # visa_passport = models.ForeignKey(to='ExpatriateInfoList', on_delete=models.SET_NULL, null=True, blank=True,
    #                            verbose_name='护照号', related_name='visa_passport', db_constraint=False)

    first_Docking = models.DateField(null=True, blank=True, verbose_name='首次对接日期')
    application_Approval = models.DateField(null=True, blank=True, verbose_name='BOI申请批文日期')
    invitation_Letter_Provided = models.DateField(null=True, blank=True, verbose_name='批文_邀请函提供日期')
    collectInfo = models.DateField(null=True, blank=True, verbose_name='收齐资料日期')
    submit_Embassy = models.DateField(null=True, blank=True, verbose_name='提交使馆日期')
    last_SupplementaryInfo = models.DateField(null=True, blank=True, verbose_name='末次补资料日期')
    signed = models.DateField(null=True, blank=True, verbose_name='出签日期')
    arrival_Thailand = models.DateField(null=True, blank=True, verbose_name='抵派驻地日期')
    visa_Application_Remarks = models.CharField(max_length=255, null=True, blank=True, verbose_name='签证申请备注')
    current_Progress = models.CharField(max_length=255, null=True, blank=True, verbose_name='当前进度')
    sending_Embassy = models.CharField(max_length=255, null=True, blank=True, verbose_name='送签使馆')
    system_Post = models.CharField(max_length=255, null=True, blank=True, verbose_name='系统岗位名称')
    visa_Type = models.CharField(max_length=255, null=True, blank=True, verbose_name='签证类型')
    visa_Validity_Period_Begin = models.DateField(null=True, blank=True, verbose_name='签证有效期开始时间')
    visa_Validity_Period_End = models.DateField(null=True, blank=True, verbose_name='签证有效期到期时间')
    backSign = models.CharField(max_length=255, null=True, blank=True, verbose_name='回头签')
    visa_Expiration_Date = models.IntegerField(null=True, blank=True, verbose_name='距签证过期日剩余')
    arrival_Thailand_First = models.DateField(null=True, blank=True, verbose_name='首次抵泰日期')     #非必填
    report_90 = models.DateField(null=True, blank=True, verbose_name='90天报道申报日')
    filing_Dead_90 = models.DateField(null=True, blank=True, verbose_name='90天申报截止日')
    expiration_Article = models.IntegerField(null=True, blank=True, verbose_name='距报道过期日剩余')
    isAssignOver = models.BooleanField(default=False, verbose_name='外派是否结束_签证是否注销')

    visaLedger_remark = models.TextField(null=True, blank=True, verbose_name='备注')

    status = models.BooleanField(default=True, verbose_name='数据是否有效')
    visaLedger_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='visaLedger_creator', db_constraint=False)
    visaLedger_modifier= models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者',related_name='visaLedger_modifier')
    visaLedger_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    visaLedger_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'visaLedgerInfoList'
        verbose_name_plural = '签证台账表'
        verbose_name = '签证台账表'


class TicketLedgerInfoList(models.Model):  # 机票台账
    people = models.ForeignKey(to='ExpatriateInfoList', on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='外派人员', related_name='people', db_constraint=False)
    ticket_code = models.CharField(max_length=255, null=True, blank=True, verbose_name='工号')
    ticket_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='姓名')
    ticket_passport = models.CharField(max_length=255, null=True, blank=True, verbose_name='护照号')
    ticket_time = models.DateTimeField(null=True, blank=True, verbose_name='订票时间')
    flight_date = models.DateField(null=True, blank=True, verbose_name='飞行日期')
    departure = models.CharField(max_length=255, null=True, blank=True, verbose_name='始发地')
    departure_time = models.DateTimeField(null=True, blank=True, verbose_name='起飞时间')
    destination = models.CharField(max_length=255, null=True, blank=True, verbose_name='目的地')
    arrival_time = models.DateTimeField(null=True, blank=True, verbose_name='到达时间')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='价格')

    remark = models.TextField(null=True, blank=True, verbose_name='备注')


    is_assignment= models.CharField(max_length=255, null=True, blank=True, verbose_name='是否去往派驻地')  #是否去往派驻地


    status = models.BooleanField(default=True, verbose_name='数据是否有效')


    ticketLedger_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='ticketLedger_creator', db_constraint=False)
    ticketLedger_modifier= models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者',related_name='ticketLedger_modifier')
    ticketLedger_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    ticketLedger_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'ticketLedgerInfoList'
        verbose_name_plural = '机票台账表'
        verbose_name = '机票台账表'


class ExpatriateFile(models.Model):
    file_status = models.BooleanField(default=True, verbose_name='文件是否有效')
    name = models.CharField(blank=True, null=True, max_length=250, verbose_name='文件名称')
    url = models.CharField(blank=True, null=True, max_length=250, verbose_name='文件路径')
    file_choices = (
        (1, '护照首页'),
        (2, '外派协议'),
    )
    filetype = models.SmallIntegerField(verbose_name='文件类型', choices=file_choices)
    expatriateFile_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='expatriateFile_creator', db_constraint=False)
    expatriateFile_modifier= models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者',related_name='expatriateFile_modifier')
    file_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    file_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'expatriateFile'
        verbose_name_plural = '附件文件管理表'
        verbose_name = '附件文件管理表'







class ImmigrationBase(models.Model):  # 派驻基地表
    base_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='基地名称')
    base_status = models.BooleanField(default=True, verbose_name='部门状态')
    class Meta:
        managed = True
        db_table = 'immigration_base'
        verbose_name_plural = '派驻基地表'
        verbose_name = '派驻基地表'
        indexes = [
            models.Index(fields=['base_name'])
        ]




