
# plot(data$x, data$y)
# abline(model)
# new_data <- data.frame(x = 6)
# predicted_y <- predict(model, newdata = data.frame(x = 100))
#预测x=6对应的y值

# a=(23.304261,
# 23.346543,
# 22.809832,
# 23.37768,
# 22.738248,
# 23.334312,
# 23.396822,
# 23.181313,
# 23.356523,
# 23.256475,
# 23.31144,
# 22.908182)

# b=(1,2,3,4,5,6,7,8,9,10,11,12)
# print(a)


# 17-09-2023
# 17-09-2023
# 17-09-2023
# 17-09-2023
# 17-09-2023
# 17-09-2023
# 17-09-2023
# 17-09-2023
# 17-09-2023
# 17-09-2023
# 17-09-2023
# 17-09-2023

# xts_data <- xts(时间序列$nta, order.by = 时间序列$time)
#
# library(xts)
# library(forecast)

from datetime import datetime, date,timedelta

from datetime import datetime

def to_date(value):
    if isinstance(value, datetime):
        return value

    if isinstance(value, str):
        try:
            date_obj = datetime.strptime(value, '%Y-%m-%d')  # 根据日期格式修改这里
            return date_obj
        except ValueError:
            return None

    return None

# 测试
value1 = datetime(2023, 10, 25)
value2 = "2023-10-25"
value3 = "This is not a date"

result1 = to_date(value1)
result2 = to_date(value2)
result3 = to_date(value3)

print(result1)  # 2023-10-25 00:00:00
print(result2)  # 2023-10-25 00:00:00
print(result3)  # None




from urllib.parse import urlparse

url = "http://10.60.13.139:8001/static/certificateFile/2023-10-26/041/wallhaven-eymdll.jpg"
parsed_url = urlparse(url)
path = parsed_url.path
print(path)


def increment_string(s, n):
    # 提取字符串中的数字部分
    num_str = s[s.rfind('0'):]
    # 将数字部分转换为整数
    num = int(num_str)
    # 增加n
    num += n
    # 将新的数字转换为字符串，并填充零
    new_num_str = str(num).zfill(len(num_str))
    # 将新的数字字符串插入到原始字符串中
    new_s = s[:s.rfind('0')] + new_num_str
    return new_s
print(increment_string('ABCEDEFG000000',1))
#
# s = "ABCEDEFG000001"
# for i in range(1, 101):
#     s = increment_string(s, 1)
#     print(s)


# import os
#
# path = "static\certificateFile\张三2023-10-27857\张三_证书.jpg"
# filename = os.path.basename(path)
#
# print(filename)
#
#
# import arrow
#
# # 获取今天的日期
# today = arrow.now()
#
# # 获取上个月的第一天，时间设为00:00:00
# first_day_last_month = today.shift(months=-1).replace(day=1, hour=0, minute=0, second=0)
#
# # 获取上个月的最后一天，时间设为23:59:59
# last_day_last_month = today.shift(months=-1).replace(day=1, hour=0, minute=0, second=0).shift(months=1).shift(seconds=-1)
#
# print("上个月的第一天：", first_day_last_month)
# print("上个月的最后一天：", last_day_last_month)



from datetime import datetime, timedelta
import calendar


# # Get the current date
# now = datetime.now()
#
# # Get the first day of the previous month at 00:00:00
# first_day_prev_month = now.replace(month=now.month - 1, day=1, hour=0, minute=0, second=0)
#
# # Get the last day of the previous month at 23:59:59
# _, num_days_prev_month = calendar.monthrange(now.year, now.month - 1)
# last_day_prev_month = now.replace(month=now.month - 1, day=num_days_prev_month, hour=23, minute=59, second=59)
#
# print('First day of previous month:', first_day_prev_month)
# print('Last day of previous month:', last_day_prev_month)


# from datetime import datetime, timedelta
#
# # Get the current date
# now = datetime.now()
#
# # Get the first day of the previous month at 00:00:00
# first_day_prev_month = now.replace(month=now.month - 1, day=1, hour=0, minute=0, second=0)
#
# # Get the last day of the previous month at 23:59:59
# _, num_days_prev_month = calendar.monthrange(now.year, now.month - 1)
# last_day_prev_month = now.replace(month=now.month - 1, day=num_days_prev_month, hour=23, minute=59, second=59)
#
# print('First day of previous month:', first_day_prev_month)
# print('Last day of previous month:', last_day_prev_month)




