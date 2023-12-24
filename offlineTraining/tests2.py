# import json
#
# # data = {'id': 26, 'content_lecturer': 51, 'content_part__department_first_name': '光伏研究院', 'content_part__department_second_name': '电池研究中心', 'content_module': '电池研发线', 'content_group': '', 'content_title': '我', 'content_type_id': 1, 'content_category_id': 1, 'content_level_id': 1, 'content_manner': '现场', 'content_begin_date': '2023-08-23T00:00:00', 'content_end_date': '2023-08-25T00:00:00', 'content_duration': '48.0', 'content_object': '111', 'content_people_number': '11', 'content_lecturer__lecturer_type': '内部讲师', 'content_lecturer__lecturer_people__employee_name': '朱彦斌', 'content_lecturer__lecturer_people__employee_code': '2020000153', 'content_lecturer__lecturer_people__employee_position__position_name': '代理副总经理', 'content_lecturer__lecturer_level_id': 1, 'content_satisfaction': '1', 'content_expenses': '1', 'content_plan': '计划外'}
# #
# #
# # json_data = json.dumps(data, indent=4)  # Convert dictionary to JSON string with indentation
# # print(json_data)
#
#
# # data =[
# #             {
# #                 "department": "全球战略供应链管理中心",
# #                 "category": "知识类",
# #                 "count_null_Satisfaction": 0,
# #                 "content_number_中层": "0",
# #                 "content_number_基层": "0",
# #                 "content_number_综合": "0",
# #                 "content_number_高层": "0",
# #                 "content_people_number": 0.0,
# #                 "content_duration": 0.0,
# #                 "content_satisfaction": 0.0,
# #                 "content_satisfaction_avg": 0.0,
# #                 "content_number_Total": "0"
# #             },
# #             {
# #                 "department": "全球战略供应链管理中心",
# #                 "category": "技能类",
# #                 "count_null_Satisfaction": 0,
# #                 "content_number_中层": "2",
# #                 "content_number_基层": "0",
# #                 "content_number_综合": "0",
# #                 "content_number_高层": "0",
# #                 "content_people_number": 12.0,
# #                 "content_duration": 4.0,
# #                 "content_satisfaction": 110.0,
# #                 "content_satisfaction_avg": 9.166666666666666,
# #                 "content_number_Total": "2"
# #             },
# #             {
# #                 "department": "全球战略供应链管理中心",
# #                 "category": "态度类",
# #                 "count_null_Satisfaction": 0,
# #                 "content_number_中层": "0",
# #                 "content_number_基层": "0",
# #                 "content_number_综合": "0",
# #                 "content_number_高层": "0",
# #                 "content_people_number": 0.0,
# #                 "content_duration": 0.0,
# #                 "content_satisfaction": 0.0,
# #                 "content_satisfaction_avg": 0.0,
# #                 "content_number_Total": "0"
# #             }]
# # # 创建一个字典用于存储求和结果
# # sum_data = {
# #     "department": "全球战略供应链管理中心",
# #     "category": "合计",
# #     "count_null_Satisfaction": 0,
# #     "content_number_中层": 0,
# #     "content_number_基层": 0,
# #     "content_number_综合": 0,
# #     "content_number_高层": 0,
# #     "content_people_number": 0,
# #     "content_duration": 0,
# #     "content_satisfaction": 0,
# #     "content_satisfaction_avg": 0,
# #     "content_number_Total": 0
# # }
#
#
#
#
# # data=[{'department': '全球战略供应链管理中心', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '全球战略供应链管理中心', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '全球战略供应链管理中心', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '全球组件营销中心', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '全球组件营销中心', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '全球组件营销中心', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '光伏研究院', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '光伏研究院', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '光伏研究院', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '集团质量中心', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '集团质量中心', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '集团质量中心', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '全球财务中心', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '全球财务中心', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '全球财务中心', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '工程事业部', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '工程事业部', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '工程事业部', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '电池事业二部', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '电池事业二部', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '电池事业二部', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '电池事业一部', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '电池事业一部', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '电池事业一部', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '人力资源中心', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '人力资源中心', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '人力资源中心', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '全球电池营销中心', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '全球电池营销中心', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '全球电池营销中心', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '组件事业部', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '组件事业部', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '组件事业部', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '硅料事业部', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '硅料事业部', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '硅料事业部', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '战略与运营管理中心', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '战略与运营管理中心', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '战略与运营管理中心', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '电站事业部', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '电站事业部', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '电站事业部', 'category': '态度类', 'count_null_Satisfaction': 0}, {'department': '润阳越南项目', 'category': '知识类', 'count_null_Satisfaction': 0}, {'department': '润阳越南项目', 'category': '技能类', 'count_null_Satisfaction': 0}, {'department': '润阳越南项目', 'category': '态度类', 'count_null_Satisfaction': 0}]
# #
# # department_category_sums = {}
# #
# # # Calculate sums
# # for entry in data:
# #     department = entry['department']
# #     category = entry['category']
# #     count = entry['count_null_Satisfaction']
# #
# #     if department not in department_category_sums:
# #         department_category_sums[department] = {}
# #
# #     if category not in department_category_sums[department]:
# #         department_category_sums[department][category] = count
# #     else:
# #         department_category_sums[department][category] += count
# #
# # # Add a "Total" category for each department
# # for department, categories in department_category_sums.items():
# #     total_count = sum(categories.values())
# #     categories['Total'] = total_count
# #
# # # Convert the dictionary back to a list of dictionaries
# # result = []
# # for department, categories in department_category_sums.items():
# #     for category, count in categories.items():
# #         result.append({'department': department, 'category': category, 'count_null_Satisfaction_Total': count})
# #
# # print(result)
#
#
#
#
#
#
#
#
#
# data = [
#   {
#     'department': '全球战略供应链管理中心',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球战略供应链管理中心',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 2,
#     'content_people_number': 12.0,
#     'content_duration': 4.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '2',
#     'content_number_middle': '2',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球战略供应链管理中心',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球战略供应链管理中心',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 2,
#     'content_people_number': 12.0,
#     'content_duration': 4.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '2',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球组件营销中心',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球组件营销中心',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球组件营销中心',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球组件营销中心',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },{
#     'department': '光伏研究院',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 2,
#     'content_people_number': 22.0,
#     'content_duration': 35.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '2',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '2',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '光伏研究院',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 1,
#     'content_people_number': 1.0,
#     'content_duration': 1.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '1',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '1'
#   },
#   {
#     'department': '光伏研究院',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 1,
#     'content_people_number': 1234.0,
#     'content_duration': 1.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '1',
#     'content_number_middle': '1',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '光伏研究院',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 4,
#     'content_people_number': 1257.0,
#     'content_duration': 37.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '4',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },{
#     'department': '集团质量中心',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 1,
#     'content_people_number': 111.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '1',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '1',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '集团质量中心',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '集团质量中心',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '集团质量中心',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 1,
#     'content_people_number': 111.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '1',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球财务中心',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球财务中心',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球财务中心',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球财务中心',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '工程事业部',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '工程事业部',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '工程事业部',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '工程事业部',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '电池事业二部',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '电池事业二部',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '电池事业二部',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '电池事业二部',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   }, {
#     'department': '电池事业一部',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '电池事业一部',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '电池事业一部',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '电池事业一部',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '人力资源中心',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '人力资源中心',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '人力资源中心',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '人力资源中心',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球电池营销中心',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球电池营销中心',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球电池营销中心',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '全球电池营销中心',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '组件事业部',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '组件事业部',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '组件事业部',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '组件事业部',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '硅料事业部',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '硅料事业部',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '硅料事业部',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '硅料事业部',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   }, {
#     'department': '战略与运营管理中心',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '战略与运营管理中心',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '战略与运营管理中心',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '战略与运营管理中心',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '电站事业部',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '电站事业部',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '电站事业部',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '电站事业部',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '润阳越南项目',
#     'category': '知识类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '润阳越南项目',
#     'category': '技能类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '润阳越南项目',
#     'category': '态度类',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': '润阳越南项目',
#     'category': 'Total',
#     'count_null_Satisfaction_Total': 0,
#     'content_people_number': 0.0,
#     'content_duration': 0.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '0',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   },
#   {
#     'department': 'Total',
#     'category': 'Total',
#     'content_people_number': 1380.0,
#     'content_duration': 41.0,
#     'content_satisfaction': 0.0,
#     'content_satisfaction_avg': 0.0,
#     'content_number_Total': '7',
#     'content_number_middle': '0',
#     'content_number_grass': '0',
#     'content_number_synthesis': '0',
#     'content_number_senior': '0'
#   }
# ]
# middle_sum_by_department = {}
# grass_sum_by_department = {}
# synthesis_sum_by_department = {}
# senior_sum_by_department = {}
#
#
# for d in data:
#     if d['category'] != 'Total':
#         if d['department'] not in middle_sum_by_department:
#             middle_sum_by_department[d['department']] = 0
#             grass_sum_by_department[d['department']] = 0
#             synthesis_sum_by_department[d['department']] = 0
#             senior_sum_by_department[d['department']] = 0
#         middle_sum_by_department[d['department']] += int(d['content_number_middle'])
#         grass_sum_by_department[d['department']] += int(d['content_number_grass'])
#         synthesis_sum_by_department[d['department']] += int(d['content_number_synthesis'])
#         senior_sum_by_department[d['department']] += int(d['content_number_senior'])
#     else:
#         d['content_number_middle'] = '0'
#         d['content_number_grass'] = '0'
#         d['content_number_synthesis'] = '0'
#         d['content_number_senior'] = '0'
#
# for d in data:
#     if d['category'] == 'Total':
#         d['content_number_middle'] = str(middle_sum_by_department[d['department']])
#         d['content_number_grass'] = str(grass_sum_by_department[d['department']])
#         d['content_number_synthesis'] = str(synthesis_sum_by_department[d['department']])
#         d['content_number_senior'] = str(senior_sum_by_department[d['department']])
#
#
#
# print(data)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


