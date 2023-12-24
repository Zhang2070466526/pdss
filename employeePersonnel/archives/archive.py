import json, arrow, os
from django.db import connection
from django.db.models import Q
from datetime import datetime, date, timedelta
from rest_framework import status
from datetime import datetime
import calendar

from employee import views
from employee.models import *
from employeePersonnel.models import HrEmployeeHistory
from pdss.settings import BASE_DIR
# from IeProposal.proposal.proposalClass import *
from django.db.models import Count
from utils.sqlServerConnect import EhrConnect
import shutil, openpyxl
import pandas as pd
from utils.save_data_to_redis import *
from employeePersonnel.publicMethods import *


# from employeePersonnel.views import get_week_begin_end,get_month_begin_end


# def calculate_week_date(day):   #跟据年和周计算对应的开始和结束日期
#     # # 计算第一周的开始日期（星期一）
#     # start_date = datetime(year, 1, 1) + timedelta(days=(week - 2) * 7)
#     # start_date = start_date + timedelta(days=(start_date.weekday() - 0) % 7) + timedelta(days=2)
#     # # 计算第一周的结束日期（星期日）
#     # end_date = start_date + timedelta(days=6)
#     # return (start_date.date(), end_date.date())
#
#     start_date=datetime.strptime(day, "%Y-%m-%d")
#     print(start_date)
#     # end_date = start_date + timedelta(days=6)
#     # return (start_date,end_date)
#     return (start_date,start_date)

def calculate_month_date(month):  # 跟据年和周计算对应的开始和结束日期
    # month = '2023-02'
    date = datetime.strptime(month, "%Y-%m-%d")
    # 获取这个月的第一天
    first_day = datetime(date.year, date.month, 1)
    # 获取这个月的最后一天
    _, last_day = calendar.monthrange(date.year, date.month)
    last_day = datetime(date.year, date.month, last_day)

    start_date = first_day.replace(hour=0, minute=0, second=0)  # 设置开始日期的时间为'00:00:00'
    end_date = last_day.replace(hour=23, minute=59, second=59)  # 设置结束日期的时间为'23:59:59'
    return (start_date, end_date)