# a=[{'id':'5','name':'zy'},{'id':'6','name':'dyj'},{'id':'7','name':'qr'}]
# b=[{'fill_record_id':'5','name':'zy','fill_leave_hour':'1111111'},{'fill_record_id':'6','name':'dyj','code':'2222222'},{'fill_record_id':'5','name':'zy','code':'333333'}]
#
# #
# # c=[
# #     {'id':'5','name':'zy','fill_record_id':'5','fill_leave_hour':'1111111','code':'333333'},
# #     {'id':'6','name':'dyj','fill_record_id':'6','code':'2222222'}
# # ]
# c=[
#     {'id':'5','name':'zy','fill_record_id':'5','fill_leave_hour':'1111111'},
#     {'id':'5','name':'zy','fill_record_id':'5','code':'333333'},
#     {'id':'6','name':'dyj','fill_record_id':'6','code':'2222222'},
#     {'id':'7','name':'qr'}
# ]


# c = []
# for item_a in a:
#     merged_item = {**item_a}
#     for item_b in b:
#         if item_b.get('fill_record_id') == item_a.get('id'):
#             merged_item.update(item_b)
#     c.append(merged_item)
#
# print(c)
#
# a = [{'id': '5', 'name': 'zy'}, {'id': '6', 'name': 'dyj'}, {'id': '7', 'name': 'qr'}]
# b = [
#     # {'fill_record_id': '5', 'name': 'zy', 'fill_leave_hour': '1111111'},
#     #  {'fill_record_id': '6', 'name': 'dyj', 'code': '2222222'},
#     #  {'fill_record_id': '5', 'name': 'zy', 'code': '333333'}
#      ]
#
# # Create a list to store the merged data
# c = []
#
# # Merge data from list 'a' and 'b' into 'c' based on 'id' and 'fill_record_id'
# for item_a in a:
#     id_a = item_a['id']
#     for item_b in b:
#         fill_record_id_b = item_b.get('fill_record_id')
#         if id_a == fill_record_id_b:
#             merged_item = item_a.copy()
#             merged_item.update(item_b)
#             c.append(merged_item)
#
# # Add the remaining items from list 'a' that don't have corresponding entries in 'b'
# for item_a in a:
#     id_a = item_a['id']
#     if not any(item['fill_record_id'] == id_a for item in c):
#         c.append(item_a)
#
# print(c)



# a = [{'id': '5', 'name': 'zy'}, {'id': '6', 'name': 'dyj'}, {'id': '7', 'name': 'qr'}]
# b = [
#     {'fill_record_id': '5', 'name': 'zy', 'fill_leave_hour': '1111111'},
#      {'fill_record_id': '6', 'name': 'dyj', 'code': '2222222'},
#      {'fill_record_id': '5', 'name': 'zy', 'code': '333333'}
#      ]
# c = []  # Initialize the result list
# d=[2,1,0]
# # Merge items from 'a' and 'b' based on matching 'id' and 'fill_record_id'
# for item_a in a:
#     id_a = item_a['id']
#     for item_b in b:
#         fill_record_id_b = item_b.get('fill_record_id')
#         if id_a == fill_record_id_b:
#             merged_item = item_a.copy()  # Create a copy of item_a
#             merged_item.update(item_b)  # Update the copy with item_b
#             c.append(merged_item)  # Append the merged item to 'c'
#
# # Add the remaining items from list 'a' that don't have corresponding entries in 'b'
# for item_a in a:
#     id_a = item_a['id']
#     if not any('fill_record_id' in item and item['fill_record_id'] == id_a for item in c):
#         c.append(item_a)  # Append unmatched items from 'a' to 'c'
#
# # 'c' now contains the merged and unmatched items from 'a'
#
# print(c)



