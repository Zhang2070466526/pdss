from django.test import TestCase

# Create your tests here.
import json

data = {'nodePath': [6, 354, 580], 'content_part': '光伏研究院', 'content_section': '电池研究中心', 'content_module': '电池研发三组', 'content_group': '', 'content_title': '12', 'content_type_id': 2, 'content_category_id': 2, 'content_level_id': 1, 'content_manner': '现场', 'content_begin_date': '2023-08-01', 'content_end_date': '2023-08-02', 'content_duration': '11', 'content_object': '11', 'content_plan': '计划外', 'content_people_number': '11', 'lecturer_type': '内部讲师', 'content_lecturer': '杜勇', 'lecturer_code': '2010001850', 'post': '班长（旧）', 'content_satisfaction': '111', 'content_expenses': '111', 'lecturer_level_id': ''}

# 将字典转换为 JSON 字符串，并用双引号替换单引号
json_string = json.dumps(data, ensure_ascii=False).replace("'", '"')

print(json_string)
