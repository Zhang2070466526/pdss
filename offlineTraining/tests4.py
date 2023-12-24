# def add_index(tree, start_index=1):
#     for node in tree:
#         node['index'] = start_index
#         start_index += 1
#         if 'children' in node:
#             start_index = add_index(node['children'], start_index)
#     return start_index
#
# data = [
#     {
#         'id': '1',
#         'type_name': '公司级培训',
#         'type_parent_id': None,
#         'value': '1'
#     },
#     {
#         'id': '2',
#         'type_name': '部门内训',
#         'type_parent_id': None,
#         'value': '2',
#         'children': [
#             {
#                 'id': '8',
#                 'type_name': '潜龙计划',
#                 'type_parent_id': 2,
#                 'value': '8'
#             }
#         ]
#     },
#     {
#         'id': '3',
#         'type_name': '集团培训',
#         'type_parent_id': None,
#         'value': '3',
#         'children': [
#             {
#                 'id': '5',
#                 'type_name': '飞龙计划',
#                 'type_parent_id': 3,
#                 'value': '5',
#                 'children': [
#                     {
#                         'id': '6',
#                         'type_name': '白银计划',
#                         'type_parent_id': 5,
#                         'value': '6'
#                     },
#                     {
#                         'id': '7',
#                         'type_name': '黄金计划',
#                         'type_parent_id': 5,
#                         'value': '7'
#                     }
#                 ]
#             }
#         ]
#     },
#     {
#         'id': '4',
#         'type_name': '外出培训',
#         'type_parent_id': None,
#         'value': '4'
#     }
# ]
#
# add_index(data)
# print(data)

# a = [1, 2, 3]
# b, c, d = a
# print(b, c, d)  # 输出：1 2 3
#
# a = [1, 2]
# b, c, d = a
# print(b, c, d)  # 输出：1 2 None
#
# a = [1]
# b, c, d = a
# print(b, c, d)  # 输出：1 None None


#
# data = [
#   {
#     'index': 1,
#     'department_name': 'C2设备部',
#     'content_part__department_first_name': '电池事业一部',
#     'content_part__department_second_name': '江苏润阳世纪光伏科技有限公司',
#     'content_part__department_third_name': 'C2设备部',
#     'content_duration': 0.5,
#     'content_people_number': 31.0,
#     'total_training_hours': 15.5,
#     'code': 'SEF200'
#   },
#   {
#     'index': 2,
#     'department_name': 'P2生产部',
#     'content_part__department_first_name': '电池事业二部',
#     'content_part__department_second_name': '江苏润阳悦达光伏科技有限公司',
#     'content_part__department_third_name': 'P2生产部',
#     'content_duration': 2.0,
#     'content_people_number': 93.0,
#     'total_training_hours': 186.0,
#     'code': 'YPD200'
#   },
#   {
#     'index': 3,
#     'department_name': '电气车间',
#     'content_part__department_first_name': '硅料事业部',
#     'content_part__department_second_name': '宁夏润阳硅材料科技有限公司',
#     'content_part__department_third_name': '机动部',
#     'content_duration': 0.5,
#     'content_people_number': 36.0,
#     'total_training_hours': 18.0,
#     'code': 'GEF120'
#   }
# ]
#
# # 使用列表推导筛选出符合条件的键值对
# filtered_data = [item for item in data if item['content_part__department_first_name'] == '硅料事业部']
#
# # 输出筛选结果
# print(filtered_data)
#




# data = [
#     {'content_part__department_first_name': '人力资源中心', 'content_category__category_name': None},
#     {'content_part__department_first_name': '人力资源中心', 'content_category__category_name': '知识类'},
#     {'content_part__department_first_name': '人力资源中心', 'content_category__category_name': '技能类'},
#     {'content_part__department_first_name': '光伏研究院', 'content_category__category_name': '知识类'},
#     {'content_part__department_first_name': '全球财务中心', 'content_category__category_name': '技能类'},
#     # Add more data as needed
# ]
#
# # Initialize a dictionary to store the counts
# department_category_counts = {}
#
# # Loop through the data and update the counts
# for item in data:
#     department_name = item['content_part__department_first_name']
#     category_name = item['content_category__category_name']
#
#     # If the department is not in the dictionary, initialize it
#     if department_name not in department_category_counts:
#         department_category_counts[department_name] = {}
#
#     # If the category is not in the department's dictionary, initialize it
#     if category_name not in department_category_counts[department_name]:
#         department_category_counts[department_name][category_name] = 0
#
#     # Increment the count for the category
#     department_category_counts[department_name][category_name] += 1
#
# # Print the results
# for department, category_counts in department_category_counts.items():
#     print(f"Department: {department}")
#     for category, count in category_counts.items():
#         print(f"  Category: {category if category else 'N/A'} - Count: {count}")


