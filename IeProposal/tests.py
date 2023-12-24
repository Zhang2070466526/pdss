# url = "http://ekp.runergy.cn:28080/sys/webservice/kmReviewWebserviceService?wsdl"
# headers = {'Content-Type': 'application/xml'}
# payload = """
#                                         <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservice.review.km.kmss.landray.com/">
#                                             <soapenv:Header/>
#                                             <soapenv:Body>
#                                                 <web:addReview>
#                                                     <!--Optional:-->
#                                                     <arg0>
#                                                         <!--Zero or more repetitions:-->
#                                                         <!--Optional:-->
#                                                         <attachmentValues></attachmentValues>
#                                                         <!--Optional:-->
#                                                         <authAreaId></authAreaId>
#                                                         <!--Optional:-->
#                                                         <docContent></docContent>
#                                                         <!--Optional:-->
#                                                         <docCreator>{"LoginName":"%s"}</docCreator>
#                                                         <!--Optional:-->
#                                                         <docProperty></docProperty>
#                                                         <!--Optional:-->
#                                                         <docStatus>20</docStatus>
#                                                         <!--Optional:-->
#                                                         <docSubject>%s</docSubject>
#                                                         <!--Optional:-->
#                                                         <fdId></fdId>
#                                                         <!--Optional:-->
#                                                         <fdKeyword></fdKeyword>
#                                                         <!--Optional:-->
#                                                         <fdSource></fdSource>
#                                                         <!--Optional:-->
#                                                         <fdTemplateId>18a4a207e56f3ad44de69a64fd2ba0db</fdTemplateId>
#                                                         <!--Optional:--><flowParam>{}</flowParam>
#                                                         <!--Optional:-->
#                                                         <formValues>
#                                                         {
#                                                             "fd_3c2d1db9377260":"%s",
#                                                             "fd_3c2d1e0306c51c":"%s",
#                                                             "fd_3c3018fd3012b2":"%s"
#                                                         }
#                                                         </formValues>
#                                                         %s
#                                                     </arg0>
#                                                 </web:addReview>
#                                             </soapenv:Body>
#                                         </soapenv:Envelope>
#                                                                 """% ('1010000407',
#                                                                        '标题',
#                                                                       '产品质量',
#                                                                       '反馈',
#                                                                       '建议',
#                                                                       '')
#
# # response = requests.post(url, headers=headers, data=payload.replace("'", '"'))


# import base64
#
# # 打开并读取图片文件
# with open('image.jpg', 'rb') as image_file:
#     # 读取图片内容
#     image_binary = image_file.read()
#
# # 将图片内容编码为Base64字符串
# base64_encoded = base64.b64encode(image_binary).decode('utf-8')
#
# # 打印Base64字符串
# print(base64_encoded)




# import urllib.parse
#
# # 假设编码后的密码为
# encoded_password = "Your%20Encoded%20Password"
#
# # 解码密码
# decoded_password = urllib.parse.unquote(encoded_password)
# print(decoded_password)