# a = [{'id': '5', 'name': 'zy'}, {'id': '6', 'name': 'dyj'}, {'id': '7', 'name': 'qr'}]
# b = [
#     {'fill_record_id': '5', 'name': 'zy', 'fill_leave_hour': '1111111'},
#     {'fill_record_id': '6', 'name': 'dyj', 'code': '2222222'},
#     {'fill_record_id': '5', 'name': 'zy', 'code': '333333'}
# ]
#
# # Create a dictionary to store the count of each 'id'
# id_count = {}
#
# # Initialize the count for each 'id' to 0
# for item_a in a:
#     id_count[item_a['id']] = 0
#
# # Create an empty list 'c' to store the merged and unmatched items
# c = []
#
# # Count how many times each 'id' appears in 'b' and merge the items
# for item_a in a:
#     id_a = item_a['id']
#     for item_b in b:
#         fill_record_id_b = item_b.get('fill_record_id')
#         if id_a == fill_record_id_b:
#             merged_item = item_a.copy()  # Create a copy of item_a
#             merged_item.update(item_b)  # Update the copy with item_b
#             c.append(merged_item)  # Append the merged item to 'c'
#             id_count[id_a] += 1
#
# # Add the remaining items from list 'a' that don't have corresponding entries in 'b' to 'c'
# for item_a in a:
#     id_a = item_a['id']
#     if not any('fill_record_id' in item and item['fill_record_id'] == id_a for item in c):
#         c.append(item_a)  # Append unmatched items from 'a' to 'c'
#
# # Convert the counts to a list
# count_list = [id_count[item['id']] for item in a]
#
# print(count_list)  # Output: [2, 1, 0]
# print(c)  # Merged and unmatched items in list 'c'

# a = [{'id': '5', 'name': 'zy'}, {'id': '6', 'name': 'dyj'}, {'id': '7', 'name': 'qr'}]
# b = [
#     {'fill_record_id': '5', 'name': 'zy', 'fill_leave_hour': '1111111'},
#     {'fill_record_id': '6', 'name': 'dyj', 'code': '2222222'},
#     {'fill_record_id': '5', 'name': 'zy', 'code': '333333'}
# ]
#
# # Create a dictionary to store the count of each 'id' and initialize it to 1
# id_count = {item_a['id']: 1 for item_a in a}
#
# # Create an empty list 'c' to store the merged and unmatched items
# c = []
#
# # Count how many times each 'id' appears in 'b' and merge the items
# for item_a in a:
#     id_a = item_a['id']
#     count = 0  # Initialize the count to 0 for each 'id'
#     for item_b in b:
#         fill_record_id_b = item_b.get('fill_record_id')
#         if id_a == fill_record_id_b:
#             merged_item = item_a.copy()  # Create a copy of item_a
#             merged_item.update(item_b)  # Update the copy with item_b
#             c.append(merged_item)  # Append the merged item to 'c'
#             count += 1  # Increase the count by 1
#     id_count[id_a] = count
#
# # Add the remaining items from list 'a' that don't have corresponding entries in 'b' to 'c'
# for item_a in a:
#     id_a = item_a['id']
#     if not any('fill_record_id' in item and item['fill_record_id'] == id_a for item in c):
#         c.append(item_a)  # Append unmatched items from 'a' to 'c'
#
# # Convert the counts to a list
# count_list = [id_count[item['id']] for item in a]
#
# print(count_list)  # Output: [2, 1, 1]
# print(c)  # Merged and unmatched items in list 'c'
#


