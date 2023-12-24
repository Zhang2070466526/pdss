from django.db import models


# Create your models here.
# class SendAcceptPerson(models.Model):
#     name = models.CharField(blank=True, null=True, max_length=50, verbose_name="收件人")
#     email_address = models.EmailField(blank=True, null=True, verbose_name="邮箱")
#     status = models.BooleanField(default=True, verbose_name='数据是否有效')
#     leader = models.ManyToManyField(to="SendModel", verbose_name='周报发送者', related_name='leader', db_constraint=False)
#     create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
#     modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
#     creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                 verbose_name='创建者', related_name='accept_person_creator', db_constraint=False)
#     modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                  verbose_name='修改者', related_name='accept_person_modifier', db_constraint=False)
#
#     class Meta:
#         verbose_name = "收件人表"
#         verbose_name_plural = "收件人表"
#         db_table = "send_accept_person"
#
#
# class SendDepartment(models.Model):
#     ParentID = models.IntegerField(blank=True, null=True, verbose_name="父ID")
#     DepartmentCode = models.CharField(blank=True, null=True, max_length=100, verbose_name="部门代码")
#     DepartmentName = models.CharField(blank=True, null=True, max_length=100, verbose_name="部门名称")
#
#     department_acceptor = models.ManyToManyField(to=SendAcceptPerson, related_name="department_acceptor",
#                                                  db_constraint=False,
#                                                  verbose_name="部门对应人")
#     department_model = models.ManyToManyField(to="SendModel", related_name="department_model",
#                                               db_constraint=False,
#                                               verbose_name="部门对应模块")
#     status = models.BooleanField(default=True, verbose_name='数据是否有效')
#     create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
#     modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
#     creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                 verbose_name='创建者', related_name='send_department_creator', db_constraint=False)
#     modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                  verbose_name='修改者', related_name='send_department_modifier', db_constraint=False)
#
#     class Meta:
#         verbose_name = "统计部门表"
#         verbose_name_plural = "统计部门表"
#         db_table = "send_department"
#
#
# class SendModel(models.Model):
#     name = models.CharField(blank=True, null=True, max_length=100, verbose_name="模块名称")
#     status = models.BooleanField(default=True, verbose_name='数据是否有效')
#     create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
#     modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
#     model_to_acceptor = models.ManyToManyField(to=SendAcceptPerson,
#                                                verbose_name='发送模块', related_name='model_to_acceptor',
#                                                db_constraint=False)
#     creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                 verbose_name='创建者', related_name='send_model_creator', db_constraint=False)
#     modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                  verbose_name='修改者', related_name='send_model_modifier', db_constraint=False)
#
#     class Meta:
#         verbose_name = "发送模块表"
#         verbose_name_plural = "发送模块表"
#         db_table = "send_model"


class SendAcceptor(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50, verbose_name="收件人")
    email_address = models.EmailField(blank=True, null=True, verbose_name="邮箱")
    accept_type = models.IntegerField(default=0, verbose_name='接收类型')
    status = models.BooleanField(default=True, verbose_name='数据是否有效')
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='accept_creator', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='accept_modifier', db_constraint=False)

    class Meta:
        verbose_name = "收件人表"
        verbose_name_plural = "收件人表"
        db_table = "send_acceptor"


class SendDepartment(models.Model):
    dept_id = models.IntegerField(blank=True, null=True, verbose_name="部门ID")
    ParentID = models.IntegerField(blank=True, null=True, verbose_name="父ID")
    dept_code = models.CharField(blank=True, null=True, max_length=100, verbose_name="部门代码")
    dept_name = models.CharField(blank=True, null=True, max_length=100, verbose_name="部门名称")
    dept_type = models.IntegerField(blank=True, null=True, verbose_name="部门对应模块")
    dept_acceptor = models.ManyToManyField(to=SendAcceptor, related_name="dept_acceptor",
                                           db_constraint=False,
                                           verbose_name="每天发送部门对应接收人")
    status = models.BooleanField(default=True, verbose_name='数据是否有效')
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='创建者', related_name='send_dept_creator', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name='修改者', related_name='send_dept_modifier', db_constraint=False)

    class Meta:
        verbose_name = "统计部门表"
        verbose_name_plural = "统计部门表"
        db_table = "send_department"


class SendRecord(models.Model):
    type_name = models.CharField(blank=True, null=True, max_length=100, verbose_name="发送类型")
    acceptor = models.ManyToManyField(to=SendAcceptor, related_name="record_acceptor",
                                      db_constraint=False, verbose_name="接收人记录")
    send_file_path = models.CharField(blank=True, null=True, max_length=255, verbose_name="文件地址")
    send_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='发送时间')
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='发送人', related_name='send_creator', db_constraint=False)

    class Meta:
        verbose_name = "发送记录表"
        verbose_name_plural = "发送记录表"
        db_table = "send_record"
