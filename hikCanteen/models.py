from django.db import models


# python manage.py makemigrations hikCanteen
# python manage.py migrate hikCanteen

# Create your models here.
class MonthmoneyToOAList(models.Model):
    month = models.DateField(blank=True, null=True, verbose_name="周期")
    status = models.BooleanField(default=True, verbose_name='是否在职')  # 0 离职  1 是在职
    # jobRankCode = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True,
    #                                 verbose_name='公司', related_name='jobRankCode',
    #                                 db_constraint=False)
    jobRankCode = models.ForeignKey(to='JobRank', on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name='合同归属', related_name='jobRankCode',
                                    db_constraint=False)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='姓名')

    departmentCode = models.CharField(max_length=255, null=True, blank=True, verbose_name='部门号')
    departmentName = models.CharField(max_length=255, null=True, blank=True, verbose_name='部门名称')
    code = models.CharField(max_length=255, null=True, blank=True, verbose_name='工号')
    jobLevelName = models.CharField(max_length=255, null=True, blank=True, verbose_name='岗位级别名称')
    postName = models.CharField(max_length=255, null=True, blank=True, verbose_name='岗位名称')

    # jobRankName= models.CharField(max_length=255, null=True, blank=True, verbose_name='合同归属')
    # jobRankCode = models.CharField(max_length=255, null=True, blank=True, verbose_name='合同归属id')

    # 润阳东方   建湖二期    悦达新实业  润阳悦达   上海新能源  润阳新能源

    # 充值日期这个月10号 month是充值日期上个月    就是sql月份
    SeparationDate = models.DateField(blank=True, null=True, verbose_name='最后结薪日期')
    balance = models.CharField(max_length=255, null=True, blank=True, verbose_name='余额')
    butie_sum = models.FloatField(null=True, blank=True, verbose_name='补贴总和')
    entryCanteenAmount = models.FloatField(null=True, blank=True, verbose_name='统一充值金额')

    baibanchuqin = models.FloatField(null=True, blank=True, verbose_name='白班出勤')
    baibanbutie = models.FloatField(null=True, blank=True, verbose_name='白班补贴')
    yebanchuqin = models.FloatField(null=True, blank=True, verbose_name='夜班出勤')
    yebanbutie = models.FloatField(null=True, blank=True, verbose_name='夜班补贴')
    qiangzhuanbanchuqin = models.FloatField(null=True, blank=True, verbose_name='强转班出勤')
    qiangzhuanbanbutie = models.FloatField(null=True, blank=True, verbose_name='强转班补贴')
    zhoumojiaban = models.FloatField(null=True, blank=True, verbose_name='周末加班')
    zhoumojiabanbutie = models.FloatField(null=True, blank=True, verbose_name='周末加班补贴')
    jiaban_gt_2 = models.FloatField(null=True, blank=True, verbose_name='加班大于2')
    jiaban_gt_2_butie = models.FloatField(null=True, blank=True, verbose_name='加班大于2补贴')
    jiaban_gt_5 = models.FloatField(null=True, blank=True, verbose_name='加班大于5')
    jiaban_gt_5_butie = models.FloatField(null=True, blank=True, verbose_name='加班大于5补贴')
    jiaban_gt_7_5 = models.FloatField(null=True, blank=True, verbose_name='加班大于7.5')
    jiaban_gt_7_5_butie = models.FloatField(null=True, blank=True, verbose_name='加班大于7.5补贴')
    jiaban_gt_10 = models.FloatField(null=True, blank=True, verbose_name='加班大于10')
    jiaban_gt_10_butie = models.FloatField(null=True, blank=True, verbose_name='加班大于10补贴')
    jiaban_gt_12_5 = models.FloatField(null=True, blank=True, verbose_name='加班大于12.5')
    jiaban_gt_12_5_butie = models.FloatField(null=True, blank=True, verbose_name='加班大于12.5补贴')
    qingjia_gt_4 = models.FloatField(null=True, blank=True, verbose_name='请假大于4,责任制')  # 次数
    qingjia_lt_7_5 = models.FloatField(null=True, blank=True, verbose_name='请假小于7.5')  # 次数
    qingjia_gt_7_5 = models.FloatField(null=True, blank=True, verbose_name='请假大于7.5')  # 次数


    chuqin_sum = models.FloatField(null=True, blank=True, verbose_name='出勤总和')
    butie_sum = models.FloatField(null=True, blank=True, verbose_name='补贴总和')
    entryCanteenAmount = models.FloatField(null=True, blank=True, verbose_name='统一充值金额')
    realEntryCanteenAmount = models.FloatField(null=True, blank=True, verbose_name='实际充值金额')
    amount_to_replenished = models.FloatField(null=True, blank=True, verbose_name='应退/应补金额')  # 应退/应补金额 =   余额- （应剩余金额= 960-补贴总和）
    amount_to_quarter = models.FloatField(null=True, blank=True, verbose_name='季度返现金额')  # 季度返现金额
    # 余额+统一充值金额 >944   4 7 10 1 月计算
    # 钱>944   -744  返回944-744的钱
    month_money_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者',
                                related_name='month_money_creator', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者',
                                 related_name='month_money_modifier', db_constraint=False)

    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    is_recharge = models.BooleanField(default=False, verbose_name='是否已充值')

    class Meta:
        managed = True
        db_table = 'month_money_to_oa_list'
        verbose_name_plural = '人员出勤表'
        verbose_name = '人员出勤表'


#         充值日期  周期下个月的十号  出勤天数=baibanchuqin+yebanchuqin+qiangzhuanbanchuqin     补贴=yebanbutie+baibanbutie+qiangzhuanbanbutie+各种补贴


class JobRank(models.Model):
    JobRankCode = models.CharField(max_length=255, default='', verbose_name='合同归属编码')
    JobRankName = models.CharField(max_length=255, default='', verbose_name='合同归属名')
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    status = models.BooleanField(default=True, verbose_name='数据是否有效')

    class Meta:
        managed = True
        db_table = 'JobRank'
        verbose_name_plural = '合同归属表'
        verbose_name = '合同归属表'



