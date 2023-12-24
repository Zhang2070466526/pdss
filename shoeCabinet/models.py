from django.db import models

# Create your models here.
from django.db.models import DO_NOTHING


class ShoeRecord(models.Model):
    regin = models.CharField(null=True, blank=True, max_length=100, verbose_name="衣柜区域")
    wardrobe_number = models.CharField(null=True, blank=True, max_length=100, verbose_name="衣柜编号")
    dept_name = models.CharField(null=True, blank=True, max_length=100, verbose_name="部门名称")
    person_code = models.CharField(null=True, blank=True, max_length=50, verbose_name="工号")
    person_name = models.CharField(null=True, blank=True, max_length=100, verbose_name="姓名")
    gender = models.CharField(null=True, blank=True, max_length=10, verbose_name="性别")
    employee_status = models.CharField(null=True, blank=True, max_length=10, verbose_name="员工状态")
    person_phone = models.CharField(null=True, blank=True, max_length=255, verbose_name="电话")
    production_processes = models.TextField(null=True, blank=True, verbose_name="工序")
    remark = models.TextField(null=True, blank=True, verbose_name="备注")
    creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.DO_NOTHING, null=True, blank=True,
                                verbose_name='创建者',
                                related_name='creator_shoe', db_constraint=False)
    modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.DO_NOTHING, null=True, blank=True,
                                 verbose_name='修改者',
                                 related_name='modifier_shoe', db_constraint=False)

    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    status = models.BooleanField(default=True, verbose_name="是否有效")

    class Meta:
        managed = True
        db_table = 'shoe_cabinet'
        verbose_name_plural = '鞋柜记录表'
        verbose_name = '鞋柜记录表'


class RepairReport(models.Model):
    shoe = models.ForeignKey(to=ShoeRecord, on_delete=DO_NOTHING, null=True, blank=True,
                             verbose_name='创建者',
                             related_name='repair_shoe', db_constraint=False)
    person_code = models.CharField(max_length=100, null=True, blank=True, verbose_name="申报工号")
    repair_content = models.TextField(null=True, blank=True, verbose_name="报修描述")
    repair_status_code = (
        (1, "待处理"),
        (2, "处理中"),
        (3, "已处理"),
    )
    repair_status = models.IntegerField(default=1, choices=repair_status_code, verbose_name="审核状态")
    repair_suggestion = models.TextField(null=True, blank=True, verbose_name="处理意见")
    repair_handle_person = models.CharField(max_length=100, null=True, blank=True, verbose_name="处理人")
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='报修时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    pic_url = models.TextField(null=True, blank=True, verbose_name="报修照片")
    status = models.BooleanField(default=True, verbose_name="是否有效")

    class Meta:
        managed = True
        db_table = 'shoe_repair_report'
        verbose_name_plural = '鞋柜维修表'
        verbose_name = '鞋柜维修表'