# data = [
#     {
#         'department': '光伏研究院',
#         'category': '知识类',
#         'content_number_senior': 0,
#         'content_number_middle': 0,
#         'content_number_grass': 0,
#         'content_number_synthesis': 0,
#         'content_number_Total': 0,
#     },
#     {
#         'department': '光伏研究院',
#         'category': '技能类',
#         'content_number_senior': 0,
#         'content_number_middle': 0,
#         'content_number_grass': 0,
#         'content_number_synthesis': 1,
#         'content_number_Total': 1,
#     },
#     {
#         'department': '光伏研究院',
#         'category': '态度类',
#         'content_number_senior': 0,
#         'content_number_middle': 0,
#         'content_number_grass': 0,
#         'content_number_synthesis': 0,
#         'content_number_Total': 0,
#     },
#     {
#         'department': '全球财务中心',
#         'category': '知识类',
#         'content_number_senior': 0,
#         'content_number_middle': 0,
#         'content_number_grass': 0,
#         'content_number_synthesis': 0,
#         'content_number_Total': 0,
#     },
#     {
#         'department': '全球财务中心',
#         'category': '技能类',
#         'content_number_senior': 0,
#         'content_number_middle': 0,
#         'content_number_grass': 0,
#         'content_number_synthesis': 0,
#         'content_number_Total': 0,
#     },
#     {
#         'department': '全球财务中心',
#         'category': '态度类',
#         'content_number_senior': 0,
#         'content_number_middle': 0,
#         'content_number_grass': 0,
#         'content_number_synthesis': 0,
#         'content_number_Total': 0,
#     },
# ]
#
# # 创建一个字典来存储每个部门的合计值
# department_totals = {}
#
# # 遍历数据列表，计算每个部门的合计值
# for item in data:
#     department = item['department']
#     category = item['category']
#     senior = item['content_number_senior']
#     middle = item['content_number_middle']
#     grass = item['content_number_grass']
#     synthesis = item['content_number_synthesis']
#
#     # 检查部门是否已经在department_totals中
#     if department in department_totals:
#         department_totals[department]['content_number_senior'] += senior
#         department_totals[department]['content_number_middle'] += middle
#         department_totals[department]['content_number_grass'] += grass
#         department_totals[department]['content_number_synthesis'] += synthesis
#         department_totals[department]['content_number_Total'] += (senior + middle + grass + synthesis)
#     else:
#         # 如果部门不在department_totals中，则创建一个新的条目
#         department_totals[department] = {
#             'department': department,
#             'category': '合计',
#             'content_number_senior': senior,
#             'content_number_middle': middle,
#             'content_number_grass': grass,
#             'content_number_synthesis': synthesis,
#             'content_number_Total': senior + middle + grass + synthesis,
#         }
#
# # 将部门合计数据添加到原始数据列表
# data += list(department_totals.values())
#
# # 打印更新后的数据列表
# for item in data:
#     print(item)


