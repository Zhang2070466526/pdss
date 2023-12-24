

name_code='Panithan Chanthawangso(陶佳月)(6010003717)'
name, code = name_code.split("(")[0], name_code.split("(")[1].replace(")", "")
info_string = "Panithan Chanthawangso(陶佳月)(6010003717)"

# 通过括号切割字符串
name, _, student_id = info_string.split('(')
print(name,_,student_id)
# 去除末尾的括号
student_id = student_id.rstrip(')')

# 打印结果
print("名字:", name)
print("学号:", student_id)


a='Panithan Chanthawangso(陶佳月)(D6010003717)'
b='sssssssss(D6010003717)'
c='大撒大撒（ddd）(1010000407)'


import re

def extract_info(input_string):
    # 使用正则表达式提取名字和学号
    match = re.match(r'^(.*?)[\(|（]([\w]+)[\)|）]$', input_string)

    if match:
        name = match.group(1)
        student_id = match.group(2)
        return name, student_id
    else:
        return None, None

# 测试样例
a = 'Panithan Chanthawangso(陶佳月)(D6010003717)'
b = 'sssssssss(D6010003717)'
c = '大撒大撒（ddd）(1010000407)'

name_a, id_a = extract_info(a)
name_b, id_b = extract_info(b)
name_c, id_c = extract_info(c)

# 打印结果
print("a:", name_a, id_a)
print("b:", name_b, id_b)
print("c:", name_c, id_c)


import re

def extract_info(input_string):
    # 使用正则表达式提取名字和学号
    match = re.match(r'^(.*?)[\(|（]([\w]+)[\)|）]$', input_string)

    if match:
        name = match.group(1)
        student_id = match.group(2)
        return name, student_id
    else:
        return None, None

# 测试样例
a = 'Panithan Chanthawangso(陶佳月)(0)(A6010003717)'
b = 'sssssssss(D6010003717)'
c = '大撒大撒（ddd）(1010000407)'

name_a, id_a = extract_info(a)
name_b, id_b = extract_info(b)
name_c, id_c = extract_info(c)

# 打印结果
print("a:", name_a, id_a)
print("b:", name_b, id_b)
print("c:", name_c, id_c)
