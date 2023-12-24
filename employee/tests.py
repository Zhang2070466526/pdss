from django.test import TestCase

# Create your tests here.
import arrow

# import arrow
#
# current_time = arrow.now()
# formatted_time = current_time.format('YYYY-MM-DD HH:mm:ss')
# begin_arrow_obj = arrow.get(formatted_time, "YYYY-MM-DD HH:mm:ss")
# datetime_obj = begin_arrow_obj.datetime
#
# end_arrow_object = arrow.Arrow(2013,  , 22, 0, 0, 0)
# print(end_arrow_object)
#
# print(formatted_time,type(formatted_time))
# print(begin_arrow_obj,type(begin_arrow_obj))
# print(datetime_obj,type(datetime_obj))
# months = begin_arrow_obj.span('months', end_arrow_object).months
# print(months)




# import arrow
#
# current_time = arrow.now()
# formatted_time = current_time.format('YYYY-MM-DD HH:mm:ss')
# begin_arrow_obj = arrow.get(formatted_time, "YYYY-MM-DD HH:mm:ss")
# end_arrow_object = arrow.Arrow(2013,  , 22, 0, 0, 0)
#
# months_between = (begin_arrow_obj.datetime - end_arrow_object.datetime).months
# print(months_between)

# from datetime import datetime
# print(datetime.now())
# begin_date = datetime(2023, 8, 21,12,3, )
# end_date = datetime(2023, 10, 1,11,2,3)
# print(begin_date,end_date)
# months_between = (end_date.year - begin_date.year) * 12 + (end_date.month - begin_date.month)
# print(months_between)

# a=[{'user_menu__nav_name_field': 'employee_identity_no', 'user_menu__nav_name': '身份证号码'}, {'user_menu__nav_name_field': 'employee_phone', 'user_menu__nav_name': '联系电话'}]
# b=[{'employee_identity_no': '身份证号码'}, {'employee_phone': '联系电话'}]


# import datetime
#
# timeStr = '2023-0 -30 00:00:00'
# date_time = datetime.datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')
# print(date_time,type(date_time))
# from datetime import datetime
# def days_until_given_date(datetime):
#     """
#
#     :param datetime:    要计算据今的日期   例datetime.datetime(2023, 7, 19, 0, 0)
#     :return:   days_difference  天数
#     """
#
#     given_date = datetime  # 给定的日期
#     current_date = datetime.now()  # 获取当前日期
#     time_difference =current_date- given_date
#
#     # 提取天数部分
#     days_difference = time_difference.days
#
#     return days_difference
#
#
# print(days_until_given_date(datetime(2023, 9, 7, 0, 0)))

# employee_departure_seniority=23
# if employee_departure_seniority <= 7:  # 7天内
#     print(' )
# elif employee_departure_seniority <= 30:  # 1个月内
#     print('30')
# elif employee_departure_seniority <= 90:  # 1-3个月
#     print('90')
# elif employee_departure_seniority <= 180:  # 3-6个月
#     print('180')
# elif employee_departure_seniority <= 36 :  # 6-12个月
#     print('36 ')
# elif employee_departure_seniority <= 730:  # 1-2年
#     print('730')
# else:  # 2年以上
#     print('2年')

a=[
   'T1-助工级',  
   'T2-工程师级',  
 'T2.2-技术员级',
    'T3-中工级',  
    'T -高工级',
   'T -资工级',
    'T6-专家级',  
    'T7-总工级',  

   'M2-班长级',  
    'M3-倒班主管级',  
   'M -主管级',
  'M -经理级',
    'M6-总监级',  
    'M7-总经理级',  
   'M8-总裁级',

   'P1-助理级',  
   'P2-专员级',  
    'P3-中专级',  
    'P -专业主管级',
    'P -专业经理级',
    'P6-专家级',  

   'O1-作业员级',  
   'O2-技工级',
   'O2-技师级',

'追光者','管培生','精英人才', '实习生',

  '操作员（旧）',  
  '班长级（旧）',  
   '员工级（旧）',  
   '技术员（旧）',
   '助工级（旧）',
   '工程师级（旧）',  
   '主管级（旧）',  
 '经理级（旧）',
'总监级及以上（旧）']
print(a)