# record_list = [{'id': '5', 'name': 'zy'}, {'id': '6', 'name': 'dyj'}, {'id': '7', 'name': 'qr'}]
# fill_list = [
#     {'fill_record_id': '5', 'name': 'zy', 'fill_leave_hour': '1111111'},
#     {'fill_record_id': '6', 'name': 'dyj', 'code': '2222222'},
#     {'fill_record_id': '5', 'name': 'zy', 'code': '333333'}
# ]
#
# # Create a dictionary to store the count of each 'id' and initialize it to 1
# id_count = {item_a['id']: 1 for item_a in record_list}
#
# # Create an empty list 'table_list' to store the merged and unmatched items
# table_list = []
#
# # Count how many times each 'id' appears in 'fill_list' and merge the items
# for item_a in record_list:
#     id_a = item_a['id']
#     count = 0  # Initialize the count to 0 for each 'id'
#     for item_b in fill_list:
#         fill_record_id_b = item_b.get('fill_record_id')
#         if id_a == fill_record_id_b:
#             merged_item = item_a.copy()  # Create a copy of item_a
#             merged_item.update(item_b)  # Update the copy with item_b
#             table_list.append(merged_item)  # Append the merged item to 'table_list'
#             count += 1  # Increase the count by 1
#     id_count[id_a] = max(count, 1)  # Set the count to at least 1
#
# # Add the remaining items from list 'record_list' that don't have corresponding entries in 'fill_list' to 'table_list'
# for item_a in record_list:
#     id_a = item_a['id']
#     if not any('fill_record_id' in item and item['fill_record_id'] == id_a for item in table_list):
#         table_list.append(item_a)  # Append unmatched items from 'record_list' to 'table_list'
#
# # Convert the counts to a list
# count_list = [id_count[item['id']] for item in record_list]
#
# print(count_list)  # Output: [2, 1, 1]
# print(table_list)  # Merged and unmatched items in list 'table_list'



# record_list = [{'id': '5', 'name': 'zy'}, {'id': '6', 'name': 'dyj'}, {'id': '7', 'name': 'qr'}]
# fill_list = [
#     {'fill_record_id': '5', 'name': 'zy', 'fill_leave_hour': '1111111'},
#     {'fill_record_id': '6', 'name': 'dyj', 'code': '2222222'},
#     {'fill_record_id': '5', 'name': 'zy', 'code': '333333'}
# ]

import datetime
record_list =[{'id': 9, 'records_people__employee_code': '1010000776', 'records_people__employee_name': '秦蕤', 'records_passport': '12345', 'records_stationed_country__country_name': '越南', 'records_stationed_base__base_name': '泰国P1P2(巴吞）', 'records_people__employee_department__department_first_name': '人力资源中心', 'records_people__employee_department__department_second_name': '信息技术部', 'records_people__employee_department__department_third_name': '软件开发', 'records_people__employee_join_date': datetime.datetime(2023, 6, 30, 0, 0), 'records_begin_data': datetime.date(2019, 10, 26), 'records_end_data': datetime.date(2022, 3, 8), 'records_work_visa': True, 'records_local_bank': False, 'records_local_social_security': False, 'records_local_individual_taxes': True}, {'id': 6, 'records_people__employee_code': '1010000407', 'records_people__employee_name': '张优', 'records_passport': 'esse Duis aute nostrud', 'records_stationed_country__country_name': '越南', 'records_stationed_base__base_name': '泰国P1P2(巴吞）', 'records_people__employee_department__department_first_name': '人力资源中心', 'records_people__employee_department__department_second_name': '信息技术部', 'records_people__employee_department__department_third_name': '软件开发', 'records_people__employee_join_date': datetime.datetime(2023, 3, 15, 0, 0), 'records_begin_data': datetime.date(2019, 10, 26), 'records_end_data': datetime.date(2022, 3, 8), 'records_work_visa': True, 'records_local_bank': False, 'records_local_social_security': False, 'records_local_individual_taxes': True}, {'id': 7, 'records_people__employee_code': '1010000401', 'records_people__employee_name': '杜衍俊', 'records_passport': '11111111', 'records_stationed_country__country_name': '越南', 'records_stationed_base__base_name': '泰国P3（罗勇）', 'records_people__employee_department__department_first_name': '人力资源中心', 'records_people__employee_department__department_second_name': '信息技术部', 'records_people__employee_department__department_third_name': '软件开发', 'records_people__employee_join_date': datetime.datetime(2023, 7, 1, 0, 0), 'records_begin_data': datetime.date(2023, 10, 1), 'records_end_data': datetime.date(2023, 10, 31), 'records_work_visa': False, 'records_local_bank': False, 'records_local_social_security': False, 'records_local_individual_taxes': False}]

