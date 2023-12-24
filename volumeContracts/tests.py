# import arrow
#
# current_month = arrow.now().month
#
# if current_month in [4, 7, 10, 1]:
#     # Trigger the event
#     print('Event triggered!')
#
# from django.db import models
#
#
# class ContractsInfo():  # 合同信息表
#     contracts_gender_choices = {
#         '0':'男',
#         '1':'女'
#     }
# a=ContractsInfo()
# #
# print(a.contracts_gender_choices['1'])


# contracts_origin_choices =(
#         (1, '江苏润阳新能源科技股份有限公司'),(2,'润阳新能源（上海）有限公司'), (3, '苏州润矽光伏科技有限公司'), (4, '盐城润宝电力科技有限公司'),
#         (5, '江苏润阳悦达光伏科技有限公司'),
#         (6, '江苏润阳光伏科技有限公司'), (7, '江苏润阳世纪光伏科技有限公司'),
#         (8, '云南润阳世纪光伏科技有限公司'), (9, '江苏海博瑞光伏科技有限公司'), (10, '宁夏润阳硅材料科技有限公司'),
#         (11, '内蒙古润阳悦达新能源科技有限公司')
#     )
# origin_dict = {}
# for item in contracts_origin_choices:
#     key = str(item[0])
#     value = item[1]
#     origin_dict[key] = value
#
# print(origin_dict)


# a=[
#     {'id': 87, 'approval_status': True, 'contracts_infoFile': 103,},
# {'id': 87, 'approval_status': True,  'contracts_infoFile': 104,},
# {'id': 86, 'approval_status': True, 'contracts_infoFile': None,},
# ]
# b=[
#     {'id': 87, 'approval_status': True, 'contracts_infoFile': [103,104]},
# {'id': 86, 'approval_status': True, 'contracts_infoFile': None,},
# ]


# a = [
#     {'id': 87, 'approval_status': True, 'contracts_infoFile': 103, },
#     {'id': 87, 'approval_status': True, 'contracts_infoFile': 104, },
#     {'id': 86, 'approval_status': True, 'contracts_infoFile': None, },
# ]
#
# b = {}
# for item in a:
#     id_value = item['id']
#     file_value = item['contracts_infoFile']
#
#     if file_value is None:
#         continue
#
#     if id_value in b:
#         b[id_value]['contracts_infoFile'].append(file_value)
#     else:
#         b[id_value] = {'id': id_value, 'approval_status': item['approval_status'], 'contracts_infoFile': [file_value]}
#
# b = list(b.values())
#
# print(b)

# a = [
#     {'id': 87, 'approval_status': True, 'contracts_infoFile': 103},
#     {'id': 87, 'approval_status': True, 'contracts_infoFile': 104},
#     {'id': 86, 'approval_status': True, 'contracts_infoFile': None}
# ]
#
# b = []
#
# temp = {}
#
# for element in a:
#     id_value = element['id']
#     contracts_infoFile = element['contracts_infoFile']
#
#     if id_value in temp:
#         if contracts_infoFile is not None:
#             temp[id_value].append(contracts_infoFile)
#     else:
#         if contracts_infoFile is not None:
#             temp[id_value] = [contracts_infoFile]
#         else:
#             temp[id_value] = None
#
# for id_value, contracts_infoFile in temp.items():
#     new_element = {'id': id_value, 'approval_status': True, 'contracts_infoFile': contracts_infoFile}
#     b.append(new_element)
#
# print(b)
# a = [
#     {'id': 87, 'approval_status': True, 'name': '王正明', 'contracts_infoFile': 103},
#     {'id': 87, 'approval_status': True, 'name': '王正明', 'contracts_infoFile': 104},
#     {'id': 86, 'approval_status': True, 'name': 'dd', 'contracts_infoFile': None}
# ]
#
# b = []
#
# for element in a:
#     id_value = element['id']
#     contracts_infoFile_value = element['contracts_infoFile']
#     matching_element = next((x for x in b if x['id'] == id_value), None)
#
#     if matching_element:
#         if contracts_infoFile_value is not None:
#             matching_element['contracts_infoFile'].append(contracts_infoFile_value)
#     else:
#         if contracts_infoFile_value is not None:
#             element['contracts_infoFile'] = [contracts_infoFile_value]
#         b.append(element)
#
# print(b)
# a=[{'id': 458, 'contracts_infoFile': 101}, {'id': 458, 'contracts_infoFile': 102}, {'id': 457, 'contracts_infoFile': 39}, {'id': 456, 'contracts_infoFile': 40}]
# # b=[{'id': 458, 'contracts_infoFile': [101,102]}, {'id': 458, 'contracts_infoFile': 102}, {'id': 457, 'contracts_infoFile': 39}, {'id': 456, 'contracts_infoFile': 40}]
#
#
# bb = {}
#
# for item in a:
#     id_value = item['id']
#     info_file = item['contracts_infoFile']
#
#     if id_value in bb:
#         bb[id_value].append(info_file)
#     else:
#         bb[id_value] = [info_file]
#
# bb = [{'id': key, 'contracts_infoFile': value} for key, value in bb.items()]
#
# print(bb)



# a=[{'id': 458, 'contracts_infoFile': [101, 102]}, {'id': 457, 'contracts_infoFile': [39, 40]}, {'id': 456, 'contracts_infoFile': [41, 42]}, {'id': 455, 'contracts_infoFile': [43, 44]}, {'id': 454, 'contracts_infoFile': [45, 46]}, {'id': 453, 'contracts_infoFile': [47, 48]}, {'id': 452, 'contracts_infoFile': [49, 50]}, {'id': 450, 'contracts_infoFile': [55, 56]}, {'id': 449, 'contracts_infoFile': [57, 58]}, {'id': 448, 'contracts_infoFile': [59, 60]}, {'id': 447, 'contracts_infoFile': [51, 52]}, {'id': 444, 'contracts_infoFile': [99, 100]}, {'id': 438, 'contracts_infoFile': [53]}]
# print(458 in a)

# a = [{'id': 458, 'contracts_infoFile': [101, 102]}, {'id': 457, 'contracts_infoFile': [39, 40]}, {'id': 456, 'contracts_infoFile': [41, 42]}, {'id': 455, 'contracts_infoFile': [43, 44]}, {'id': 454, 'contracts_infoFile': [45, 46]}, {'id': 453, 'contracts_infoFile': [47, 48]}, {'id': 452, 'contracts_infoFile': [49, 50]}, {'id': 450, 'contracts_infoFile': [55, 56]}, {'id': 449, 'contracts_infoFile': [57, 58]}, {'id': 448, 'contracts_infoFile': [59, 60]}, {'id': 447, 'contracts_infoFile': [51, 52]}, {'id': 444, 'contracts_infoFile': [99, 100]}, {'id': 438, 'contracts_infoFile': [53]}]
#
# target_id = 458
#
# if check_id_in_list(a, target_id):
#     print(f"'a' contains an object with an id of {target_id}.")
# else:
#     print(f"'a' does not contain an object with an id of {target_id}.")

# a={'id': 458, 'contracts_infoFile': [101, 102]}

