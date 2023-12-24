from abc import ABC

import arrow

from employeePersonnel.section.models import *
from employeePersonnel.models import *
from employee.models import HrEmployee

from utils.genericMethods import *
from employeePersonnel.views import *

class Section(methHeader):

    def add_meth(self):
        self.meth['section_every_week'] = self.section_every_week
        self.meth['section_every_month'] = self.section_every_month

    # 每周切片
    def section_every_week(self):
        employee_record_begin_time, employee_record_end_time = get_week_begin_end()  # 这周的
        # 记录类型  1 周 2 月
        employee_record_type = '1'
        emp_obj = HrEmployee.objects.all().defer('id').values()
        employee_history = []
        for e_obj in emp_obj:
            e_obj.pop('id')
            e_obj['employee_record_begin_time'] = employee_record_begin_time
            e_obj['employee_record_type'] = employee_record_type
            e_obj['employee_record_end_time'] = employee_record_end_time
            # HrEmployeeHistory.objects.create(**e_obj)
            employee_history.append(HrEmployeeHistory(**e_obj))
        HrEmployeeHistory.objects.bulk_create(employee_history)
        self.return_data['msg'] = '每周数据切片成功'

    # 每周切片
    def section_every_month(self):
        employee_record_begin_time, employee_record_end_time = get_month_begin_end()  # 这个月的
        # employee_record_begin_time, employee_record_end_time ='2023-10-01 00:00:00','2023-10-31 23:59:59'
        # 记录类型  1 周 2 月
        employee_record_type = '2'
        emp_obj = HrEmployee.objects.all().defer('id').values()
        employee_history = []
        for e_obj in emp_obj:
            e_obj.pop('id')
            e_obj['employee_record_begin_time'] = employee_record_begin_time
            e_obj['employee_record_type'] = employee_record_type
            e_obj['employee_record_end_time'] = employee_record_end_time
            # HrEmployeeHistory.objects.create(**e_obj)
            employee_history.append(HrEmployeeHistory(**e_obj))
        HrEmployeeHistory.objects.bulk_create(employee_history)
        self.return_data['msg'] = '每月数据切片成功'
