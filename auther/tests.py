# [{"nav_index": "1", "nav_name": "招聘", "nav_url": "/recruit", "nav_icon": "el-icon-user", "nav_component": "layout/index", "nav_parent_id": "None", "nav_type": 1, "permission": [], "children": [{"nav_index": "1-1", "nav_name": "DL", "nav_url": "/Dl", "nav_icon": " ", "nav_component": "views/recruit/Dl", "nav_parent_id": 44, "nav_type": 1, "permission": []}, {"nav_index": "1-2", "nav_name": "Idl", "nav_url": "/Idl", "nav_icon": " ", "nav_component": "views/recruit/Idl", "nav_parent_id": 44, "nav_type": 1, "permission": []}, {"nav_index": "1-3", "nav_name": "Sal", "nav_url": "/Sal", "nav_icon": " ", "nav_component": "views/recruit/Sal", "nav_parent_id": 44, "nav_type": 1, "permission": []}, {"nav_index": "1-4", "nav_name": "汇总", "nav_url": "/total", "nav_icon": " ", "nav_component": "views/recruit/Total", "nav_parent_id": 44, "nav_type": 1, "permission": []}]}, {"nav_index": "2", "nav_name": "薪资调研", "nav_url": "/salarySurvey", "nav_icon": "el-icon-s-finance", "nav_component": "layout/index", "nav_parent_id": "None", "nav_type": 1, "permission": [], "children": [{"nav_index": "2-1", "nav_name": "台账", "nav_url": "/record", "nav_icon": " ", "nav_component": "views/salarySurvey/Record", "nav_parent_id": 49, "nav_type": 1, "permission": ["add", "delete", "upload", "download", "edit"]}]}]



# data = [
#     {
#         'nav_index': None,
#         'nav_name': None,
#         'nav_url': None,
#         'nav_icon': None,
#         'nav_component': None,
#         'nav_parent_id': None,
#         'nav_type': None
#     },
#     {
#         'nav_index': '10',
#         'nav_name': '设置',
#         'nav_url': '/setup',
#         'nav_icon': 'el-icon-setting',
#         'nav_component': 'layout/index',
#         'nav_parent_id': None,
#         'nav_type': 1,
#         'children': [
#             # ...
#         ]
#     },
#     # ...
# ]
#
# # 使用列表解析删除所有值为 None 的字典
# filtered_data = [item for item in data if not all(value is None for value in item.values())]
#
# print(filtered_data)


# def transform_data(input_data):
#     result = []
#     parent_map = {}
#
#     for item in input_data:
#         nav_item = {
#             'nav_id': item['user_nav__id'],
#             'nav_index': item['user_nav__menu_index'],
#             'nav_name': item['user_nav__menu_name'],
#             'nav_url': item['user_nav__menu_path'],
#             'nav_icon': '',
#             'nav_component': 'layout/index',  # 根据需要设置默认值
#             'nav_parent_id': None,
#             'nav_type': item['user_nav__menu_type'],
#             'nav_level': item['user_nav__menu_level'],
#             'nav_category': item['user_nav__menu_category'],
#         }
#
#         parent_id = item['user_nav__menu_parent_id']
#         if parent_id:
#             if parent_id in parent_map:
#                 parent_map[parent_id]['children'].append(nav_item)
#             else:
#                 parent_map[parent_id] = {
#                     'children': [nav_item]
#                 }
#
#         if item['user_nav__menu_level'] == 2:
#             result.append(nav_item)
#     for item in result:
#         item['children'] = parent_map.get(item['nav_id'], {}).get('children', [])
#
#     return result