fill_list= [{'fill_record_id': 6, 'fill_inout_status__type_name': '离泰', 'fill_into_thailand_date': datetime.datetime(2023, 11, 2, 11, 0), 'fill_leave_thailand_date': datetime.datetime(2023, 11, 2, 12, 0), 'fill_trip_reason': 1, 'fill_leave_thailand_address': None, 'fill_leave_thailand_days': None, 'fill_leave_hour': None, 'fill_absenteeism_hour': None, 'fill_remark': '', 'fill_id': 9}, {'fill_record_id': 6, 'fill_inout_status__type_name': '离泰', 'fill_into_thailand_date': datetime.datetime(2023, 11, 3, 11, 0), 'fill_leave_thailand_date': datetime.datetime(2023, 11, 2, 12, 0), 'fill_trip_reason': 1, 'fill_leave_thailand_address': None, 'fill_leave_thailand_days': None, 'fill_leave_hour': None, 'fill_absenteeism_hour': None, 'fill_remark': '', 'fill_id': 10}, {'fill_record_id': 9, 'fill_inout_status__type_name': '入越', 'fill_into_thailand_date': datetime.datetime(2023, 11, 1, 11, 0), 'fill_leave_thailand_date': datetime.datetime(2023, 11, 6, 12, 0), 'fill_trip_reason': 5, 'fill_leave_thailand_address': None, 'fill_leave_thailand_days': None, 'fill_leave_hour': None, 'fill_absenteeism_hour': None, 'fill_remark': '', 'fill_id': 11}]
# Create a dictionary to store the count of each 'id' and initialize it to 1
id_count = {item_a['id']: 1 for item_a in record_list}

# Create an empty list 'table_list' to store the merged and unmatched items
table_list = []

# Count how many times each 'id' appears in 'fill_list' and merge the items
for item_a in record_list:
    id_a = item_a['id']
    count = 0  # Initialize the count to 0 for each 'id'
    for item_b in fill_list:
        fill_record_id_b = item_b.get('fill_record_id')
        if id_a == fill_record_id_b:
            merged_item = item_a.copy()  # Create a copy of item_a
            merged_item.update(item_b)  # Update the copy with item_b
            table_list.append(merged_item)  # Append the merged item to 'table_list'
            count += 1  # Increase the count by 1
    id_count[id_a] = max(count, 1)  # Set the count to at least 1

# Add the remaining items from list 'record_list' that don't have corresponding entries in 'fill_list' to 'table_list'
for item_a in record_list:
    id_a = item_a['id']
    if not any('fill_record_id' in item and item['fill_record_id'] == id_a for item in table_list):
        table_list.append(item_a)  # Append unmatched items from 'record_list' to 'table_list'

# Convert the counts to a list
count_list = [id_count[item['id']] for item in record_list]

print(count_list)  # Output: [2, 1, 1]
print(table_list)  # Merged and unmatched items in list 'table_list'


print("+++++++++++++++++++++++++++++++++++++")




record_list =[{'id': 6, 'records_people__employee_code': '1010000407', 'records_people__employee_name': '张优', 'records_passport': 'esse Duis aute nostrud'}, {'id': 7, 'records_people__employee_code': '1010000401', 'records_people__employee_name': '杜衍俊', 'records_passport': '11111111'}]

fill_list = [{'fill_record_id': 6, 'fill_inout_status__type_name': '离泰', 'fill_remark': '', 'fill_id': 9},
             {'fill_record_id': 6, 'fill_inout_status__type_name': '离泰', 'fill_remark': '', 'fill_id': 10}]

table_list=[{'id': 6, 'records_people__employee_code': '1010000407', 'records_people__employee_name': '张优', 'records_passport': 'esse Duis aute nostrud','fill_record_id': 6, 'fill_inout_status__type_name': '离泰', 'fill_remark': '', 'fill_id': 9},
            {'id': 6, 'records_people__employee_code': '1010000407', 'records_people__employee_name': '张优', 'records_passport': 'esse Duis aute nostrud','fill_record_id': 6, 'fill_inout_status__type_name': '离泰', 'fill_remark': '', 'fill_id': 10},
            {'id': 7, 'records_people__employee_code': '1010000401', 'records_people__employee_name': '杜衍俊', 'records_passport': '11111111','fill_record_id': None, 'fill_inout_status__type_name': None, 'fill_remark': None, 'fill_id':None}]


