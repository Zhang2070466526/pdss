from django.db import models


# Create your models here.

# python manage.py makemigrations competeRestrictions
# python manage.py migrate competeRestrictions


class CompeteRestrictionsFile(models.Model):  # 竞业限制文件表
    name = models.CharField(max_length=255, default='', verbose_name='文件名')
    url = models.CharField(max_length=255, default='', verbose_name='文件路径')

    file_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')

    class Meta:
        managed = True
        db_table = 'CompeteRestrictionsFile'
        verbose_name_plural = '竞业限制文件表'
        verbose_name = '竞业限制文件表'


class CompeteRestrictions(models.Model):  # 竞业限制表

    people = models.ForeignKey(to='CompeteRestrictionsWhitelist', on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='竞业人员', related_name='people', db_constraint=False)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='姓名')
    idCard = models.CharField(max_length=255, null=True, blank=True, verbose_name='身份证号')
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='联系电话')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='联系地址')
    cycleData = models.DateField(blank=True, null=True, verbose_name="竞业周期")
    # cycleBeginData = models.DateField(blank=True, null=True, verbose_name="竞业开始日期")
    # cycleEndData = models.DateField(blank=True, null=True, verbose_name="竞业结束日期")
    lon = models.CharField(max_length=255, null=True, blank=True, verbose_name='经度')
    lat = models.CharField(max_length=255, null=True, blank=True, verbose_name='纬度')
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name='位置')

    photograph_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='强制拍照',
                                             related_name='photograph_file', db_constraint=False)
    insured_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='参保证明',
                                          related_name='insured_file', db_constraint=False)
    incomeTax_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='所得税缴税证明',
                                            related_name='incomeTax_file', db_constraint=False)
    accumulationFund_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='公积金账户信息',
                                                   related_name='accumulationFund_file', db_constraint=False)
    workPhotos_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='工作照片',
                                             related_name='workPhotos_file', db_constraint=False)
    workVideo_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='工作视频',
                                            related_name='workVideo_file', db_constraint=False)
    dailyPhotos_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='日常照片',
                                              related_name='dailyPhotos_file', db_constraint=False)
    dailyVideo_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='日常视频',
                                             related_name='dailyVideo_file', db_constraint=False)
    incumbency_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='在职证明',
                                             related_name='incumbency_file', db_constraint=False)
    noWork_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='无工作承诺函',
                                         related_name='noWork_file', db_constraint=False)

    cllBack_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='电话回访',
                                         related_name='cllBack_file', db_constraint=False)
    firstlivevideo_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='实时视频(第一次)',
                                         related_name='firstlivevideo_file', db_constraint=False)
    secondlivevideo_file = models.ManyToManyField(to='CompeteRestrictionsFile', verbose_name='实时视频(第二次)',
                                         related_name='secondlivevideo_file', db_constraint=False)


    compete_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='compete_creator', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='compete_modifier', db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'CompeteRestrictions'
        verbose_name_plural = '竞业限制表'
        verbose_name = '竞业限制表'


class CompeteRestrictionsWhitelist(models.Model):  # 竞业限制人员白名单表
    cr_base = models.ForeignKey(to='general.center_base', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='公司', related_name='cr_base',
                                db_constraint=False)
    # people = models.ForeignKey(to='CompeteRestrictions', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='竞业人员', related_name='people', db_constraint=False)
    contract = models.CharField(max_length=255, null=True, blank=True, verbose_name='合同归属')
    isExpiration = models.BooleanField(default=False,
                                       verbose_name='是否届满')  # true 届满  false 未届满  届满：开始和结束日期内有几个月 ，限制表就有几条记录
    workNumber = models.CharField(max_length=255, null=True, blank=True, verbose_name='工号')
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='姓名')
    idCard = models.CharField(max_length=255, null=True, blank=True, verbose_name='身份证号')
    cycleBeginData = models.DateField(blank=True, null=True, verbose_name="竞业开始日期")
    cycleEndData = models.DateField(blank=True, null=True, verbose_name="竞业结束日期")
    # jobRank_choices = (
    #     (1, '江苏润阳新能源科技股份有限公司'),(2,'润阳新能源（上海）有限公司'), (3, '苏州润矽光伏科技有限公司'), (4, '盐城润宝电力科技有限公司'),
    #     (5, '江苏润阳悦达光伏科技有限公司'),
    #     (6, '江苏润阳光伏科技有限公司'), (7, '江苏润阳世纪光伏科技有限公司'),
    #     (8, '云南润阳世纪光伏科技有限公司'), (9, '江苏海博瑞光伏科技有限公司'), (10, '宁夏润阳硅材料科技有限公司'),
    #     (11, '内蒙古润阳悦达新能源科技有限公司')
    # )
    # jobRank = models.SmallIntegerField(verbose_name='合同归属', choices=jobRank_choices)




    compete_remark = models.TextField(null=True, blank=True, verbose_name='备注')
    compete_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='competeWhitelist_creator', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='competeWhitelist_modifier', db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'CompeteRestrictionsWhitelist'
        verbose_name_plural = '竞业限制白名单表'
        verbose_name = '竞业限制白名单表'
