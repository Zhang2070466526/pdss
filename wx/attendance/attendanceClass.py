import arrow

from utils.sqlServerConnect import EhrConnect
from wx.attendance.sql import *


class AttendanceInfo:
    def __init__(self):
        self.ehr = EhrConnect()

    def get_daliy_data(self, code, search_month, language):
        # def get_daliy_data(self, code, search_month):
        """
        根据工号、时间范围查找考勤日报
        :param code: 工号
        :param begin_date: 开始查询日期
        :param end_date: 结束查询日期
        :return: 日期、考勤状态的对象数组
        """
        # 处理日期范围
        # 之前月的情况,返回当前月每一天的值
        lang_type = {
            'Chinese': {
                'statue': {
                    '正常': '正常',
                    '迟到/旷工': '迟到/旷工',
                    '迟到/早退': '迟到/早退',
                    '迟到/早退/旷工': '迟到/早退/旷工',
                    '旷工': '旷工',
                    '缺卡': '缺卡',
                    '早退': '早退',
                    '早退/旷工': '早退/旷工',
                },
                'count_field': '月度考勤汇总',
                'count_statue': {
                    # '正常': 0,
                    '迟到': 0,
                    '旷工': 0,
                    '早退': 0,
                    '缺卡': 0,
                },
            },
            'English': {
                'statue': {
                    '正常': 'Normal',
                    '迟到/旷工': 'Late/Absenteeism',
                    '迟到/早退': 'Late/LeaveEarly',
                    '迟到/早退/旷工': 'Late/LeaveEarly/Absenteeism',
                    '旷工': 'Absenteeism',
                    '缺卡': 'Check in less',
                    '早退': 'LeaveEarly',
                    '早退/旷工': 'LeaveEarly/Absenteeism',
                },
                'count_field': 'Monthly attendance summary',
                'count_statue': {
                    # 'Normal': 0,
                    'Late': 0,
                    'Absenteeism': 0,
                    'LeaveEarly': 0,
                    'Clock in': 0,
                },
            },
        }
        if arrow.get(search_month, "YYYY-MM") < arrow.get(str(arrow.now().date())[:7], "YYYY-MM"):
            search_month_first_time = arrow.get(search_month, "YYYY-MM")
            search_month_first_day = search_month_first_time.date()
            search_month_last_day = search_month_first_time.shift(months=1, days=-1).date()
        # 当前月的第一天或者下个月，不查询考勤
        elif (arrow.now().date().day == 1 and arrow.get(search_month,
                                                        "YYYY-MM").date().month == arrow.now().date().month) or arrow.get(
            search_month, "YYYY-MM") > arrow.get(
            str(arrow.now().date())[:7], "YYYY-MM"):
            return {
                'msg': '查询成功',
                'code': 200,
                'data': {
                    'daliy_list': [],
                    'count_list': [],
                },
            }
        else:
            search_month_first_day = str(arrow.now().date())[:7] + '-01'
            search_month_last_day = str(arrow.now().shift(days=-1).date())

        daliy_data_list = self.ehr.select(
            daliy_attendance_data_sql(code, search_month_first_day, search_month_last_day))
        color = ['#daf0fe', '#fef2dc', '#fcd9df', '#f1e9fe']
        if daliy_data_list:
            # 获取员工某一天的上下班时间
            daliy_list = []
            for item in daliy_data_list:
                daliy_list.append(
                    {'date': item['work_date'], 'info': lang_type[language]['statue'][item['attendance_status']]})
                for statu in lang_type[language]['statue'][item['attendance_status']].split('/'):
                    if statu in lang_type[language]['count_statue']:
                        # lang_type[language]['count_statue'][lang_type[language]['statue'][item['attendance_status']]] += 1
                        lang_type[language]['count_statue'][statu] += 1
            return {
                'msg': '查询成功',
                'code': 200,
                'data': {
                    'daliy_list': daliy_list,
                    'count_field': lang_type[language]['count_field'],
                    'count_list': [
                        {'title': key, 'value': lang_type[language]['count_statue'][key], 'color': color[index]} for
                        index, key in
                        enumerate(lang_type[language]['count_statue'].keys())],
                },
            }