# import  datetime
# # 原始列表
# data =[{'fd_process_id': '18a73b6fb0b6d8936135b364fd7aad35', 'fd_fact_node_name': '起草节点', 'fd_create_time': datetime.datetime(2023, 9, 8, 15, 35, 10, 653000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '测试3'}, {'fd_process_id': '18a73b6fb0b6d8936135b364fd7aad35', 'fd_fact_node_name': '直接上级审批', 'fd_create_time': datetime.datetime(2023, 9, 8, 15, 36, 8, 117000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '测试3'}, {'fd_process_id': '18a73b6fb0b6d8936135b364fd7aad35', 'fd_fact_node_name': '部门负责人', 'fd_create_time': datetime.datetime(2023, 9, 8, 15, 36, 8, 517000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '测试3'}, {'fd_process_id': '18a73b6fb0b6d8936135b364fd7aad35', 'fd_fact_node_name': 'IE审批', 'fd_create_time': datetime.datetime(2023, 9, 8, 15, 37, 29, 490000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '测试3'}, {'fd_process_id': '18a73b6fb0b6d8936135b364fd7aad35', 'fd_fact_node_name': 'IE主管', 'fd_create_time': datetime.datetime(2023, 9, 8, 15, 38, 39, 330000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '测试3'}, {'fd_process_id': '18a73b6fb0b6d8936135b364fd7aad35', 'fd_fact_node_name': 'IE负责人', 'fd_create_time': datetime.datetime(2023, 9, 8, 15, 38, 39, 647000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '测试3'}, {'fd_process_id': '18a73b6fb0b6d8936135b364fd7aad35', 'fd_fact_node_name': '实施单位主管', 'fd_create_time': datetime.datetime(2023, 9, 8, 15, 40, 19, 717000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '测试3'}, {'fd_process_id': '18a73b6fb0b6d8936135b364fd7aad35', 'fd_fact_node_name': '实施部门负责人', 'fd_create_time': datetime.datetime(2023, 9, 8, 15, 40, 20, 147000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '测试3'}, {'fd_process_id': '18a86fea1740a0a8dfa60c645b3b8a89', 'fd_fact_node_name': '起草节点', 'fd_create_time': datetime.datetime(2023, 9, 12, 9, 27, 9, 243000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '11'}, {'fd_process_id': '18a86fea1740a0a8dfa60c645b3b8a89', 'fd_fact_node_name': '直接上级审批', 'fd_create_time': datetime.datetime(2023, 9, 12, 9, 27, 45, 757000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '11'}, {'fd_process_id': '18a86fea1740a0a8dfa60c645b3b8a89', 'fd_fact_node_name': '部门负责人', 'fd_create_time': datetime.datetime(2023, 9, 12, 9, 27, 46, 100000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '11'}, {'fd_process_id': '18a86fea1740a0a8dfa60c645b3b8a89', 'fd_fact_node_name': 'IE审批', 'fd_create_time': datetime.datetime(2023, 9, 12, 9, 28, 5, 63000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '11'}, {'fd_process_id': '18a86fea1740a0a8dfa60c645b3b8a89', 'fd_fact_node_name': 'IE主管', 'fd_create_time': datetime.datetime(2023, 9, 12, 9, 31, 32, 770000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '11'}, {'fd_process_id': '18a86fea1740a0a8dfa60c645b3b8a89', 'fd_fact_node_name': 'IE负责人', 'fd_create_time': datetime.datetime(2023, 9, 12, 9, 31, 33, 173000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '11'}, {'fd_process_id': '18a876ea211cec36cc48d7048c9a2a7c', 'fd_fact_node_name': '起草节点', 'fd_create_time': datetime.datetime(2023, 9, 12, 11, 28, 57, 823000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '设备维护', 'wentifankui': '555'}, {'fd_process_id': '18a876ea211cec36cc48d7048c9a2a7c', 'fd_fact_node_name': '直接上级审批', 'fd_create_time': datetime.datetime(2023, 9, 12, 11, 36, 55, 490000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '设备维护', 'wentifankui': '555'}, {'fd_process_id': '18a876ea211cec36cc48d7048c9a2a7c', 'fd_fact_node_name': '部门负责人', 'fd_create_time': datetime.datetime(2023, 9, 12, 11, 36, 55, 797000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '设备维护', 'wentifankui': '555'}, {'fd_process_id': '18a876ea211cec36cc48d7048c9a2a7c', 'fd_fact_node_name': 'IE审批', 'fd_create_time': datetime.datetime(2023, 9, 12, 11, 38, 48, 317000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '设备维护', 'wentifankui': '555'}, {'fd_process_id': '18a876ea211cec36cc48d7048c9a2a7c', 'fd_fact_node_name': 'IE主管', 'fd_create_time': datetime.datetime(2023, 9, 12, 11, 39, 13, 263000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '设备维护', 'wentifankui': '555'}, {'fd_process_id': '18a876ea211cec36cc48d7048c9a2a7c', 'fd_fact_node_name': 'IE负责人', 'fd_create_time': datetime.datetime(2023, 9, 12, 11, 39, 13, 540000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '设备维护', 'wentifankui': '555'}, {'fd_process_id': '18a8805d048d180d01c1e194160b0b8e', 'fd_fact_node_name': '起草节点', 'fd_create_time': datetime.datetime(2023, 9, 12, 14, 13, 58, 400000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '111'}, {'fd_process_id': '18a8805d048d180d01c1e194160b0b8e', 'fd_fact_node_name': '直接上级审批', 'fd_create_time': datetime.datetime(2023, 9, 12, 14, 14, 39, 57000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '111'}, {'fd_process_id': '18a8805d048d180d01c1e194160b0b8e', 'fd_fact_node_name': '部门负责人', 'fd_create_time': datetime.datetime(2023, 9, 12, 14, 14, 40, 110000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '111'}, {'fd_process_id': '18a8805d048d180d01c1e194160b0b8e', 'fd_fact_node_name': 'IE审批', 'fd_create_time': datetime.datetime(2023, 9, 12, 14, 17, 27, 557000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '111'}, {'fd_process_id': '18a8805d048d180d01c1e194160b0b8e', 'fd_fact_node_name': 'IE主管', 'fd_create_time': datetime.datetime(2023, 9, 12, 14, 18, 45, 73000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '111'}, {'fd_process_id': '18a8805d048d180d01c1e194160b0b8e', 'fd_fact_node_name': 'IE负责人', 'fd_create_time': datetime.datetime(2023, 9, 12, 14, 18, 45, 423000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '生产管理', 'wentifankui': '111'}, {'fd_process_id': '18a881bb466f52905310e4d4a30add43', 'fd_fact_node_name': '起草节点', 'fd_create_time': datetime.datetime(2023, 9, 12, 14, 37, 47, 717000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '设备维护', 'wentifankui': '44'}, {'fd_process_id': '18a881bb466f52905310e4d4a30add43', 'fd_fact_node_name': '直接上级审批', 'fd_create_time': datetime.datetime(2023, 9, 12, 14, 38, 45, 230000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '设备维护', 'wentifankui': '44'}, {'fd_process_id': '18a881bb466f52905310e4d4a30add43', 'fd_fact_node_name': '部门负责人', 'fd_create_time': datetime.datetime(2023, 9, 12, 14, 38, 45, 553000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '设备维护', 'wentifankui': '44'}, {'fd_process_id': '18a881bb466f52905310e4d4a30add43', 'fd_fact_node_name': 'IE审批', 'fd_create_time': datetime.datetime(2023, 9, 12, 14, 41, 20, 287000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '设备维护', 'wentifankui': '44'}, {'fd_process_id': '18a881bb466f52905310e4d4a30add43', 'fd_fact_node_name': 'IE主管', 'fd_create_time': datetime.datetime(2023, 9, 12, 14, 42, 28, 840000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '设备维护', 'wentifankui': '44'}, {'fd_process_id': '18a881bb466f52905310e4d4a30add43', 'fd_fact_node_name': 'IE负责人', 'fd_create_time': datetime.datetime(2023, 9, 12, 14, 42, 29, 113000), 'doc_status': '20', 'gonghao': '2050002446', 'tianleixing': '设备维护', 'wentifankui': '44'}]
#
#
#
#
# # 自定义排序键函数
# def custom_sort_key(item):
#     # 定义节点顺序
#     node_order = ['起草节点', '直接上级审批', '部门负责人', 'IE审批', 'IE主管', 'IE负责人', '实施单位主管','实施部门负责人']
#     return (item['fd_process_id'], node_order.index(item['fd_fact_node_name']))
#
# # 使用sorted()进行排序
# sorted_data = sorted(data, key=custom_sort_key)
#
# # 打印排序后的结果
# for item in sorted_data:
#     print(item)
# # 原始列表
# my_list = ['生产管理']
#
# # 转换为元组
# my_tuple = (my_list[0])
#
# # 打印元组
# print(my_tuple)



# my_list = ['4', '7', '5', '6']
# my_tuple = tuple(my_list)
# print(my_tuple)


a=[
  {
    'id': '18aac9758d61317d8d0c52848d4bca3a',
    'ie_proposal_employee__employee_code': '2010002980',
    'ie_proposal_employee__employee_name': '郭晴',
    'ie_proposal_type__ie_proposal_type_name': '设备维护',

    'ie_proposal_create_time': '2023-09-1916: 38: 34',

    'file2_num': 0
  },
  {
    'id': '18a883ecaa093d2fd27190c41a7b8f6d',
    'ie_proposal_employee__employee_code': '2050002446',
    'ie_proposal_employee__employee_name': '李秀旻',
    'ie_proposal_type__ie_proposal_type_name': '生产管理',

    'ie_proposal_create_time': '2023-09-1215: 15: 56',

  },
  {
    'id': '18a881bb466f52905310e4d4a30add43',
    'ie_proposal_employee__employee_code': '2050002446',

    'ie_proposal_create_time': '2023-09-1214: 37: 47',

  }]