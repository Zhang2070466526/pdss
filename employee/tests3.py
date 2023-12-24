# import json
# import datetime
# data = [
#     "{'id': 1, 'employee_name': '杨灼坚', 'employee_code': '2020000001', 'employee_record_time': datetime.datetime(2023, 10, 17, 8, 37, 42, 254286), 'employee_record_type': '1'}",
#     "{'id': 2, 'employee_name': '沙泉', 'employee_code': '1010000064', 'employee_record_time': datetime.datetime(2023, 10, 17, 8, 37, 42, 260287), 'employee_record_type': '1'}",
#     "{'id': 3, 'employee_name': '朱彦斌', 'employee_code': '2020000153','employee_record_time': datetime.datetime(2023, 10, 17, 8, 37, 42, 264288), 'employee_record_type': '1'}"]

# # Parse the JSON-formatted strings into dictionaries
# formatted_data = [eval(item) for item in data]
#
# print(formatted_data)

import datetime

# input_str = "{'id': 1, 'employee_name': '杨灼坚', 'employee_code': '2020000001', 'employee_record_time':  datetime.datetime(2023, 10, 17, 8, 37, 42, 264288), 'employee_record_type': '1'}"
#
# # 使用 eval 函数来解析字符串
# data = eval(input_str)
#
# # 打印转换后的字典
# print(data)




# a=[{'department_full_name': '集团公司 全球战略供应链管理中心', 'department_full_code': 'RYGF10 RPR100'}, {'department_full_name': '集团公司 光伏研究院', 'department_full_code': 'RYGF10 RRI100'}, {'department_full_name': '集团公司 集团质量中心', 'department_full_code': 'RYGF10 RQA100'},]
# b=[{'department_full_name': '集团公司 全球战略供应链管理中心', 'department_full_code': 'RYGF10 RPR100'}, {'department_full_name': '集团公司 光伏研究院', 'department_full_code': 'RYGF10 RRI100'}]
# diff = [i for i in a if i not in b]
# print(diff)

# a=[['个人-其他原因', 632, 683, 2711], ['个人-家庭原因', 458, 602, 3866], ['个人-职业发展', 609, 697, 1533], ['个人-身体原因', 113, 218, 1322], ['体检不合格', 0, 0, 1], ['公司-其他原因', 50, 74, 360], ['公司-同事关系', 3, 7, 31], ['公司-工作环境', 73, 101, 618], ['公司-文化氛围', 7, 6, 27], ['公司-职业发展', 25, 20, 28], ['公司-薪酬原因', 46, 104, 458], ['公司-领导原因', 7, 25, 134], ['合计', 2059, 2594, 11596], ['因劝离、员工主动离职', 13, 15, 81], ['旷离', 5, 17, 330], ['辞职', 14, 6, 25], ['辞退', 4, 19, 71]]
# z_reason=[]
# z_sal=[]
# z_idl=[]
# z_dl=[]
# for line in a:
#     print(line)
#     z_reason.append(line[0])
#     z_sal.append(line[1])
#     z_idl.append(line[2])
#     z_dl.append(line[3])
# print(z_reason)
# print(z_idl)
# print(z_sal)
# print(z_sal)



# a=[{'name': '中国', 'value': 12213}, {'name': '克罗地亚', 'value': 1}, {'name': '哥伦比亚', 'value': 1}, {'name': '墨西哥', 'value': 1}, {'name': '巴西', 'value': 1}, {'name': '法国', 'value': 1}, {'name': '泰国', 'value': 4140}, {'name': '美国', 'value': 14}, {'name': '菲律宾', 'value': 2}, {'name': '西班牙', 'value': 1}, {'name': '越南', 'value': 205}, {'name': '马来西亚', 'value': 1}, {'name': '其他', 'value': 7}]
#
# from translate import Translator
#
# # 创建 Translator 对象，指定源语言为中文，目标语言为英文
# translator = Translator(to_lang="en", from_lang="zh")
#
# # 原始中文列表
# chinese_list = ['中国', '克罗地亚', '哥伦比亚', '墨西哥', '巴西', '法国', '泰国', '美国', '菲律宾', '西班牙', '越南', '马来西亚', '其他']
#
# # 转换为英文列表
# english_list = [translator.translate(chinese) for chinese in chinese_list]
#
# # 打印结果
# print(english_list)


# # 创建一个中文到英文的映射字典
# translation_dict = {
#     '中国': 'China',
#     '克罗地亚': 'Croatia',
#     '哥伦比亚': 'Colombia',
#     '墨西哥': 'Mexico',
#     '巴西': 'Brazil',
#     '法国': 'France',
#     '泰国': 'Thailand',
#     '美国': 'United States',
#     '菲律宾': 'Philippines',
#     '西班牙': 'Spain',
#     '越南': 'Vietnam',
#     '马来西亚': 'Malaysia',
#     '其他': 'Other'
# }
#
# # 原始中文列表
# chinese_list = ['中国', '克罗地亚', '哥伦比亚', '墨西哥', '巴西', '法国', '泰国', '美国', '菲律宾', '西班牙', '越南', '马来西亚', '其他']
#
# # 转换为英文列表
# english_list = [translation_dict.get(chinese, chinese) for chinese in chinese_list]
#
# # 打印结果
# print(english_list)
#
# # 原始中文列表
# chinese_list = ['中国', '克罗地亚', '哥伦比亚', '墨西哥', '巴西', '法国', '泰国', '美国', '菲律宾', '西班牙', '越南', '马来西亚', '其他']
#
# # 对应的英文列表
# english_list = ['China', 'Croatia', 'Colombia', 'Mexico', 'Brazil', 'France', 'Thailand', 'United States', 'Philippines', 'Spain', 'Vietnam', 'Malaysia', 'Other']
#
# # 使用 zip 函数将两个列表的元素一一对应
# zipped_lists = zip(english_list,chinese_list)
#
# # 构建字典
# result_dict = {chinese: english for chinese, english in zipped_lists}
#
# # 打印结果
# print(result_dict)



from mtranslate import translate

# 原始中文列表
chinese_list = ['中国', '克罗地亚', '哥伦比亚', '墨西哥', '巴西', '法国', '泰国', '美国', '菲律宾', '西班牙', '越南', '马来西亚', '其他']

# 转换为英文列表
english_list = [translate(chinese, 'en') for chinese in chinese_list]

# 打印结果
print(english_list)
