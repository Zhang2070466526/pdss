from django.db import models


# Create your models here.
class TranslateField(models.Model):
    trans_field = models.CharField(max_length=255, null=True, blank=True, verbose_name='翻译的字段')
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    status = models.BooleanField(default=True, verbose_name="是否有效")

    class Meta:
        managed = True
        db_table = 'translate_field'
        verbose_name_plural = '字段表'
        verbose_name = '字段表'


class Translate(models.Model):
    tran_field = models.ForeignKey(to=TranslateField, on_delete=models.DO_NOTHING, db_constraint=False,
                                   null=True, blank=True, related_name='tran_field',
                                   verbose_name='字段')
    trans_language = models.CharField(max_length=100, null=True, blank=True, verbose_name='语种')
    trans_value = models.CharField(max_length=255, null=True, blank=True, verbose_name='翻译的内容')
    create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
    modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
    status = models.BooleanField(default=True, verbose_name="是否有效")

    class Meta:
        managed = True
        db_table = 'translate_value'
        verbose_name_plural = '翻译表'
        verbose_name = '翻译表'