# input_data = [{'user_nav__id': 2, 'user_nav__menu_index': '1-1', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/employeeInformation/Roster', 'user_nav__menu_name': '花名册', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 1, 'user_nav__menu_level': 2, 'user_nav__menu_category': 1}, {'user_nav__id': 3, 'user_nav__menu_index': '1-2', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/volumeContracts/Record', 'user_nav__menu_name': '追光者', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 1, 'user_nav__menu_level': 2, 'user_nav__menu_category': 1}, {'user_nav__id': 42, 'user_nav__menu_index': '5-1', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/offlineTraining', 'user_nav__menu_name': '线下培训', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 41, 'user_nav__menu_level': 2, 'user_nav__menu_category': 5}, {'user_nav__id': 43, 'user_nav__menu_index': '5-1-2', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/offlineTraining', 'user_nav__menu_name': '讲师库', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 42, 'user_nav__menu_level': 3, 'user_nav__menu_category': 5}, {'user_nav__id': 44, 'user_nav__menu_index': '5-1-2-1', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/LecturerDetail', 'user_nav__menu_name': '讲师明细', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 43, 'user_nav__menu_level': 4, 'user_nav__menu_category': 5}, {'user_nav__id': 45, 'user_nav__menu_index': '5-1-2-2', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/SummaryDetail', 'user_nav__menu_name': '讲师分析', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 43, 'user_nav__menu_level': 4, 'user_nav__menu_category': 5}, {'user_nav__id': 46, 'user_nav__menu_index': '5-1-2-3', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/OutgoingLecturer', 'user_nav__menu_name': '卸任/离职讲师明细', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 43, 'user_nav__menu_level': 4, 'user_nav__menu_category': 5}]
#
#
# output_data = transform_data(input_data)
# print(output_data)

# def convert_nav(nav_data, parent_id=None, level=2):
#     result = []
#     for item in nav_data:
#         if item['user_nav__menu_parent_id'] == parent_id:
#             new_item = {
#                 'nav_id': item['user_nav__id'],
#                 'nav_index': item['user_nav__menu_index'],
#                 'nav_name': item['user_nav__menu_name'],
#                 'nav_url': item['user_nav__menu_path'],
#                 'nav_icon': '',
#                 'nav_component': 'layout/index',
#                 'nav_parent_id': parent_id,
#                 'nav_type': item['user_nav__menu_type'],
#                 'nav_level': level,
#                 'nav_category': item['user_nav__menu_category']
#             }
#             children = convert_nav(nav_data, item['user_nav__id'], level + 1)
#             if children:
#                 new_item['children'] = children
#             result.append(new_item)
#     return result
#
# original_data = [{'user_nav__id': 2, 'user_nav__menu_index': '1-1', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/employeeInformation/Roster', 'user_nav__menu_name': '花名册', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 1, 'user_nav__menu_level': 2, 'user_nav__menu_category': 1}, {'user_nav__id': 3, 'user_nav__menu_index': '1-2', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/volumeContracts/Record', 'user_nav__menu_name': '追光者', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 1, 'user_nav__menu_level': 2, 'user_nav__menu_category': 1}, {'user_nav__id': 42, 'user_nav__menu_index': '5-1', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/offlineTraining', 'user_nav__menu_name': '线下培训', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 41, 'user_nav__menu_level': 2, 'user_nav__menu_category': 5}, {'user_nav__id': 43, 'user_nav__menu_index': '5-1-2', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/offlineTraining', 'user_nav__menu_name': '讲师库', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 42, 'user_nav__menu_level': 3, 'user_nav__menu_category': 5}, {'user_nav__id': 44, 'user_nav__menu_index': '5-1-2-1', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/LecturerDetail', 'user_nav__menu_name': '讲师明细', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 43, 'user_nav__menu_level': 4, 'user_nav__menu_category': 5}, {'user_nav__id': 45, 'user_nav__menu_index': '5-1-2-2', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/SummaryDetail', 'user_nav__menu_name': '讲师分析', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 43, 'user_nav__menu_level': 4, 'user_nav__menu_category': 5}, {'user_nav__id': 46, 'user_nav__menu_index': '5-1-2-3', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/OutgoingLecturer', 'user_nav__menu_name': '卸任/离职讲师明细', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 43, 'user_nav__menu_level': 4, 'user_nav__menu_category': 5}]
#
#
# result = convert_nav(original_data, parent_id=None, level=2)
# print(result)


# # 如果nav_parent_id是上级的nav_id那么children就加入改项

# 生成的树节点里面user_nav__menu_level=2是一级，user_nav__menu_level=3是二级，user_nav__menu_level=4是三级


# def transform_data(data):
#     transformed_data = []
#     parent_map = {}
#
#     for item in data:
#         nav_item = {
#             'nav_id': item['user_nav__id'],
#             'nav_index': item['user_nav__menu_index'],
#             'nav_name': item['user_nav__menu_name'],
#             'nav_url': item['user_nav__menu_path'],
#             'nav_icon': '',
#             'nav_component': 'layout/index',
#             'nav_parent_id': item['user_nav__menu_parent_id'],
#             'nav_type': item['user_nav__menu_type'],
#             'nav_level': item['user_nav__menu_level'],
#             'nav_category_id': item['user_nav__menu_category_id'],
#             'nav_category_name': item['user_nav__menu_category_name'],
#             'nav_secondary_category_id': item['user_nav__menu_secondary_category_id'],
#         }
#
#         if nav_item['nav_id'] not in parent_map:
#             nav_item['children'] = []
#             parent_map[nav_item['nav_id']] = nav_item
#
#         if nav_item['nav_parent_id'] in parent_map:
#             parent_map[nav_item['nav_parent_id']]['children'].append(nav_item)
#         else:
#             transformed_data.append(nav_item)
#
#     return transformed_data

