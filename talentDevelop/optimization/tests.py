# from datetime import datetime, timedelta
# import calendar
#
# def last_day_of_month(any_day):
#  """
#  获取获得一个月中的最后一天
#  :param any_day: 任意日期
#  :return: string
#  """
#  next_month = any_day.replace(day=28) + timedelta(days=4) # this will never fail
#  return next_month - timedelta(days=next_month.day)
#
# current_date = datetime.now()
#
# date_list = []
# start_date = datetime(2023, 11, 30)
# while start_date <= current_date:
#  last_day = last_day_of_month(start_date)
#  if last_day not in date_list:
#      date_list.append(last_day)
#      start_date = last_day + timedelta(days=1)
#
# for date in date_list:
#  print(date)
#
#  from datetime import datetime, timedelta
#  import calendar
#
#
#  def last_day_of_month(any_day):
#      """
#      获取获得一个月中的最后一天
#      :param any_day: 任意日期
#      :return: string
#      """
#      next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
#      return next_month - timedelta(days=next_month.day)
#
#
#  current_date = datetime.now()
#
#  date_list = []
#  start_date = datetime(2023, 11, 30)
#  while start_date <= current_date:
#      last_day = last_day_of_month(start_date)
#      if last_day not in date_list:
#          date_list.append(last_day)
#      start_date = last_day + timedelta(days=1)
#
#  for date in date_list:
#      print(date)
#
#
#
# 如果当前时间在2024年1月的最后一天或之前：返回[
# 2023/11/30,
# 2023/12/31,
# 2024/1/31,
# 2024/2/29,
# 2024/3/31]
# 如果当前时间在2024年2月的第一天到2024年3月的最后一天：[2023/11/30,
# 2023/12/31,
# 2024/1/31,
# 2024/2/29,
# 2024/3/31,
# 2023/4/30,
# 2023/5/31]
# 如果当前时间在2024年4月的第一天到2024年5月的最后一天返回[2023/11/30,
# 2023/12/31,
# 2024/1/31,
# 2024/2/29,
# 2024/3/31,
# 2023/4/30,
# 2023/5/31,
# 2023/6/30,
# 2023/7/31]
# 以此类推，你可以按照相同的模式继续生成月份的最后一天日期。


from datetime import datetime, timedelta


def generate_dates(current_date):
    dates = []

    if current_date <= datetime(2024, 1, 31):
        dates.extend([datetime(2023, 11, 30), datetime(2023, 12, 31), datetime(2024, 1, 31), datetime(2024, 2, 29),
                      datetime(2024, 3, 31)])
    elif datetime(2024, 2, 1) <= current_date <= datetime(2024, 3, 31):
        dates.extend([datetime(2023, 11, 30), datetime(2023, 12, 31), datetime(2024, 1, 31), datetime(2024, 2, 29),
                      datetime(2024, 3, 31),
                      datetime(2024, 4, 30), datetime(2024, 5, 31)])
    elif datetime(2024, 4, 1) <= current_date <= datetime(2024, 5, 31):
        dates.extend([datetime(2023, 11, 30), datetime(2023, 12, 31), datetime(2024, 1, 31), datetime(2024, 2, 29),
                      datetime(2024, 3, 31),
                      datetime(2024, 4, 30), datetime(2024, 5, 31), datetime(2024, 6, 30), datetime(2024, 7, 31)])
    elif datetime(2024,6, 1) <= current_date <= datetime(2024, 7, 31):
        dates.extend([datetime(2023, 11, 30), datetime(2023, 12, 31), datetime(2024, 1, 31), datetime(2024, 2, 29),
                      datetime(2024, 3, 31),
                      datetime(2024, 4, 30), datetime(2024, 5, 31), datetime(2024, 6, 30), datetime(2024, 7, 31),datetime(2024, 9, 30),datetime(2024, 10, 31),])
    elif datetime(2024,8, 1) <= current_date <= datetime(2024, 9, 30):
        dates.extend([datetime(2023, 11, 30), datetime(2023, 12, 31), datetime(2024, 1, 31), datetime(2024, 2, 29),
                      datetime(2024, 3, 31),
                      datetime(2024, 4, 30), datetime(2024, 5, 31), datetime(2024, 6, 30), datetime(2024, 7, 31),datetime(2024, 9, 30),datetime(2024, 10, 31),datetime(2024, 11, 30),datetime(2024, 10, 31),])
    # Add more conditions for other months
    return dates
    # return [date.strftime("%Y/%m/%d") for date in dates]


# 用当前日期调用函数
# current_date = datetime.now()
current_date=datetime(2024, 1, 2)
result = generate_dates(current_date)

print(result)


