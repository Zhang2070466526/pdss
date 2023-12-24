from django.db import models
import employee


# Create your models here.


# python manage.py makemigrations offlineTraining
# python manage.py migrate offlineTraining


class TrainingLecturerLevel(models.Model):  # 讲师级别
    level_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='级别名称')
    level_status = models.BooleanField(default=True, verbose_name='级别状态')

    class Meta:
        managed = True
        db_table = 'training_lecturer_level'
        verbose_name_plural = '讲师级别表'
        verbose_name = '讲师级别表'


class TrainingContentType(models.Model):  # 培训类型
    type_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='类型名称')
    type_parent_id = models.IntegerField(verbose_name='上级id', null=True, blank=True)
    type_first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='第一级类型名称')
    type_second_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='第二级类型名称')
    type_third_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='第三级级类型名称')
    type_status = models.BooleanField(default=True, verbose_name='类型状态')

    class Meta:
        managed = True
        db_table = 'training_content_type'
        verbose_name_plural = '培训类型表'
        verbose_name = '培训类型表'


class TrainingContentCategory(models.Model):  # 培训类别
    category_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='类别名称')
    category_status = models.BooleanField(default=True, verbose_name='类别状态')

    class Meta:
        managed = True
        db_table = 'training_content_category'
        verbose_name_plural = '培训类别表'
        verbose_name = '培训类别表'


class TrainingContentLevel(models.Model):  # 培训层级
    level_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='层级名称')
    level_status = models.BooleanField(default=True, verbose_name='层级状态')

    class Meta:
        managed = True
        db_table = 'training_content_level'
        verbose_name_plural = '培训层级表'
        verbose_name = '培训层级表'


# class TrainingLecturerInterior(models.Model):  # 培训讲师内
#     lecturer_people = models.ForeignKey(to='employee.HrEmployee', on_delete=models.DO_NOTHING, db_constraint=False,
#                                         null=True, blank=True, verbose_name='讲师')
#     lecturer_level = models.ForeignKey(to=TrainingLecturerLevel, on_delete=models.DO_NOTHING, db_constraint=False,
#                                        null=True, blank=True, verbose_name='讲师级别')
#     lecturer_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
#     lecturer_status = models.BooleanField(default=True, verbose_name='数据是否有效')
#     lecturer_creater = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                          verbose_name='创建者', related_name='lecturer_creater', db_constraint=False)
#     lecturer_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                           verbose_name='修改者', related_name='lecturer_modifier')
#     lecturer_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
#     lecturer_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
#
#     class Meta:
#         managed = True
#         db_table = 'training_lecturer_interior'
#         verbose_name_plural = '培训讲师表'
#         verbose_name = '培训讲师表'


class TrainingLecturer(models.Model):  #培训讲师
    lecturer_people = models.ForeignKey(to='employee.HrEmployee', on_delete=models.DO_NOTHING, db_constraint=False,
                                                                                null=True, blank=True, verbose_name='讲师')
    lecturer_name= models.CharField(max_length=255, null=True, blank=True,verbose_name='讲师姓名')
    lecturer_level = models.ForeignKey(to=TrainingLecturerLevel, on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True,verbose_name='讲师级别')
    lecturer_type = models.CharField(max_length=255, null=True, blank=True,
                                                choices=(('内部讲师', '内部讲师'), ('外部讲师', '外部讲师')),
                                                verbose_name='讲师类型')
    lecturer_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    lecturer_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    lecturer_creater = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='创建者', related_name='lecturer_creater', db_constraint=False)
    lecturer_modifier= models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='修改者',related_name='lecturer_modifier')
    lecturer_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    lecturer_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'training_lecturer'
        verbose_name_plural = '培训讲师表'
        verbose_name = '培训讲师表'


