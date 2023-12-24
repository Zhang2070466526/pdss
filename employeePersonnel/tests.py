from django.test import TestCase

# Create your tests here.

from datetime import datetime, timedelta

from datetime import date, datetime, timedelta

# from datetime import date, datetime, time, timedelta
#
# def get_start_end_of_week():
#     # 获取当前日期
#     today = date.today()
#     # 计算今天是这周的第几天（0代表周一，6代表周日）
#     current_day_of_week = today.weekday()
#     # 计算日期差值以获取本周的周一
#     days_until_monday = current_day_of_week
#     monday = today - timedelta(days=days_until_monday)
#     # 计算日期差值以获取本周的周日
#     days_until_sunday = 6 - current_day_of_week
#     sunday = today + timedelta(days=days_until_sunday)
#     # 创建时间对象并设置时间为00:00:00
#     begin_time = time(0, 0, 0)
#     begin_date = datetime.combine(monday, begin_time)
#     # 创建时间对象并设置时间为23:59:59
#     end_time = time(23, 59, 59)
#     end_date = datetime.combine(sunday, end_time)
#     return begin_date, end_date
#
# # 调用函数获取本周的起始时间和结束时间
# start_time, end_time = get_start_end_of_week()
# print("本周周一:", start_time,type(start_time))
# print("本周周日:", end_time)
#
#
# from datetime import datetime, timedelta
#
# from datetime import datetime, timedelta
#
# # 获取当前日期和时间
# today = datetime.now()
#
# # 计算今天是星期几（0代表周一，1代表周二，以此类推）
# current_day_of_week = today.weekday()
#
# # 计算日期差值以获取上周的周一
# days_until_last_monday = current_day_of_week + 7
# last_monday = today - timedelta(days=days_until_last_monday)
#
# # 计算日期差值以获取上周的周日
# days_until_last_sunday = current_day_of_week + 1
# last_sunday = today - timedelta(days=days_until_last_sunday)
#
# # 手动设置微秒部分为0
# last_monday = last_monday.replace(hour=23, minute=59, second=59, microsecond=0)
# last_sunday = last_sunday.replace(hour=23, minute=59, second=59, microsecond=0)
#
# print("上周周一:", last_monday)
# print("上周周日:", last_sunday)
#



from datetime import date, datetime, timedelta,time

def get_start_end_of_week(flag=0):
    # 获取当前日期
    today = date.today()

    if flag == 1:
        # 计算上周的周一
        days_until_monday = today.weekday() + 7 * flag
    else:
        # 计算这周的周一
        days_until_monday = today.weekday()
    monday = today - timedelta(days=days_until_monday)
    # 计算日期差值以获取周日
    days_until_sunday = 6 - days_until_monday
    sunday = today + timedelta(days=days_until_sunday)
    # 创建时间对象并设置时间为00:00:00
    begin_time = time(0, 0, 0)
    begin_date = datetime.combine(monday, begin_time)
    # 创建时间对象并设置时间为23:59:59
    end_time = time(23, 59, 59)
    end_date = datetime.combine(sunday, end_time)
    return begin_date, end_date

# 调用方法获取这周的周一和周日
start_time, end_time = get_start_end_of_week()
print("这周周一:", start_time,type(start_time))
print("这周周日:", end_time)

# 调用方法获取上周的周一和周日
start_time_last_week, end_time_last_week = get_start_end_of_week(flag=1)
print("上周周一:", start_time_last_week)
print("上周周日:", end_time_last_week)



from datetime import date, datetime, timedelta, time

from datetime import date, datetime, time
from datetime import date, datetime, timedelta, time

# def calculate_dates(param):
#    today = date.today()
#
#    if param == 0:
#        first_day = today.replace(day=1)
#        last_day = today.replace(day=1) + timedelta(days=32)
#        last_day = last_day.replace(day=1) - timedelta(days=1)
#    elif param == 1:
#        if today.month == 1:
#            first_day = today.replace(year=today.year - 1, month=12, day=1)
#        else:
#            first_day = today.replace(month=today.month - 1, day=1)
#        last_day = first_day.replace(day=1) + timedelta(days=32)
#        last_day = last_day.replace(day=1) - timedelta(days=1)
#
#    begin_date = datetime.combine(first_day, time(0, 0, 0))
#    end_date = datetime.combine(last_day, time(23, 59, 59))
#
#    return begin_date, end_date
#
# print(calculate_dates(0)) # For current month
# print(calculate_dates(1)) # For previous month






from datetime import date, datetime, timedelta, time
from datetime import date, datetime, timedelta, time
from datetime import date
from dateutil.relativedelta import relativedelta



