from django.db import models


# python manage.py makemigrations volumeContracts
# python manage.py migrate volumeContracts

# Create your models here.
class ContractsJobrank(models.Model):#合同归属
    jobrank_status = models.BooleanField(default=True, verbose_name='合同归属是否有效')
    jobrank_name = models.CharField(blank=True, null=True, max_length=250, verbose_name='合同归属')
    jobrank_address = models.CharField(blank=True, null=True, max_length=250, verbose_name='注册地址')
    jobrank_type = models.CharField(blank=True, null=True, max_length=250, verbose_name='注册类型')
    jobrank_people = models.CharField(blank=True, null=True, max_length=250, verbose_name='法定代表人')
    jobrank_workPlace = models.CharField(blank=True, null=True, max_length=250, verbose_name='工作地')

    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='jobrank_creator', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='jobrank_modifier', db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'ContractsJobrank'
        verbose_name_plural = '合同归属管理表'
        verbose_name = '合同归属管理表'


class ContractsInfo(models.Model):  # 合同信息表
    approval_status = models.BooleanField(default=False, verbose_name='是否已审核')
    code = models.CharField(max_length=255, null=True, blank=True, verbose_name='工号')
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='姓名')
    contracts_gender_choices = (
        (0, '男'), (1, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=contracts_gender_choices)
    contracts_origin_choices = (
        (
            1,
            '北京市'
        ),
        (
            2,
            '天津市'
        ),
        (
            3,
            '河北省'
        ),
        (
            4,
            '山西省'
        ),
        (
            5,
            '内蒙古自治区'
        ),
        (
            6,
            '辽宁省'
        ),
        (
            7,
            '吉林省'
        ),
        (
            8,
            '黑龙江省'
        ),
        (
            9,
            '上海市'
        ),
        (
            10,
            '江苏省'
        ),
        (
            11,
            '浙江省'
        ),
        (
            12,
            '安徽省'
        ),
        (
            13,
            '福建省'
        ),
        (
            14,
            '江西省'
        ),
        (
            15,
            '山东省'
        ),
        (
            16,
            '河南省'
        ),
        (
            17,
            '湖北省'
        ),
        (
            18,
            '湖南省'
        ),
        (
            19,
            '广东省'
        ),
        (
            20,
            '广西壮族自治区'
        ),
        (
            21,
            '海南省'
        ),
        (
            22,
            '重庆市'
        ),
        (
            23,
            '四川省'
        ),
        (
            24,
            '贵州省'
        ),
        (
            25,
            '云南省'
        ),
        (
            26,
            '西藏自治区'
        ),
        (
            27,
            '陕西省'
        ),
        (
            28,
            '甘肃省'
        ),
        (
            29,
            '青海省'
        ),
        (
            30,
            '宁夏回族自治区'
        ),
        (
            31,
            '新疆维吾尔自治区'
        ),
        (
            32,
            '台湾省'
        ),
        (
            33,
            '香港特别行政区'
        ),
        (
            34,
            '澳门特别行政区'
        ),
    )
    nativePlaceId = models.SmallIntegerField(verbose_name='籍贯', choices=contracts_origin_choices)
    idCard = models.CharField(max_length=255, null=True, blank=True, verbose_name='身份证号')
    birthday = models.DateField(blank=True, null=True, verbose_name="出生日期")
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='手机号')
    entryData = models.DateField(blank=True, null=True, verbose_name="入职日期")
    contracts_politicalLandscape_choices = (
        (
            1,
            "党员"
        ),
        (
            2,
            "预备党员"
        ),
        (
            3,
            "群众"
        )
    )
    politicsStatus = models.SmallIntegerField(verbose_name='政治面貌', choices=contracts_politicalLandscape_choices)
    contracts_natureOfAccount_choices = (
        (0, '农业户口'), (1, '非农户口')
    )
    accountNature = models.SmallIntegerField(verbose_name='户口性质', choices=contracts_natureOfAccount_choices)
    domicileAddress = models.CharField(max_length=255, null=True, blank=True, verbose_name='户籍地址')
    contracts_ethnicGroup_choices = (
        (
            1,
            "汉族"
        ),
        (
            2,
            "蒙古族"
        ),
        (
            3,
            "回族"
        ),
        (
            4,
            "藏族"
        ),
        (
            5,
            "维吾尔族"
        ),
        (
            6,
            "苗族"
        ),
        (
            7,
            "彝族"
        ),
        (
            8,
            "壮族"
        ),
        (
            9,
            "布依族"
        ),
        (
            10,
            "朝鲜族"
        ),
        (
            11,
            "满族"
        ),
        (
            12,
            "侗族"
        ),
        (
            13,
            "瑶族"
        ),
        (
            14,
            "白族"
        ),
        (
            15,
            "土家族"
        ),
        (
            16,
            "哈尼族"
        ),
        (
            17,
            "哈萨克族"
        ),
        (
            18,
            "傣族"
        ),
        (
            19,
            "黎族"
        ),
        (
            20,
            "傈僳族"
        ),
        (
            21,
            "佤族"
        ),
        (
            22,
            "畲族"
        ),
        (
            23,
            "高山族"
        ),
        (
            24,
            "拉祜族"
        ),
        (
            25,
            "水族"
        ),
        (
            26,
            "东乡族"
        ),
        (
            27,
            "纳西族"
        ),
        (
            28,
            "景颇族"
        ),
        (
            29,
            "柯尔克孜族"
        ),
        (
            30,
            "土族"
        ),
        (
            31,
            "达斡尔族"
        ),
        (
            32,
            "仫佬族"
        ),
        (
            33,
            "羌族"
        ),
        (
            34,
            "布朗族"
        ),
        (
            35,
            "撒拉族"
        ),
        (
            36,
            "毛难族"
        ),
        (
            37,
            "仡佬族"
        ),
        (
            38,
            "锡伯族"
        ),
        (
            39,
            "阿昌族"
        ),
        (
            40,
            "普米族"
        ),
        (
            41,
            "塔吉克族"
        ),
        (
            42,
            "怒族"
        ),
        (
            43,
            "乌孜别克族"
        ),
        (
            44,
            "俄罗斯族"
        ),
        (
            45,
            "鄂温克族"
        ),
        (
            46,
            "崩龙族"
        ),
        (
            47,
            "保安族"
        ),
        (
            48,
            "裕固族"
        ),
        (
            49,
            "京族"
        ),
        (
            50,
            "塔塔尔族"
        ),
        (
            51,
            "独龙族"
        ),
        (
            52,
            "鄂伦春族"
        ),
        (
            53,
            "赫哲族"
        ),
        (
            54,
            "门巴族"
        ),
        (
            55,
            "珞巴族"
        ),
        (
            56,
            "基诺族"
        ),
        (
            57,
            "其他"
        )
    )
    nationId = models.SmallIntegerField(verbose_name='民族', choices=contracts_ethnicGroup_choices)
    legalAddress = models.CharField(max_length=255, null=True, blank=True, verbose_name='法定送达地址')
    contracts_maritalStatus_choices = (
        (1, '未婚'), (0, '已婚'),
    )
    marriage = models.SmallIntegerField(verbose_name='婚姻状况', choices=contracts_maritalStatus_choices)
    urgentPerson = models.CharField(max_length=255, null=True, blank=True, verbose_name='紧急联系人姓名')
    urgentPersonPhone = models.CharField(max_length=255, null=True, blank=True, verbose_name='紧急联系人电话')
    contracts_emergencyContactRelationships_choices = (
        (0, '父母'), (1, '配偶'), (2, '兄弟姐妹'), (3, '其他')
    )
    urgentRelation = models.SmallIntegerField(verbose_name='与紧急联系人关系',
                                              choices=contracts_emergencyContactRelationships_choices)
    contracts_highestEducation_choices = (
        (0, '高中及以下'),
        (1, '中专'),
        (2, '大专'),
        (3, '本科'),
        (4, '硕士'),
        (5, '博士及以上')
    )
    latestDegreeId = models.SmallIntegerField(verbose_name='最高学历', choices=contracts_highestEducation_choices)
    graduateTime = models.DateField(blank=True, null=True, verbose_name="最高学历毕业时间")
    graduateInsituation = models.CharField(max_length=255, null=True, blank=True, verbose_name='毕业学校')
    major = models.CharField(max_length=255, null=True, blank=True, verbose_name='毕业专业')
    contracts_educationalMethods_choices = (
        (0, '全日制'), (1, '非全日制'),
    )
    educateMethod = models.SmallIntegerField(verbose_name='教育方式', choices=contracts_educationalMethods_choices)
    bankIdCard = models.CharField(max_length=255, null=True, blank=True, verbose_name='卡号')
    openBank = models.CharField(max_length=255, null=True, blank=True, verbose_name='开户银行')
    contractExpirationDate = models.DateField(blank=True, null=True, verbose_name="合同到期日")
    probation = models.IntegerField(null=True, blank=True, verbose_name='试用期(月)')
    summerSize_choices = (
        (0, 'XS'), (1, 'S'), (2, 'M'), (3, 'L'),
        (4, 'XL'), (5, 'XXL'),
        (6, '3XL'), (7, '4XL'), (8, '5XL'), (9, '其他')
    )
    summerSize = models.SmallIntegerField(verbose_name='夏装尺寸', choices=summerSize_choices)
    height = models.CharField(max_length=255, null=True, blank=True, verbose_name='身高')
    weight = models.CharField(max_length=255, null=True, blank=True, verbose_name='体重')
    bust = models.CharField(max_length=255, null=True, blank=True, verbose_name='胸围')
    bellyCircumference = models.CharField(max_length=255, null=True, blank=True, verbose_name='肚围')
    department = models.CharField(max_length=255, null=True, blank=True, verbose_name='部门')

    contracts_posts = models.CharField(max_length=255, null=True, blank=True, verbose_name='岗位', default='追光者')

    # placeWorkOptions=(
    #     ( 0, '盐城'), ( 1, "上海"), ( 2, "昆山"), ( 3, "建湖"),
    #     ( 1, "云南"),
    #     ( 1, "宁夏"), ( 1, "内蒙古")
    # )
    # contracts_placeWork = models.SmallIntegerField(verbose_name='工作地',choices=summerSize_choices)
    contracts_placeWork = models.CharField(max_length=255, null=True, blank=True, verbose_name='工作地')
    base_salary = models.IntegerField(null=True, blank=True, verbose_name='基本工资')
    jobRank_choices = (
        (1, '江苏润阳新能源科技股份有限公司'),(2,'润阳新能源（上海）有限公司'), (3, '苏州润矽光伏科技有限公司'), (4, '盐城润宝电力科技有限公司'),
        (5, '江苏润阳悦达光伏科技有限公司'),
        (6, '江苏润阳光伏科技有限公司'), (7, '江苏润阳世纪光伏科技有限公司'),
        (8, '云南润阳世纪光伏科技有限公司'), (9, '江苏海博瑞光伏科技有限公司'), (10, '宁夏润阳硅材料科技有限公司'),
        (11, '内蒙古润阳悦达新能源科技有限公司')
    )
    jobRank = models.SmallIntegerField(verbose_name='合同归属', choices=jobRank_choices)

    # jobRank = models.ForeignKey(to='ContractsJobrank', on_delete=models.SET_NULL, null=True, blank=True,
    #                                         verbose_name='合同归属', related_name='jobRank',
    #                                         db_constraint=False)

    contracts_infoFile = models.ManyToManyField(to='volumeContracts.ContractsFile', verbose_name='合同文档',
                                                related_name='contracts_infoFile', db_constraint=False)
    pic_file=models.CharField(max_length=255, null=True, blank=True, verbose_name='上传照片')

    # contracts_basicInfo = models.ForeignKey(to='volumeContracts.ContractsFile', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='基本信息表',related_name='contracts_basicInfo', db_constraint=False)
    # contracts_onboardingInfo = models.ForeignKey(to='volumeContracts.ContractsFile',  on_delete=models.SET_NULL, null=True, blank=True, verbose_name='入职资料表',related_name='contracts_onboardingInfo', db_constraint=False)
    # contracts_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    contracts_remark = models.TextField(null=True,blank=True, verbose_name='备注')
    contracts_status = models.BooleanField(default=True, verbose_name='数据是否有效')

    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='contracts_creator', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='contracts_modifier', db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'contractsinfo'
        verbose_name_plural = '合同信息表'
        verbose_name = '合同信息表'


class ContractsFile(models.Model):
    file_status = models.BooleanField(default=True, verbose_name='文件是否有效')
    name = models.CharField(blank=True, null=True, max_length=250, verbose_name='文件名称')
    url = models.CharField(blank=True, null=True, max_length=250, verbose_name='文件路径')
    file_choices = (
        (2, '入职资料-润阳新能源（合同、保密、竞业）.docx'),
        (1, '基本信息表、法律送达文书、重要事项、反腐败等.docx'),
    )
    filetype = models.SmallIntegerField(verbose_name='文件类型', choices=file_choices)
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='file_creator', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='file_modifier', db_constraint=False)
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'contractsfile'
        verbose_name_plural = '合同文件管理表'
        verbose_name = '合同文件管理表'