# def transform_data(data):
#     nav_map = {}
#     root_items = []
#
#     for item in data:
#         nav_id = item['user_nav__id']
#         parent_id = item['user_nav__menu_parent_id']
#
#         if nav_id not in nav_map:
#             nav_item = {
#                 'nav_id': nav_id,
#                 'nav_index': item['user_nav__menu_index'],
#                 'nav_name': item['user_nav__menu_name'],
#                 'nav_url': item['user_nav__menu_path'],
#                 'nav_icon': '',
#                 'nav_component': 'layout/index',
#                 'nav_type': item['user_nav__menu_type'],
#                 'nav_level': item['user_nav__menu_level'],
#                 'nav_category_id': item['user_nav__menu_category_id'],
#                 'nav_category_name': item['user_nav__menu_category_name'],
#                 'nav_secondary_category_id': item['user_nav__menu_secondary_category_id']
#             }
#
#             if parent_id != nav_id:
#                 nav_item['nav_parent_id'] = parent_id
#
#             nav_map[nav_id] = nav_item
#         else:
#             nav_map[nav_id].update({
#                 'nav_index': item['user_nav__menu_index'],
#                 'nav_name': item['user_nav__menu_name'],
#                 'nav_url': item['user_nav__menu_path'],
#                 'nav_type': item['user_nav__menu_type'],
#                 'nav_level': item['user_nav__menu_level'],
#                 'nav_category_id': item['user_nav__menu_category_id'],
#                 'nav_category_name': item['user_nav__menu_category_name'],
#                 'nav_secondary_category_id': item['user_nav__menu_secondary_category_id']
#             }
#             )
#     for nav_id, nav_item in nav_map.items():
#         if 'nav_parent_id' in nav_item:
#             parent_id = nav_item['nav_parent_id']
#             if parent_id in nav_map:
#                 parent = nav_map[parent_id]
#                 if 'children' not in parent:
#                     parent['children'] = []
#                 parent['children'].append(nav_item)
#             else:
#                 root_items.append(nav_item)
#         else:
#             root_items.append(nav_item)
#
#     return root_items
#
# data = [
#     # Your input data here
# ]
#
# transformed_data = transform_data(data)
# print(transformed_data)



