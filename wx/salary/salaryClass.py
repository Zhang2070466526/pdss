import arrow
from django.contrib.auth.hashers import make_password, check_password

from employee.models import HrEmployee
from utils.sqlServerConnect import EhrConnect
from wx.salary.sql import *
from translate.translateAPI.method import *


class SalaryInfo:
    def __init__(self):
        self.ehr = EhrConnect()

    def get_year_salary_list(self, code, year, language_type):
        """
        查询工资条列表
        薪资报表中加入查看状态字段（1：未查看；2：已查看）
        :param code: 工号
        :param year: 年
        :param language_type: 语言类型
        :return:
        """
        translate_obj = {
            'hrssc_salary_year': '',
            'hrssc_salary_month': '',
            'hrssc_salary_wxStatus': '',
        }
        translate_obj = translate(translate_obj, language_type)
        translate_obj['salary_wxStatus'] = eval(translate_obj['hrssc_salary_wxStatus'])
        emp_obj = HrEmployee.objects.filter(employee_code=code, employee_status=1)
        person_info = {}
        if emp_obj.exists():
            person_info['name'] = emp_obj[0].employee_name
            person_info['dept'] = emp_obj[0].employee_department.department_name  # 当前年的月份列表
        month_list = [
            str(year) + translate_obj['hrssc_salary_year'] + (str(item) if len(str(item)) == 2 else '0' + str(item)) +
            translate_obj['hrssc_salary_month'] for item in
            range(1, 13)]
        # 前端已处理,传到后端的年份只会小于等于当前
        year_salary_list = self.ehr.select(get_year_salary_list_sql(code, year))
        for obj in year_salary_list:
            obj['PeriodNameSearch'] = obj['PeriodName']
            obj['PeriodName'] = obj['PeriodName'].replace('年', translate_obj['hrssc_salary_year']).replace('月',
                                                                                                           translate_obj[
                                                                                                               'hrssc_salary_month'])
        # 有值,代表此时已入职hrssc_salary_month
        if year_salary_list:
            # 取第一条和最后一条记录
            first_data = month_list[:month_list.index(year_salary_list[0]['PeriodName'])]
            for first_data_obj in reversed(first_data):
                year_salary_list.insert(0, {'PeriodName': first_data_obj, 'wxStatus': 3})
            last_data = month_list[month_list.index(year_salary_list[len(year_salary_list) - 1]['PeriodName']) + 1:]
            for last_data_obj in last_data:
                year_salary_list.append({'PeriodName': last_data_obj, 'wxStatus': 4})
            # for obj in year_salary_list:
            #     obj['wxStatus'] = translate_obj['salary_wxStatus'][obj['wxStatus']]
            translate_field = {
                'year': translate_obj['hrssc_salary_year'],
            }

            for key, value in translate_obj['salary_wxStatus'].items():
                translate_field[f'statue{key}'] = value
            return {
                'code': 200,
                'msg': '薪资列表成功',
                'data': {
                    'year_salary_list': year_salary_list,
                    'personInfo': person_info,
                    'translate_field': translate_field,
                },

            }
        else:
            return {
                'code': 400,
                'msg': '该年份暂无数据',
            }

    def get_month_salary_data(self, code, period, language_type):
        """
        查询每月薪资
        :param code: 工号
        :param period: 查询周期
        :param language_type: 语言类型
        :return:
        """
        # 先不处理薪资查询状态
        translate_obj = {
            'hrssc_salary_cycle': '',
            'hrssc_salary_basic_salary': '',
            'hrssc_salary_position_salary': '',
            'hrssc_salary_performance_salary': '',
            'hrssc_salary_phone_bill_salary': '',
            'hrssc_salary_should_basic_salary': '',
            'hrssc_salary_should_position_salary': '',
            'hrssc_salary_ratio_of_total_performance': '',
            'hrssc_salary_should_performance_salary': '',
            'hrssc_salary_Bonus/Allowance': '',
            'hrssc_salary_total_subsidies': '',
            'hrssc_salary_total_payable': '',
            'hrssc_salary_undertaken_by_social_security_and_provident_fund_units': '',
            'hrssc_salary_withholding_individual_income_tax': '',
            'hrssc_salary_water/electricity_fees': '',
            'hrssc_salary_Rent/property_management_fees': '',
            'hrssc_salary_actual_fees': '',
            'hrssc_salary_remarks': '',
            'hrssc_salary_detail': '',
            'hrssc_salary_detail_confirm': '',
            'hrssc_salary_grylao': '',
            'hrssc_salary_gryliao': '',
            'hrssc_salary_grdb': '',
            'hrssc_salary_grsy': '',
            'hrssc_salary_grgjj': '',
            'hrssc_salary_grhj': '',
        }
        field_to_field = {
            'hrssc_salary_cycle': 'PeriodName',
            'hrssc_salary_basic_salary': 'BasePay',
            'hrssc_salary_position_salary': 'PostSalary',
            'hrssc_salary_performance_salary': '_jxgz',
            'hrssc_salary_phone_bill_salary': '_hfbt',
            'hrssc_salary_should_basic_salary': '_yfjbgz',
            'hrssc_salary_should_position_salary': '_yfgwgz',
            'hrssc_salary_ratio_of_total_performance': '_jxzhxs',
            'hrssc_salary_should_performance_salary': '_yfjxgz',
            'hrssc_salary_Bonus/Allowance': '_jjbt',
            'hrssc_salary_total_subsidies': '_yfbthj',
            'hrssc_salary_total_payable': '_yfhj',
            'hrssc_salary_grylao': 'grylao',
            'hrssc_salary_gryliao': 'gryliao',
            'hrssc_salary_grdb': 'grdb',
            'hrssc_salary_grsy': 'grsy',
            'hrssc_salary_grgjj': 'grgjj',
            'hrssc_salary_grhj': 'grhj',
            'hrssc_salary_undertaken_by_social_security_and_provident_fund_units': 'sbgjjdw',
            'hrssc_salary_withholding_individual_income_tax': '_dkgs',
            'hrssc_salary_water/electricity_fees': '_shuidf',
            'hrssc_salary_Rent/property_management_fees': '_fangzf',
            'hrssc_salary_actual_fees': 'RealPay',
            'hrssc_salary_remarks': 'remark',

        }
        translate_obj = translate(translate_obj, language_type)
        month_salary_list = self.ehr.select(get_month_salary_sql(code, period))
        salary_data = []
        for key, value in field_to_field.items():
            salary_data.append({'text': translate_obj[key], 'value': month_salary_list[0][value]})
        for i in salary_data:
            for key, value in i.items():
                if value is None or value == '':
                    i[key] = 0
        if month_salary_list:
            self.change_salary_statue(code, period, 2)
            return {
                'code': 200,
                'msg': '薪资查询成功',
                'data': {
                    'personData': {
                        'name': month_salary_list[0]['Name'],
                        'deptName': month_salary_list[0]['DepartmentName'],
                        'position': month_salary_list[0]['PostName'],
                    },
                    'data': salary_data,
                    'translate_field': {
                        'salary_detail': translate_obj['hrssc_salary_detail'],
                        'salary_detail_confirm': translate_obj['hrssc_salary_detail_confirm'],
                    },
                }
            }

    def month_salary_language(self, language_type):
        """
        翻译字段
        :param language_type: 1、中文；2、英文；3、泰文；4、越南文
        :return:
        """
        column_obj = {
            'chinese': {
                'PeriodName': {'title': '周期', 'unit': ''},
                'BasePay': {'title': '基本工资', 'unit': '￥'},
                'PostSalary': {'title': '岗位工资', 'unit': '￥'},
                '_jxgz': {'title': '绩效工资', 'unit': '￥'},
                '_hfbt': {'title': '话费补贴', 'unit': '￥'},
                '_yfjbgz': {'title': '应发基本工资', 'unit': '￥'},
                '_yfgwgz': {'title': '应发岗位工资', 'unit': '￥'},
                '_jxzhxs': {'title': '绩效综合系数', 'unit': ''},
                '_yfjxgz': {'title': '绩效', 'unit': ''},
                '_jjbt': {'title': '奖金/津贴', 'unit': '￥'},
                '_yfbthj': {'title': '补贴合计', 'unit': '￥'},
                '_yfhj': {'title': '应发合计', 'unit': '￥'},
                'sbgjjdw': {'title': '社保公积金单位承担', 'unit': '￥'},
                '_dkgs': {'title': '代扣个税', 'unit': '￥'},
                '_shuidf': {'title': '水费/电费', 'unit': '￥'},
                '_fangzf': {'title': '房租费/物业费', 'unit': '￥'},
                'RealPay': {'title': '实发工资', 'unit': '￥'},
                'remark': {'title': '薪资备注', 'unit': ''}
            }
        }
        return column_obj.get(language_type)

    # 薪资确认
    def salary_confirm(self, code, period):
        res = self.change_salary_statue(code, period, 5)
        return res

    @staticmethod
    def check_password(code, pwd):
        if pwd is None or pwd == '':
            return {
                'code': 400,
                'msg': '请输入密码'
            }
        obj = HrEmployee.objects.filter(employee_code=code, employee_status=1)[0]
        check = check_password(pwd, obj.employee_salary_password)
        if check:
            return {
                'code': 200,
                'msg': '验证成功'
            }
        else:
            return {
                'code': 400,
                'msg': '密码错误'
            }

    # 输入查询密码界面
    @staticmethod
    def is_have_password(code, language_type):
        translate_obj = {
            'hrssc_salary_check_bar_head': '',
            'hrssc_salary_check_tip': '',
            'confirm': '',
            'hrssc_salary_check_forget_password': ''
        }
        translate_obj = translate(translate_obj, language_type)
        emp = HrEmployee.objects.filter(employee_code=code, employee_status=1)
        if emp.exists() is False:
            return {
                'code': 400,
                'msg': '未找到您的员工信息'
            }
        pwd = emp[0].employee_salary_password
        if pwd is None or pwd == '':
            return {
                'code': 200,
                'msg': '请设置初始密码',
                'flag': False
            }
        else:
            return {
                'code': 200,
                'msg': '请驶入密码',
                'flag': True,
                'data': translate_obj
            }

    # 忘记密码界面
    @staticmethod
    def forget_password_page(language_type):
        translate_obj = {
            'hrssc_salary_forget_bar_head': '',
            'hrssc_salary_forget_tip_of_write': '',
            'hrssc_salary_forget_tip_of_sfz': '',
            'hrssc_salary_forget_tip_of_code': '',
            'hrssc_salary_forget_tip_of_input_password': '',
            'hrssc_salary_forget_tip_of_input_re_password': '',
            'confirm': '',
        }
        translate_obj = translate(translate_obj, language_type)
        return {
            'code': 200,
            'msg': '',
            'data': translate_obj
        }

    # 忘记密码的提交
    @staticmethod
    def forget_password(sfz, code, pwd, pwd2):
        if pwd != pwd2:
            return {
                'code': 400,
                'msg': '两次密码不一致'
            }
        if len(pwd) < 8:
            return {
                'code': 400,
                'msg': '密码不足8位'
            }
        if len(pwd) > 32:
            return {
                'code': 400,
                'msg': '密码不得超过32位'
            }
        emp = HrEmployee.objects.filter(employee_code=code, employee_identity_no=sfz, employee_status=1)
        if emp.exists() and len(emp) == 1:
            emp.update(employee_salary_password=make_password(pwd))
            return {
                'code': 200,
                'msg': '密码重置成功'
            }
        else:
            if len(emp) > 1:
                return {
                    'code': 400,
                    'msg': '存在重复信息，请联系管理员处理'
                }
            else:
                return {
                    'code': 400,
                    'msg': '不存在该员工在职信息'
                }

    # 改变薪资状态
    def change_salary_statue(self, code, period, wsStatus):
        try:
            EmpID = self.get_employee_id(code)
            MonthID = self.get_period_id(period)
            sql = f"update T_HR_Payroll set wxStatus={wsStatus} where EmpID={EmpID} and MonthID={MonthID}"
            print(sql)
            self.ehr.update(sql)
            return {
                'code': 200,
                'msg': '确认成功'
            }
        except Exception as e:
            print(e)
            return {
                'code': 400,
                'msg': '确认失败'
            }

    def get_employee_id(self, code):
        sql = f"select ID from T_HR_Employee where Code='{code}'"
        result = self.ehr.select(sql)
        return result[0]['ID']

    def get_period_id(self, period):
        sql = f"select ID from T_HR_Period where PeriodName='{period}'"
        result = self.ehr.select(sql)
        return result[0]['ID']
