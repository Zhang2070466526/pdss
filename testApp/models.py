# # from abc import ABC, abstractmethod
# #
# # from arrow import arrow
# # from django.db import models
# # from django.http import JsonResponse
# # from rest_framework.views import APIView
#
#
#
#
# from django.db import models
# # from django_bulk_update_or_create import BulkUpdateOrCreateManager
#
# # Create your models here.
#
# """
# python manage.py makemigrations testApp
# python manage.py migrate testApp
# """
#
#
#
# class OverseasTrace(models.Model):  # 海外本土跟踪   personnelOptimization    #当前时间在12-1月，显示区间为11-3月；当前时间在2-3月，显示区间为1-5月；当前时间在4-5月，显示区间为3-7月；
#     overseas_dept = models.ForeignKey(to='employee.HrDepartment', on_delete=models.DO_NOTHING, db_constraint=False,
#                                        blank=True, verbose_name='培训基地部门')
#     overseas_authorized_total = models.IntegerField(verbose_name='初始总编制', null=True, blank=True)
#     overseas_authorized_chinese = models.IntegerField(verbose_name='初始中方外派编制', null=True, blank=True)
#     overseas_initial  = models.IntegerField(verbose_name='初始在职人数', null=True, blank=True)
#     overseas_expatriate_number = models.IntegerField(verbose_name='初始中方外派人数', null=True, blank=True)
#
#     overseas_status = models.BooleanField(default=True, verbose_name='数据是否有效')
#     overseas_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                          verbose_name='创建者', related_name='overseas_creator', db_constraint=False)
#     overseas_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                           verbose_name='修改者', related_name='overseas_modifier')
#     overseas_create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
#     overseas_modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
#
#     class Meta:
#         managed = True
#         db_table = 'Overseas_trace'
#         verbose_name_plural = '人员优化跟踪表'
#         verbose_name = '人员优化跟踪表'
# class OverseasMonth(models.Model):  # 海外本土跟踪月份
#     month_trace = models.ForeignKey(to=OverseasTrace, on_delete=models.DO_NOTHING, db_constraint=False,
#                                        null=True, blank=True, verbose_name='部门跟踪')
#     month_time = models.DateField(null=True, blank=True, verbose_name='记录时间')
#     month_target_expatriate = models.IntegerField(verbose_name='目标外派人数', null=True, blank=True)
#     month_practical_expatriate = models.IntegerField(verbose_name='实际外派人数', null=True, blank=True)
#
#     month_status = models.BooleanField(default=True, verbose_name='数据是否有效')
#     month_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                          verbose_name='创建者', related_name='month_creator', db_constraint=False)
#     month_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
#                                           verbose_name='修改者', related_name='month_modifier')
#     month_create_time = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
#     month_modify_time = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
#
#     class Meta:
#         managed = True
#         db_table = 'Overseas_month'
#         verbose_name_plural = '人员优化月份表'
#         verbose_name = '人员月份表'
#
#
#
#
# #
# # class personnelOptimization(models.Model):  # 人员优化   personnelOptimization    #当前时间在12-1月，显示区间为11-3月；当前时间在2-3月，显示区间为1-5月；当前时间在4-5月，显示区间为3-7月；
# #     optimize_dept = models.ForeignKey(to='employee.HrDepartment', on_delete=models.DO_NOTHING, db_constraint=False,
# #                                       null=True, blank=True, verbose_name='培训基地部门')
# #     optimize_month = models.DateField(null=True, blank=True, verbose_name='记录时间')
# #     optimize_initial = models.IntegerField(verbose_name='初始在职人数', null=True, blank=True)
# #     optimize_forecast = models.IntegerField(verbose_name='预测在职人数', null=True, blank=True)
# #     optimize_practical = models.IntegerField(verbose_name='实际在职人数', null=True, blank=True)
# #     optimize_title = models.TextField(null=True, blank=True, verbose_name='备注')
# #
# #     optimize_status = models.BooleanField(default=True, verbose_name='数据是否有效')
# #     optimize_creator = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
# #                                          verbose_name='创建者', related_name='optimize_creator', db_constraint=False)
# #     optimize_modifier = models.ForeignKey(to='auther.AdminUser', on_delete=models.SET_NULL, null=True, blank=True,
# #                                           verbose_name='修改者', related_name='optimize_modifier')
# #     optimize_createTime = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='创建时间')
# #     optimize_modifyTime = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='修改时间')
# #
# #     class Meta:
# #         managed = True
# #         db_table = 'personnel_optimization'
# #         verbose_name_plural = '人员优化表'
# #         verbose_name = '人员优化表'
# #
# #
# # '''
# # 如果日期在
# #
# #
# # '''
# #
# #
# # # 类名方法头
# # class methHeader(ABC):
# #
# #     def __init__(self, request):
# #         self.request = request
# #         self.return_data = {
# #             'code': 200,
# #             'msg': '信息返回成功',
# #             'data': {}
# #         }
# #         self.meth = {}
# #         self.now_time = arrow.now().format("YYYY-MM-DD HH:mm:ss")
# #         self.operate_user_id = ''
# #         self.operate_user_name = ''
# #
# #     def method_center(self, method):
# #         self.operate_user_id = self.request.check_token
# #         self.operate_user_name = get_admin_user_by_id(self.operate_user_id)
# #         self.meth[method]()
# #         return JsonResponse(self.return_data)
# #
# #     @abstractmethod
# #     def add_meth(self):
# #         pass
# #
# #
# # # 基本增删改查方法
# # class BasicClass(ABC):
# #     @abstractmethod
# #     def create(self):
# #         pass
# #
# #     @abstractmethod
# #     def update(self):
# #         pass
# #
# #     @abstractmethod
# #     def search(self):
# #         pass
# #
# #     @abstractmethod
# #     def delete(self):
# #         pass
# #
# #
# # class FileClass(ABC):
# #     @abstractmethod
# #     def upload(self):
# #         pass
# #
# #     def download(self):
# #         pass
# #
# #
# # class ViewBasicTemplate(APIView):
# #
# #     def __init__(self, className):
# #         self.obj = className(None)
# #         self.obj.add_meth()
# #
# #     def post(self, request):
# #         """
# #         查询
# #         :param request:
# #         :return:
# #         """
# #         self.obj.request = request
# #         return self.obj.method_center('search')
# #
# #     def put(self, request):
# #         """
# #         新增
# #         检测创建重复放在前端，使用查询完成
# #         :param request:
# #         :return:
# #         """
# #         self.obj.request = request
# #         return self.obj.method_center('create')
# #
# #     def patch(self, request):
# #         """
# #         修改
# #         :param request:
# #         :return:
# #         """
# #         self.obj.request = request
# #         return self.obj.method_center('update')
# #
# #     def delete(self, request):
# #         """
# #         删除
# #         :param request:
# #         :return:
# #         """
# #         self.obj.request = request
# #         return self.obj.method_center('delete')