data = [
  {
    'department': '云南润阳世纪光伏科技有限公司',
    'category': '知识类',
    'content_number_senior': 0,
    'content_number_middle': 0,
  },
  {
    'department': '云南润阳世纪光伏科技有限公司',
    'category': '技能类',
    'content_number_senior': 0,
    'content_number_middle': 0,
  },
  {
    'department': '云南润阳世纪光伏科技有限公司',
    'category': '态度类',
    'content_number_senior': 0,
    'content_number_middle': 0,
  },
  {
    'department': '云南润阳世纪光伏科技有限公司',
    'category': '合计',
    'content_number_senior': 0,
    'content_number_middle': 0,
  },

  {
    'department': '人力资源中心',
    'category': '知识类',
    'content_number_senior': 0,
    'content_number_middle': 0,
  },
  {
    'department': '人力资源中心',
    'category': '技能类',
    'content_number_senior': 0,
    'content_number_middle': 0,
  },
  {
    'department': '人力资源中心',
    'category': '态度类',
    'content_number_senior': 1,
    'content_number_middle': 0,
  },

  {
    'department': '人力资源中心',
    'category': '合计',
    'content_number_senior': 2,
    'content_number_middle': 0,
  },
]
#
# # 找出所有部门的唯一列表
# departments = set(item['department'] for item in data)
# # 自动生成"润阳集团"部门的键值对
# runyang_group_data = []
# for category in set(item['category'] for item in data if item['category'] != '合计'):
#     senior_total = sum(item['content_number_senior'] for item in data if item['category'] == category)
#     runyang_group_data.append({
#         'department': '润阳集团',
#         'category': category,
#         'content_number_senior': senior_total,
#         'content_number_middle': 0,  # 设置中级内容的初始值
#     })
#
# # 将"润阳集团"部门的数据添加到原有数据中
# data.extend(runyang_group_data)
#
# # 创建字典用于存储合计值
# department_totals = {}
#
# # 遍历数据并计算合计值
# for item in data:
#     department = item['department']
#     category = item['category']
#     senior = item['content_number_senior']
#
#     # 忽略'合计'项，因为它是自动计算的
#     if category != '合计':
#         if department in department_totals:
#             department_totals[department][category] = department_totals[department].get(category, 0) + senior
#         else:
#             department_totals[department] = {category: senior}
#
# # 更新数据中的'合计'项
# for item in data:
#     if item['category'] == '合计':
#         department = item['department']
#         item['content_number_senior'] = sum(department_totals[department].values())
#
# # 打印更新后的数据
# for item in data:
#     print(item)
# #
# # my_list = [1, 2, 3, 4, 5]  # 一个示例列表
# # data_to_insert = [6, 7, 8]  # 要插入的数组
# # my_list[:0] = data_to_insert  # 使用切片和extend()方法将数组中的项插入到列表的索引0处
# # print(my_list)
#
#
#
#
#

# # 找出所有不同的部门和类别
# departments = set(entry['department'] for entry in data)
# categories = set(entry['category'] for entry in data)
#
# # 创建润阳集团的字典数据
# runyang_group_data = []
# for category in categories:
#     senior_sum = sum(entry['content_number_senior'] for entry in data if entry['category'] == category)
#     middle_sum = sum(entry['content_number_middle'] for entry in data if entry['category'] == category)
#     runyang_group_data.append({
#         'department': '润阳集团',
#         'category': category,
#         'content_number_senior': senior_sum,
#         'content_number_middle': middle_sum,
#     })
#
# # 合并原始数据和润阳集团的数据
# data.extend(runyang_group_data)
#
# # 打印结果
# for entry in data:
#     print(entry)



# data = [
#     {'department': '润阳集团', 'category': '技能类'},
#     {'department': '润阳集团', 'category': '合计', 'content_number_senior': 1},
#     {'department': '润阳集团', 'category': '知识类'},
#     {'department': '润阳集团', 'category': '态度类'},
#     {'department': '云南润阳世纪光伏科技有限公司', 'category': '知识类'},
#     {'department': '云南润阳世纪光伏科技有限公司', 'category': '技能类', 'content_number_senior': 0},
#     {'department': '云南润阳世纪光伏科技有限公司', 'category': '态度类', 'content_number_senior': 0},
#     {'department': '云南润阳世纪光伏科技有限公司', 'category': '合计', 'content_number_senior': 0},
#     {'department': '人力资源中心', 'category': '知识类', 'content_number_senior': 0},
# ]
#
# # 将数据按照 'department' 和 'category' 字段进行排序
# sorted_data = sorted(data, key=lambda x: ('润阳集团' not in x['department'], x['department'], ['知识类', '技能类', '态度类', '合计'].index(x['category'])))
#
# # 打印排序后的结果
# for item in sorted_data:
#     print(item)

# # 定义部门顺序
# department_order = ['润阳集团', '云南润阳世纪光伏科技有限公司', '人力资源中心']
#
# # 定义类别顺序
# category_order = ['知识类', '技能类', '态度类', '合计']
#
# # 自定义排序函数
# def custom_sort(item):
#     return (department_order.index(item['department']), category_order.index(item['category']))
#
# # 对数据进行排序
# sorted_data = sorted(data, key=custom_sort)
#
# # 打印排序后的结果
# for item in sorted_data:
#     print(item)


