import arrow
import requests

from general.models import center_base
from hikCanteen.sql import month_meal_allowance_sql
from utils.sqlServerConnect import EhrConnect
from .hikMethods import HikvisonInterface
from .models import *
from datetime import datetime

from hikCanteen.sql import month_meal_allowance_sql
    # search_dismiss_record_sql


def if_None(val):
    if val is None:
        return 0
    else:
        return val


class Rules:
    """
    其他数据规则接口
        1、管理各基地新入职发放补贴金额
        2、管理不需要充值人员信息
    """

    def __init__(self):
        self.sqlserver = EhrConnect()

    def update_job_rank_new_entry_amount(self):
        """
        修改各合同归属的新入职补贴金额
        :return:
        """
        pass

    def select_job_rank_new_entry_amount(self):
        """
        查看各合同归属的新入职补贴金额
        :return:
        """
        pass

    def update_dont_need_employee(self):
        """
        修改不需要发放补贴金额的人（例如新能源在昆山办公的）
        :return:
        """
        pass

    def select_dont_need_employee(self):
        """
        修改不需要发放补贴金额的人（例如新能源在昆山办公的）
        :return:
        """
        pass

    def search_dismiss_record(self):
        return_data = {
            'code': 200,
            'msg': '每日离职人员信息更新成功'
        }
        today = arrow.now().shift(days=-1)
        # sql = search_dismiss_record_sql(today.year, today.month, today.day)
        sql = search_dismiss_record_sql(today.year, today.month, today.day)
        print(sql)
        result = self.sqlserver.select(sql)
        hik = HikvisonInterface()
        for i in result:
            data = hik.select_balance(i['Code'])
            if data['code'] == 200:
                balance = data['balance']
            else:
                balance = "查询失败"
            kwargs = {
                "name": i['Name'],
                "code": i['Code'],
            }
            default = {
                "name": i['Name'],
                "code": i['Code'],
                "modify_time": datetime.now(),
                "status": True,
                "balance": balance,
                "SeparationDate": i['DimissionDate'],
            }
            del default['modify_time']
            try:
                MonthmoneyToOAList.objects.update_or_create(defaults=default, **kwargs)
            except Exception as e:
                return_data = {
                    'code': 200,
                    'msg': i['Name'] + ":更新or创建失败。\n" + str(e)
                }
                return return_data
        return return_data

    def month_money_to_oa(self):
        """
        每天同步离职人员信息到
        每月7号统计上月出勤和补贴金额

        :return:
        """
        begin = '2023-06-01 00:00:00'
        end = '2023-06-30 00:00:00'
        print(month_meal_allowance_sql(begin, end))
        month_meal_allowance_obj = self.sqlserver.select(
            month_meal_allowance_sql(begin, end))
        if month_meal_allowance_obj:
            department_month_meal_allowance = {}
            for month_meal_allowance in month_meal_allowance_obj:
                # print(month_meal_allowance)
                # 写入部门
                if month_meal_allowance['DepartmentCode'] not in department_month_meal_allowance:
                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']] = {}
                # 写入部门下的人员工号和初始数据
                if month_meal_allowance['code'] not in department_month_meal_allowance[month_meal_allowance['DepartmentCode']]:
                    # print(month_meal_allowance['PostName'])
                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][month_meal_allowance['code']] = {
                        'name': month_meal_allowance['name'],
                        'status': month_meal_allowance['EmployeeStatusID'],
                        'departmentName': month_meal_allowance['DepartmentName'],
                        'departmentCode': month_meal_allowance['DepartmentCode'],
                        'jobLevelName': month_meal_allowance['JobClassName'],
                        'postName': month_meal_allowance['PostName'],
                        'jobRankName': month_meal_allowance['JobRankName'],
                        # 'jobRankName':month_meal_allowance['JobRankName'],
                        'entryCanteenAmount': month_meal_allowance['entryCanteenAmount'],
                        'jobRankCode': month_meal_allowance['JobRankCode'],
                        'baibanchuqin': 0,
                        'baibanbutie': 0,
                        'yebanchuqin': 0,
                        'yebanbutie': 0,
                        'qiangzhuanbanchuqin': 0,
                        'qiangzhuanbanbutie': 0,
                        'zhoumojiaban': 0,
                        'zhoumojiabanbutie': 0,
                        'jiaban>2': 0,
                        'jiaban>2butie': 0,
                        'jiaban>5': 0,
                        'jiaban>5butie': 0,
                        'jiaban>7.5': 0,
                        'jiaban>7.5butie': 0,
                        'jiaban>10': 0,
                        'jiaban>10butie': 0,
                        'jiaban>12.5': 0,
                        'jiaban>12.5butie': 0,
                        'qingjia>4': 0
                    }

                # **************************************************************
                # 宁夏
                if month_meal_allowance['job_rank_id'] in (27, 45, 48, 49):
                    # 根据joblevel判断是否是经理级以上
                    # 经理级以上就添加应出勤日期
                    if month_meal_allowance['JobClassCode'] == 'ZL01' or month_meal_allowance['JobClassCode'] == 'ZL02' or month_meal_allowance['JobClassCode'] == 'XZ02' or \
                            month_meal_allowance['JobClassCode'][-1] in ('5', '6', '7', '8'):
                        if month_meal_allowance['ifWork'] > 0:
                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                month_meal_allowance['code']]['baibanchuqin'] += 1
                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                month_meal_allowance['code']]['baibanbutie'] += 45
                    # 不是经理级，需要根据出勤计算餐补
                    else:
                        # 工作日
                        if month_meal_allowance['ifWork'] > 0:
                            # 夜班
                            if month_meal_allowance['night'] == 1:
                                # 没有请假、调休加起来4小时
                                if if_None(month_meal_allowance['njxs']) + if_None(
                                        month_meal_allowance['sjxs']) + if_None(month_meal_allowance['bjxs']) + if_None(
                                    month_meal_allowance['hjxs']) + if_None(month_meal_allowance['njxs']) + if_None(
                                    month_meal_allowance['cjxs']) + if_None(month_meal_allowance['gsxs']) + if_None(
                                    month_meal_allowance['txxs']) + if_None(
                                    month_meal_allowance['sajxs']) + if_None(month_meal_allowance['pcjxs']) + if_None(
                                    month_meal_allowance['cjjxs']) + if_None(month_meal_allowance['hljxs']) + if_None(
                                    month_meal_allowance['brjxs']) + if_None(month_meal_allowance['ccxs']) + if_None(
                                    month_meal_allowance['yejxs']) <= 4:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['yebanchuqin'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['yebanbutie'] += 55
                                else:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['qingjia>4'] += 1
                            else:
                                # 没有请假、调休加起来4小时
                                if if_None(month_meal_allowance['njxs']) + if_None(
                                        month_meal_allowance['sjxs']) + if_None(month_meal_allowance['bjxs']) + if_None(
                                    month_meal_allowance['hjxs']) + if_None(month_meal_allowance['njxs']) + if_None(
                                    month_meal_allowance['cjxs']) + if_None(month_meal_allowance['gsxs']) + if_None(
                                    month_meal_allowance['txxs']) + if_None(
                                    month_meal_allowance['sajxs']) + if_None(month_meal_allowance['pcjxs']) + if_None(
                                    month_meal_allowance['cjjxs']) + if_None(month_meal_allowance['hljxs']) + if_None(
                                    month_meal_allowance['brjxs']) + if_None(month_meal_allowance['ccxs']) + if_None(
                                    month_meal_allowance['yejxs']) <= 4:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['baibanchuqin'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['baibanbutie'] += 45
                                else:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['qingjia>4'] += 1
                        # 非工作日
                        else:
                            # 加班4小时以上补贴
                            if month_meal_allowance['_ctxxs'] >= 4:
                                department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                    month_meal_allowance['code']]['zhoumojiaban'] += 1
                                department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                    month_meal_allowance['code']]['zhoumojiabanbutie'] += 45
                # 不是宁夏
                else:
                    # 副经理及以上（后续需要单独处理+4的补贴）
                    if month_meal_allowance['JobClassCode'] in (
                            'ZL01', 'ZL02', 'ZDM8', 'ZDM7', 'ZDM6', 'ZDM5', 'ZDT7', 'ZDT6', 'ZDT5', 'ZDP6', 'ZDP5', 'XZ02'):
                        if month_meal_allowance['ifWork'] == 1:
                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                month_meal_allowance['code']]['baibanchuqin'] += 1
                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                month_meal_allowance['code']]['baibanbutie'] += 24
                    # 副经理以下
                    else:
                        # 责任制
                        if month_meal_allowance['PayTypeID'] == 2:
                            # 工作日
                            if month_meal_allowance['ifWork'] > 0:
                                # 请假时长小于4小时
                                if if_None(month_meal_allowance['njxs']) + if_None(
                                        month_meal_allowance['sjxs']) + if_None(month_meal_allowance['bjxs']) + if_None(
                                    month_meal_allowance['hjxs']) + if_None(month_meal_allowance['njxs']) + if_None(
                                    month_meal_allowance['cjxs']) + if_None(month_meal_allowance['gsxs']) + if_None(
                                    month_meal_allowance['txxs']) + if_None(
                                    month_meal_allowance['sajxs']) + if_None(month_meal_allowance['pcjxs']) + if_None(
                                    month_meal_allowance['cjjxs']) + if_None(month_meal_allowance['hljxs']) + if_None(
                                    month_meal_allowance['brjxs']) + if_None(month_meal_allowance['ccxs']) + if_None(
                                    month_meal_allowance['yejxs']) <= 4:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['baibanchuqin'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['baibanbutie'] += 12
                                else:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['qingjia>4'] += 1
                                    # 加班
                                # 2小时补贴12， 7.5小时补贴12， 12.5小时补贴6元
                                if month_meal_allowance['_ctxxs'] >= 2:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>2'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>2butie'] += 12
                                if month_meal_allowance['_ctxxs'] >= 7.5:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>7.5'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>7.5butie'] += 12
                                if month_meal_allowance['_ctxxs'] >= 12.5:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>12.5'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>12.5butie'] += 12
                            # 周末节假日
                            else:
                                # 加班4小时以上有补贴
                                if month_meal_allowance['_ctxxs'] >= 4:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['zhoumojiaban'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['zhoumojiabanbutie'] += 12
                        # 计时制
                        else:
                            # 工作日
                            if month_meal_allowance['ifWork'] > 0:
                                # 强转班次
                                if month_meal_allowance['MstID'] == 6:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['qiangzhuanbanchuqin'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['qiangzhuanbanbutie'] += 24
                                else:
                                    # 夜班
                                    if month_meal_allowance['night'] == 1:
                                        # 请假4小时以内
                                        if if_None(month_meal_allowance['njxs']) + if_None(
                                                month_meal_allowance['sjxs']) + if_None(month_meal_allowance['bjxs']) + if_None(
                                            month_meal_allowance['hjxs']) + if_None(month_meal_allowance['njxs']) + if_None(
                                            month_meal_allowance['cjxs']) + if_None(month_meal_allowance['gsxs']) + if_None(
                                            month_meal_allowance['txxs']) + if_None(
                                            month_meal_allowance['sajxs']) + if_None(month_meal_allowance['pcjxs']) + if_None(
                                            month_meal_allowance['cjjxs']) + if_None(month_meal_allowance['hljxs']) + if_None(
                                            month_meal_allowance['brjxs']) + if_None(month_meal_allowance['ccxs']) + if_None(
                                            month_meal_allowance['yejxs']) <= 4:
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['yebanchuqin'] += 1
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['yebanbutie'] += 18
                                        else:
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['qingjia>4'] += 1

                                        # 加班5小时补贴12，加班10小时补贴6
                                        if month_meal_allowance['_ctxxs'] >= 5:
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['jiaban>5'] += 1
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['jiaban>5butie'] += 12
                                        if month_meal_allowance['_ctxxs'] >= 10:
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['jiaban>10'] += 1
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['jiaban>10butie'] += 6
                                    # 白班
                                    else:
                                        # 请假4小时以内
                                        if if_None(month_meal_allowance['njxs']) + if_None(
                                                month_meal_allowance['sjxs']) + if_None(month_meal_allowance['bjxs']) + if_None(
                                            month_meal_allowance['hjxs']) + if_None(month_meal_allowance['njxs']) + if_None(
                                            month_meal_allowance['cjxs']) + if_None(month_meal_allowance['gsxs']) + if_None(
                                            month_meal_allowance['txxs']) + if_None(
                                            month_meal_allowance['sajxs']) + if_None(month_meal_allowance['pcjxs']) + if_None(
                                            month_meal_allowance['cjjxs']) + if_None(month_meal_allowance['hljxs']) + if_None(
                                            month_meal_allowance['brjxs']) + if_None(month_meal_allowance['ccxs']) + if_None(
                                            month_meal_allowance['yejxs']) <= 4:
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['baibanchuqin'] += 1
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['baibanbutie'] += 24
                                        else:
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['qingjia>4'] += 1

                                        # 加班5小时补贴12，加班10小时补贴12
                                        if month_meal_allowance['_ctxxs'] >= 5:
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['jiaban>5'] += 1
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['jiaban>5butie'] += 12
                                        if month_meal_allowance['_ctxxs'] >= 10:
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['jiaban>10'] += 1
                                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                                month_meal_allowance['code']]['jiaban>10butie'] += 12

            # print(department_month_meal_allowance)
            # 根据各部门发起审批流
            # for depart_code, department_month_info in department_month_meal_allowance.items():
            #     # 部门内部整理成数据进行发送
            #     code = []
            #     name = []
            #     position = []
            #     baibanchuqin = []
            #     baibancanbu = []
            #     yebanchuqin = []
            #     yebancanbu = []
            #     jiabanchuqin = []
            #     jiabancanbu = []
            #     hejicanbu = []
            #     chongzhijine = []
            #     chongzhiqianjine = []
            #     chongzhihouyue = []
            #     beizhu = []
            #     jobrank = ''
            #     # 查询部门在oa中的fd_id
            #     self.sqlserver.host = '172.16.6.194'
            #     self.sqlserver.username = 'sa'
            #     self.sqlserver.passward = 'Runergy@0919'
            #     self.sqlserver.database = 'ekp1002'
            #     dept_fd_id_list = self.sqlserver.select("select fd_id from sys_org_element where fd_no = '%s'" % depart_code)
            #     print(dept_fd_id_list)
            #     if dept_fd_id_list:
            #         dept_fd_id = dept_fd_id_list[0]['fd_id']
            #         for employee_code, personal_info in department_month_info.items():
            #             jobrank=personal_info['jobRankName']
            #             code.append(employee_code)
            #             name.append(personal_info['name'])
            #             position.append(personal_info['postName'])
            #             baibanchuqin.append(personal_info['baibanchuqin']+personal_info['qiangzhuanbanchuqin'])
            #             baibancanbu.append(personal_info['baibanbutie']+personal_info['qiangzhuanbanbutie'])
            #             yebanchuqin.append(personal_info['yebanchuqin'])
            #             yebancanbu.append(personal_info['yebanbutie'])
            #             jiabanchuqin.append(personal_info['zhoumojiaban'])
            #             jiabancanbu.append(
            #                 personal_info['zhoumojiabanbutie'] + personal_info['jiaban>2butie'] + personal_info['jiaban>5butie'] + personal_info['jiaban>7.5butie'] + personal_info['jiaban>10butie'] +
            #                 personal_info['jiaban>12.5butie'])
            #             hejicanbu.append(
            #                 personal_info['baibanbutie'] + personal_info['yebanbutie'] ++personal_info['qiangzhuanbanbutie']+ personal_info['zhoumojiabanbutie'] + personal_info['jiaban>2butie'] + personal_info['jiaban>5butie'] +
            #                 personal_info['jiaban>7.5butie'] + personal_info['jiaban>10butie'] + personal_info['jiaban>12.5butie'])
            #             chongzhijine.append(0)
            #             hik = HikvisonInterface()
            #             balance = hik.select_balance(employee_code)
            #             print(balance)
            #             chongzhiqianjine.append(float(balance['balance']))
            #             chongzhihouyue.append(
            #                 float(balance['balance']) + personal_info['baibanbutie'] + personal_info['yebanbutie'] + personal_info['zhoumojiabanbutie'] ++personal_info['qiangzhuanbanbutie']+ personal_info['jiaban>2butie'] +
            #                 personal_info['jiaban>5butie'] +
            #                 personal_info['jiaban>7.5butie'] + personal_info['jiaban>10butie'] + personal_info['jiaban>12.5butie'])
            #             beizhu.append('')
            #
            #         url = "http://ekp.runergy.cn:28083/sys/webservice/kmReviewWebserviceService?wsdl"
            #         headers = {'Content-Type': 'application/xml'}
            #         payload = """
            #                             <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservice.review.km.kmss.landray.com/">
            #                                 <soapenv:Header/>
            #                                 <soapenv:Body>
            #                                     <web:addReview>
            #                                         <!--Optional:-->
            #                                         <arg0>
            #                                             <!--Zero or more repetitions:-->
            #                                             <!--Optional:-->
            #                                             <attachmentValues></attachmentValues>
            #                                             <!--Optional:-->
            #                                             <authAreaId></authAreaId>
            #                                             <!--Optional:-->
            #                                             <docContent></docContent>
            #                                             <!--Optional:-->
            #                                             <docCreator>{"LoginName":"2010009598"}</docCreator>
            #                                             <!--Optional:-->
            #                                             <docProperty></docProperty>
            #                                             <!--Optional:-->
            #                                             <docStatus>20</docStatus>
            #                                             <!--Optional:-->
            #                                             <docSubject>%s</docSubject>
            #                                             <!--Optional:-->
            #                                             <fdId></fdId>
            #                                             <!--Optional:-->
            #                                             <fdKeyword></fdKeyword>
            #                                             <!--Optional:-->
            #                                             <fdSource></fdSource>
            #                                             <!--Optional:-->
            #                                             <fdTemplateId>189239c8f59eeec11283e9f458fa6400</fdTemplateId>
            #                                             <!--Optional:--><flowParam>{}</flowParam>
            #                                             <!--Optional:-->
            #                                             <formValues>
            #                                             {
            #                                             "fd_3bec90746441b8":"%s",
            #                                             "fd_3bfcff91dc2a60":"%s",
            #                                             "fd_3bf0a07c929588":"%s",
            #                                             "fd_3bec91b70559d4.fd_3bec91eb046d44":%s,
            #                                             "fd_3bec91b70559d4.fd_3bed77a00d1a7e":%s,
            #                                             "fd_3bec91b70559d4.fd_3bec91ec2aa232":%s,
            #                                             "fd_3bec91b70559d4.fd_3bec92a42dfb34":%s,
            #                                             "fd_3bec91b70559d4.fd_3bec92a727382e":%s,
            #                                             "fd_3bec91b70559d4.fd_3bec92c2c9fc8e":%s,
            #                                             "fd_3bec91b70559d4.fd_3bec92acfa17ec":%s,
            #                                             "fd_3bec91b70559d4.fd_3bec92b049f7ac":%s,
            #                                             "fd_3bec91b70559d4.fd_3bec92bbc68210":%s,
            #                                             "fd_3bec91b70559d4.fd_3bed78aa024376":%s,
            #                                             "fd_3bec91b70559d4.fd_3bec92b6eed1d2":%s,
            #                                             "fd_3bec91b70559d4.fd_3bec92b5c2b724":%s,
            #                                             "fd_3bec91b70559d4.fd_3bed78b4ddb2be":%s,
            #                                             "fd_3bec91b70559d4.fd_3bec92b2c95054":%s
            #                                             }
            #                                             </formValues>
            #                                         </arg0>
            #                                     </web:addReview>
            #                                 </soapenv:Body>
            #                             </soapenv:Envelope>
            #                                                     """ % ('2023-7饭卡充值流程',
            #                                                            '2023-7饭卡充值流程',
            #                                                            dept_fd_id,
            #                                                            jobrank,
            #                                                            code,
            #                                                            name,
            #                                                            position,
            #                                                            baibanchuqin,
            #                                                            baibancanbu,
            #                                                            yebanchuqin,
            #                                                            yebancanbu,
            #                                                            jiabanchuqin,
            #                                                            jiabancanbu,
            #                                                            hejicanbu,
            #                                                            chongzhijine,
            #                                                            chongzhiqianjine,
            #                                                            chongzhihouyue,
            #                                                            beizhu
            #                                                            )
            #         print(payload.replace("'", '"'))
            #         response = requests.post(url, headers=headers, data=payload.replace("'", '"'))
            #         print(response.content)

            month_data = []
            for key, value in department_month_meal_allowance.items():
                for sub_key, sub_value in value.items():
                    sub_value['code'] = sub_key
                    month_data.append(sub_value)
            # print(len(month_data))
            code_to_balance_obj = MonthmoneyToOAList.objects.filter(month_money_status=True, month=begin[0:10], status=0).values_list("code", "balance")
            code_to_balance = {}
            for obj in code_to_balance_obj:
                code_to_balance[obj[0]] = obj[1]
            # print(code_to_balance)
            for line in month_data:
                line['month'] = begin[:10]
                # i['month'] = str(datetime.now())[:7]+'-01'
                line['jiaban_gt_2'] = line['jiaban>2']
                line['jiaban_gt_2_butie'] = line['jiaban>2butie']
                line['jiaban_gt_5'] = line['jiaban>5']
                line['jiaban_gt_5_butie'] = line['jiaban>5butie']
                line['jiaban_gt_7_5'] = line['jiaban>7.5']
                line['jiaban_gt_7_5_butie'] = line['jiaban>7.5butie']
                line['jiaban_gt_10'] = line['jiaban>10']
                line['jiaban_gt_10_butie'] = line['jiaban>10butie']
                line['jiaban_gt_12_5'] = line['jiaban>12.5']
                line['jiaban_gt_12_5_butie'] = line['jiaban>12.5butie']
                line['qingjia_gt_4'] = line['qingjia>4']
                #
                # try:
                line['jobRankCode_id'] = self.get_jobRank_id(line['jobRankCode'])
                # except:
                #     i['jobRankCode_id'] =None
                # print(i['jobRankCode_id'])
                #
                del line['jiaban>2']
                del line['jiaban>2butie']
                del line['jiaban>5']
                del line['jiaban>5butie']
                del line['jiaban>7.5']
                del line['jiaban>7.5butie']
                del line['jiaban>10']
                del line['jiaban>10butie']
                del line['jiaban>12.5']
                del line['jiaban>12.5butie']
                del line['qingjia>4']
                del line['jobRankName']
                del line['jobRankCode']
                line['butie_sum'] = eval(str(line['yebanbutie'])) + eval(str(line['baibanbutie'])) + eval(
                    str(line['qiangzhuanbanbutie'])) + eval(str(line['zhoumojiabanbutie'])) + eval(
                    str(line['jiaban_gt_2_butie'])) + eval(str(line['jiaban_gt_5_butie'])) + eval(
                    str(line['jiaban_gt_7_5_butie'])) + eval(str(line['jiaban_gt_10_butie'])) + eval(
                    str(line['jiaban_gt_12_5_butie']))
                line['chuqin_sum'] = eval(str(line['baibanchuqin'])) + eval(str(line['yebanchuqin'])) + eval(
                    str(line['qiangzhuanbanchuqin']))
                if line['status'] == str(2) or line['status'] == str(99):  # 离职
                    line['status'] = 0
                elif line['status'] == str(1):
                    line['status'] = 1
                else:
                    line['status'] = None
                line['balance'] = self.select_balance(line['code'])  # 每人余额
                # 计算余额
                if line['status'] != 1:
                    try:
                        if line['code'] in code_to_balance:
                            entry_canteen_amount = line['entryCanteenAmount']
                            butie_sum = line['butie_sum']
                            balance = code_to_balance[line['code']]
                            if type(balance) is str:
                                balance = eval(balance)
                            elif balance is None:
                                balance = 0
                            amount_to_replenished = entry_canteen_amount - butie_sum - balance
                            line['amount_to_replenished'] = amount_to_replenished
                    except:
                        print('{}计算错误'.format(line['code']))
                current_month = arrow.now().month
                if current_month in [4, 7, 10, 1]:
                    if line['balance'] is not None:
                        money = line['balance'] + line['entryCanteenAmount']
                        if money > 944:
                            line['amount_to_quarter'] = money - 744  # 季度返现金额
                        else:
                            line['amount_to_quarter'] = 0
                # line['month'] = datetime.strptime(line['month'], '%Y-%m-%d').date()
                # print(line)
                MonthmoneyToOAList.objects.update_or_create(defaults=line, code=line['code'], month=line['month'], month_money_status=1)

    def get_previous_month_first_last_day(self, date_string):
        import datetime
        date_string = date_string[:10]
        date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
        first_day = date.replace(day=1)
        last_day = first_day.replace(day=1) - datetime.timedelta(days=1)
        return (first_day, last_day)

    def get_jobRank_id(self, code):
        return JobRank.objects.filter(JobRankCode=code).values_list('id')[0][0]

    def select_balance(self, code):
        try:
            hik = HikvisonInterface()
            balance = hik.select_balance(code)
            balance = eval(str(balance['balance']))
        except:
            balance = None
        return balance