month = self.request.GET.get('month', None)
print('month', month)
# kwargs = {}
# if month != "":
#     kwargs['sessions_record_time'] = month


columnList = [
    {'value': '润阳集团', 'children': [
        {'label': 'department', 'value': '基地', 'width': 160}]
     },
    {'label': 'category', 'value': '类别', 'width': ''},
    {'value': '培训层级(场次)', 'children': [
        {'label': 'content_number_middle', 'value': '中层', 'width': 130},
        {'label': 'content_number_grass', 'value': '基层', 'width': 130},
        {'label': 'content_number_synthesis', 'value': '综合', 'width': 130},
        {'label': 'content_number_senior', 'value': '高层', 'width': 130},
    ]},
    {'value': '总分析', 'children': [
        {'label': 'content_number_Total', 'value': '场次', 'width': 130},
        {'label': 'content_people_number', 'value': '人次', 'width': 130},
        {'label': 'content_duration', 'value': '总时长(H)', 'width': 130},
        {'label': 'content_satisfaction', 'value': '平均满意度', 'width': 130},
        {'label': 'content_satisfaction_avg', 'value': '已评分平均满意度', 'width': 130},
        {'label': 'count_null_Satisfaction_Total', 'value': '未评分场次', 'width': 130},
    ]},
]