def get_month_dates(month):
    # 获取当前日期
    today = date.today()

    if month == "last":
        # 计算上个月的第一天
        if today.month == 1:
            last_month = today.replace(year=today.year - 1, month=12, day=1)
        else:
            last_month = today.replace(month=today.month - 1, day=1)

        # 计算日期差值以获取上个月的最后一天
        last_day_of_last_month = today.replace(day=1) - timedelta(days=1)

        # 创建时间对象并设置时间为00:00:00
        begin_date = datetime.combine(last_month, time(0, 0, 0))
        end_date = datetime.combine(last_day_of_last_month, time(23, 59, 59))
    elif month == "current":
        # 计算本月的第一天
        first_day_of_current_month = today.replace(day=1)

        # 计算本月的最后一天
        if today.month == 12:
            last_day_of_current_month = today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1)
        else:
            last_day_of_current_month = today.replace(month=today.month + 1, day=1) - timedelta(days=1)

        # 创建时间对象并设置时间为00:00:00
        begin_date = datetime.combine(first_day_of_current_month, time(0, 0, 0))
        end_date = datetime.combine(last_day_of_current_month, time(23, 59, 59))
    else:
        raise ValueError("Invalid month parameter. Use 'last' or 'current'.")

    return begin_date, end_date

# 使用函数计算上个月的日期范围
begin_date_last_month, end_date_last_month = get_month_dates("last")

# 使用函数计算这个月的日期范围
begin_date_current_month, end_date_current_month = get_month_dates("current")

print("上个月的第一天:", begin_date_last_month)
print("上个月的最后一天:", end_date_last_month)
print("这个月的第一天:", begin_date_current_month)
print("这个月的最后一天:", end_date_current_month)




print("===========================")

import calendar
from datetime import datetime, time

def get_month_dates(month):
   # Get the current date
   today = datetime.today()

   # Calculate the year and month for the previous, current, or next month
   if month == "last":
       year, month = today.year, today.month - 1
       if month == 0:
           year, month = year - 1, 12
   elif month == "current":
       year, month = today.year, today.month
   elif month == "next":
       year, month = today.year, today.month + 1
       if month == 13:
           year, month = year + 1, 1
   else:
       raise ValueError("Invalid month parameter. Use 'last', 'current', or 'next'.")

   # Calculate the first and last day of the month
   _, num_days = calendar.monthrange(year, month)
   first_day = datetime(year, month, 1)
   last_day = datetime(year, month, num_days)

   # Create datetime objects and set the time to 00:00:00 and 23:59:59
   begin_date = datetime.combine(first_day, time(0, 0, 0))
   end_date = datetime.combine(last_day, time(23, 59, 59))

   return begin_date, end_date

# Get the dates for the previous month
begin_date_last_month, end_date_last_month = get_month_dates("last")
print("上个月的第一天:", begin_date_last_month)
print("上个月的最后一天:", end_date_last_month)

# Get the dates for the current month
begin_date_current_month, end_date_current_month = get_month_dates("current")
print("这个月的第一天:", begin_date_current_month)
print("这个月的最后一天:", end_date_current_month)

# Get the dates for the next month
begin_date_next_month, end_date_next_month = get_month_dates("next")
print("下个月的第一天:", begin_date_next_month)
print("下个月的最后一天:", end_date_next_month)



# # 获取当前日期
# today = date.today()
#
# # 获取当月的第一天（设置为1号）
# first_day_of_month = date(today.year, today.month, 1)
#
# # 计算下个月的第一天
# if today.month == 12:
#     next_month = today.replace(year=today.year + 1, month=1, day=1)
# else:
#     next_month = today.replace(month=today.month + 1, day=1)
#
# # 计算日期差值以获取本月的最后一天
# last_day_of_month = next_month - timedelta(days=1)
#
# # 创建时间对象并设置时间为00:00:00
# begin_date = datetime.combine(first_day_of_month, time(0, 0, 0))
#
# # 创建时间对象并设置时间为23:59:59
# end_date = datetime.combine(last_day_of_month, time(23, 59, 59))
#
# print(begin_date, end_date)
#
#
#
# from datetime import date, datetime, timedelta, time
#
# # 获取当前日期
# today = date.today()
#
# # 计算上个月的第一天
# if today.month == 1:
#     last_month = today.replace(year=today.year - 1, month=12, day=1)
# else:
#     last_month = today.replace(month=today.month - 1, day=1)
#
# # 计算本月的第一天
# first_day_of_last_month = last_month.replace(day=1)
#
# # 计算本月的第一天（设置为1号）
#
# # 计算下个月的第一天
# if today.month == 12:
#     next_month = today.replace(year=today.year + 1, month=1, day=1)
# else:
#     next_month = today.replace(month=today.month + 1, day=1)
#
# # 计算日期差值以获取上个月的最后一天
# last_day_of_last_month = today.replace(day=1) - timedelta(days=1)
#
# # 创建时间对象并设置时间为00:00:00
# begin_date = datetime.combine(first_day_of_last_month, time(0, 0, 0))
#
# # 创建时间对象并设置时间为23:59:59
# end_date = datetime.combine(last_day_of_last_month, time(23, 59, 59))
#
# print(begin_date, end_date)