# data = [
#     {'department': '润阳泰国四期组件',  'content_number_senior': 0, 'content_number_middle': 0,
#      'content_number_grass': 0, 'content_number_synthesis': 0, 'content_number_Total': 0,
#      'content_people_number_sum': 0, 'content_duration_sum': 0, 'content_satisfaction_avg': 0,'category': '态度类',
#      'content_satisfaction_None_count': 0, 'content_satisfaction_noNone_avg': 0},
#     {'department': '润阳泰国四期组件', 'category': '合计', 'content_number_senior': 0, 'content_number_middle': 0,
#      'content_number_grass': 0, 'content_number_synthesis': 0, 'content_number_Total': 0,
#      'content_people_number_sum': 0, 'content_duration_sum': 0, 'content_satisfaction_avg': 0,
#      'content_satisfaction_noNone_avg': 0, 'content_satisfaction_None_count': 0}
# ]
#
# sorted_data = sorted(a, key=lambda x: (
#     x['department'],
#     x['category'],
#     x['content_number_senior'],
#     x['content_number_middle'],
#     x['content_number_grass'],
#     x['content_number_synthesis'],
#     x['content_number_Total'],
#     x['content_people_number_sum'],
#     x['content_duration_sum'],
#     x['content_satisfaction_avg'],
#     x['content_satisfaction_noNone_avg'],
#     x['content_satisfaction_None_count']
# ))
#
# print(sorted_data)
# for i in sorted_data:
#     print(i)

# a = [
#     {'department': '润阳泰国四期组件',  'content_number_senior': 0, 'content_number_middle': 0,
#      'content_number_grass': 0, 'content_number_synthesis': 0, 'content_number_Total': 0,
#      'content_people_number_sum': 0, 'content_duration_sum': 0, 'content_satisfaction_avg': 0,'category': '态度类',
#      'content_satisfaction_None_count': 0, 'content_satisfaction_noNone_avg': 0},
#     {'department': '润阳泰国四期组件', 'category': '合计', 'content_number_senior': 0, 'content_number_middle': 0,
#      'content_number_grass': 0, 'content_number_synthesis': 0, 'content_number_Total': 0,
#      'content_people_number_sum': 0, 'content_duration_sum': 0, 'content_satisfaction_avg': 0,
#      'content_satisfaction_noNone_avg': 0, 'content_satisfaction_None_count': 0}
# ]
#
# sorted_a = sorted(a, key=lambda x: (
#     x['department'],
#     x['category'],
#     x['content_number_senior'],
#     x['content_number_middle'],
#     x['content_number_grass'],
#     x['content_number_synthesis'],
#     x['content_number_Total'],
#     x['content_people_number_sum'],
#     x['content_duration_sum'],
#     x['content_satisfaction_avg'],
#     x['content_satisfaction_noNone_avg'],
#     x['content_satisfaction_None_count']
# ))
#
# for item in sorted_a:
#     print(item)

# # 要排序的字典
# dictionary_to_sort = {
#     'department': '润阳泰国四期组件',
#     'content_number_senior': 0,
#     'content_number_middle': 0,
#     'content_number_grass': 0,
#     'content_number_synthesis': 0,
#     'content_number_Total': 0,
#     'content_people_number_sum': 0,
#     'content_duration_sum': 0,
#     'content_satisfaction_avg': 0,
#     'category': '态度类',
#     'content_satisfaction_None_count': 0,
#     'content_satisfaction_noNone_avg': 0
# }
# # 定义排序键函数，按照指定的顺序排序
# def custom_sort_key(dictionary):
#     return (
#     'department',
#     'category',
#     'content_number_senior',
#     'content_number_middle',
#     'content_number_grass',
#     'content_number_synthesis',
#     'content_number_Total',
#     'content_people_number_sum',
#     'content_duration_sum',
#     'content_satisfaction_avg',
#     'content_satisfaction_noNone_avg',
#     'content_satisfaction_None_count'
#     )
#
# # 对字典进行排序
# sorted_dictionary = sorted(dictionary_to_sort, key=custom_sort_key)
#
# print(sorted_dictionary)

# from collections import OrderedDict
#
# dictionary_to_sort = {
#     'department': '润阳泰国四期组件',
#     'content_number_senior': 0,
#     'content_number_middle': 0,
#     'content_number_grass': 0,
#     'content_number_synthesis': 0,
#     'content_number_Total': 0,
#     'content_people_number_sum': 0,
#     'content_duration_sum': 0,
#     'content_satisfaction_avg': 0,
#     'category': '态度类',
#     'content_satisfaction_None_count': 0,
#     'content_satisfaction_noNone_avg': 0
# }
#
# # 指定排序顺序
# order = [
#     'department',
#     'category',
#     'content_number_senior',
#     'content_number_middle',
#     'content_number_grass',
#     'content_number_synthesis',
#     'content_number_Total',
#     'content_people_number_sum',
#     'content_duration_sum',
#     'content_satisfaction_avg',
#     'content_satisfaction_noNone_avg',
#     'content_satisfaction_None_count'
# ]
#
# # 使用OrderedDict进行排序
# sorted_dict = OrderedDict((key, dictionary_to_sort[key]) for key in order)
#
# # 打印排序后的字典
# for key, value in sorted_dict.items():
#     print(f'{key}: {value}')