# from django.db.models import Count
#
# # 查询每个基地、每个培训类别和每个培训层级的培训场次数量
# base_category_level_counts = TrainingContent.objects.values('content_part__department_first_name', 'content_category__category_name', 'content_level__level_name').annotate(count=Count('id'))
#
# # 打印查询结果
# for entry in base_category_level_counts:
#     base_id = entry['content_part__department_first_name']
#     category_id = entry['content_category__category_name']
#     level_id = entry['content_level__level_name']
#     count = entry['count']
#     print(base_id,category_id,level_id,count)
#
#     # base_name = YourBaseModel.objects.get(pk=base_id).base_name  # 假设您的基地模型中有一个 base_name 字段
#     # category_name = YourCategoryModel.objects.get(
#     #     pk=category_id).category_name  # 假设您的培训类别模型中有一个 category_name 字段
#     # level_name = YourLevelModel.objects.get(pk=level_id).level_name  # 假设您的培训层级模型中有一个 level_name 字段
#     #
#     # print(f"基地：{base_name}，培训类别：{category_name}，培训层级：{level_name}，培训场次数量：{count}")


# from django.db.models import Count, F
# from django.db.models.functions import Coalesce
#
# # 生成基地、培训类别和培训层级的所有组合
# base_category_level_combinations = HrDepartment.objects.all().values('department_first_name') \
#     .cross_join(TrainingContentCategory.objects.all()) \
#     .cross_join(TrainingContentLevel.objects.all())
#
# # 使用 annotate() 和 Coalesce() 来计算培训场次数量，没有数据的情况下置为 0
# result = base_category_level_combinations.annotate(
#     count=Coalesce(Count('trainingcontent', filter=Q(trainingcontent__content_part=F('id') &
#                                                                                    Q(trainingcontent__content_category=F(
#                                                                                        'trainingcontentcategory__id')) &
#                                                                                    Q(trainingcontent__content_level=F(
#                                                                                        'trainingcontentlevel__id')))),
#                    0)
# )
#
# # 打印结果
# for entry in result:
#     base_name = entry['department_first_name']
#     category_name = entry['trainingcontentcategory__category_name']
#     level_name = entry['trainingcontentlevel__level_name']
#     count = entry['count']
#
#     print(f"基地：{base_name}，培训类别：{category_name}，培训层级：{level_name}，培训场次数量：{count}")

















