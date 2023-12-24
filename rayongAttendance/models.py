from django.db import models

# Create your models here.


class AttendanceDetailRecord(models.Model):
    pin = models.CharField(blank=True, null=True, max_length=100, verbose_name='工号')
    name = models.CharField(blank=True, null=True, max_length=255, verbose_name='姓名')
    dept_code = models.CharField(blank=True, null=True, max_length=100, verbose_name="部门代码")
    dept_name = models.CharField(blank=True, null=True, max_length=100, verbose_name="部门名称")
    job_time = models.CharField(blank=True, null=True, max_length=100, verbose_name="班制")
    status = models.BooleanField(default=True, verbose_name='数据是否有效')
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')

    class Meta:
        managed = True
        db_table = 'attendance_record'
        verbose_name_plural = '考勤记录统计表'
        verbose_name = '考勤记录统计表'


class AttendanceTimeRecord(models.Model):
    event_time = models.DateTimeField(blank=True, null=True, verbose_name='事件发生时间')
    render_name = models.CharField(blank=True, null=True, max_length=100, verbose_name="考勤机")
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    status = models.BooleanField(default=True, verbose_name='数据是否有效')
    person = models.ForeignKey(AttendanceDetailRecord, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='人', related_name='person', db_constraint=False)

    class Meta:
        managed = True
        db_table = 'attendance_time_record'
        verbose_name_plural = '考勤记录时间表'
        verbose_name = '考勤记录时间表'