# list_of_dicts = [
#     {'department': '润阳泰国四期组件', 'content_number_senior': 0, 'content_number_middle': 0,
#      'content_number_grass': 0, 'content_number_synthesis': 0, 'content_number_Total': 0,
#      'content_people_number_sum': 0, 'content_duration_sum': 0, 'content_satisfaction_avg': 0, 'category': '态度类',
#      'content_satisfaction_None_count': 0, 'content_satisfaction_noNone_avg': 0},
#     {'department': '润阳泰国四期组件', 'category': '合计', 'content_number_senior': 0, 'content_number_middle': 0,
#      'content_number_grass': 0, 'content_number_synthesis': 0, 'content_number_Total': 0,
#      'content_people_number_sum': 0, 'content_duration_sum': 0, 'content_satisfaction_avg': 0,
#      'content_satisfaction_noNone_avg': 0, 'content_satisfaction_None_count': 0}
# ]
#
# # 指定排序顺序
# order = [
#     'department',
#     'category',
#     'content_number_senior',
#     'content_number_middle',
#     'content_number_grass',
#     'content_number_synthesis',
#     'content_number_Total',
#     'content_people_number_sum',
#     'content_duration_sum',
#     'content_satisfaction_avg',
#     'content_satisfaction_noNone_avg',
#     'content_satisfaction_None_count'
# ]
#
# # 对列表中的每个字典按照指定的顺序排序
# sorted_list_of_dicts = [dict(sorted(d.items(), key=lambda x: order.index(x[0]))) for d in list_of_dicts]
# print(sorted_list_of_dicts)
# # 打印排序后的列表中的每个字典
# for dictionary in sorted_list_of_dicts:
#     for key, value in dictionary.items():
#         print(f'{key}: {value}')
#     print()


def sort_list_of_dicts(list_of_dicts, order):
    """
    对列表中的字典按照指定的顺序排序。

    Args:
    list_of_dicts (list): 包含多个字典的列表。
    order (list): 指定排序顺序的键的列表。

    Returns:
    list: 排序后的列表中的字典。
    """
    # 对列表中的每个字典按照指定的顺序排序
    sorted_list_of_dicts = [dict(sorted(d.items(), key=lambda x: order.index(x[0]))) for d in list_of_dicts]
    return sorted_list_of_dicts


# 列表中的字典
list_of_dicts = [
    {'department': '润阳泰国四期组件', 'content_number_senior': 0, 'content_number_middle': 0,
     'content_number_grass': 0, 'content_number_synthesis': 0, 'content_number_Total': 0,
     'content_people_number_sum': 0, 'content_duration_sum': 0, 'content_satisfaction_avg': 0, 'category': '态度类',
     'content_satisfaction_None_count': 0, 'content_satisfaction_noNone_avg': 0},
    {'department': '润阳泰国四期组件', 'category': '合计', 'content_number_senior': 0, 'content_number_middle': 0,
     'content_number_grass': 0, 'content_number_synthesis': 0, 'content_number_Total': 0,
     'content_people_number_sum': 0, 'content_duration_sum': 0, 'content_satisfaction_avg': 0,
     'content_satisfaction_noNone_avg': 0, 'content_satisfaction_None_count': 0}
]

# 指定排序顺序
order = [
    'department',
    'category',
    'content_number_senior',
    'content_number_middle',
    'content_number_grass',
    'content_number_synthesis',
    'content_number_Total',
    'content_people_number_sum',
    'content_duration_sum',
    'content_satisfaction_avg',
    'content_satisfaction_noNone_avg',
    'content_satisfaction_None_count'
]

# 调用排序方法
sorted_list_of_dicts = sort_list_of_dicts(list_of_dicts, order)

# 打印排序后的结果
for dictionary in sorted_list_of_dicts:
    for key, value in dictionary.items():
        print(f'{key}: {value}')
    print()
