import json, os, arrow, openpyxl, time, requests, random, calendar

from django.db.models import Q, F
from rest_framework import status
from django.http import JsonResponse

from auther.models import AdminUser
from employee.models import *

from datetime import datetime, date, timedelta

from expatriateRecord.immigration.models import *
from expatriateRecord.models import ImmigrationBase
from socialSecurity.Anomalies.models import *
from pdss.settings import BASE_DIR
from socialSecurity.publicMethods import *
from utils.sqlServerConnect import EhrConnect
from utils.wechat_interface import *


class Immigration:
    def __init__(self, request, meth):
        self.request = request
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功'
        }
        self.meth = meth
        self.now = arrow.now()
        self.t1 = self.now.format('YYYY-MM-DD')
        self.t2 = self.now.timestamp()
        self.methods = {
            'get_immigration_vietnam': self.get_immigration_vietnam,  # 出入境记录 查询越南的
            'down_immigration_vietnam': self.down_immigration_vietnam,  # 出入境记录 下载越南
            'get_immigration_thailand_not': self.get_immigration_thailand_not,  # 出入境记录 查询泰国没有签证的
            'get_immigration_thailand': self.get_immigration_thailand,  # 出入境记录 查询泰国有签证的
            'edit_immigration_info': self.edit_immigration_info,  # 出入境记录 修改
            'del_immigration_info': self.del_immigration_info,  # 出入境记录 删除
            'post_immigration_info': self.post_immigration_info,  # 出入境记录 新增

            'import_immigration_info': self.import_immigration_info,  # 出入境记录 上传
            'alert_info': self.alert_info,  # 消息提醒
            'calculate_attendance':self.calculate_attendance,#计算考勤
            'employee_fill': self.employee_fill,  # 员工提交
            'employee_fill_verify':self.employee_fill_verify,#校验填写时间
            'employee_fill_overrule': self.employee_fill_overrule,  # 员工提交驳回
        }
        self.Enterprise_WeChat = Enterprise_WeChat()  # 企业微信的接口

    def method_center(self):
        if self.meth in ['employee_fill', 'alert_info']:
            pass
        else:
            if self.request.check_token is None:
                self.return_data = {'code': status.HTTP_403_FORBIDDEN, "msg": '没有权限访问!'}
                return JsonResponse(self.return_data)

        self.methods[self.meth]()
        return JsonResponse(self.return_data)

    # 获取信息列表
    def get_immigration_vietnam(self):  # 越南
        column_list = [{'label': 'index', 'value': '序号', 'width': 60},
                       {'label': 'records_people__employee_code', 'value': '工号', 'width': 100},
                       {'label': 'records_people__employee_name', 'value': '姓名', 'width': 100},
                       {'label': 'records_passport', 'value': '护照号', 'width': ""},
                       {'label': 'records_stationed_country__country_name', 'value': '派驻国', 'width': ""},
                       {'label': 'records_stationed_base__base_name', 'value': '派驻基地', 'width': ""},
                       {'label': 'records_people__employee_join_date', 'value': '入职日期', 'width': ""},
                       {'label': 'records_people__employee_department__department_first_name', 'value': '一级部门','width': ""},
                       {'label': 'records_people__employee_department__department_second_name', 'value': '二级部门','width': ""},
                       {'label': 'records_people__employee_department__department_third_name', 'value': '三级部门','width': ""},
                       {'label': 'records_work_visa', 'value': '工作签', 'width': ""},
                       {'label': 'records_local_bank', 'value': '本地银行号', 'width': ""},
                       {'label': 'records_local_social_security', 'value': '本地社保号', 'width': ""},
                       {'label': 'records_local_individual_taxes', 'value': '本地个税号', 'width': ""},
                       {'label': 'records_leave_hour', 'value': '请假小时数', 'width': ""},
                       {'label': 'records_absenteeism_hour', 'value': '旷工小时数', 'width': ""},
                       {'label': 'fill_inout_status__type_name', 'value': '入越/离越/未离越', 'width': ""},
                       {'label': 'fill_into_date', 'value': '入越日期', 'width': ""},
                       {'label': 'fill_leave_date', 'value': '离越日期', 'width': ""},
                       {'label': 'fill_trip_reason', 'value': '行程原因', 'width': ""},
                       {'label': 'fill_remark', 'value': '备注', 'width': ""},
                       {'label': 'annex_ls', 'value': '出入境记录', 'width': ""},
                       {'label': 'fill_leave_address', 'value': '离越目的地', 'width': ""},
                       {'label': 'fill_leave_days', 'value': '离越天数', 'width': ""},
                       ]
        current_page = json.loads(self.request.body).get('currentPage')
        page_size = json.loads(self.request.body).get('pageSize')
        begin_date = to_date(json.loads(self.request.body).get('beginDate'))
        end_date = to_date(json.loads(self.request.body).get('endDate'))


        if begin_date is None or begin_date == '':
            begin_date = datetime(1901, 10, 29, 7, 17, 1, 177)
        if end_date is None or end_date == '':
            end_date =  datetime(3221, 10, 29, 7, 17, 1, 177)
        """     
        越南  11月默认看
            签证记录10/01  --  10/31     员工提交记录在11/01  --  11/03
        """
        record_list = list(ImmigrationRecords.objects.filter(records_status=1,
                                                             records_create_time__gte=begin_date,
                                                             records_create_time__lte=end_date,
                                                             records_stationed_country_id=2).values('id',
                                                                                                    'records_people__employee_code',
                                                                                                    'records_people__employee_name',
                                                                                                    'records_passport',
                                                                                                    'records_stationed_country__country_name',
                                                                                                    'records_stationed_base__base_name',
                                                                                                    'records_people__employee_department__department_first_name',
                                                                                                    'records_people__employee_department__department_second_name',
                                                                                                    'records_people__employee_department__department_third_name',
                                                                                                    'records_people__employee_join_date',
                                                                                                    'records_begin_data',
                                                                                                    'records_end_data',
                                                                                                    'records_work_visa',
                                                                                                    'records_local_bank',
                                                                                                    'records_local_social_security',
                                                                                                    'records_local_individual_taxes',
                                                                                                    'records_leave_hour',
                                                                                                    'records_absenteeism_hour'
                                                                                                    ).order_by(
            '-records_create_time'))[(current_page - 1) * page_size:current_page * page_size]

        record_id = [item['id'] for item in record_list]


        fill_list = list(ImmigrationFill.objects.filter(fill_status=True, fill_record_id__in=record_id,
                                                        # fill_create_time__lte=fill_end,
                                                        # fill_create_time__gte=fill_begin,
                                                        fill_approval_status=2
                                                        ).values('id','fill_record_id',
                                                                     'fill_inout_status__type_name',
                                                                     'fill_into_date',
                                                                     'fill_leave_date',
                                                                     'fill_trip_reason',
                                                                     'fill_leave_address',
                                                                     'fill_leave_days',
                                                                     'fill_remark'))


        fill_id_list = []
        for item_fill in fill_list:
            fill_id_list.append(item_fill['id'])
            item_fill['fill_id'] = item_fill.pop('id')
        print('fill_list', fill_list)

        print(fill_id_list)
        file_list = list(
            ImmigrationFiles.objects.filter(fill_file_id__in=fill_id_list, status=True).values('id','name','url','type','fill_file_id'))
        print(file_list)

        immigration_annex = {}  # 附件 出入境记录
        for item in file_list:  # 查找每份提案对应的文件
            fill_file_id = item.get('fill_file_id')
            if item['type'] == 1:  # 附件
                if fill_file_id not in immigration_annex:
                    immigration_annex[fill_file_id] = []
                immigration_annex[fill_file_id].append(item)

        for item in fill_list:
            fill_id = item.get('fill_id')
            if fill_id in immigration_annex:
                item['annex_ls'] = immigration_annex[fill_id]
                item['annex_num'] = len(immigration_annex[fill_id])
            else:
                item['annex_ls'] = []
                item['annex_num'] = 0


        table_list=[]
        for item_record in record_list:
            id_record = item_record['id']
            for item_fill in fill_list:
                fill_record_id_fill = item_fill.get('fill_record_id')
                if id_record == fill_record_id_fill:
                    merged_item = item_record.copy()
                    merged_item.update(item_fill)
                    table_list.append(merged_item)
        print(table_list)
        for item_record in record_list:
            id_record = item_record['id']
            if not any('fill_record_id' in item and  item['fill_record_id'] == id_record for item in table_list):
                table_list.append(item_record)


        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "信息返回成功",
            "data": {
                'columnList': column_list,
                'tableList': table_list,
                # 'totalNumber': totalNumber,
            }
        }

    def down_immigration_vietnam(self):
        dummy_path = os.path.join(BASE_DIR, 'static', 'immigrationFile', 'download_file', self.t1,str(self.t2))  # 创建文件夹
        mkdir(dummy_path)
        file_ls = [
            "序号", "工号", "姓名", "护照号", "派驻国家", "派驻基地", "入职日期", "一级部门", "二级部门", "三级部门",
            "考勤开始周期", "考勤结束周期", "工作签", "本地银行号", "本地社保号", "本地个税号","请假小时数", "旷工小时数",
            "入/离越/未离越", "入越日期", "离泰日期", "此次行程原因", "备注", "离越目的地", "离越天数",
        ]
        path = createExcelPath('出入境记录明细.xlsx', 'immigrationFile', str(self.t2), '出入境记录明细表', 40, 'A1:AA1',
                               *file_ls)
        print(path)
        id_list = json.loads(self.request.body).get('idList')
        downloadAll = json.loads(self.request.body).get('downloadAll')
        row_data = []
        if downloadAll == True:  # 是下载全部   有条件

            kwargs = {

            }
            begin_date = to_date(json.loads(self.request.body).get('beginDate'))
            end_date = to_date(json.loads(self.request.body).get('endDate'))
            if begin_date is None or begin_date == '':
                begin_date = datetime(1901, 10, 29, 7, 17, 1, 177)
            if end_date is None or end_date == '':
                end_date = datetime(3221, 10, 29, 7, 17, 1, 177)
            record_list = list(ImmigrationRecords.objects.filter(records_status=1, records_create_time__gte=begin_date,
                                                                 records_create_time__lte=end_date,
                                                                 records_stationed_country_id=2).values('id',
                                                                                                        'records_people__employee_code',
                                                                                                        'records_people__employee_name',
                                                                                                        'records_passport',
                                                                                                        'records_stationed_country__country_name',
                                                                                                        'records_stationed_base__base_name',
                                                                                                        'records_people__employee_department__department_first_name',
                                                                                                        'records_people__employee_department__department_second_name',
                                                                                                        'records_people__employee_department__department_third_name',
                                                                                                        'records_people__employee_join_date',
                                                                                                        'records_begin_data',
                                                                                                        'records_end_data',
                                                                                                        'records_work_visa',
                                                                                                        'records_local_bank',
                                                                                                        'records_local_social_security',
                                                                                                        'records_local_individual_taxes',
                                                                                                        'records_leave_hour',
                                                                                                        'records_absenteeism_hour'
                                                                                                        ).order_by('-records_create_time'))

            record_id = [item['id'] for item in record_list]
            index = 0
            for line in record_list:
                line['index'] = index + 1
                if len(line) == 0:
                    index = index
                index += 1
                line['records_work_visa']= '是' if line['records_work_visa'] == True else '否'
                line['records_local_bank'] = '是' if line['records_local_bank'] == True else '否'
                line['records_local_social_security'] = '是' if line['records_local_social_security'] == True else '否'
                line['records_local_individual_taxes'] = '是' if line['records_local_individual_taxes'] == True else '否'
            print(record_list)
            fill_list = list(ImmigrationFill.objects.filter(fill_status=True, fill_record_id__in=record_id,
                                                            # fill_create_time__lte=fill_end,
                                                            # fill_create_time__gte=fill_begin,
                                                            fill_approval_status=2).values('fill_record_id',
                                                                                           'fill_inout_status__type_name',
                                                                                           'fill_into_date',
                                                                                           'fill_leave_date',
                                                                                           'fill_trip_reason',
                                                                                           'fill_leave_address',
                                                                                           'fill_leave_days',
                                                                                           'fill_remark'
                                                                                           ))

            id_count = {item_a['id']: 1 for item_a in record_list}
            table_list = []
            for item_a in record_list:
                id_a = item_a['id']
                count = 0
                for item_b in fill_list:
                    fill_record_id_b = item_b.get('fill_record_id')
                    if id_a == fill_record_id_b:
                        merged_item = item_a.copy()
                        merged_item.update(item_b)
                        table_list.append(merged_item)
                        count += 1
                id_count[id_a] = max(count, 1)
            for item_a in record_list:
                id_a = item_a['id']
                if not any('fill_record_id' in item and item['fill_record_id'] == id_a for item in table_list):
                    table_list.append(item_a)  # Append unmatched items from 'record_list' to 'table_list'
            count_list = [id_count[item['id']] for item in record_list]
            table_list = self.sort_list_of_dicts(table_list)
            table_list = sorted(table_list, key=lambda x: x['index'])
            for line in table_list:
                # print(line)
                line_data = []
                for k, v in line.items():
                    if k not in ('id', 'fill_record_id'):
                        line_data.append(v)
                row_data.append(line_data)
            exc = openpyxl.load_workbook(path)  # 打开整个excel文件
            sheet = exc.worksheets[0]  # 打开第0张工作表(也就是第一张)
            for row in row_data:
                sheet.append(row)  # 在工作表中添加一行

            merge_rows_list = count_list
            # 初始化起始行
            start_row = 3

            # 循合并指定行数的A列到F列
            for merge_rows in merge_rows_list:
                end_row = start_row + merge_rows - 1
                for col in range(1, 19):  # 合并A列到F列
                    sheet.merge_cells(start_row=start_row, start_column=col, end_row=end_row, end_column=col)
                start_row = end_row + 1

            # 保存修改后的Excel文件
            exc.save(path)
            # 关闭Excel文件
            exc.close()

        else:
            record_list = list(ImmigrationRecords.objects.filter(records_status=1,id__in=id_list,
                                                                 records_stationed_country_id=2).values('id',
                                                                                                        'records_people__employee_code',
                                                                                                        'records_people__employee_name',
                                                                                                        'records_passport',
                                                                                                        'records_stationed_country__country_name',
                                                                                                        'records_stationed_base__base_name',
                                                                                                        'records_people__employee_department__department_first_name',
                                                                                                        'records_people__employee_department__department_second_name',
                                                                                                        'records_people__employee_department__department_third_name',
                                                                                                        'records_people__employee_join_date',
                                                                                                        'records_begin_data',
                                                                                                        'records_end_data',
                                                                                                        'records_work_visa',
                                                                                                        'records_local_bank',
                                                                                                        'records_local_social_security',
                                                                                                        'records_local_individual_taxes',
                                                                                                        'records_leave_hour',
                                                                                                        'records_absenteeism_hour'
                                                                                                        ).order_by('-records_create_time'))

            record_id = [item['id'] for item in record_list]
            index = 0
            for line in record_list:
                line['index'] = index + 1
                if len(line) == 0:
                    index = index
                index += 1
                line['records_work_visa'] = '是' if line['records_work_visa'] == True else '否'
                line['records_local_bank'] = '是' if line['records_local_bank'] == True else '否'
                line['records_local_social_security'] = '是' if line['records_local_social_security'] == True else '否'
                line['records_local_individual_taxes'] = '是' if line['records_local_individual_taxes'] == True else '否'
            print(record_list)
            fill_list = list(ImmigrationFill.objects.filter(fill_status=True, fill_record_id__in=record_id,
                                                            # fill_create_time__lte=fill_end,
                                                            # fill_create_time__gte=fill_begin,
                                                            fill_approval_status=2).values('fill_record_id',
                                                                                           'fill_inout_status__type_name',
                                                                                           'fill_into_date',
                                                                                           'fill_leave_date',
                                                                                           'fill_trip_reason',
                                                                                           'fill_leave_address',
                                                                                           'fill_leave_days',
                                                                                           'fill_remark'
                                                                                           ))

            id_count = {item_a['id']: 1 for item_a in record_list}
            table_list = []
            for item_a in record_list:
                id_a = item_a['id']
                count = 0
                for item_b in fill_list:
                    fill_record_id_b = item_b.get('fill_record_id')
                    if id_a == fill_record_id_b:
                        merged_item = item_a.copy()
                        merged_item.update(item_b)
                        table_list.append(merged_item)
                        count += 1
                id_count[id_a] = max(count, 1)
            for item_a in record_list:
                id_a = item_a['id']
                if not any('fill_record_id' in item and item['fill_record_id'] == id_a for item in table_list):
                    table_list.append(item_a)  # Append unmatched items from 'record_list' to 'table_list'
            count_list = [id_count[item['id']] for item in record_list]
            table_list = self.sort_list_of_dicts(table_list)
            table_list = sorted(table_list, key=lambda x: x['index'])
            for line in table_list:
                # print(line)
                line_data = []
                for k, v in line.items():
                    if k not in ('id', 'fill_record_id'):
                        line_data.append(v)
                row_data.append(line_data)
            exc = openpyxl.load_workbook(path)  # 打开整个excel文件
            sheet = exc.worksheets[0]  # 打开第0张工作表(也就是第一张)
            for row in row_data:
                sheet.append(row)  # 在工作表中添加一行

            merge_rows_list = count_list
            # 初始化起始行
            start_row = 3

            # 循合并指定行数的A列到F列
            for merge_rows in merge_rows_list:
                end_row = start_row + merge_rows - 1
                for col in range(1, 19):  # 合并A列到F列
                    sheet.merge_cells(start_row=start_row, start_column=col, end_row=end_row, end_column=col)
                start_row = end_row + 1

            # 保存修改后的Excel文件
            exc.save(path)
            # 关闭Excel文件
            exc.close()

        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "下载成功",
            "downloadUrl": path
        }

    @staticmethod
    def sort_list_of_dicts(list_of_dicts):
        # 指定排序顺序
        order = [
            'index', 'records_people__employee_code', 'records_people__employee_name', 'records_passport',
            'records_stationed_country__country_name', 'records_stationed_base__base_name',
            'records_people__employee_join_date', 'records_people__employee_department__department_first_name',
            'records_people__employee_department__department_second_name',
            'records_people__employee_department__department_third_name',
            'records_begin_data', 'records_end_data',
            'records_work_visa', 'records_local_bank', 'records_local_social_security',
            'records_local_individual_taxes','records_leave_hour','records_absenteeism_hour',
            'fill_inout_status__type_name', 'fill_into_date', 'fill_leave_date',
            'fill_trip_reason', 'fill_remark', 'fill_leave_address', 'fill_leave_days','fill_record_id', 'id'
        ]

        def sort_key(item):
            # 将缺失的键的值设置为默认值，这里默认值可以是 None
            key = item[0]
            return (order.index(key) if key in order else len(order), item[0])

        # 对列表中的每个字典按照指定的顺序排序
        sorted_list_of_dicts = [dict(sorted(d.items(), key=sort_key)) for d in list_of_dicts]
        return sorted_list_of_dicts

    def get_immigration_thailand_not(self):  # 泰国没有签证的
        column_list = [{'label': 'index', 'value': '序号', 'width': 60},
                       {'label': 'records_people__employee_code', 'value': '工号', 'width': 100},
                       {'label': 'records_people__employee_name', 'value': '姓名', 'width': 100},
                       {'label': 'records_passport', 'value': '护照号', 'width': ""},
                       {'label': 'records_stationed_country__country_name', 'value': '派驻国', 'width': ""},
                       {'label': 'records_stationed_base__base_name', 'value': '派驻基地', 'width': ""},
                       {'label': 'records_people__employee_join_date', 'value': '入职日期', 'width': ""},
                       {'label': 'records_people__employee_department__department_first_name', 'value': '一级部门','width': ""},
                       {'label': 'records_people__employee_department__department_second_name', 'value': '二级部门','width': ""},
                       {'label': 'records_people__employee_department__department_third_name', 'value': '三级部门','width': ""},
                       {'label': 'records_work_visa', 'value': '工作签', 'width': ""},
                       {'label': 'records_local_bank', 'value': '本地银行号', 'width': ""},
                       {'label': 'records_local_social_security', 'value': '本地社保号', 'width': ""},
                       {'label': 'records_local_individual_taxes', 'value': '本地个税号', 'width': ""}]
        current_page = json.loads(self.request.body).get('currentPage')
        page_size = json.loads(self.request.body).get('pageSize')
        begin_date = to_date(json.loads(self.request.body).get('beginDate'))
        end_date = to_date(json.loads(self.request.body).get('endDate'))
        now = datetime.now()
        if begin_date is None or begin_date == '':
            begin_date = now.replace(month=now.month - 1, day=1, hour=0, minute=0, second=0)  # 上个月第一天的00:00:00
        if end_date is None or end_date == '':
            _, num_days_prev_month = calendar.monthrange(now.year, now.month)
            end_date = now.replace(month=now.month - 1, day=num_days_prev_month, hour=23, minute=59,second=59)  # 上个月的最后一天的23:59:59

        fill_begin = datetime(self.now.year, self.now.month, 1, 00, 00, 00)  # 本月1号 00:00:00  员工上传的开始时间
        fill_end = datetime(self.now.year, self.now.month, 3, 17, 00, 00)  # 本月3号 17:00:00    员工上传的结束时间
        print(begin_date, end_date, fill_begin, fill_end)
        """     
        泰无签  11月默认看
            签证记录10/01  --  10/31     员工提交记录在11/01  --  11/03
        """

        record_list = list(ImmigrationRecords.objects.filter(Q(records_stationed_country_id=1) &
                                                             (Q(records_work_visa=False) | Q(
                                                                 records_local_bank=False) | Q(
                                                                 records_local_social_security=False) | Q(
                                                                 records_local_individual_taxes=False)),
                                                             records_status=1, records_create_time__gte=begin_date,
                                                             records_create_time__lte=end_date).values('id',
                                                                                                       'records_people__employee_code',
                                                                                                       'records_people__employee_name',
                                                                                                       'records_passport',
                                                                                                       'records_stationed_country__country_name',
                                                                                                       'records_stationed_base__base_name',
                                                                                                       'records_begin_data',
                                                                                                       'records_end_data',
                                                                                                       'records_work_visa',
                                                                                                       'records_local_bank',
                                                                                                       'records_local_social_security',
                                                                                                       'records_local_individual_taxes'
                                                                                                       ).order_by(
            '-records_create_time'))[(current_page - 1) * page_size:current_page * page_size]

        record_id = [item['id'] for item in record_list]


        fill_list = list(ImmigrationFill.objects.filter(fill_status=True, fill_record_id__in=record_id,
                                                        fill_create_time__lte=fill_end,
                                                        fill_create_time__gte=fill_begin).values('id','fill_record_id',
                                                                                                 'fill_inout_status__type_name',
                                                                                                 'fill_into_thailand_date',
                                                                                                 'fill_leave_thailand_date',
                                                                                                 'fill_trip_reason',
                                                                                                 'fill_leave_thailand_address',
                                                                                                 'fill_leave_thailand_days',
                                                                                                 'fill_leave_hour',
                                                                                                 'fill_absenteeism_hour',
                                                                                                 'fill_remark'))


        fill_id_list=[]
        for item_fill in fill_list:
            fill_id_list.append(item_fill['id'])
            item_fill['fill_id'] = item_fill.pop('id')
        print(fill_id_list)
        file_list = list(
            ImmigrationFiles.objects.filter(fill_file_id__in=fill_id_list, status=True).values('id',
                                                                                        'name',
                                                                                        'url',
                                                                                        'type',
                                                                                        'fill_file_id'))
        print(file_list)

        immigration_annex= {}  # 附件 出入境记录
        for item in file_list:  # 查找每份提案对应的文件
            fill_file_id = item.get('fill_file_id')
            if item['type'] == 1:  # 附件
                if fill_file_id not in immigration_annex:
                    immigration_annex[fill_file_id] = []
                immigration_annex[fill_file_id].append(item)

        for item in fill_list:
            fill_id = item.get('fill_id')
            if fill_id in immigration_annex:
                item['annex_ls'] = immigration_annex[fill_id]
                item['annex_num'] = len(immigration_annex[fill_id])
            else:
                item['annex_ls'] = []
                item['annex_num'] = 0


        table_list = []
        for item_record in record_list:
            id_record = item_record['id']
            for item_fill in fill_list:
                fill_record_id_fill = item_fill.get('fill_record_id')
                if id_record == fill_record_id_fill:
                    merged_item = item_record.copy()
                    merged_item.update(item_fill)
                    table_list.append(merged_item)
        for item_record in record_list:
            id_record = item_record['id']
            if not any('fill_record_id' in item and  item['fill_record_id'] == id_record for item in table_list):
                table_list.append(item_record)

        # print('table_list',table_list)

        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "信息返回成功",
            "data": {
                'columnList': column_list,
                'tableList': table_list,
                # 'totalNumber': totalNumber,
            }
        }

    def get_immigration_thailand(self):  #泰国有签证的
        column_list = [{'label': 'index', 'value': '序号', 'width': 60},
                      {'label': 'records_people__employee_code', 'value': '工号', 'width': 100},
                      {'label': 'records_people__employee_name', 'value': '姓名', 'width': 100},
                      {'label': 'records_passport', 'value': '护照号', 'width': ""},
                      {'label': 'records_stationed_country__country_name', 'value': '派驻国', 'width': ""},
                      {'label': 'records_stationed_base__base_name', 'value': '派驻基地', 'width': ""},
                      {'label': 'records_people__employee_join_date', 'value': '入职日期', 'width': ""},
                      {'label': 'records_people__employee_department__department_first_name', 'value': '一级部门',
                       'width': ""},
                      {'label': 'records_people__employee_department__department_second_name', 'value': '二级部门',
                       'width': ""},
                      {'label': 'records_people__employee_department__department_third_name', 'value': '三级部门',
                       'width': ""},
                      {'label': 'records_work_visa', 'value': '工作签', 'width': ""},
                      {'label': 'records_local_bank', 'value': '本地银行号', 'width': ""},
                      {'label': 'records_local_social_security', 'value': '本地社保号', 'width': ""},
                      {'label': 'records_local_individual_taxes', 'value': '本地个税号', 'width': ""},

                      ]
        current_page = json.loads(self.request.body).get('currentPage')
        page_size = json.loads(self.request.body).get('pageSize')
        begin_date = to_date(json.loads(self.request.body).get('beginDate'))
        end_date = to_date(json.loads(self.request.body).get('endDate'))
        now = datetime.now()
        if begin_date is None or begin_date == '':
            begin_date = datetime(self.now.year, self.now.month - 1, 21, 00, 00, 00)  # 上个月21日00：00：00
        fill_begin = datetime(self.now.year, self.now.month, 21, 00, 00, 00)  # 本月21 00:00:00  员工上传的开始时间
        if end_date is None or end_date == '':
            end_date = datetime(self.now.year, self.now.month, 20, 23, 59, 59)  # 这个月20日23：59：59
        fill_end = datetime(self.now.year, self.now.month, 23, 17, 00, 00)  # 本月23 17:00:00    员工上传的结束时间

        """     
        泰有签  11月默认看
            签证记录10/21  --  11/20     员工提交记录在11/21  --  11/23
        """



        record_list = list(ImmigrationRecords.objects.filter(records_status=1,
                                                                records_stationed_country_id=1,
                                                                records_work_visa=True, records_local_bank=True,
                                                                records_local_social_security=True,
                                                                records_local_individual_taxes=True,
                                                                records_create_time__gte=begin_date,
                                                                records_create_time__lte=end_date).values('id',
                                                                                                    'records_people__employee_code',
                                                                                                    'records_people__employee_name',
                                                                                                    'records_passport',
                                                                                                    'records_stationed_country__country_name',
                                                                                                    'records_stationed_base__base_name',
                                                                                                    'records_begin_data',
                                                                                                    'records_end_data',
                                                                                                    'records_work_visa',
                                                                                                    'records_local_bank',
                                                                                                    'records_local_social_security',
                                                                                                    'records_local_individual_taxes'
                                                                                                    ).order_by(
            '-records_create_time'))[(current_page - 1) * page_size:current_page * page_size]

        record_id = [item['id'] for item in record_list]


        fill_list = list(ImmigrationFill.objects.filter(fill_status=True, fill_record_id__in=record_id,
                                                        fill_create_time__lte=fill_end,
                                                        fill_create_time__gte=fill_begin).values('id','fill_record_id',
                                                                                                 'fill_inout_status__type_name',
                                                                                                 'fill_into_thailand_date',
                                                                                                 'fill_leave_thailand_date',
                                                                                                 'fill_trip_reason',
                                                                                                 'fill_leave_thailand_address',
                                                                                                 'fill_leave_thailand_days',
                                                                                                 'fill_leave_hour',
                                                                                                 'fill_absenteeism_hour',
                                                                                                 'fill_remark'))


        fill_id_list=[]
        for item_fill in fill_list:
            fill_id_list.append(item_fill['id'])
            item_fill['fill_id'] = item_fill.pop('id')
        print(fill_id_list)
        file_list = list(
            ImmigrationFiles.objects.filter(fill_file_id__in=fill_id_list, status=True).values('id',
                                                                                        'name',
                                                                                        'url',
                                                                                        'type',
                                                                                        'fill_file_id'))
        print(file_list)

        immigration_annex= {}  # 附件 出入境记录
        for item in file_list:  # 查找每份提案对应的文件
            fill_file_id = item.get('fill_file_id')
            if item['type'] == 1:  # 附件
                if fill_file_id not in immigration_annex:
                    immigration_annex[fill_file_id] = []
                immigration_annex[fill_file_id].append(item)

        for item in fill_list:
            fill_id = item.get('fill_id')
            if fill_id in immigration_annex:
                item['annex_ls'] = immigration_annex[fill_id]
                item['annex_num'] = len(immigration_annex[fill_id])
            else:
                item['annex_ls'] = []
                item['annex_num'] = 0


        table_list = []
        for item_record in record_list:
            id_record = item_record['id']
            for item_fill in fill_list:
                fill_record_id_fill = item_fill.get('fill_record_id')
                if id_record == fill_record_id_fill:
                    merged_item = item_record.copy()
                    merged_item.update(item_fill)
                    table_list.append(merged_item)
        for item_record in record_list:
            id_record = item_record['id']
            if not any(item['fill_record_id'] == id_record for item in table_list):
                table_list.append(item_record)

        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "信息返回成功",
            "data": {
                # 'columnList': columnList,
                'tableList': table_list,
                # 'totalNumber': totalNumber,
            }
        }

    def edit_immigration_info(self):
        info = json.loads(self.request.body)
        records = {
            'records_passport': info['records_passport'],
            'records_stationed_country_id': info['records_stationed_country'],
            'records_stationed_base_id': info['records_stationed_base'],
            'records_begin_data': to_date(info['records_begin_data']),
            'records_end_data': to_date(info['records_end_data']),
            'records_work_visa': info['records_work_visa'],
            'records_local_bank': info['records_local_bank'],
            'records_local_social_security': info['records_local_social_security'],
            'records_local_individual_taxes': info['records_local_individual_taxes'],
            'records_modifier_id': self.request.check_token,
        }
        ImmigrationRecords.objects.filter(id=info['id']).update(**records)
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "修改成功"
        }

    def post_immigration_info(self):
        info = json.loads(self.request.body)
        print(info)
        immigration_params={'records_people_id': info['records_people'],
                            'records_passport': info['records_passport'],
                            'records_stationed_country_id': info['records_stationed_country'],
                            'records_stationed_base_id':info['records_stationed_base'],
                            'records_begin_data':info['records_begin_data'],
                            'records_end_data': info['records_end_data'],
                            'records_work_visa': info['records_work_visa'],
                            'records_local_bank':info['records_local_bank'],
                            'records_local_social_security': info['records_local_social_security'],
                            'records_local_individual_taxes': info['records_local_individual_taxes'],
                            'records_creator_id':self.request.check_token
                            }
        ImmigrationRecords.objects.update_or_create(defaults=immigration_params,records_people_id=immigration_params['records_people_id'],records_status=True,records_begin_data=immigration_params['records_begin_data'],records_end_data=immigration_params['records_end_data'])

        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "新增成功",
        }

    def del_immigration_info(self):
        info = json.loads(self.request.body)
        id_list=info['idList']
        ImmigrationRecords.objects.filter(id__in=id_list).update(records_status=False)
        ImmigrationFill.objects.filter(fill_record_id__in=id_list).update(fill_status=False)
        ImmigrationFiles.objects.filter(fill_file_id__in=id_list).update(status=False)
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "删除成功",
        }

    def import_immigration_info(self):
        file = self.request.FILES.get("file", None)

        dummy_path = os.path.join(BASE_DIR, 'static', 'expatriateRecordFile', 'upload_file', self.t1,
                                  '出入境签证组文件上传')  # 创建文件夹
        mkdir(dummy_path)
        file_url, file_name, file_suffix = createPath(file, '出入境签证组文件上传', 'expatriateRecordFile',
                                                      '出入境签证组文件' + str(self.t2))
        saveFile(file_url, file)
        exc = openpyxl.load_workbook(file_url, data_only=True)
        sheet = exc.active
        # access_token = self.Enterprise_WeChat.get_wx_access_token()  # access_token
        for line in range(1, sheet.max_row):  # 每行数据
            code = sheet.cell(line + 1, 2).value
            name = sheet.cell(line + 1, 3).value
            passport = sheet.cell(line + 1, 4).value
            country = sheet.cell(line + 1, 5).value
            base = sheet.cell(line + 1, 6).value
            begin_data = to_date(sheet.cell(line + 1, 7).value)
            end_data = to_date(sheet.cell(line + 1, 8).value)

            employee_obj = HrEmployee.objects.filter(employee_code=code, employee_status='1').first()
            if employee_obj:
                country_obj = ImmigrationCountry.objects.filter(country_name=country, country_status='1').first()
                if country_obj:
                    base_obj = ImmigrationBase.objects.filter(base_name=base, base_status='1').first()
                    if base_obj:
                        if begin_data is None or end_data is None:
                            self.return_data = {
                                "code": status.HTTP_200_OK,
                                "msg": "考勤开始或结束周期日期格式错误,应为日期类型,格式为%Y-%m-%d"
                            }
                            continue
                        else:
                            # records_month=date(self.now.year, self.now.month, 1)  # 这个月的第一天
                            # print(records_month)
                            records = {
                                'records_people_id': employee_obj.id,
                                'records_passport': passport,
                                'records_stationed_country_id': country_obj.id,
                                'records_stationed_base_id': base_obj.id,
                                'records_begin_data': begin_data,
                                'records_end_data': end_data,
                                'records_creator_id':self.request.check_token,
                            }
                            ImmigrationRecords.objects.update_or_create(defaults=records,records_people_id=employee_obj.id ,records_status=True,records_begin_data=records['records_begin_data'],records_end_data=records['records_end_data'])
                            self.return_data = {
                                "code": status.HTTP_200_OK,
                                "msg": "上传成功·!"
                            }
                    else:
                        self.return_data = {
                            "code": status.HTTP_200_OK,
                            "msg": "派驻基地错误,无法上传"
                        }
                        continue
                else:
                    self.return_data = {
                        "code": status.HTTP_200_OK,
                        "msg": "派驻国家错误,无法上传"
                    }
                    continue
            else:
                self.return_data = {
                    "code": status.HTTP_200_OK,
                    "msg": "该员工已离职,或工号错误,无法上传"
                }
                continue

    def alert_info(self):  # 每天10点执行
        '''

         2023-10-27 09：00：00   --   2023-10-27 17：00：00     第三天     今天
         2023-10-26 09：00：00   --   2023-10-27 09：00：00     第二天     昨天
         2023-10-25 09：00：00   --   2023-10-26 09：00：00     第一天     前天  这条记录的创建时间

         2023-10-27 09：00：00执行推送  我可以找创建记录在2023-10-25 09：00：00   --   2023-10-26 09：00：00里面的记录
                                            如果员工没有在2023-10-25 09:00:00和2023-10-27 09：00：00之间填写，那么是不是就是第二天没有提交的       执行推送
                                            如果员工有在2023-10-25 09:00:00和2023-10-27 09：00：00之间填写，那么就是第二天有提交的
                                                        分为  有驳回的 和   未驳回的(不执行推送)
                                                        有驳回的  点击驳回 推送

         # 越南
         #    签证记录09/01  --  09/30     员工提交记录在10/01  --  10/03
         #    签证记录10/01  --  10/31     员工提交记录在11/01  --  11/03
         #    签证记录11/01  --  11/30     员工提交记录在12/01  --  12/03



         2023-10-23 10：00：00   --   2023-10-23 17：00：00     第三天
         2023-10-22 10：00：00   --   2023-10-23 09：59：59     第二天
         2023-10-21 10：00：00   --   2023-10-22 09：59：59     第一天        第一次推送


         2023-10-03 10：00：00   --   2023-10-03 17：00：00     第三天
         2023-10-02 10：00：00   --   2023-10-03 09：59：59     第二天
         2023-10-01 10：00：00   --   2023-10-02 09：59：59     第一天        第一次推送

        泰国有签证:每月21日推送 签证组上传记录在上月21日00：00：00到本月20日23：59：59创建的数据
        泰国无签证:每月1日推送 签证组上传记录在上月1日00：00：00到上月最后一日23：59：59创建的数据
        越南:每月1日推送 签证组上传记录在上月1日00：00：00到上月最后一日23：59：59创建的数据

        '''

        access_token = self.Enterprise_WeChat.get_wx_access_token()  # access_token
        # 第一次推送信息
        if self.now.day == 21:
            if self.now.hour == 10:
                begin = datetime(self.now.year, self.now.month - 1, 21, 00, 00, 00)  # 上个月21日00：00：00
                end = datetime(self.now.year, self.now.month, 20, 23, 59, 59)  # 这个月20日23：59：59

                record_list = list(
                    ImmigrationRecords.objects.filter(records_status=True, records_stationed_country_id=1,
                                                      records_work_visa=True, records_local_bank=True,
                                                      records_local_social_security=True,
                                                      records_local_individual_taxes=True,
                                                      records_create_time__lte=end,  # 这个月20日23：59：59
                                                      records_create_time__gte=begin  # 上个月21日00：00：00
                                                      ).values('records_people__employee_code',
                                                               'records_people__employee_name'))  # 上月泰国有工作签的
                for item in record_list:
                    push_info = {
                        'code': item['records_people__employee_code'],
                        'name': item['records_people__employee_name'],
                        'content': '请您在{}起的三天内上传您的出入境记录'.format(self.t1)
                    }
                    self.Enterprise_WeChat.post_wx_message(access_token, **push_info)
        elif self.now.day == 1:
            if self.now.hour == 10:
                now = datetime.now()
                first_day_last_month = now.replace(month=now.month - 1, day=1, hour=0, minute=0,
                                                   second=0)  # 上个月第一天的00:00:00
                _, num_days_prev_month = calendar.monthrange(now.year, now.month - 1)
                last_day_last_month = now.replace(month=now.month - 1, day=num_days_prev_month, hour=23, minute=59,
                                                  second=59)  # 上个月的最后一天的23:59:59

                # 查询派驻国是泰国的，且四个签证只要有一个不是Flase的，还有就是派驻国是越南的
                record_list = list(ImmigrationRecords.objects.filter(
                    Q(records_stationed_country__country_name='泰国') &
                    (Q(records_work_visa=False) | Q(records_local_bank=False) | Q(
                        records_local_social_security=False) | Q(records_local_individual_taxes=False)),
                    records_status=True, records_create_time__gte=first_day_last_month,
                    records_create_time__lte=last_day_last_month
                ).values('records_people__employee_code',
                         'records_people__employee_name') | ImmigrationRecords.objects.filter(
                    records_stationed_country__country_name='越南', records_status=True,
                    records_create_time__gte=first_day_last_month, records_create_time__lte=last_day_last_month).values(
                    'records_people__employee_code', 'records_people__employee_name'))

                for item in record_list:
                    push_info = {
                        'code': item['records_people__employee_code'],
                        'name': item['records_people__employee_name'],
                        'content': '请您在{}起的三天内上传您的出入境记录'.format(self.t1)
                    }
                    self.Enterprise_WeChat.post_wx_message(access_token, **push_info)

        # 给未提交的员工第二次推送信息
        if self.now.day == 22 and self.now.hour == 10:  # 第一天未提交的 第二天开始推送   泰国有签证
            record_begin = datetime(self.now.year, self.now.month - 1, 21, 00, 00, 00)  # 上个月21日00：00：00
            record_end = datetime(self.now.year, self.now.month, 20, 23, 59, 59)  # 这个月20日23：59：59
            fill_begin = datetime(self.now.year, self.now.month, 21, 00, 00, 00)  # 本月21 00:00:00  员工第一天的上传的开始时间
            fill_end = datetime(self.now.year, self.now.month, 22, 9, 59, 59)  # 本月22 09:59:59    员工第一天的上传的结束时间
            all_record_list = list(
                ImmigrationRecords.objects.filter(records_status=True, records_stationed_country_id=1,
                                                  records_work_visa=True, records_local_bank=True,
                                                  records_local_social_security=True,
                                                  records_local_individual_taxes=True,
                                                  records_create_time__lte=record_end,  # 这个月20日23：59：59
                                                  records_create_time__gte=record_begin  # 上个月21日00：00：00
                                                  ).values('id', 'records_people__employee_code',
                                                           'records_people__employee_name'))  # 上月泰国有工作签的员工
            # 查找所有签证组上传的所有员工        在员工填写表中,跟据该员工id,以及填写时间,找到该员工的填写记录
            # 如果找到了状态是已驳回依然要发送，
            # 没有记录也要发送
            for item in all_record_list:
                # 员工要么没填写 要么已经填写，如果已经填写找出这个人的最后一条记录，如果审批状态是驳回，再次发送
                fill_obj = ImmigrationFill.objects.filter(fill_record_id=item['id'], fill_status=True,
                                                          fill_create_time__gte=fill_begin,
                                                          fill_create_time__lte=fill_end).last()
                print(fill_obj)
                if fill_obj:
                    if fill_obj.fill_approval_status == 3:
                        push_info = {
                            'code': item['records_people__employee_code'],
                            'name': item['records_people__employee_name'],
                            'content': '因为您的上传记录被驳回,请您再次上传您的出入境记录'
                        }
                        self.Enterprise_WeChat.post_wx_message(access_token, **push_info)
                else:
                    push_info = {
                        'code': item['records_people__employee_code'],
                        'name': item['records_people__employee_name'],
                        'content': '因为您未在规定时间内再次上传，请您尽快提交您的出入境记录'
                    }
                    self.Enterprise_WeChat.post_wx_message(access_token, **push_info)
            '''
            第一次推送时间 2023-10-21 10:00:00   
            员工填写时间   2023-10-21 12:00:00  但是这条员工填写记录不久之后被驳回了,
                                              第二天即 2023-10-22 10:00:00 之前这名员工都没有再次提交记录 ,
                                              那么2023-10-22 10:00:00这次提醒也需要再次提醒该员工提交
            '''
        if self.now.day == 2 and self.now.hour == 10:  # 第一天未提交的 第二天开始推送   泰国无签证  及越南
            now = datetime.now()
            record_begin = now.replace(month=now.month - 1, day=1, hour=0, minute=0, second=0)  # 上个月第一天的00:00:00
            _, num_days_prev_month = calendar.monthrange(now.year, now.month - 1)
            record_end = now.replace(month=now.month - 1, day=num_days_prev_month, hour=23, minute=59,
                                     second=59)  # 上个月的最后一天的23:59:59

            fill_begin = datetime(self.now.year, self.now.month, 2, 00, 00, 00)  # 本月2号 00:00:00  员工第一天的上传的开始时间
            fill_end = datetime(self.now.year, self.now.month, 3, 9, 59, 59)  # 本月3号 09:59:59    员工第一天的上传的结束时间
            all_record_list = list(ImmigrationRecords.objects.filter(
                Q(records_stationed_country__country_name='泰国') &
                (Q(records_work_visa=False) | Q(records_local_bank=False) | Q(records_local_social_security=False) | Q(
                    records_local_individual_taxes=False)),
                records_status=True, records_create_time__gte=record_begin,
                records_create_time__lte=record_end
            ).values('id', 'records_people__employee_code',
                     'records_people__employee_name') | ImmigrationRecords.objects.filter(
                records_stationed_country__country_name='越南', records_status=True,
                records_create_time__gte=record_begin, records_create_time__lte=record_end).values('id',
                                                                                                 'records_people__employee_code',
                                                                                                 'records_people__employee_name'))
            for item in all_record_list:
                # 员工要么没填写 要么已经填写，如果已经填写找出这个人的最后一条记录，如果审批状态是驳回，再次发送
                fill_obj = ImmigrationFill.objects.filter(fill_record_id=item['id'], fill_status=True,
                                                          fill_create_time__gte=fill_begin,
                                                          fill_create_time__lte=fill_end).last()
                print(fill_obj)
                if fill_obj:
                    if fill_obj.fill_approval_status == 3:
                        push_info = {
                            'code': item['records_people__employee_code'],
                            'name': item['records_people__employee_name'],
                            'content': '因为您的上传记录被驳回,请您再次上传您的出入境记录'
                        }
                        self.Enterprise_WeChat.post_wx_message(access_token, **push_info)
                else:
                    push_info = {
                        'code': item['records_people__employee_code'],
                        'name': item['records_people__employee_name'],
                        'content': '因为您未在规定时间内再次上传，请您尽快提交您的出入境记录'
                    }
                    self.Enterprise_WeChat.post_wx_message(access_token, **push_info)

        # 给未提交的员工第三次推送信息
        if self.now.day == 23 and self.now.hour == 10:  # 第一天未提交的或驳回没有成功的 第三天开始推送   泰国有签证
            record_begin = datetime(self.now.year, self.now.month - 1, 21, 00, 00, 00)  # 上个月21日00：00：00   签证组上传记录
            record_end = datetime(self.now.year, self.now.month, 20, 23, 59, 59)  # 这个月20日23：59：59
            fill_begin = datetime(self.now.year, self.now.month, 21, 00, 00, 00)  # 本月21 00:00:00  员工第一天的上传的开始时间
            fill_end = datetime(self.now.year, self.now.month, 23, 9, 59, 59)  # 本月22 09:59:59    员工第二天的上传的结束时间
            all_record_list = list(
                ImmigrationRecords.objects.filter(records_status=True, records_stationed_country_id=1,
                                                  records_work_visa=True, records_local_bank=True,
                                                  records_local_social_security=True,
                                                  records_local_individual_taxes=True,
                                                  records_create_time__lte=record_end,  # 这个月20日23：59：59
                                                  records_create_time__gte=record_begin  # 上个月21日00：00：00
                                                  ).values('id', 'records_people__employee_code',
                                                           'records_people__employee_name'))
            for item in all_record_list:
                # 员工要么没填写 要么已经填写，如果已经填写找出这个人的最后一条记录，如果审批状态是驳回，再次发送
                fill_obj = ImmigrationFill.objects.filter(fill_record_id=item['id'], fill_status=True,
                                                          fill_create_time__gte=fill_begin,
                                                          fill_create_time__lte=fill_end).last()
                if fill_obj:
                    if fill_obj.fill_approval_status == 3:
                        push_info = {
                            'code': item['records_people__employee_code'],
                            'name': item['records_people__employee_name'],
                            'content': '因为您的上传记录被驳回,请您再次上传您的出入境记录'
                        }
                        self.Enterprise_WeChat.post_wx_message(access_token, **push_info)
                else:
                    push_info = {
                        'code': item['records_people__employee_code'],
                        'name': item['records_people__employee_name'],
                        'content': '因为您未在规定时间内再次上传，请您尽快提交您的出入境记录'
                    }
                    self.Enterprise_WeChat.post_wx_message(access_token, **push_info)
        if self.now.day == 3 and self.now.hour == 10:  # 第俩天都没有提交，或提交被驳回没有再次上传的 第三天开始推送   泰国无签证  及越南
            now = datetime.now()
            record_begin = now.replace(month=now.month - 1, day=1, hour=0, minute=0, second=0)  # 上个月第一天的00:00:00
            _, num_days_prev_month = calendar.monthrange(now.year, now.month - 1)
            record_end = now.replace(month=now.month - 1, day=num_days_prev_month, hour=23, minute=59,
                                     second=59)  # 上个月的最后一天的23:59:59

            fill_begin = datetime(self.now.year, self.now.month, 1, 00, 00, 00)  # 本月1号 00:00:00  员工第一天的上传的开始时间
            fill_end = datetime(self.now.year, self.now.month, 3, 9, 59, 59)  # 本月3号 09:59:59    员工第二天的上传的结束时间
            all_record_list = list(ImmigrationRecords.objects.filter(
                Q(records_stationed_country__country_name='泰国') &
                (Q(records_work_visa=False) | Q(records_local_bank=False) | Q(records_local_social_security=False) | Q(
                    records_local_individual_taxes=False)),
                records_status=True, records_create_time__gte=record_begin,
                records_create_time__lte=record_end
            ).values('id', 'records_people__employee_code',
                     'records_people__employee_name') | ImmigrationRecords.objects.filter(
                records_stationed_country__country_name='越南', records_status=True,
                records_create_time__gte=record_begin, records_create_time__lte=record_end).values('id',
                                                                                                 'records_people__employee_code',
                                                                                                 'records_people__employee_name'))
            for item in all_record_list:
                # 员工要么没填写 要么已经填写，如果已经填写找出这个人的最后一条记录，如果审批状态是驳回，再次发送
                fill_obj = ImmigrationFill.objects.filter(fill_record_id=item['id'], fill_status=True,
                                                          fill_create_time__gte=fill_begin,
                                                          fill_create_time__lte=fill_end).last()
                print(fill_obj)
                if fill_obj:
                    if fill_obj.fill_approval_status == 3:
                        push_info = {
                            'code': item['records_people__employee_code'],
                            'name': item['records_people__employee_name'],
                            'content': '因为您的上传记录被驳回,请您再次上传您的出入境记录'
                        }
                        self.Enterprise_WeChat.post_wx_message(access_token, **push_info)
                else:
                    push_info = {
                        'code': item['records_people__employee_code'],
                        'name': item['records_people__employee_name'],
                        'content': '因为您未在规定时间内再次上传，请您尽快提交您的出入境记录'
                    }
                    self.Enterprise_WeChat.post_wx_message(access_token, **push_info)

        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "推送消息发送成功",
        }


    def calculate_attendance(self):
        """
        11月 计算考勤开始周期是10月1号到最后一天   泰无签
        11月 计算考勤开始周期是上个月10月21号到这个月的20号  泰有签
        :return:
        """
        now = datetime.now()
        record_begin = now.replace(month=now.month - 1, day=1)  # 上个月第一天
        _, num_days_prev_month = calendar.monthrange(now.year, now.month - 1)
        record_end = now.replace(month=now.month - 1, day=num_days_prev_month)  # 上个月的最后一天 转换为日期类型
        record_list=list(ImmigrationRecords.objects.filter(records_status=True,records_begin_data=record_begin,records_end_data=record_end).values('id','records_people_id','records_begin_data','records_end_data'))
        ehr_connect = EhrConnect()
        for line in record_list:
            select_sql='''
                SELECT
                 EmpID,
                 (COALESCE(SUM(sj) / 60.0, 0) +
                 COALESCE(SUM(bj) / 60.0, 0) +
                 COALESCE(SUM(hj) / 60.0, 0) +
                 COALESCE(SUM(nj) / 60.0, 0) +
                 COALESCE(SUM(cj) / 60.0, 0) +
                 COALESCE(SUM(gs) / 60.0, 0) +
                 COALESCE(SUM(cc) / 60.0, 0) +
                 COALESCE(SUM(tx) / 60.0, 0) +
                 COALESCE(SUM(saj) / 60.0, 0) +
                 COALESCE(SUM(pcj) / 60.0, 0) +
                 COALESCE(SUM(brj) / 60.0, 0) +
                 COALESCE(SUM(yqjxs), 0) +
                 COALESCE(SUM(yejxs), 0) +
                 COALESCE(SUM(hljxs), 0) +
                 COALESCE(SUM(dxsjxs), 0) +
                 COALESCE(SUM(dxbjxs), 0) +
                 COALESCE(SUM(chujjxs), 0) +
                 COALESCE(SUM(tqjxs), 0) +
                 COALESCE(SUM(byxlxs), 0) +
                 COALESCE(SUM(chujiaxs), 0) +
                 COALESCE(SUM(peixunxs), 0) +
                 COALESCE(SUM(lqxwxs), 0) +
                 COALESCE(SUM(jueyuxs), 0) +
                 COALESCE(SUM(fdxcjxs), 0) +
                 COALESCE(SUM(lcxs), 0) ) as total_qj_hours,
                 COALESCE(SUM(kgxs), 0) as Total_kgxs_hours
                FROM
                 T_HR_WorkingTime
                WHERE
                 EmpID = {}
                 AND WorkDate BETWEEN '{}' AND '{}'
                GROUP BY
                 EmpID
            '''.format(line['records_people_id'], line['records_begin_data'],line['records_end_data'])
            ehr_kq_data = ehr_connect.select(select_sql)
            ImmigrationRecords.objects.filter(pk=line['id'],records_status=True).update(records_leave_hour=float(ehr_kq_data[0]['total_qj_hours']),records_absenteeism_hour=float(ehr_kq_data[0]['Total_kgxs_hours']))



        # #泰有签的记录
        record_begin_t = datetime(self.now.year, self.now.month - 1, 21, 00, 00, 00)  # 上个月21日00：00：00   签证组上传记录
        record_end_t = datetime(self.now.year, self.now.month, 20, 23, 59, 59)  # 这个月20日23：59：59
        record_list=list(ImmigrationRecords.objects.filter(records_status=True,records_begin_data=record_begin_t, records_end_data=record_end_t).values('id','records_people_id','records_begin_data','records_end_data'))
        ehr_connect = EhrConnect()
        for line in record_list:
            select_sql='''
                SELECT
                 EmpID,
                 (COALESCE(SUM(sj) / 60.0, 0) +
                 COALESCE(SUM(bj) / 60.0, 0) +
                 COALESCE(SUM(hj) / 60.0, 0) +
                 COALESCE(SUM(nj) / 60.0, 0) +
                 COALESCE(SUM(cj) / 60.0, 0) +
                 COALESCE(SUM(gs) / 60.0, 0) +
                 COALESCE(SUM(cc) / 60.0, 0) +
                 COALESCE(SUM(tx) / 60.0, 0) +
                 COALESCE(SUM(saj) / 60.0, 0) +
                 COALESCE(SUM(pcj) / 60.0, 0) +
                 COALESCE(SUM(brj) / 60.0, 0) +
                 COALESCE(SUM(yqjxs), 0) +
                 COALESCE(SUM(yejxs), 0) +
                 COALESCE(SUM(hljxs), 0) +
                 COALESCE(SUM(dxsjxs), 0) +
                 COALESCE(SUM(dxbjxs), 0) +
                 COALESCE(SUM(chujjxs), 0) +
                 COALESCE(SUM(tqjxs), 0) +
                 COALESCE(SUM(byxlxs), 0) +
                 COALESCE(SUM(chujiaxs), 0) +
                 COALESCE(SUM(peixunxs), 0) +
                 COALESCE(SUM(lqxwxs), 0) +
                 COALESCE(SUM(jueyuxs), 0) +
                 COALESCE(SUM(fdxcjxs), 0) +
                 COALESCE(SUM(lcxs), 0) ) as total_qj_hours,
                 COALESCE(SUM(kgxs), 0) as Total_kgxs_hours
                FROM
                 T_HR_WorkingTime
                WHERE
                 EmpID = {}
                 AND WorkDate BETWEEN '{}' AND '{}'
                GROUP BY
                 EmpID
            '''.format(line['records_people_id'], line['records_begin_data'],line['records_end_data'])
            ehr_kq_data = ehr_connect.select(select_sql)
            ImmigrationRecords.objects.filter(pk=line['id'],records_status=True).update(records_leave_hour=float(ehr_kq_data[0]['total_qj_hours']),records_absenteeism_hour=float(ehr_kq_data[0]['Total_kgxs_hours']))


    def employee_fill_verify(self):
        code=self.request.GET.get('code')
        # print(code)
        # start_time =date(self.now.year, self.now.month, 1)  # 这个月的第一天
        record_obj=ImmigrationRecords.objects.filter(records_people__employee_code=code,records_status=1).order_by('records_create_time').last()
        print(record_obj)
        records_country_id=record_obj.records_stationed_country_id
        # records_month=record_obj.records_month
        records_records_work_visa=record_obj.records_work_visa
        records_local_bank = record_obj.records_local_bank
        records_local_social_security = record_obj.records_local_social_security
        records_local_individual_taxes = record_obj.records_local_individual_taxes
        records_create_time= record_obj.records_create_time
        if records_country_id==1 and records_records_work_visa==True and  records_local_bank==True and  records_local_social_security==True and  records_local_individual_taxes==True:  #泰有签
            print('泰签证')
            record_begin = datetime(self.now.year, self.now.month - 1, 21, 00, 00, 00)  # 上个月21日00：00：00   签证组上传记录
            record_end = datetime(self.now.year, self.now.month, 20, 23, 59, 59)  # 这个月20日23：59：59
            fill_begin = datetime(self.now.year, self.now.month, 21, 00, 00, 00)  # 本月21 00:00:00  员工第一天的上传的开始时间
            fill_end = datetime(self.now.year, self.now.month, 23, 9, 59, 59)  # 本月22 09:59:59    员工第二天的上传的结束时间
            if fill_begin <= self.now <= fill_end:  # 当前时间在填写时间段内
                if record_begin <= records_create_time <= record_end:  # 当前时间在上传时间段内
                    self.return_data = {
                        "code": status.HTTP_200_OK,
                        "msg": "可以正常填写!",
                    }
                else:
                    self.return_data = {
                        "code": status.HTTP_401_UNAUTHORIZED,
                        "msg": "您上月并未出现签证数据，如有疑问请联系签证组成员!",
                    }
            else:
                self.return_data = {
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "msg": "当前时间不在指定的填写时间范围内,填写通道已关闭",
                }


        elif records_country_id==2 or (records_country_id==1 and (records_records_work_visa==False or  records_local_bank==False or  records_local_social_security==False or  records_local_individual_taxes==False)):#越南 泰无签
            print('泰无签证和越南')
            fill_begin = arrow.get(self.now.year, self.now.month, 1, 0, 0, 0)  #员工填写时间
            fill_end= arrow.get(self.now.year, self.now.month, 3, 17, 0, 0)
            if fill_begin <= self.now <= fill_end:  #当前时间在填写时间段内
                now = datetime.now()
                record_begin = now.replace(month=now.month - 1, day=1, hour=0, minute=0, second=0)  # 上个月第一天的00:00:00
                _, num_days_prev_month = calendar.monthrange(now.year, now.month - 1)
                record_end = now.replace(month=now.month - 1, day=num_days_prev_month, hour=23, minute=59,second=59)  # 上个月的最后一天的23:59:59
                if record_begin <= records_create_time <= record_end:  # 当前时间在上传时间段内
                    self.return_data = {
                        "code": status.HTTP_200_OK,
                        "msg": "可以正常填写!",
                    }
                else:
                    self.return_data = {
                        "code": status.HTTP_401_UNAUTHORIZED,
                        "msg": "您上月并未出现签证数据，如有疑问请联系签证组成员!",
                    }
            else:
                self.return_data = {
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "msg": "当前时间不在指定的填写时间范围内,填写通道已关闭",
                }
        else:
            self.return_data = {
                "code": status.HTTP_401_UNAUTHORIZED,
                "msg": "我不知道",
            }



    def employee_fill(self):
        '''
           出入境状态
            入泰 填写 入泰日期 行程原因 出入境记录     离泰日期非必填
            离泰 填写 离泰日期 离泰目的地 离泰天数 行程原因 出入境记录     入泰日期非必填
            未离泰 填写 出入境记录
        :return:
        '''


        fill_inout_status = self.request.POST.get('fill_inout_status', None)  # 出入境状态
        code = self.request.POST.get('code', None)
        record_obj = ImmigrationRecords.objects.filter(records_people__employee_code=code,records_status=True).order_by('records_create_time').last()
        print(record_obj,fill_inout_status, type(fill_inout_status))
        if record_obj:
            if fill_inout_status in [1, 4, '1', '4']:  # 入泰,入越
                fill_params = {
                    'fill_record_id': record_obj.id,
                    'fill_inout_status_id': fill_inout_status,  # 出入境状态
                    'fill_into_date': self.request.POST.get('fill_into_date', None),  # 入境日期
                    'fill_leave_date': self.request.POST.get('fill_leave_date', None),  # 离境日期
                    'fill_trip_reason_id': self.request.POST.get('fill_trip_reason', None),  # 行程原因
                    'fill_remark': self.request.POST.get('fill_remark', None)
                }
                fill_obj = ImmigrationFill.objects.create(**fill_params)
                record_file_ls = self.request.FILES.getlist('file')  # 出入境记录 附件
                dummy_path = os.path.join(BASE_DIR, 'static', 'immigrationFile', 'upload_file', str(self.t1),
                                          str(code))  # 创建文件夹
                mkdir(dummy_path)
                for file_obj in record_file_ls:
                    file_url, file_name, suffix = createPath(file_obj, str(code), 'immigrationFile',
                                                             str(random.random())[-5:] + '_出入境记录附件')
                    saveFile(file_url, file_obj)  # 保存文件
                    file_kwargs = {
                        'type': 1,
                        'name': file_name,
                        'url': file_url,
                        'fill_file_id': fill_obj.id  # 员工
                    }
                    file_dbobj = ImmigrationFiles.objects.create(**file_kwargs)
                    self.return_data = {
                        "code": status.HTTP_200_OK,
                        "msg": "填写成功",
                    }
            elif fill_inout_status in [2, 5, '2', '5']:  # 离泰,离越
                fill_params = {
                    'fill_record_id': record_obj.id,
                    'fill_inout_status_id': fill_inout_status,  # 出入境状态
                    'fill_into_date': self.request.POST.get('fill_into_date', None),  # 入境日期
                    'fill_leave_date': self.request.POST.get('fill_leave_date', None),  # 离境日期
                    'fill_trip_reason_id': self.request.POST.get('fill_trip_reason', None),  # 行程原因
                    'fill_leave_days': self.request.POST.get('fill_leave_days', None),  # 离境天数
                    'fill_leave_address': self.request.POST.get('fill_leave_address', None),  # 离境目的地
                    'fill_remark': self.request.POST.get('fill_remark', None)
                }
                fill_obj = ImmigrationFill.objects.create(**fill_params)
                record_file_ls = self.request.FILES.getlist('file')  # 出入境记录 附件
                dummy_path = os.path.join(BASE_DIR, 'static', 'immigrationFile', 'upload_file', str(self.t1),
                                          str(code))  # 创建文件夹
                mkdir(dummy_path)
                for file_obj in record_file_ls:
                    file_url, file_name, suffix = createPath(file_obj, str(code), 'immigrationFile',
                                                             str(random.random())[-5:] + '_出入境记录附件')
                    saveFile(file_url, file_obj)  # 保存文件
                    file_kwargs = {
                        'type': 1,
                        'name': file_name,
                        'url': file_url,
                        'fill_file_id': fill_obj.id  # 员工
                    }
                    file_dbobj = ImmigrationFiles.objects.create(**file_kwargs)
                    self.return_data = {
                        "code": status.HTTP_200_OK,
                        "msg": "填写成功",
                    }
            elif fill_inout_status in [3, 6, '3', '6']:  # 未离泰,未离越
                fill_params = {
                    'fill_record_id': record_obj.id,
                    'fill_inout_status_id': fill_inout_status,  # 出入境状态

                }
                fill_obj = ImmigrationFill.objects.create(**fill_params)
                record_file_ls = self.request.FILES.getlist('file')  # 出入境记录 附件
                dummy_path = os.path.join(BASE_DIR, 'static', 'immigrationFile', 'upload_file', str(self.t1),
                                          str(code))  # 创建文件夹
                mkdir(dummy_path)
                for file_obj in record_file_ls:
                    file_url, file_name, suffix = createPath(file_obj, str(code), 'immigrationFile',
                                                             str(random.random())[-5:] + '_出入境记录附件')
                    saveFile(file_url, file_obj)  # 保存文件
                    file_kwargs = {
                        'type': 1,
                        'name': file_name,
                        'url': file_url,
                        'fill_file_id': fill_obj.id  # 员工
                    }
                    file_dbobj = ImmigrationFiles.objects.create(**file_kwargs)
                    self.return_data = {
                        "code": status.HTTP_200_OK,
                        "msg": "填写成功",
                    }
            else:
                self.return_data = {
                    "code": status.HTTP_401_UNAUTHORIZED,
                    "msg": "我不知道",
                }







    def employee_fill_overrule(self):  # 驳回
        """
        传日期 跟据当前日期查找记录
        {
            签证记录id:[员工填写记录id,员工填写记录id,]
        }
        :return:
        """
        # 驳回的是这个人的这个月的最后一条记录
        info = json.loads(self.request.body)
        fill_id_all = []
        for line in info['idList']:
            for key, value in line.items():
                fill_id_all.append(value[-1])
        ImmigrationFill.objects.filter(id__in=fill_id_all, fill_approval_status=1, fill_status=1).update(
            fill_approval_status=3)  # 所有未审批的变成已驳回的
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "驳回成功",
        }
