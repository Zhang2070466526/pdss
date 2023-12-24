


# import arrow
#
# ar = arrow.get('2023-02-03','YYYY-MM-DD')
# print(ar,type(ar))
# date_object = ar.date()
# print(type(date_object),date_object)
# a=date_object.replace(day=1)
# print(a,type(a))




# 第一组数据：部门、类别和满意度为空值数量的信息
data1 = [{'department': '全球战略供应链管理中心', 'category': '知识类', 'count_null_Satisfaction': 0},
         {'department': '全球战略供应链管理中心', 'category': '技能类', 'count_null_Satisfaction': 0},
         {'department': '全球战略供应链管理中心', 'category': '态度类', 'count_null_Satisfaction': 0},
         # ... (其他数据)
        ]

# 第二组数据：部门、类别以及不同类别下的具体评价情况
data2 = [{'department': '全球战略供应链管理中心', 'category': '知识类', 'content_number_中层': '0', 'content_number_基层': '0'},
         {'department': '全球战略供应链管理中心', 'category': '技能类', 'content_number_中层': '0', 'content_number_基层': '0'},
         {'department': '全球战略供应链管理中心', 'category': '态度类', 'content_number_中层': '0', 'content_number_基层': '0'},

        ]

# merged_data = []

# Create a dictionary to store merged data using unique keys formed by 'department' and 'category'
merged_dict = {}

# Merge data1 into the merged_dict
for item in data1:
    key = (item['department'], item['category'])
    merged_dict[key] = item

# Merge data2 into the merged_dict
for item in data2:
    key = (item['department'], item['category'])
    if key in merged_dict:
        merged_dict[key].update(item)
    else:
        merged_dict[key] = item

# Convert the merged_dict values back to a list to get the final merged_data
merged_data = list(merged_dict.values())

print(merged_data)