# def transform_data(data):
#     nav_map = {}
#     root_items = []
#
#     for item in data:
#         nav_id = item['user_nav__id']
#         parent_id = item['user_nav__menu_parent_id']
#
#         nav_item = {
#             'nav_id': nav_id,
#             'nav_index': item['user_nav__menu_index'],
#             'nav_name': item['user_nav__menu_name'],
#             'nav_url': item['user_nav__menu_path'],
#             'nav_icon': '',
#             'nav_component': 'layout/index',
#             'nav_type': item['user_nav__menu_type'],
#             'nav_level': item['user_nav__menu_level'],
#             'nav_category_id': item['user_nav__menu_category_id'],
#             'nav_category_name': item['user_nav__menu_category_name'],
#             'nav_secondary_category_id': item['user_nav__menu_secondary_category_id']
#         }
#
#         nav_map[nav_id] = nav_item
#
#         if parent_id in nav_map:
#             if 'children' not in nav_map[parent_id]:
#                 nav_map[parent_id]['children'] = []
#             nav_map[parent_id]['children'].append(nav_item)
#         else:
#             root_items.append(nav_item)
#
#     return root_items
#
# data = [
#     # Your input data here
# ]
#
# transformed_data = transform_data(data)
# print(transformed_data)
#
#
# data = [{'user_nav__id': 2, 'user_nav__menu_index': '1-1', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/employeeInformation/Roster', 'user_nav__menu_name': '花名册', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 1, 'user_nav__menu_level': 2, 'user_nav__menu_category_id': 1, 'user_nav__menu_category_name': '组织员工', 'user_nav__menu_secondary_category_id': None}, {'user_nav__id': 3, 'user_nav__menu_index': '1-2', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/volumeContracts/Record', 'user_nav__menu_name': '追光者', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 1, 'user_nav__menu_level': 2, 'user_nav__menu_category_id': 1, 'user_nav__menu_category_name': '组织员工', 'user_nav__menu_secondary_category_id': None}, {'user_nav__id': 42, 'user_nav__menu_index': '5-1', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/offlineTraining', 'user_nav__menu_name': '线下培训', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 41, 'user_nav__menu_level': 2, 'user_nav__menu_category_id': 5, 'user_nav__menu_category_name': '培训', 'user_nav__menu_secondary_category_id': None}, {'user_nav__id': 47, 'user_nav__menu_index': '5-1-1', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/TrainingReport', 'user_nav__menu_name': '培训报表', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 42, 'user_nav__menu_level': 3, 'user_nav__menu_category_id': 5, 'user_nav__menu_category_name': '培训', 'user_nav__menu_secondary_category_id': 42}, {'user_nav__id': 43, 'user_nav__menu_index': '5-1-2', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/offlineTraining', 'user_nav__menu_name': '讲师库', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 42, 'user_nav__menu_level': 3, 'user_nav__menu_category_id': 5, 'user_nav__menu_category_name': '培训', 'user_nav__menu_secondary_category_id': 42}, {'user_nav__id': 44, 'user_nav__menu_index': '5-1-2-1', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/LecturerDetail', 'user_nav__menu_name': '讲师明细', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 43, 'user_nav__menu_level': 4, 'user_nav__menu_category_id': 5, 'user_nav__menu_category_name': '培训', 'user_nav__menu_secondary_category_id': 42}, {'user_nav__id': 45, 'user_nav__menu_index': '5-1-2-2', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/SummaryDetail', 'user_nav__menu_name': '讲师分析', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 43, 'user_nav__menu_level': 4, 'user_nav__menu_category_id': 5, 'user_nav__menu_category_name': '培训', 'user_nav__menu_secondary_category_id': 42}, {'user_nav__id': 46, 'user_nav__menu_index': '5-1-2-3', 'user_nav__menu_icon': None, 'user_nav__menu_path': '/OutgoingLecturer', 'user_nav__menu_name': '卸任/离职讲师明细', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 43, 'user_nav__menu_level': 4, 'user_nav__menu_category_id': 5, 'user_nav__menu_category_name': '培训', 'user_nav__menu_secondary_category_id': 42}]
#
#
# transformed_data = transform_data(data)
# print(transformed_data)
#
# b = [{'nav_id': 2, 'nav_index': '1-1', 'nav_name': '花名册', 'nav_url': '/employeeInformation/Roster', 'nav_icon': '',
#       'nav_component': 'layout/index', 'nav_type': 1, 'nav_level': 2, 'nav_category_id': 1,
#       'nav_category_name': '组织员工', 'nav_secondary_category_id': None},
#      {'nav_id': 3, 'nav_index': '1-2', 'nav_name': '追光者', 'nav_url': '/volumeContracts/Record', 'nav_icon': '',
#       'nav_component': 'layout/index', 'nav_type': 1, 'nav_level': 2, 'nav_category_id': 1,
#       'nav_category_name': '组织员工', 'nav_secondary_category_id': None},
#      {'nav_id': 42, 'nav_index': '5-1', 'nav_name': '线下培训', 'nav_url': '/offlineTraining', 'nav_icon': '',
#       'nav_component': 'layout/index', 'nav_type': 1, 'nav_level': 2, 'nav_category_id': 5, 'nav_category_name': '培训',
#       'nav_secondary_category_id': None, 'children': [
#          {'nav_id': 47, 'nav_index': '5-1-1', 'nav_name': '培训报表', 'nav_url': '/TrainingReport', 'nav_icon': '',
#           'nav_component': 'layout/index', 'nav_type': 1, 'nav_level': 3, 'nav_category_id': 5,
#           'nav_category_name': '培训', 'nav_secondary_category_id': 42},
#          {'nav_id': 43, 'nav_index': '5-1-2', 'nav_name': '讲师库', 'nav_url': '/offlineTraining', 'nav_icon': '',
#           'nav_component': 'layout/index', 'nav_type': 1, 'nav_level': 3, 'nav_category_id': 5,
#           'nav_category_name': '培训', 'nav_secondary_category_id': 42, 'children': [
#              {'nav_id': 44, 'nav_index': '5-1-2-1', 'nav_name': '讲师明细', 'nav_url': '/LecturerDetail',
#               'nav_icon': '', 'nav_component': 'layout/index', 'nav_type': 1, 'nav_level': 4, 'nav_category_id': 5,
#               'nav_category_name': '培训', 'nav_secondary_category_id': 42},
#              {'nav_id': 45, 'nav_index': '5-1-2-2', 'nav_name': '讲师分析', 'nav_url': '/SummaryDetail', 'nav_icon': '',
#               'nav_component': 'layout/index', 'nav_type': 1, 'nav_level': 4, 'nav_category_id': 5,
#               'nav_category_name': '培训', 'nav_secondary_category_id': 42},
#              {'nav_id': 46, 'nav_index': '5-1-2-3', 'nav_name': '卸任/离职讲师明细', 'nav_url': '/OutgoingLecturer',
#               'nav_icon': '', 'nav_component': 'layout/index', 'nav_type': 1, 'nav_level': 4, 'nav_category_id': 5,
#               'nav_category_name': '培训', 'nav_secondary_category_id': 42}]}]}]