#
# table_list = []
#
# # Create a dictionary to store 'fill_list' items based on 'fill_record_id'
# fill_dict = {item['fill_record_id']: item for item in fill_list}
#
# # Iterate through 'record_list' and create 'table_list'
# for item in record_list:
#     id_a = item['id']
#     fill_item = fill_dict.get(id_a, {})
#     merged_item = item.copy()
#     merged_item.update(fill_item)
#     table_list.append(merged_item)
#
# # Add the remaining 'fill_list' items with 'fill_record_id' not in 'record_list' as None values
# for item in fill_list:
#     if item['fill_record_id'] not in {item['id'] for item in record_list}:
#         table_list.append({**item, **{key: None for key in record_list[0].keys()}})
#
# print(table_list)







print("++++++++++++++++++++++++++++++++++++++")

# import datetime
# list_of_dicts=[
#   {
#     'id': 6,
#     'records_people__employee_code': '1010000407',
#     'records_people__employee_name': '张优',
#     'records_passport': 'esseDuisautenostrud',
#     'records_stationed_country__country_name': '越南',
#     'records_stationed_base__base_name': '泰国P1P2(巴吞）',
#     'records_people__employee_department__department_first_name': '人力资源中心',
#     'records_people__employee_department__department_second_name': '信息技术部',
#     'records_people__employee_department__department_third_name': '软件开发',
#     'records_people__employee_join_date': datetime.datetime(2023,3,15,0,0),
#     'records_begin_data': datetime.date(2019,10,26),
#     'records_end_data': datetime.date(2022,3,8),
#     'records_work_visa': True,
#     'records_local_bank': False,
#     'records_local_social_security': False,
#     'records_local_individual_taxes': True,
#     'index': 2,
#     'fill_record_id': 6,
#     'fill_inout_status__type_name': '离泰',
#     'fill_into_thailand_date': datetime.datetime(2023,11,2,11,0),
#     'fill_leave_thailand_date': datetime.datetime(2023,11,2,12,0),
#     'fill_trip_reason': 1,
#     'fill_leave_thailand_address': None,
#     'fill_leave_thailand_days': None,
#     'fill_leave_hour': None,
#     'fill_absenteeism_hour': None,
#     'fill_remark': ''
#   },
#
#   {
#     'id': 7,
#     'records_people__employee_code': '1010000401',
#     'records_people__employee_name': '杜衍俊',
#     'records_passport': '11111111',
#     'records_stationed_country__country_name': '越南',
#     'records_stationed_base__base_name': '泰国P3（罗勇）',
#
#     'index': 3
#   }
# ]
#
#
# def sort_list_of_dicts(list_of_dicts):
#     # 指定排序顺序
#     order = [
#         'index', 'records_people__employee_code', 'records_people__employee_name', 'records_passport',
#         'records_stationed_country__country_name', 'records_stationed_base__base_name',
#         'records_people__employee_join_date', 'records_people__employee_department__department_first_name',
#         'records_people__employee_department__department_second_name',
#         'records_people__employee_department__department_third_name',
#         'records_work_visa', 'records_local_bank', 'records_local_social_security', 'records_local_individual_taxes',
#         'fill_inout_status__type_name', 'fill_into_thailand_date', 'fill_leave_thailand_date',
#         'fill_trip_reason', 'fill_remark', 'fill_leave_thailand_address', 'fill_leave_thailand_days',
#         'fill_leave_hour', 'fill_absenteeism_hour', 'fill_record_id', 'id'
#     ]
#
#     def sort_key(item):
#         # 将缺失的键的值设置为默认值，这里默认值可以是 None
#         key = item[0]
#         return (order.index(key) if key in order else len(order), item[0])
#
#     # 对列表中的每个字典按照指定的顺序排序
#     sorted_list_of_dicts = [dict(sorted(d.items(), key=sort_key)) for d in list_of_dicts]
#     return sorted_list_of_dicts
#
#
# # 使用函数进行排序
# sorted_list = sort_list_of_dicts(list_of_dicts)
#
# # 打印排序后的列表
# for item in sorted_list:
#     print(item)
