#
# from datetime import datetime, timedelta
#
#
#
# year = 2023
# week = 1
#
# # 计算第一周的开始日期（星期一）
# start_date = datetime(year, 1, 1) + timedelta(days=(week - 2) * 7)
# start_date = start_date + timedelta(days=(start_date.weekday() - 0) % 7)+ timedelta(days=2)
#
# # 计算第一周的结束日期（星期日）
# end_date = start_date + timedelta(days=6)
# print(start_date.date(),end_date.date())
#
#
#
# # 周一00：00:00  周日 23：59：59：59
# # 周日23：59：59           周六
#
# from datetime import datetime
# import calendar
#
# # 定义一个月份
# month = '2023-02'
#
# # 将字符串转换为datetime对象
# start_date = datetime.strptime(month + '-01', '%Y-%m-%d')
#
# # 获取该月份的结束日期
# _, num_days = calendar.monthrange(start_date.year, start_date.month)
# end_date = datetime.strptime(month + '-' + str(num_days), '%Y-%m-%d')
#
# # 打印开始和结束日期
# print("开始日期: ", start_date)
# print("结束日期: ", end_date)



import json

# data = {
#    'id_list': [],
#    'downloadAll': False,
#    'searchName': 'w',
#    'sliceType': 1,
#    'sliceDate': '2023-12-04',
#    'employeeGroupJoinDate': ['2023-12-20', '2024-01-16'],
#    'employeeDl': ['IDL', 'DL'],
#    'employeePayType': [1, 2],
#    'employeeJobRank': [6, 7, 5, 2, 1, 3],
#    'department_id': [3, 187, 540, 543, 544, 541, 545, 546, 547, 548, 714, 666, 542, 549, 551, 552, 550, 553, 554, 555, 665, 715, 223, 251, 717, 718, 252, 709, 279, 387, 388, 560, 329, 703, 705, 706, 707, 708, 704, 345, 380, 562, 381, 347, 201, 386, 567, 568, 561, 569, 570, 348, 389, 563, 564, 390, 394, 397, 391, 565, 566, 393, 383, 384, 556, 571, 719, 720, 721, 722, 701, 710, 711, 712, 713, 702, 385],
#    'employeeStatus': ['2', '1'],
#    'employeeWorkStatus': ['劳务工', '实习生'],
#    'currentPage': 1,
#    'pageSize': 25
# }

data={'id_list': [], 'downloadAll': False, 'currentPage': 1, 'pageSize': 25, 'searchName': '', 'baseNameId': [], 'employeeDl': [], 'jxGrade': [], 'employeePayType': [], 'employeeJobGrade': [], 'employeeJobSequence': [], 'PeriodDate': []}
json_data = json.dumps(data)
print(json_data)