class Archive:  # 员工档案切片
    def __init__(self, request, meth):
        self.request = request
        self.now = arrow.now()
        self.t1 = self.now.format('YYYY-MM-DD')
        self.t2 = self.now.timestamp()
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功'
        }
        self.meth = meth
        self.methods = {
            'slice_info_down': self.slice_info_down,
            'slice_info_select': self.slice_info_select,
        }

    def meth_center(self):
        self.return_data = {'code': status.HTTP_403_FORBIDDEN, "msg": '没有权限访问'}
        if self.request.check_token is None:
            return JsonResponse(self.return_data)
        self.methods[self.meth]()
        return JsonResponse(self.return_data)

    def slice_info_select(self):
        from employeePersonnel.views import get_week_begin_end
        from employeePersonnel.views import get_month_begin_end
        slice_begin_week, slice_end_week = get_week_begin_end(flag=1)  # 上周的   切片时间
        # print(slice_begin_week,slice_end_week)
        user_field_all = views.get_user_field(self.request, 151)
        user_field_all_keys = [list(d.keys())[0] for d in user_field_all]

        column_list = [{'label': 'index', 'value': '序号', 'width': 60}]
        for dictionary in user_field_all:
            key = list(dictionary.keys())[0]
            value = list(dictionary.values())[0]
            new_dict = {'label': key, 'value': value, 'width': 100}
            if new_dict['label'] in ['employee_department__department_full_name', 'employee_identity_no',
                                     'employee_position__position_name', 'employee_group_join_date',
                                     'employee_join_date', 'employee_department__department_first_name',
                                     'employee_department__department_second_name',
                                     'employee_department__department_third_name', 'employee_position__position_name',
                                     'employee_job_duty__job_duty_name', 'employee_job_class__job_class_name']:
                new_dict['width'] = 210

            column_list.append(new_dict)
        info = json.loads(self.request.body)
        if 'employee_age' in user_field_all_keys:
            user_field_all_keys.remove('employee_age')

        current_page = info.get('currentPage', 1)
        page_size = info.get('pageSize', 25)
        search_name = info.get('searchName', '')
        employee_work_status = info.get('employeeWorkStatus', [])  # 在职状态
        employee_pay_type = info.get('employeePayType', [])  # 计薪方式
        employee_status = info.get('employeeStatus', [])  # 状态
        # employee_group_join_begin_date = info.get('employeeGroupJoinBeginDate', datetime(1901, 10, 29, 7, 17, 1, 177))  # 集团入职日期
        # employee_group_join_end_date = info.get('employeeGroupJoinEndDate', datetime(3221, 10, 29, 7, 17, 1, 177))
        employeeGroupJoinDate = info.get('employeeGroupJoinDate', [])
        if employeeGroupJoinDate is None or len(employeeGroupJoinDate) == 0:
            employee_group_join_begin_date, employee_group_join_end_date = datetime(1901, 10, 29, 7, 17, 1,177), datetime(3221, 10, 29, 7, 17,1, 177)
        else:
            employee_group_join_begin_date, employee_group_join_end_date = employeeGroupJoinDate

        employee_record_type = info.get('sliceType', 1)  # 切片类型
        employee_job_rank = info.get('employeeJobRank', [])  # 合同归属
        employee_department = info.get('department_id', [])  # 部门归属
        employee_dl = info.get('employeeDl', [])  # 部门归属
        # slice_begin_date, slice_end_date = '2023-10-16 00:00:00','2023-10-22 23:59:59'
        slice_begin_date, slice_end_date = slice_begin_week, slice_end_week
        slice_begin_date = slice_begin_date.replace(hour=0, minute=0, second=0)  # 设置开始日期的时间为'00:00:00'
        slice_end_date = slice_end_date.replace(hour=23, minute=59, second=59)  # 设置结束日期的时间为'23:59:59'
        if employee_record_type == 1:
            slice_date = info.get('sliceDate', str(slice_begin_week)[:10])  # 切片日期
            if slice_date is None or len(slice_date) == 0:
                slice_begin_date, slice_end_date = slice_begin_week, slice_end_week
            else:
                slice_begin_date = datetime.strptime(slice_date, "%Y-%m-%d")
                slice_end_date = slice_begin_date + timedelta(days=6)
            slice_begin_date = slice_begin_date.replace(hour=0, minute=0, second=0)  # 设置开始日期的时间为'00:00:00'
            slice_end_date = slice_end_date.replace(hour=23, minute=59, second=59)  # 设置结束日期的时间为'23:59:59'

        elif employee_record_type == 2:
            slice_date = info.get('sliceDate', '')  # 切片日期
            if slice_date is None or len(slice_date) == 0:
                slice_begin_date, slice_end_date = get_month_begin_end(flag=1)  # 上月的   切片时间
            else:
                slice_begin_date, slice_end_date = calculate_month_date(slice_date)

        kwargs = {
            'employee_job_rank__in': employee_job_rank,
            'employee_record_type': employee_record_type,
            'employee_group_join_date__gte': employee_group_join_begin_date,
            'employee_group_join_date__lte': employee_group_join_end_date,
            'employee_status__in': employee_status,
            'employee_pay_type__in': employee_pay_type,
            'employee_work_status__in': employee_work_status,
            'employee_record_begin_time': slice_begin_date,
            'employee_record_end_time': slice_end_date,
            'employee_department__in': self.request.user_department_employee if len(
                employee_department) == 0 or employee_department is None else employee_department,
            'employee_dl__in': employee_dl
        }
        kwargs = {key: value for key, value in kwargs.items() if
                  value is not None and value != '' and value != []}  # 过滤掉值为None或''或[]的项

        total_number = HrEmployeeHistory.objects.filter(
            Q(employee_name__contains=search_name) | Q(employee_code__contains=search_name), **kwargs).count()
        table_list = list(
            HrEmployeeHistory.objects.filter(
                Q(employee_name__contains=search_name) | Q(employee_code__contains=search_name), **kwargs).values(
                *tuple(user_field_all_keys), 'id').order_by('-employee_group_join_date')[
            (current_page - 1) * page_size:current_page * page_size])

        employee_status_choices = {'1': '在职', '2': '离职', '99': '黑名单'}
        employee_sex_choices = {'1': '男', '2': '女'}
        employee_dl_choices = {'DL': 'DL', 'IDL': 'IDL', 'SAL': 'SAL'}
        employee_marriage_status_choices = {'0': '未婚', '1': '已婚', '2': '离异'}
        employee_work_status_choices = {'正式工': '正式工', '实习生': '实习生', '试用期': '试用期', '劳务工': '劳务工',
                                        '产线承包': '产线承包', '顾问': '顾问', '': ''}
        employee_political_status_choices = {'党员': '党员', '预备党员': '预备党员', '群众': '群众'}
        employee_first_degree_type_choices = {'全日制': '全日制', "非全日制": '非全日制'}
        employee_train_degree_type_choices = {'01': '全日制', '02': '自考', '03': '远程教育', '04': '成人高考'}
        employee_turn_status_choices = {'1': '已转正', '0': '未转正'}


        for index, item in enumerate(table_list):
            item['index'] = (current_page - 1) * page_size + index + 1
            try:
                item['employee_age'] = self.calculate_age(str(item['employee_birthday']))
            except:
                pass
            try:
                item['employee_turn_status'] = employee_turn_status_choices.get(item['employee_turn_status'], None)
            except:
                pass
            try:
                item['employee_birthday']=str(item['employee_birthday'])[:10] if item['employee_birthday'] != None else None
            except:
                pass
            try:
                item['employee_sex'] = employee_sex_choices.get(item['employee_sex'], None)
            except:
                pass
            try:
                item['employee_status'] = employee_status_choices.get(item['employee_status'], None)
            except:
                pass
            try:
                item['employee_dl'] = employee_dl_choices.get(item['employee_dl'], None)
            except:
                pass
            try:
                item['employee_marriage_status'] = employee_marriage_status_choices.get(
                    item['employee_marriage_status'], None)
            except:
                pass
            try:
                item['employee_work_status'] = employee_work_status_choices.get(item['employee_work_status'], None)
            except:
                pass
            try:
                item['employee_political_status'] = employee_political_status_choices.get(
                    item['employee_political_status'], None)
            except:
                pass
            try:
                item['employee_first_degree_type'] = employee_first_degree_type_choices.get(
                    item['employee_first_degree_type'], None)
            except:
                pass
            try:
                item['employee_train_degree_type'] = employee_train_degree_type_choices.get(
                    item['employee_train_degree_type'], None)
            except:
                pass
            try:
                item['employee_group_join_date'] = str(item['employee_group_join_date'])[:10] if item['employee_group_join_date'] != None else None
            except:
                pass
            try:
                item['employee_join_date'] = str(item['employee_join_date'])[:10] if item['employee_join_date'] != None else None
            except:
                pass
            try:
                item['employee_departure_date'] = str(item['employee_departure_date'])[:10] if item['employee_departure_date'] != None else None
            except:
                pass
            try:
                item['employee_departure_notice_date'] = str(item['employee_departure_notice_date'])[:10] if item['employee_departure_notice_date'] != None else None
            except:
                pass
            try:
                item['employee_departure_handle_date'] = str(item['employee_departure_handle_date'])[:10] if item['employee_departure_handle_date'] != None else None
            except:
                pass
            try:
                item['employee_plan_turn_date'] = str(item['employee_plan_turn_date'])[:10] if item['employee_plan_turn_date'] != None else None
            except:
                pass
            try:
                item['employee_identity_no_effective_date'] = str(item['employee_identity_no_effective_date'])[:10] if item['employee_identity_no_effective_date'] != None else None
            except:
                pass
            try:
                item['employee_identity_no_failre_date'] = str(item['employee_identity_no_failre_date'])[:10] if item['employee_identity_no_failre_date'] != None else None
            except:
                pass
            try:
                item['employee_train_degree_graduate_date'] = str(item['employee_train_degree_graduate_date'])[:10] if item['employee_train_degree_graduate_date'] != None else None
            except:
                pass
            try:
                item['employee_first_degree_graduate_date'] = str(item['employee_first_degree_graduate_date'])[:10] if item['employee_first_degree_graduate_date'] != None else None
            except:
                pass
            try:
                item['employee_plan_turn_date'] = str(item['employee_plan_turn_date'])[:10] if item['employee_plan_turn_date'] != None else None
            except:
                pass
            try:
                item['employee_turn_date'] = str(item['employee_turn_date'])[:10] if item['employee_turn_date'] != None else None
            except:
                pass



        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "信息返回成功",
            "data": {
                'columnList': column_list,
                'tableList': table_list,
                'totalNumber': total_number,
            }
        }

    def slice_info_down(self):
        dummy_path = os.path.join(BASE_DIR, 'static', 'employeePersonnelFile', 'download_file', self.t1,
                                  str(self.t2))  # 创建文件夹
        self.mkdir(dummy_path)
        user_field_all = views.get_user_field(self.request, 151)
        user_field_all_keys = [list(d.keys())[0] for d in user_field_all]
        user_field_all_values = [list(d.values())[0] for d in user_field_all]
        file_ls = user_field_all_values
        file_ls.insert(0, "序号")
        path = createExcelPath('档案切片.xlsx', 'employeePersonnelFile', str(self.t2), '档案切片', 60, 'A1:BH1',
                               *file_ls)
        info = json.loads(self.request.body)
        id_list = info.get('id_list',[])
        download_all = info.get('downloadAll',False)

        print("下载",info)
        from employeePersonnel.views import get_week_begin_end
        from employeePersonnel.views import get_month_begin_end
        slice_begin_week, slice_end_week = get_week_begin_end(flag=1)  # 上周的   切片时间
        print(info)
        row_data = []
        index_t = 1
        employee_status_choices = {'1': '在职', '2': '离职', '99': '黑名单'}
        employee_sex_choices = {'1': '男', '2': '女'}
        employee_dl_choices = {'DL': 'DL', 'IDL': 'IDL', 'SAL': 'SAL'}
        employee_marriage_status_choices = {'0': '未婚', '1': '已婚', '2': '离异'}
        employee_work_status_choices = {'正式工': '正式工', '实习生': '实习生', '试用期': '试用期', '劳务工': '劳务工',
                                        '产线承包': '产线承包', '顾问': '顾问', '': ''}
        employee_political_status_choices = {'党员': '党员', '预备党员': '预备党员', '群众': '群众'}
        employee_first_degree_type_choices = {'全日制': '全日制', "非全日制": '非全日制'}
        employee_train_degree_type_choices = {'01': '全日制', '02': '自考', '03': '远程教育', '04': '成人高考'}
        employee_turn_status_choices = {'1': '已转正', '0': '未转正'}
        user_field_all_keys_new=[]
        if 'employee_age' in user_field_all_keys:
            user_field_all_keys_new=[item for item in user_field_all_keys if item != 'employee_age']
        else:
            user_field_all_keys_new=user_field_all_keys
        # '2023-12-17 23:59:59.000000'
        if download_all == True:  # 是下载全部   有条件
            search_name = info.get('searchName', '')
            employee_work_status = info.get('employeeWorkStatus', [])  # 在职状态
            employee_pay_type = info.get('employeePayType', [])  # 计薪方式
            employee_status = info.get('employeeStatus', [])  # 状态
            employeeGroupJoinDate = info.get('employeeGroupJoinDate', [])
            if employeeGroupJoinDate is None or len(employeeGroupJoinDate) == 0:
                employee_group_join_begin_date, employee_group_join_end_date = datetime(1901, 10, 29, 7, 17, 1,177), datetime(3221, 10, 29, 7,17, 1, 177)
            else:
                employee_group_join_begin_date, employee_group_join_end_date = employeeGroupJoinDate

            employee_record_type = info.get('sliceType', 1)  # 切片类型
            employee_job_rank = info.get('employeeJobRank', [])  # 合同归属
            employee_department = info.get('department_id', [])  # 部门归属
            employee_dl = info.get('employeeDl', [])  # 部门归属
            slice_begin_date, slice_end_date = slice_begin_week, slice_end_week
            slice_begin_date = slice_begin_date.replace(hour=0, minute=0, second=0)  # 设置开始日期的时间为'00:00:00'
            slice_end_date = slice_end_date.replace(hour=23, minute=59, second=59)  # 设置结束日期的时间为'23:59:59'
            if employee_record_type == 1:
                slice_date = info.get('sliceDate', str(slice_begin_week)[:10])  # 切片日期
                if slice_date is None or len(slice_date) == 0:
                    slice_begin_date, slice_end_date = slice_begin_week, slice_end_week
                else:
                    slice_begin_date = datetime.strptime(slice_date, "%Y-%m-%d")
                    slice_end_date = slice_begin_date + timedelta(days=6)
                slice_begin_date = slice_begin_date.replace(hour=0, minute=0, second=0)  # 设置开始日期的时间为'00:00:00'
                slice_end_date = slice_end_date.replace(hour=23, minute=59, second=59)  # 设置结束日期的时间为'23:59:59'

            elif employee_record_type == 2:
                slice_date = info.get('sliceDate', '')  # 切片日期
                if slice_date is None or len(slice_date) == 0:
                    slice_begin_date, slice_end_date = get_month_begin_end(flag=1)  # 上月的   切片时间
                else:
                    slice_begin_date, slice_end_date = calculate_month_date(slice_date)
            kwargs = {
                'employee_job_rank__in': employee_job_rank,
                'employee_record_type': employee_record_type,
                'employee_group_join_date__gte': employee_group_join_begin_date,
                'employee_group_join_date__lte': employee_group_join_end_date,
                'employee_status__in': employee_status,
                'employee_pay_type__in': employee_pay_type,
                'employee_work_status__in': employee_work_status,
                'employee_record_begin_time': slice_begin_date,
                'employee_record_end_time': slice_end_date,
                'employee_department__in': self.request.user_department_employee if len(
                    employee_department) == 0 or employee_department is None else employee_department,
                'employee_dl__in': employee_dl
            }
            kwargs = {key: value for key, value in kwargs.items() if
                      value is not None and value != '' and value != []}  # 过滤掉值为None或''或[]的项
            table_list = list(
                HrEmployeeHistory.objects.filter(
                    Q(employee_name__contains=search_name) | Q(employee_code__contains=search_name), **kwargs).values(
                    *tuple(user_field_all_keys_new), 'id').order_by('-employee_group_join_date'))
            for index, item in enumerate(table_list):
                try:
                    item['employee_age'] = self.calculate_age(str(item['employee_birthday']))
                except:
                    pass
                try:
                    item['employee_turn_status'] = employee_turn_status_choices.get(item['employee_turn_status'], None)
                except:
                    pass
                try:
                    item['employee_birthday'] = str(item['employee_birthday'])[:10] if item['employee_birthday'] != None else None
                except:
                    pass
                try:
                    item['employee_sex'] = employee_sex_choices.get(item['employee_sex'], None)
                except:
                    pass
                try:
                    item['employee_status'] = employee_status_choices.get(item['employee_status'], None)
                except:
                    pass
                try:
                    item['employee_dl'] = employee_dl_choices.get(item['employee_dl'], None)
                except:
                    pass
                try:
                    item['employee_marriage_status'] = employee_marriage_status_choices.get(
                        item['employee_marriage_status'], None)
                except:
                    pass
                try:
                    item['employee_work_status'] = employee_work_status_choices.get(item['employee_work_status'], None)
                except:
                    pass
                try:
                    item['employee_political_status'] = employee_political_status_choices.get(
                        item['employee_political_status'], None)
                except:
                    pass
                try:
                    item['employee_first_degree_type'] = employee_first_degree_type_choices.get(
                        item['employee_first_degree_type'], None)
                except:
                    pass
                try:
                    item['employee_train_degree_type'] = employee_train_degree_type_choices.get(
                        item['employee_train_degree_type'], None)
                except:
                    pass
                try:
                    item['employee_group_join_date'] = str(item['employee_group_join_date'])[:10] if item['employee_group_join_date'] != None else None
                except:
                    pass
                try:
                    item['employee_join_date'] = str(item['employee_join_date'])[:10] if item['employee_join_date'] != None else None
                except:
                    pass
                try:
                    item['employee_departure_date'] = str(item['employee_departure_date'])[:10] if item['employee_departure_date'] != None else None
                except:
                    pass
                try:
                    item['employee_departure_notice_date'] = str(item['employee_departure_notice_date'])[:10] if item['employee_departure_notice_date'] != None else None
                except:
                    pass
                try:
                    item['employee_departure_handle_date'] = str(item['employee_departure_handle_date'])[:10] if item['employee_departure_handle_date'] != None else None
                except:
                    pass
                try:
                    item['employee_plan_turn_date'] = str(item['employee_plan_turn_date'])[:10] if item['employee_plan_turn_date'] != None else None
                except:
                    pass
                try:
                    item['employee_identity_no_effective_date'] = str(item['employee_identity_no_effective_date'])[:10] if item['employee_identity_no_effective_date'] != None else None
                except:
                    pass
                try:
                    item['employee_identity_no_failre_date'] = str(item['employee_identity_no_failre_date'])[:10] if item['employee_identity_no_failre_date'] != None else None
                except:
                    pass
                try:
                    item['employee_train_degree_graduate_date'] = str(item['employee_train_degree_graduate_date'])[:10] if item['employee_train_degree_graduate_date'] != None else None
                except:
                    pass
                try:
                    item['employee_first_degree_graduate_date'] = str(item['employee_first_degree_graduate_date'])[:10] if item['employee_first_degree_graduate_date'] != None else None
                except:
                    pass
                try:
                    item['employee_plan_turn_date'] = str(item['employee_plan_turn_date'])[:10] if item['employee_plan_turn_date'] != None else None
                except:
                    pass
                try:
                    item['employee_turn_date'] = str(item['employee_turn_date'])[:10] if item['employee_turn_date'] != None else None
                except:
                    pass
            for line in table_list:
                line_data = [line.get(key,None) for key in user_field_all_keys]
                line_data.insert(0, index_t)
                row_data.append(line_data)
                if len(line_data) == 0:
                    index_t = index_t
                index_t += 1
        else:
            table_list = list(
                HrEmployeeHistory.objects.filter(pk__in=id_list).values(*tuple(user_field_all_keys_new)).order_by(
                    '-employee_group_join_date'))
            for index, item in enumerate(table_list):
                try:
                    item['employee_age'] = self.calculate_age(str(item['employee_birthday']))
                except:
                    pass
                try:
                    item['employee_turn_status'] = employee_turn_status_choices.get(item['employee_turn_status'], None)
                except:
                    pass
                try:
                    item['employee_birthday'] = str(item['employee_birthday'])[:10] if item['employee_birthday'] != None else None
                except:
                    pass
                try:
                    item['employee_sex'] = employee_sex_choices.get(item['employee_sex'], None)
                except:
                    pass
                try:
                    item['employee_status'] = employee_status_choices.get(item['employee_status'], None)
                except:
                    pass
                try:
                    item['employee_dl'] = employee_dl_choices.get(item['employee_dl'], None)
                except:
                    pass
                try:
                    item['employee_marriage_status'] = employee_marriage_status_choices.get(
                        item['employee_marriage_status'], None)
                except:
                    pass
                try:
                    item['employee_work_status'] = employee_work_status_choices.get(item['employee_work_status'], None)
                except:
                    pass
                try:
                    item['employee_political_status'] = employee_political_status_choices.get(
                        item['employee_political_status'], None)
                except:
                    pass
                try:
                    item['employee_first_degree_type'] = employee_first_degree_type_choices.get(
                        item['employee_first_degree_type'], None)
                except:
                    pass
                try:
                    item['employee_train_degree_type'] = employee_train_degree_type_choices.get(
                        item['employee_train_degree_type'], None)
                except:
                    pass
                try:
                    item['employee_group_join_date'] = str(item['employee_group_join_date'])[:10] if item['employee_group_join_date'] != None else None
                except:
                    pass
                try:
                    item['employee_join_date'] = str(item['employee_join_date'])[:10] if item['employee_join_date'] != None else None
                except:
                    pass
                try:
                    item['employee_departure_date'] = str(item['employee_departure_date'])[:10] if item['employee_departure_date'] != None else None
                except:
                    pass
                try:
                    item['employee_departure_notice_date'] = str(item['employee_departure_notice_date'])[:10] if item['employee_departure_notice_date'] != None else None
                except:
                    pass
                try:
                    item['employee_departure_handle_date'] = str(item['employee_departure_handle_date'])[:10] if item['employee_departure_handle_date'] != None else None
                except:
                    pass
                try:
                    item['employee_plan_turn_date'] = str(item['employee_plan_turn_date'])[:10] if item['employee_plan_turn_date'] != None else None
                except:
                    pass
                try:
                    item['employee_identity_no_effective_date'] = str(item['employee_identity_no_effective_date'])[:10] if item['employee_identity_no_effective_date'] != None else None
                except:
                    pass
                try:
                    item['employee_identity_no_failre_date'] = str(item['employee_identity_no_failre_date'])[:10] if item['employee_identity_no_failre_date'] != None else None
                except:
                    pass
                try:
                    item['employee_train_degree_graduate_date'] = str(item['employee_train_degree_graduate_date'])[:10] if item['employee_train_degree_graduate_date'] != None else None
                except:
                    pass
                try:
                    item['employee_first_degree_graduate_date'] = str(item['employee_first_degree_graduate_date'])[:10] if item['employee_first_degree_graduate_date'] != None else None
                except:
                    pass
                try:
                    item['employee_plan_turn_date'] = str(item['employee_plan_turn_date'])[:10] if item['employee_plan_turn_date'] != None else None
                except:
                    pass
                try:
                    item['employee_turn_date'] = str(item['employee_turn_date'])[:10] if item['employee_turn_date'] != None else None
                except:
                    pass
            for line in table_list:
                line_data = [line.get(key, None) for key in user_field_all_keys]
                line_data.insert(0, index_t)
                row_data.append(line_data)
                if len(line_data) == 0:
                    index_t = index_t
                index_t += 1

        exc = openpyxl.load_workbook(path)  # 打开整个excel文件
        sheet = exc.worksheets[0]  # 打开第0张工作表(也就是第一张)
        for row in row_data:
            sheet.append(row)  # 在工作表中添加一行
        exc.save(path)  # 指定路径,保存文件
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "下载成功",
            "downloadUrl": path
        }

    @staticmethod
    def days_until_given_date(calculate_time):
        """
        :param datetime:    要计算据今的日期   例datetime.datetime(2023, 7, 19, 0, 0)
        :return:   days_difference 相差的天数
        """
        given_date = calculate_time  # 给定的日期
        current_date = datetime.now()  # 获取当前日期
        time_difference = current_date - given_date
        days_difference = time_difference.days  # 天数
        return days_difference

    @staticmethod
    def mkdir(path):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
        else:
            pass

    @staticmethod
    def createPath(pic, path, fileName, father_file):  # 生成路径     文件对象  文件上一级目录名称 文件名称   static下面的目录名称（父目录）
        now = arrow.now().format('YYYY-MM-DD')
        file_suffix = str(pic).split(".")[-1]  # 文件后缀
        file_name = f"{fileName}.{file_suffix}"  # 文件名称
        file_path = os.path.join('static', father_file, 'report_upload_file', now, path, file_name)  # 文件路径
        file_path = file_path.replace('\\', '/')
        return (file_path, file_name, file_suffix)  # 文件路径   文件名字  文件后缀

    @staticmethod
    def saveFile(file_path, file_obj):  # 文件名,图像对象   文件保存
        with open(str(file_path), 'wb+') as f:
            for dot in file_obj.chunks():
                f.write(dot)
    @staticmethod
    def calculate_age(birthdate):
        # print(birthdate)
        today = datetime.today()
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