# from django.db import connection
#
# # 构建 SQL 查询语句
# sql_query = """
#            SELECT
#                IFNULL(dc.department_first_name, 'Total') AS base_name,
#                IFNULL(cat.category_name, 'Total') AS category_name,
#                IFNULL(lvl.level_name, 'Total') AS level_name,
#                COALESCE(COUNT(tc.id), 0) AS count,
#                COALESCE(SUM(tc.content_people_number), 0) AS total_people,
#                COALESCE(SUM(tc.content_duration), 0) AS total_duration,
#                COALESCE(SUM(tc.content_satisfaction), 0) AS total_satisfaction,
#                CASE WHEN SUM(tc.content_people_number) > 0 THEN
#                    COALESCE(SUM(tc.content_satisfaction) / SUM(tc.content_people_number), 0)
#                ELSE
#                    0
#                END AS avg_satisfaction
#            FROM (
#                SELECT id, department_first_name
#                FROM hr_department
#                WHERE department_first_name IS NOT NULL
#                  AND (department_expiry_date IS NULL OR department_expiry_date >= NOW())
#            ) dc
#            CROSS JOIN
#                training_content_category cat
#            CROSS JOIN
#                training_content_level lvl
#            LEFT JOIN (
#                SELECT *
#                FROM training_content
#                WHERE content_end_date >= DATE_FORMAT(NOW(), '%Y-%m-01 00:00:00')
#                      AND content_end_date <= LAST_DAY(NOW()) + INTERVAL 1 DAY - INTERVAL 1 SECOND
#            ) tc ON tc.content_part_id = dc.id
#                  AND tc.content_category_id = cat.id
#                  AND tc.content_level_id = lvl.id
#            GROUP BY
#                dc.department_first_name, cat.category_name, lvl.level_name
#            WITH ROLLUP;
#
#        """
#
# # 执行 SQL 查询
# with connection.cursor() as cursor:
#     cursor.execute(sql_query)
#     # print(cursor)
#     result = cursor.fetchall()
# # print(result)
# tableData = []
# # result = []
#
# for entry in result:
#     department, category, level, content_number, content_people_number, content_duration, content_satisfaction, content_satisfaction_avg = entry
#     tableData.append({
#         "department": department,
#         "category": category,
#         "level": level,
#         "content_number": str(content_number),
#         "content_people_number": float(content_people_number),
#         "content_duration": float(content_duration),
#         "content_satisfaction": float(content_satisfaction),
#         "content_satisfaction_avg": float(content_satisfaction_avg)
#     })
# # print(tableData)
#
# original_list = tableData
#
# transformed_list = []
#
# # Create a dictionary to store the transformed data
# department_category_data = {}
#
# # print('original',original_list)
#
# # Process each item in the original list
# for item in original_list:
#     department = item['department']
#     category = item['category']
#     level = item['level']
#     content_number = item['content_number']
#
#     if department not in department_category_data:
#         department_category_data[department] = {}
#
#     if category not in department_category_data[department]:
#         department_category_data[department][category] = {
#             'department': department,
#             'category': category,
#             'content_number_中层': '0',
#             'content_number_基层': '0',
#             'content_number_综合': '0',
#             'content_number_高层': '0',
#             'content_people_number': 0.0,
#             'content_duration': 0.0,
#             'content_satisfaction': 0.0,
#             'content_satisfaction_avg': 0.0
#         }
#
#     department_category_data[department][category]['content_number_' + level] = content_number
#     department_category_data[department][category]['content_people_number'] = item['content_people_number']
#     department_category_data[department][category]['content_duration'] = item['content_duration']
#     department_category_data[department][category]['content_satisfaction'] = item['content_satisfaction']
#     department_category_data[department][category]['content_satisfaction_avg'] = item[
#         'content_satisfaction_avg']
#
# # Convert the department_category_data dictionary back to a list
# # print('original2',original_list)
# for department_data in department_category_data.values():
#     transformed_list.extend(department_data.values())
#
# print('tran', transformed_list)
# for item in transformed_list:
#     item['content_number_middle'] = item.pop('content_number_中层', '0')
#     item['content_number_grass'] = item.pop('content_number_基层', '0')
#     item['content_number_synthesis'] = item.pop('content_number_综合', '0')
#     item['content_number_senior'] = item.pop('content_number_高层', '0')
#
# # print(data)
# # tableList=transformed_list
# # print(tableList)
#
# # from django.db.models import Count
# #
# # result = TrainingContent.objects.filter(content_satisfaction__isnull=True).values(
# #     'content_part__department_first_name', 'content_category'
# # ).annotate(num_sessions=Count('id'))
# #
# # for item in result:
# #     department_name = item['content_part__department_first_name']
# #     category = item['content_category']
# #     num_sessions = item['num_sessions']
# #     print(
# #         f"Department: {department_name}, Category: {category}, Num Sessions with Null Satisfaction: {num_sessions}")
#
# # tableList=transformed_list
#
#
# # from django.db.models import Count, Q
# # from django.utils import timezone
# # from datetime import datetime
# #
# # # Get the first and last day of the current month
# # now = timezone.now()
# # first_day = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
# # last_day = (first_day + timezone.timedelta(days=32)).replace(day=1) - timezone.timedelta(seconds=1)
# #
# # # Construct the query
# # training_sessions = TrainingContent.objects.filter(
# #         ~Q(id=999999),
# #         Q(content_part__department_expiry_date__isnull=True) | Q(content_part__department_expiry_date__gt=datetime.now()),
# #         content_part__department_first_name__isnull=False,
# #         content_part__department_status=1,
# #         content_status=True,    content_begin_date__range=(first_day, last_day),
# #         content_end_date__range=(first_day, last_day),
# # ).annotate(
# #     department_name=models.F('content_part__department_first_name'),
# #     category_name=models.F('content_category__category_name'),
# #     level_name=models.F('content_level__level_name')
# # ).values(
# #     'department_name',
# #     'category_name',
# #     'level_name'
# # ).annotate(
# #     session_count=Count('id')
# # ).order_by(
# #     'department_name',
# #     'category_name',
# #     'level_name'
# # )
# #
# # # Display the results
# # for session in training_sessions:
# #     print(
# #         f"Department: {session['department_name']}, "
# #         f"Category: {session['category_name']}, "
# #         f"Level: {session['level_name']}, "
# #         f"Session Count: {session['session_count']}"
# #     )
#
# from django.db.models import Count
# from itertools import product
#
# # 获取所有可能的部门和类别组合
# all_departments = HrDepartment.objects.filter(
#     Q(department_expiry_date__isnull=True) | Q(department_expiry_date__gt=datetime.now()),
#     department_first_name__isnull=False,
#     department_status=1).exclude(id=999999).values_list('department_first_name', flat=True).distinct()
# all_categories = TrainingContentCategory.objects.exclude(id=999999).values_list('category_name', flat=True)
#
# # 查询并统计满意度为空的场次数量
# result = TrainingContent.objects.filter(content_satisfaction__isnull=True).values(
#     'content_part__department_first_name', 'content_category__category_name'
# ).annotate(num_sessions=Count('id'))
#
# # 生成所有可能的部门和类别组合的字典
# department_category_combinations = list(product(all_departments, all_categories))
# department_category_dict = {(department, category): 0 for department, category in
#                             department_category_combinations}
#
# # 更新字典中的数量信息
# for item in result:
#     department_name = item['content_part__department_first_name']
#     category = item['content_category__category_name']
#     num_sessions = item['num_sessions']
#     department_category_dict[(department_name, category)] = num_sessions
#
# # 生成包含信息的列表
# result_list = []
# for department, category in department_category_combinations:
#     num_sessions = department_category_dict[(department, category)]
#     result_list.append(
#         {'department': department, 'category': category, 'count_null_Satisfaction': num_sessions})
#
# # 打印结果列表
# # for item in result_list:
# #     print(item)
# # print(result_list)  #空满意度
# department_category_sums = {}
# for entry in result_list:
#     department = entry['department']
#     category = entry['category']
#     count = entry['count_null_Satisfaction']
#
#     if department not in department_category_sums:
#         department_category_sums[department] = {}
#
#     if category not in department_category_sums[department]:
#         department_category_sums[department][category] = count
#     else:
#         department_category_sums[department][category] += count
# for department, categories in department_category_sums.items():
#     total_count = sum(categories.values())
#     categories['Total'] = total_count
# result = []
# for department, categories in department_category_sums.items():
#     for category, count in categories.items():
#         result.append({'department': department, 'category': category, 'count_null_Satisfaction_Total': count})
#
# # print('1',result)
# # print('2',transformed_list)
#
# merged_dict = {}
# # Merge data1 into the merged_dict
# for item in result:
#     key = (item['department'], item['category'])
#     merged_dict[key] = item
#
# # Merge data2 into the merged_dict
# for item in transformed_list:
#     key = (item['department'], item['category'])
#     if key in merged_dict:
#         merged_dict[key].update(item)
#     else:
#         merged_dict[key] = item
#
# # Convert the merged_dict values back to a list to get the final merged_data
# tableList = list(merged_dict.values())[:-1]
# # print(tableList)
# # print(tableList)
# # for line in tableList:
# #     print(line)
#
# middle_sum_by_department = {}
# grass_sum_by_department = {}
# synthesis_sum_by_department = {}
# senior_sum_by_department = {}
#
# for d in tableList:
#     if d['category'] != 'Total':
#         if d['department'] not in middle_sum_by_department:
#             middle_sum_by_department[d['department']] = 0
#             grass_sum_by_department[d['department']] = 0
#             synthesis_sum_by_department[d['department']] = 0
#             senior_sum_by_department[d['department']] = 0
#         middle_sum_by_department[d['department']] += int(d['content_number_middle'])
#         grass_sum_by_department[d['department']] += int(d['content_number_grass'])
#         synthesis_sum_by_department[d['department']] += int(d['content_number_synthesis'])
#         senior_sum_by_department[d['department']] += int(d['content_number_senior'])
#     else:
#         d['content_number_middle'] = '0'
#         d['content_number_grass'] = '0'
#         d['content_number_synthesis'] = '0'
#         d['content_number_senior'] = '0'
#
# for d in tableList:
#     if d['category'] == 'Total':
#         d['content_number_middle'] = str(middle_sum_by_department[d['department']])
#         d['content_number_grass'] = str(grass_sum_by_department[d['department']])
#         d['content_number_synthesis'] = str(synthesis_sum_by_department[d['department']])
#         d['content_number_senior'] = str(senior_sum_by_department[d['department']])
#
# # tableList=transformed_list
# self.return_data = {
#     'code': 200,
#     'msg': '信息返回成功',
#     'data': {
#         'columnList': columnList,
#         'tableList': tableList,
#     }
# }
# # print(self.return_data)