a=[{'user_nav__id': 1, 'user_nav__menu_index': '1', 'user_nav__menu_icon': '/icon/zuzhi.png', 'user_nav__menu_complete_path': None, 'user_nav__menu_name': '组织员工', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': None, 'user_nav__menu_level': 1, 'user_nav__menu_category_id': None, 'user_nav__menu_category_name': None}, {'user_nav__id': 2, 'user_nav__menu_index': '1-1', 'user_nav__menu_icon': 'el-icon-notebook-1', 'user_nav__menu_complete_path': '/employeeInformation/Roster', 'user_nav__menu_name': '花名册', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 1, 'user_nav__menu_level': 2, 'user_nav__menu_category_id': 1, 'user_nav__menu_category_name': '组织员工'}, {'user_nav__id': 3, 'user_nav__menu_index': '1-2', 'user_nav__menu_icon': 'el-icon-document', 'user_nav__menu_complete_path': '/volumeContracts/Record', 'user_nav__menu_name': '追光者', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 1, 'user_nav__menu_level': 2, 'user_nav__menu_category_id': 1, 'user_nav__menu_category_name': '组织员工'}, {'user_nav__id': 41, 'user_nav__menu_index': '5', 'user_nav__menu_icon': '/icon/peixun.png', 'user_nav__menu_complete_path': None, 'user_nav__menu_name': '培训', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': None, 'user_nav__menu_level': 1, 'user_nav__menu_category_id': None, 'user_nav__menu_category_name': None}, {'user_nav__id': 42, 'user_nav__menu_index': '5-1', 'user_nav__menu_icon': 'el-icon-data-line', 'user_nav__menu_complete_path': None, 'user_nav__menu_name': '讲师库', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 41, 'user_nav__menu_level': 2, 'user_nav__menu_category_id': 41, 'user_nav__menu_category_name': '培训'}, {'user_nav__id': 43, 'user_nav__menu_index': '5-1-1', 'user_nav__menu_icon': None, 'user_nav__menu_complete_path': '/offlineTraining/LecturerDetail', 'user_nav__menu_name': '讲师明细', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 42, 'user_nav__menu_level': 3, 'user_nav__menu_category_id': 41, 'user_nav__menu_category_name': '培训'}, {'user_nav__id': 44, 'user_nav__menu_index': '5-1-2', 'user_nav__menu_icon': None, 'user_nav__menu_complete_path': '/offlineTraining/SummaryDetail', 'user_nav__menu_name': '讲师分析', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 42, 'user_nav__menu_level': 3, 'user_nav__menu_category_id': 41, 'user_nav__menu_category_name': '培训'}, {'user_nav__id': 45, 'user_nav__menu_index': '5-1-3', 'user_nav__menu_icon': None, 'user_nav__menu_complete_path': '/offlineTraining/OutgoingLecturer', 'user_nav__menu_name': '卸任/离职讲师明细', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 42, 'user_nav__menu_level': 3, 'user_nav__menu_category_id': 41, 'user_nav__menu_category_name': '培训'}, {'user_nav__id': 46, 'user_nav__menu_index': '5-2', 'user_nav__menu_icon': 'el-icon-data-line', 'user_nav__menu_complete_path': '/offlineTraining/TrainingReport', 'user_nav__menu_name': '培训报表', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 41, 'user_nav__menu_level': 2, 'user_nav__menu_category_id': 41, 'user_nav__menu_category_name': '培训'}, {'user_nav__id': 47, 'user_nav__menu_index': '5-3', 'user_nav__menu_icon': 'el-icon-data-line', 'user_nav__menu_complete_path': '/offlineTraining/TrainingType', 'user_nav__menu_name': '培训类型', 'user_nav__menu_type': 1, 'user_nav__menu_parent_id': 41, 'user_nav__menu_level': 2, 'user_nav__menu_category_id': 41, 'user_nav__menu_category_name': '培训'}]
# b=[
#   {
#     "icon": "/icon/zuzhi.png",
#     "name": "组织员工",
#     "path": None,
#     "parent_id": None,
#     "type": 1,
#     "id": 1,
#     "children": [
#       {
#         "icon": None,
#         "name": "花名册",
#         "path": "/employeeInformation/Roster",
#         "parent_id": 1,
#         "type": 1,
#         "id": 2,
#         "category_id": 1,
#         "category_name": "组织员工"
#       },
#       {
#         "icon": None,
#         "name": "追光者",
#         "path": "/volumeContracts/Record",
#         "parent_id": 1,
#         "type": 1,
#         "id": 3,
#         "category_id": 1,
#         "category_name": "组织员工"
#       },
#
#     ]
#   },
#
#   {
#     "icon": "/icon/peixun.png",
#     "name": "培训",
#     "path": None,
#     "parent_id": None,
#     "type": 1,
#     "id": 41,
#     "children": [
#       {
#         "icon": "el-icon-data-line",
#         "name": "讲师库",
#         "path": None,
#         "parent_id": 41,
#         "type": 1,
#         "id": 42,
#         "category_id": 41,
#         "category_name": "培训",
#         "children": [
#           {
#             "icon": None,
#             "name": "讲师明细",
#             "path": "/offlineTraining/LecturerDetail",
#             "parent_id": 42,
#             "type": 1,
#             "id": 43,
#             "category_id": 41,
#             "category_name": "培训"
#           },
#           {
#             "icon": None,
#             "name": "讲师分析",
#             "path": "/offlineTraining/SummaryDetail",
#             "parent_id": 42,
#             "type": 1,
#             "id": 44,
#             "category_id": 41,
#             "category_name": "培训"
#           },
#           {
#             "icon": None,
#             "name": "卸任/离职讲师明细",
#             "path": "/offlineTraining/OutgoingLecturer",
#             "parent_id": 42,
#             "type": 1,
#             "id": 45,
#             "category_id": 41,
#             "category_name": "培训"
#           }
#         ]
#       },
#       {
#         "icon": "el-icon-data-line",
#         "name": "培训报表",
#         "path": "/offlineTraining/TrainingReport",
#         "parent_id": 41,
#         "type": 1,
#         "id": 46,
#         "category_id": 41,
#         "category_name": "培训"
#       },
#       {
#         "icon": "el-icon-data-line",
#         "name": "培训类型",
#         "path": "/offlineTraining/TrainingType",
#         "parent_id": 41,
#         "type": 1,
#         "id": 47,
#         "category_id": 41,
#         "category_name": "培训"
#       },
#       {
#         "icon": "el-icon-data-line",
#         "name": "培训记录",
#         "path": "/offlineTraining/TrainingSignIn",
#         "parent_id": 41,
#         "type": 1,
#         "id": 48,
#         "category_id": 41,
#         "category_name": "培训"
#       },
#       {
#         "icon": "el-icon-data-line",
#         "name": "本月汇总分析",
#         "path": "/offlineTraining/SummaryAnalysis",
#         "parent_id": 41,
#         "type": 1,
#         "id": 49,
#         "category_id": 41,
#         "category_name": "培训"
#       },
#       {
#         "icon": "el-icon-data-line",
#         "name": "本月人均课时",
#         "path": "/offlineTraining/TrainingPeriod",
#         "parent_id": 41,
#         "type": 1,
#         "id": 50,
#         "category_id": 41,
#         "category_name": "培训"
#       }
#     ]
#   }
# ]
def build_menu_tree(menu_items, parent_id=None):
    tree = []
    for item in menu_items:
        if item['user_nav__menu_parent_id'] == parent_id:
            children = build_menu_tree(menu_items, item['user_nav__id'])
            if children:
                item['children'] = children
            tree.append(item)
    return tree

b = build_menu_tree(a)
print(b)