class TrainingContent(models.Model):  # 培训内容
    content_lecturer = models.ForeignKey(to='TrainingLecturer', on_delete=models.SET_NULL, null=True,
                                                  blank=True, verbose_name='培训讲师',
                                                  related_name='content_lecturer', db_constraint=False)
    # content_title = models.CharField(max_length=255, null=True, blank=True, verbose_name='培训主题/课题')
    content_title =models.TextField(null=True, blank=True, verbose_name='备注')
    content_part = models.ForeignKey(to='employee.HrDepartment', on_delete=models.DO_NOTHING, db_constraint=False,
                                     null=True, blank=True, verbose_name='培训基地部门')
    content_module = models.CharField(max_length=255, null=True, blank=True, verbose_name='模块')
    content_group = models.CharField(max_length=255, null=True, blank=True, verbose_name='组')
    content_type = models.ForeignKey(to=TrainingContentType, on_delete=models.DO_NOTHING, db_constraint=False,
                                     null=True, blank=True, verbose_name='培训类型')  #公司级
    content_category = models.ForeignKey(to=TrainingContentCategory, on_delete=models.DO_NOTHING, db_constraint=False,
                                         null=True, blank=True, verbose_name='培训类别')  #知识类
    content_level = models.ForeignKey(to=TrainingContentLevel, on_delete=models.DO_NOTHING, db_constraint=False,
                                      null=True, blank=True, verbose_name='培训层级')  #高层 中层
    content_manner = models.CharField(max_length=255, null=True, blank=True,
                                      choices=(('现上', '现上'), ('现场', '现场')), verbose_name='培训方式')
    content_begin_date = models.DateTimeField(null=True, blank=True, verbose_name='开始培训日期')
    content_end_date = models.DateTimeField(null=True, blank=True, verbose_name='截至培训日期')
    content_duration = models.CharField(max_length=255, null=True, blank=True, verbose_name='培训时长(H)')
    content_object = models.CharField(max_length=255, null=True, blank=True, verbose_name='培训对象')
    content_people_number = models.CharField(max_length=255, null=True, blank=True, verbose_name='参训人数')
    content_satisfaction = models.CharField(max_length=255, null=True, blank=True, verbose_name='培训满意度')
    content_expenses = models.CharField(max_length=255, null=True, blank=True, verbose_name='培训费用')
    content_plan = models.CharField(max_length=255, null=True, blank=True,
                                    choices=(('计划内', '计划内'), ('计划外', '计划外')), verbose_name='计划内/计划外')
    content_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    content_creater= models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name='创建者', related_name='content_creater', db_constraint=False)
    content_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name='修改者', related_name='content_modifier')
    content_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    content_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'training_content'
        verbose_name_plural = '培训内容表'
        verbose_name = '培训内容表'



class TrainingSessions(models.Model):  # 培训课时
    sessions_base_first = models.CharField(max_length=255, null=True, blank=True, verbose_name='培训基地(一级)')
    sessions_base_second = models.CharField(max_length=255, null=True, blank=True, verbose_name='培训基地(二级)')
    sessions_base_third = models.CharField(max_length=255, null=True, blank=True, verbose_name='培训基地(三级)')
    sessions_base= models.CharField(max_length=255, null=True, blank=True, verbose_name='培训基地')
    # sessions_base = models.ForeignKey(to='employee.HrDepartment', on_delete=models.DO_NOTHING, db_constraint=False,
    #                                  null=True, blank=True, verbose_name='培训基地')
    sessions_offline_total= models.FloatField( null=True, blank=True, verbose_name='线下培训总时数')
    sessions_cloud_total = models.FloatField(null=True, blank=True, verbose_name='线上(云学堂)培训总时数',default=0)
    sessions_persons_register = models.FloatField(null=True, blank=True, verbose_name='月平均在册人数',default=0)
    sessions_per_people = models.FloatField(null=True, blank=True, verbose_name='基地人均培训课时',default=0)
    sessions_record_time = models.DateField(null=True, blank=True, verbose_name='记录时间')


    class Meta:
        managed = True
        db_table = 'training_sessions'
        verbose_name_plural = '培训课时表'
        verbose_name = '培训课时表'

class TrainingFiles(models.Model):
    training_file_choices = (
        (1, '培训照片'),
        (2,'培训附件(课件)'),
        (3, '签到表'),
        (4, '培训满意度'),
    )
    training_file_type = models.SmallIntegerField(verbose_name='文件类型', choices=training_file_choices)
    training_file_name = models.CharField(max_length=255, default='', verbose_name='文件名')
    training_file_url = models.CharField(max_length=255, default='', verbose_name='文件路径')
    training_content_file = models.ForeignKey(to=TrainingContent, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='培训文件', related_name='training_content_file', db_constraint=False)
    training_file_createtime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    training_file_creater = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='training_file_creater', db_constraint=False)
    training_file_status = models.BooleanField(default=True, verbose_name='数据是否有效')

    class Meta:
        managed = True
        db_table = 'training_files'
        verbose_name_plural = '上传文件表'
        verbose_name = '上传文件表'

class TrainingCheckin(models.Model):#培训签到
    checkin_people = models.ForeignKey(to='employee.HrEmployee', on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True, verbose_name='签到人')
    checkin_content= models.ForeignKey(to='TrainingContent', on_delete=models.SET_NULL, null=True,blank=True, verbose_name='签到课程',related_name='checkin_content', db_constraint=False)
    checkin_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='签到时间')
    checkin_address = models.CharField(max_length=255, null=True, blank=True, verbose_name='签到会场')
    checkin_user_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='用户类型')
    # checkin_associated_files= models.BooleanField(default=True, verbose_name='文件是否有效')
    checkin_associated_files = models.ForeignKey(to='TrainingFiles', on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name='签到表', related_name='checkin_associated_files', db_constraint=False)

    checkin_status = models.BooleanField(default=True, verbose_name='数据是否有效')
    # checkin_remark = models.CharField(max_length=255, null=True, blank=True, verbose_name='备注')
    checkin_creater= models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='创建者', related_name='checkin_creater', db_constraint=False)
    checkin_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,verbose_name='修改者', related_name='checkin_modifier')
    checkin_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    checkin_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')

    class Meta:
        managed = True
        db_table = 'training_checkin'
        verbose_name_plural = '培训签到表'
        verbose_name = '培训签到表'




