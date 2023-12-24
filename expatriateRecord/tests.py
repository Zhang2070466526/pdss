# # # # # # # # # # # # # # # from django.test import TestCase
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Create your tests here.
# # # # # # # # # # # # # # # # import arrow
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # now = str(arrow.now().datetime)
# # # # # # # # # # # # # # # # print(str(now)[:10])
# # # # # # # # # # # # # # # # print(str(now)[11:19])
# # # # # # # # # # # # # # # # print(now)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # a = {
# # # # # # # # # # # # # # # #     "code": "string",
# # # # # # # # # # # # # # # #     "name": "string",
# # # # # # # # # # # # # # # #     'date_Of_Entry': "string",
# # # # # # # # # # # # # # # #     'expatriate_Dept': "string",
# # # # # # # # # # # # # # # #     'post': "string",
# # # # # # # # # # # # # # # #     'expatriate_jobRank': "string",
# # # # # # # # # # # # # # # #     'expatriate_Before_Base': "string",
# # # # # # # # # # # # # # # #     'expatriate_Before_Manage': "string",
# # # # # # # # # # # # # # # #     'expatriate_Before_Factory': "string",
# # # # # # # # # # # # # # # #     'resident_Dept': "string",
# # # # # # # # # # # # # # # #     'expatriate_Cycle': "string",
# # # # # # # # # # # # # # # #     'expatriate_Begin': "string",
# # # # # # # # # # # # # # # #     'expatriate_End': "string",
# # # # # # # # # # # # # # # #     'isCross_Division': "string",
# # # # # # # # # # # # # # # #     'expatriate_After_Base': "string",
# # # # # # # # # # # # # # # #     'expatriate_After_Manage': "string",
# # # # # # # # # # # # # # # #     'expatriate_After_Factory': "string",
# # # # # # # # # # # # # # # #     'expatriate_Reason': "string",
# # # # # # # # # # # # # # # #     'expatriate_Target': "string",
# # # # # # # # # # # # # # # #     'expatriate_Allowance': "string",
# # # # # # # # # # # # # # # #     'description_Allowance': "string",
# # # # # # # # # # # # # # # #     'expatriate_Type': "string",
# # # # # # # # # # # # # # # #     'expatriate_After_Cost': "string",
# # # # # # # # # # # # # # # #     'first_Expatriate': "string",
# # # # # # # # # # # # # # # #     'last_Expatriate_Begin': "string",
# # # # # # # # # # # # # # # #     'last_Expatriate_End': "string",
# # # # # # # # # # # # # # # #     'number_Of_Expatriate': "string",
# # # # # # # # # # # # # # # #     'rank': "string",
# # # # # # # # # # # # # # # #     'isSigned_Expatriate': "string",
# # # # # # # # # # # # # # # #     'expatriate_Quality': "string",
# # # # # # # # # # # # # # # #     'expatriate_Place': "string",
# # # # # # # # # # # # # # # #     'remark': "string",
# # # # # # # # # # # # # # # #     'expatriate_creatorCode': "string",
# # # # # # # # # # # # # # # #     'expatriate_creatorName': "string",
# # # # # # # # # # # # # # # #     'expatriate_modifierCode': "string",
# # # # # # # # # # # # # # # #     'expatriate_modifierName': "string",
# # # # # # # # # # # # # # # #     'expatriate_createTime': "string",
# # # # # # # # # # # # # # # #     'expatriate_modifyTime': "string",
# # # # # # # # # # # # # # # # }
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # "visa_passport"
# # # # # # # # # # # # # # # # "first_Docking"
# # # # # # # # # # # # # # # # "application_Approval"
# # # # # # # # # # # # # # # # "invitation_Letter_Provided"
# # # # # # # # # # # # # # # # "collectInfo"
# # # # # # # # # # # # # # # # "submit_Embassy"
# # # # # # # # # # # # # # # # "last_SupplementaryInfo"
# # # # # # # # # # # # # # # # "signed"
# # # # # # # # # # # # # # # # "arrival_Thailand"
# # # # # # # # # # # # # # # # "visa_Application_Remarks"
# # # # # # # # # # # # # # # # "current_Progress"
# # # # # # # # # # # # # # # # "sending_Embassy"
# # # # # # # # # # # # # # # # "system_Post"
# # # # # # # # # # # # # # # # "visa_Type"
# # # # # # # # # # # # # # # # "visa_Validity_Period_Begin"
# # # # # # # # # # # # # # # # "visa_Validity_Period_End"
# # # # # # # # # # # # # # # # "backSign"
# # # # # # # # # # # # # # # # "visa_Expiration_Date"
# # # # # # # # # # # # # # # # "arrival_Thailand_First"
# # # # # # # # # # # # # # # # "report_90"
# # # # # # # # # # # # # # # # "filing_Dead_90 "
# # # # # # # # # # # # # # # # "expiration_Article "
# # # # # # # # # # # # # # # # "isAssignOver"
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # SELECT
# # # # # # # # # # # # # # # # 	b.code AS code,
# # # # # # # # # # # # # # # # 	b.name AS name,
# # # # # # # # # # # # # # # # 	d.D_glgs AS expatriate_Before_Manage,
# # # # # # # # # # # # # # # # 	c.JobRankName AS expatriate_jobRank,
# # # # # # # # # # # # # # # # 	d.shortname AS abbreviation_Dept,
# # # # # # # # # # # # # # # # 	e.PostName AS post
# # # # # # # # # # # # # # # # FROM
# # # # # # # # # # # # # # # # 	T_HR_ExpatriateRecord AS a
# # # # # # # # # # # # # # # # 	INNER JOIN T_HR_Employee AS b ON a.emp_id = b.id
# # # # # # # # # # # # # # # # 	LEFT JOIN T_HR_Employee_File AS fi ON fi.employee_id= b.id
# # # # # # # # # # # # # # # # 	LEFT JOIN T_HR_JobRank AS c ON b.JobRankID = c.id
# # # # # # # # # # # # # # # # 	LEFT JOIN T_HR_Department AS d ON b.DeptID = d.id
# # # # # # # # # # # # # # # # 	LEFT JOIN T_HR_Post AS e ON b.PostID = e.id
# # # # # # # # # # # # # # # # WHERE
# # # # # # # # # # # # # # # # 	1 = 1
# # # # # # # # # # # # # # # # 	AND a.data_status = 1
# # # # # # # # # # # # # # # # 	AND d.IfUse= 1
# # # # # # # # # # # # # # # # 	AND c.IfUse= 1
# # # # # # # # # # # # # # # # 	AND e.IfUse= 1
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # a=[
# # # # # # # # # # # # # # # #           { "value": "1010000075", "address": {
# # # # # # # # # # # # # # # #             "name": "宋文祥",
# # # # # # # # # # # # # # # #             "expatriate_Before_Manage": "总部",
# # # # # # # # # # # # # # # #             "expatriate_jobRank": "苏州润矽",
# # # # # # # # # # # # # # # #             "abbreviation_Dept": "润阳光伏科技（泰国）有限公司",
# # # # # # # # # # # # # # # #             "post": "分/子公司总经理"
# # # # # # # # # # # # # # # #         	}
# # # # # # # # # # # # # # # # 		  }
# # # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # # # data = [
# # # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # # #         "code": "1010000075",
# # # # # # # # # # # # # # # #         "name": "宋文祥",
# # # # # # # # # # # # # # # #         "expatriate_Before_Manage": "总部",
# # # # # # # # # # # # # # # #         "expatriate_jobRank": "苏州润矽",
# # # # # # # # # # # # # # # #         "abbreviation_Dept": "润阳光伏科技（泰国）有限公司",
# # # # # # # # # # # # # # # #         "post": "分/子公司总经理"
# # # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # Extract values and create a new dictionary
# # # # # # # # # # # # # # # # converted_data = [
# # # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # # #         "value": item["code"],
# # # # # # # # # # # # # # # #         "address": {
# # # # # # # # # # # # # # # #             "name": item["name"],
# # # # # # # # # # # # # # # #             "expatriate_Before_Manage": item["expatriate_Before_Manage"],
# # # # # # # # # # # # # # # #             "expatriate_jobRank": item["expatriate_jobRank"],
# # # # # # # # # # # # # # # #             "abbreviation_Dept": item["abbreviation_Dept"],
# # # # # # # # # # # # # # # #             "post": item["post"]
# # # # # # # # # # # # # # # #         }
# # # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # #     for item in data
# # # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(converted_data)
# # # # # # # # # # # # # # # import datetime
# # # # # # # # # # # # # # # # a=[{'gonghao': '1010000032', 'number_Of_Expatriate': 1, 'first_Expatriate': datetime.datetime(2023, 2, 12, 0, 0), 'last_Expatriate_Begin': datetime.datetime(2023, 2, 12, 0, 0), 'last_Expatriate_End': datetime.datetime(2023, 5, 11, 0, 0)},
# # # # # # # # # # # # # # # #    {'gonghao': '1010000033', 'number_Of_Expatriate': 1, 'first_Expatriate': datetime.datetime(2023, 6, 1, 0, 0), 'last_Expatriate_Begin': datetime.datetime(2023, 6, 1, 0, 0), 'last_Expatriate_End': datetime.datetime(2023, 7, 31, 0, 0)},
# # # # # # # # # # # # # # # #    {'gonghao': '1010000034', 'number_Of_Expatriate': 1, 'first_Expatriate': datetime.datetime(2023, 8, 25, 0, 0), 'last_Expatriate_Begin': datetime.datetime(2023, 8, 25, 0, 0), 'last_Expatriate_End': datetime.datetime(2023, 9, 25, 0, 0)}]
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # desired_gonghao = '1010000033'
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # for data in a:
# # # # # # # # # # # # # # # #     if data['gonghao'] == desired_gonghao:
# # # # # # # # # # # # # # # #         print(data)
# # # # # # # # # # # # # # # #         break
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # a={'msg': '查询成功', 'data': [
# # # # # # # # # # # # # # #     {'code': '1010000032', 'number_Of_Expatriate': 1, 'first_Expatriate': datetime.datetime(2023, 2, 12, 0, 0), 'last_Expatriate_Begin': datetime.datetime(2023, 2, 12, 0, 0), 'last_Expatriate_End': datetime.datetime(2023, 5, 11, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '2010003712', 'number_Of_Expatriate': 3, 'first_Expatriate': datetime.datetime(2023, 2, 1, 0, 0), 'last_Expatriate_Begin': datetime.datetime(2023, 5, 31, 0, 0), 'last_Expatriate_End': datetime.datetime(2023, 6, 30, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '9010000043', 'number_Of_Expatriate': 1, 'first_Expatriate': datetime.datetime(2023, 7, 1, 0, 0), 'last_Expatriate_Begin': datetime.datetime(2023, 7, 1, 0, 0), 'last_Expatriate_End': datetime.datetime(2023, 12, 31, 0, 0)}
# # # # # # # # # # # # # # # ], 'code': 200}
# # # # # # # # # # # # # # # desired_code = '7010000488'
# # # # # # # # # # # # # # # # print(a['data'])
# # # # # # # # # # # # # # # # Find the dictionary with the desired code
# # # # # # # # # # # # # # # # desired_dict = None
# # # # # # # # # # # # # # # # for d in a['data']:
# # # # # # # # # # # # # # # #     if d['code'] == desired_code:
# # # # # # # # # # # # # # # #         desired_dict = d
# # # # # # # # # # # # # # # #         break
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # Print the desired dictionary
# # # # # # # # # # # # # # # # print(desired_dict)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # b={'msg': '查询成功', 'data': [{'code': '2010003712', 'name': '蒋王华',  'post': '工艺经理', 'expatriate_jobRank': None, 'expatriate_Before_Base': None, 'expatriate_Before_Manage': '润阳世纪', 'expatriate_Before_Factory': '一厂',  'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 1, 31, 11, 43, 32, 673000)},   {'code': '2060000704', 'name': '陆品龙','post': '质量副经理', 'expatriate_jobRank': '江苏海博瑞', 'expatriate_Before_Base': '组件事业部', 'expatriate_Before_Manage': '江苏海博瑞', 'expatriate_Before_Factory': '江苏海博瑞', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 8, 1, 14, 1, 5, 403000)}], 'code': 200}
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # c=[{'code': '1010000075', 'rank': 'M7.2-总经理'}, {'code': '2010003712', 'rank': 'T2.3-工程师/倒工3级'}, {'code': '2050000225', 'rank': 'T3.2-中级工程师2级'}, {'code': '2010008744', 'rank': '普通员工'}, {'code': '2010008486', 'rank': '技术员工'}, {'code': '2010009431', 'rank': 'T2.5-工程师/倒工5级'}]
# # # # # # # # # # # # # # # # merged_data = []
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # for dict_a in a['data']:
# # # # # # # # # # # # # # # #     for dict_b in b['data']:
# # # # # # # # # # # # # # # #         if dict_a['code'] == dict_b['code']:
# # # # # # # # # # # # # # # #             merged_dict = dict_a.copy()
# # # # # # # # # # # # # # # #             merged_dict.update(dict_b)
# # # # # # # # # # # # # # # #             print(merged_dict)
# # # # # # # # # # # # # # # # #             merged_data.append(merged_dict)
# # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # print(merged_data)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # a=[
# # # # # # # # # # # # # # #         {
# # # # # # # # # # # # # # #             "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # #             "visa_Validity_Period_End": None,
# # # # # # # # # # # # # # #             "arrival_Thailand": None,
# # # # # # # # # # # # # # #             "expatriate_Begin": "2023-01-19",
# # # # # # # # # # # # # # #             "expatriate_End": "2023-04-18",
# # # # # # # # # # # # # # #             "id":1234
# # # # # # # # # # # # # # #         },
# # # # # # # # # # # # # # #         {
# # # # # # # # # # # # # # #             "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # #             "visa_Validity_Period_End": None,
# # # # # # # # # # # # # # #             "arrival_Thailand": None,
# # # # # # # # # # # # # # #             "expatriate_Begin": None,
# # # # # # # # # # # # # # #             "expatriate_End": None,
# # # # # # # # # # # # # # #             'id':2323
# # # # # # # # # # # # # # #         },
# # # # # # # # # # # # # # #         {
# # # # # # # # # # # # # # #             "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # #             "visa_Validity_Period_End": None,
# # # # # # # # # # # # # # #             "arrival_Thailand": None,
# # # # # # # # # # # # # # #             "expatriate_Begin": "2023-01-11",
# # # # # # # # # # # # # # #             "expatriate_End": "2023-02-28",
# # # # # # # # # # # # # # #             "id":4444
# # # # # # # # # # # # # # #         }
# # # # # # # # # # # # # # #     ]
# # # # # # # # # # # # # # # # b=[
# # # # # # # # # # # # # # # #         {
# # # # # # # # # # # # # # # #             "value": "1234",
# # # # # # # # # # # # # # # #             "label": {
# # # # # # # # # # # # # # # #                 "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # # #                 "visa_Validity_Period_End": None,
# # # # # # # # # # # # # # # #                 "arrival_Thailand": None,
# # # # # # # # # # # # # # # #                 "expatriate_Begin": "2023-01-19",
# # # # # # # # # # # # # # # #                 "expatriate_End": "2023-04-18"
# # # # # # # # # # # # # # # #             }
# # # # # # # # # # # # # # # #         },
# # # # # # # # # # # # # # # #         {
# # # # # # # # # # # # # # # #             "value": "2323",
# # # # # # # # # # # # # # # #             "label":{
# # # # # # # # # # # # # # # #                 "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # # #                 "visa_Validity_Period_End": None,
# # # # # # # # # # # # # # # #                 "arrival_Thailand": None,
# # # # # # # # # # # # # # # #                 "expatriate_Begin": None,
# # # # # # # # # # # # # # # #                 "expatriate_End": None
# # # # # # # # # # # # # # # #             }
# # # # # # # # # # # # # # # #         },
# # # # # # # # # # # # # # # #         {
# # # # # # # # # # # # # # # #             "value": "4444",
# # # # # # # # # # # # # # # #             "label": {
# # # # # # # # # # # # # # # #                 "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # # #                 "visa_Validity_Period_End": None,
# # # # # # # # # # # # # # # #                 "arrival_Thailand": None,
# # # # # # # # # # # # # # # #                 "expatriate_Begin": "2023-01-11",
# # # # # # # # # # # # # # # #                 "expatriate_End": "2023-02-28"
# # # # # # # # # # # # # # # #             }
# # # # # # # # # # # # # # # #         },
# # # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # b = [
# # # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # # #         "value": str(d["id"]),
# # # # # # # # # # # # # # # #         "label": {
# # # # # # # # # # # # # # # #             k: v for k, v in d.items() if k != "id"
# # # # # # # # # # # # # # # #         }
# # # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # #     for d in a
# # # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # a = [
# # # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # # #         "arrival_Thailand": None,
# # # # # # # # # # # # # # # #         "expatriate_Begin": "2023-01-19",
# # # # # # # # # # # # # # # #         "id": 1234
# # # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # # #         "arrival_Thailand": None,
# # # # # # # # # # # # # # # #         "expatriate_Begin": None,
# # # # # # # # # # # # # # # #         "id": 2323
# # # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # # #         "arrival_Thailand": None,
# # # # # # # # # # # # # # # #         "expatriate_Begin": "2023-01-11",
# # # # # # # # # # # # # # # #         "id": 4444
# # # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # b = []
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # for item in a:
# # # # # # # # # # # # # # # #     expat_begin = item.get("expatriate_Begin")
# # # # # # # # # # # # # # # #     visa_begin = item.get("visa_Validity_Period_Begin")
# # # # # # # # # # # # # # # #     arrival_thailand = item.get("arrival_Thailand")
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #     label = f"签证有效期开始时间为{visa_begin};抵泰日期为{arrival_thailand};外派起始时间为{expat_begin}"
# # # # # # # # # # # # # # # #     b.append({"value": str(item["id"]), "label": label})
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # b = []
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # for item in a:
# # # # # # # # # # # # # # # #     new_dict = {
# # # # # # # # # # # # # # # #         "value": str(item["id"]),
# # # # # # # # # # # # # # # #         "label": {
# # # # # # # # # # # # # # # #             f"签证有效期开始时间为{str(item['visa_Validity_Period_Begin'])};抵泰日期为{str(item['arrival_Thailand'])};外派起始时间为{str(item['expatriate_Begin'])}"
# # # # # # # # # # # # # # # #         }
# # # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # #     b.append(new_dict)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # a = [
# # # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": "2023-02-21",
# # # # # # # # # # # # # # # #         "arrival_Thailand": None,
# # # # # # # # # # # # # # # #         "expatriate_Begin": "2023-01-19",
# # # # # # # # # # # # # # # #         "id": 1234
# # # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # # #         "arrival_Thailand": "2023-01-03",
# # # # # # # # # # # # # # # #         "expatriate_Begin": None,
# # # # # # # # # # # # # # # #         "id": 2323
# # # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # # #         "arrival_Thailand": None,
# # # # # # # # # # # # # # # #         "expatriate_Begin": "2023-01-11",
# # # # # # # # # # # # # # # #         "id": 4444
# # # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # b = []
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # for dictionary in a:
# # # # # # # # # # # # # # # #     if (
# # # # # # # # # # # # # # # #             dictionary["expatriate_Begin"] is None
# # # # # # # # # # # # # # # #             or dictionary["visa_Validity_Period_Begin"] is None
# # # # # # # # # # # # # # # #             or dictionary["arrival_Thailand"] is None
# # # # # # # # # # # # # # # #     ):
# # # # # # # # # # # # # # # #         continue
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #     new_dict = {
# # # # # # # # # # # # # # # #         "value": str(dictionary["id"]),
# # # # # # # # # # # # # # # #         "label": {
# # # # # # # # # # # # # # # #             f"签证有效期开始时间为{dictionary['visa_Validity_Period_Begin']};外派起始时间为{dictionary['expatriate_Begin']}"
# # # # # # # # # # # # # # # #         }
# # # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #     b.append(new_dict)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # a = [
# # # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": "2023-02-21",
# # # # # # # # # # # # # # # #         "arrival_Thailand": None,
# # # # # # # # # # # # # # # #         "expatriate_Begin": "2023-01-19",
# # # # # # # # # # # # # # # #         "id": 1234
# # # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # # #         "arrival_Thailand": "2023-01-03",
# # # # # # # # # # # # # # # #         "expatriate_Begin": None,
# # # # # # # # # # # # # # # #         "id": 2323
# # # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # # #         "arrival_Thailand": None,
# # # # # # # # # # # # # # # #         "expatriate_Begin": "2023-01-11",
# # # # # # # # # # # # # # # #         "id": 4444
# # # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # b = []
# # # # # # # # # # # # # # # # for item in a:
# # # # # # # # # # # # # # # #     if (
# # # # # # # # # # # # # # # #         item["expatriate_Begin"] is None
# # # # # # # # # # # # # # # #         or item["visa_Validity_Period_Begin"] is None
# # # # # # # # # # # # # # # #         or item["arrival_Thailand"] is None
# # # # # # # # # # # # # # # #     ):
# # # # # # # # # # # # # # # #         continue
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # #     new_dict = {
# # # # # # # # # # # # # # # #         "value": str(item["id"]),
# # # # # # # # # # # # # # # #         "label": {
# # # # # # # # # # # # # # # #             "签证有效期开始时间为" + item["visa_Validity_Period_Begin"] + ";抵泰日期为" + item["arrival_Thailand"]+ ";外派起始时间为" + item["expatriate_Begin"]
# # # # # # # # # # # # # # # #         }
# # # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # #     b.append(new_dict)
# # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # a = [
# # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": "2023-02-21",
# # # # # # # # # # # # # # #         "arrival_Thailand": None,
# # # # # # # # # # # # # # #         "expatriate_Begin": "2023-01-19",
# # # # # # # # # # # # # # #         "id": 1234
# # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # #         "arrival_Thailand": "2023-01-03",
# # # # # # # # # # # # # # #         "expatriate_Begin": None,
# # # # # # # # # # # # # # #         "id": 2323
# # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # #         "arrival_Thailand": None,
# # # # # # # # # # # # # # #         "expatriate_Begin": "2023-01-11",
# # # # # # # # # # # # # # #         "id": 4444
# # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # b = [
# # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # #         "value": "1234",
# # # # # # # # # # # # # # #         "label": {
# # # # # # # # # # # # # # #             "签证有效期开始时间为2023-02-21;外派起始时间为2023-01-19"
# # # # # # # # # # # # # # #         }
# # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # #         "value": "2323",
# # # # # # # # # # # # # # #         "label": {
# # # # # # # # # # # # # # #             "抵泰日期为2023-01-03"
# # # # # # # # # # # # # # #         }
# # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # #         "value": "4444",
# # # # # # # # # # # # # # #         "label": {
# # # # # # # # # # # # # # #             "外派起始时间为2023-01-11;"
# # # # # # # # # # # # # # #         }
# # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # new_dict = {}
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for item in a:
# # # # # # # # # # # # # # #     expatriate_Begin = item.get("expatriate_Begin")
# # # # # # # # # # # # # # #     visa_Validity_Period_Begin = item.get("visa_Validity_Period_Begin")
# # # # # # # # # # # # # # #     arrival_Thailand = item.get("arrival_Thailand")
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     if expatriate_Begin is None or visa_Validity_Period_Begin is None or arrival_Thailand is None:
# # # # # # # # # # # # # # #         continue
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     value = str(item["id"])
# # # # # # # # # # # # # # #     label = {
# # # # # # # # # # # # # # #         "签证有效期开始时间为{};外派起始时间为{}".format(visa_Validity_Period_Begin, expatriate_Begin)
# # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     new_dict[value] = {"value": value, "label": label}
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(new_dict)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # a=[
# # # # # # # # # # # # # # #         {
# # # # # # # # # # # # # # #             "visa_Validity_Period_Begin": 2023-02-21,
# # # # # # # # # # # # # # #             "arrival_Thailand": None,
# # # # # # # # # # # # # # #             "expatriate_Begin": "2023-01-19",
# # # # # # # # # # # # # # #             "id":1234
# # # # # # # # # # # # # # #         },
# # # # # # # # # # # # # # #         {
# # # # # # # # # # # # # # #             "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # #             "arrival_Thailand": 2023-01-03,
# # # # # # # # # # # # # # #             "expatriate_Begin": None,
# # # # # # # # # # # # # # #             'id':2323
# # # # # # # # # # # # # # #         },
# # # # # # # # # # # # # # #         {
# # # # # # # # # # # # # # #             "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # #             "arrival_Thailand": None,
# # # # # # # # # # # # # # #             "expatriate_Begin": "2023-01-11",
# # # # # # # # # # # # # # #             "id":4444
# # # # # # # # # # # # # # #         }
# # # # # # # # # # # # # # #     ] b=[
# # # # # # # # # # # # # # #         {
# # # # # # # # # # # # # # #             "value": "1234",
# # # # # # # # # # # # # # #             "label": {
# # # # # # # # # # # # # # #                 "签证有效期开始时间为2023-02-21;外派起始时间为2023-01-19"
# # # # # # # # # # # # # # #             }
# # # # # # # # # # # # # # #         },
# # # # # # # # # # # # # # #         {
# # # # # # # # # # # # # # #             "value": "2323",
# # # # # # # # # # # # # # #             "label":{
# # # # # # # # # # # # # # #                 "抵泰日期为2023-01-03"
# # # # # # # # # # # # # # #             }
# # # # # # # # # # # # # # #         },
# # # # # # # # # # # # # # #         {
# # # # # # # # # # # # # # #             "value": "4444",
# # # # # # # # # # # # # # #             "label": {
# # # # # # # # # # # # # # #                 "外派起始时间为2023-01-11;"
# # # # # # # # # # # # # # #             }
# # # # # # # # # # # # # # #         },
# # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # # # 其中外派起始时间是expatriate_Begin  签证有效期开始时间是visa_Validity_Period_Begin  抵泰日期是arrival_Thailand   将a转换为b，同时如果expatriate_Begin  ，visa_Validity_Period_Begin  ，arrival_Thailand   任意一个时间为None就不打印该时间
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # a = [
# # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": "2023-02-21",
# # # # # # # # # # # # # # #         "arrival_Thailand": None,
# # # # # # # # # # # # # # #         "expatriate_Begin": "2023-01-19",
# # # # # # # # # # # # # # #         "id": 1234
# # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # #         "arrival_Thailand": "2023-01-03",
# # # # # # # # # # # # # # #         "expatriate_Begin": None,
# # # # # # # # # # # # # # #         "id": 2323
# # # # # # # # # # # # # # #     },
# # # # # # # # # # # # # # #     {
# # # # # # # # # # # # # # #         "visa_Validity_Period_Begin": None,
# # # # # # # # # # # # # # #         "arrival_Thailand": None,
# # # # # # # # # # # # # # #         "expatriate_Begin": "2023-01-11",
# # # # # # # # # # # # # # #         "id": 4444
# # # # # # # # # # # # # # #     }
# # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # b = []
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for dictionary in a:
# # # # # # # # # # # # # # #     new_dict = {}
# # # # # # # # # # # # # # #     if dictionary["expatriate_Begin"] is not None:
# # # # # # # # # # # # # # #         new_dict["label"] = f"外派起始时间为{dictionary['expatriate_Begin']}"
# # # # # # # # # # # # # # #     if dictionary["visa_Validity_Period_Begin"] is not None:
# # # # # # # # # # # # # # #         new_dict["label"] = f"签证有效期开始时间为{dictionary['visa_Validity_Period_Begin']}"
# # # # # # # # # # # # # # #     if dictionary["arrival_Thailand"] is not None:
# # # # # # # # # # # # # # #         new_dict["label"] = f"抵泰日期为{dictionary['arrival_Thailand']}"
# # # # # # # # # # # # # # #     if new_dict:
# # # # # # # # # # # # # # #         new_dict["value"] = str(dictionary["id"])
# # # # # # # # # # # # # # #         b.append(new_dict)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # import json,datetime
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # data = [{'id': 53, 'photograph_file__id': 369, 'photograph_file__name': '刘开心2023-08-01_照片.mp4', 'photograph_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-08-01_照片.mp4', 'insured_file__id': None, 'insured_file__name': None, 'insured_file__url': None, 'incomeTax_file__id': 372, 'incomeTax_file__name': '刘开心2023-08-01_所得税缴税证明.png', 'incomeTax_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-08-01_所得税缴税证明.png', 'accumulationFund_file__id': None, 'accumulationFund_file__name': None, 'accumulationFund_file__url': None, 'workPhotos_file__id': 371, 'workPhotos_file__name': '刘开心2023-08-01_工作照片.docx', 'workPhotos_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-08-01_工作照片.docx', 'workVideo_file__id': None, 'workVideo_file__name': None, 'workVideo_file__url': None, 'dailyPhotos_file__id': 374, 'dailyPhotos_file__name': '刘开心2023-08-01_日常照片.jpg', 'dailyPhotos_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-08-01_日常照片.jpg', 'dailyVideo_file__id': 373, 'dailyVideo_file__name': '刘开心2023-08-01_日常视频.docx', 'dailyVideo_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-08-01_日常视频.docx', 'incumbency_file__id': 370, 'incumbency_file__name': '刘开心2023-08-01_在职证明.jpg', 'incumbency_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-08-01_在职证明.jpg', 'noWork_file__id': 375, 'noWork_file__name': '刘开心2023-08-01_无工作承诺函.docx', 'noWork_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-08-01_无工作承诺函.docx', 'cllBack_file__id': 376, 'cllBack_file__name': '刘开心2023-08-01_电话回访录音.jpg', 'cllBack_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-08-01_电话回访录音.jpg', 'firstlivevideo_file__id': 377, 'firstlivevideo_file__name': '刘开心2023-08-01_实时视频(第一次).mp4', 'firstlivevideo_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-08-01_实时视频(第一次).mp4', 'secondlivevideo_file__id': 378, 'secondlivevideo_file__name': '刘开心2023-08-01_实时视频(第二次).docx', 'secondlivevideo_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-08-01_实时视频(第二次).docx'}, {'id': 54, 'photograph_file__id': 379, 'photograph_file__name': '刘开心2023-09-01_照片.mp4', 'photograph_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_照片.mp4', 'insured_file__id': 389, 'insured_file__name': '刘开心2023-09-01_参保证明.jpg', 'insured_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_参保证明.jpg', 'incomeTax_file__id': 382, 'incomeTax_file__name': '刘开心2023-09-01_所得税缴税证明.png', 'incomeTax_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_所得税缴税证明.png', 'accumulationFund_file__id': 391, 'accumulationFund_file__name': '刘开心2023-09-01_公积金账户信息.jpg', 'accumulationFund_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_公积金账户信息.jpg', 'workPhotos_file__id': 381, 'workPhotos_file__name': '刘开心2023-09-01_工作照片.docx', 'workPhotos_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_工作照片.docx', 'workVideo_file__id': 390, 'workVideo_file__name': '刘开心2023-09-01_工作视频.jpg', 'workVideo_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_工作视频.jpg', 'dailyPhotos_file__id': 384, 'dailyPhotos_file__name': '刘开心2023-09-01_日常照片.mp4', 'dailyPhotos_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_日常照片.mp4', 'dailyVideo_file__id': 383, 'dailyVideo_file__name': '刘开心2023-09-01_日常视频.docx', 'dailyVideo_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_日常视频.docx', 'incumbency_file__id': 380, 'incumbency_file__name': '刘开心2023-09-01_在职证明.jpg', 'incumbency_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_在职证明.jpg', 'noWork_file__id': 385, 'noWork_file__name': '刘开心2023-09-01_无工作承诺函.docx', 'noWork_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_无工作承诺函.docx', 'cllBack_file__id': 386, 'cllBack_file__name': '刘开心2023-09-01_电话回访录音.jpg', 'cllBack_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_电话回访录音.jpg', 'firstlivevideo_file__id': 387, 'firstlivevideo_file__name': '刘开心2023-09-01_实时视频(第一次).mp4', 'firstlivevideo_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_实时视频(第一次).mp4', 'secondlivevideo_file__id': 388, 'secondlivevideo_file__name': '刘开心2023-09-01_实时视频(第二次).docx', 'secondlivevideo_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/刘开心_412722199811204070/刘开心2023-09-01_实时视频(第二次).docx'}, {'id': 55, 'photograph_file__id': 393, 'photograph_file__name': '李以权2023-08-01_照片.png', 'photograph_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_照片.png', 'insured_file__id': 392, 'insured_file__name': '李以权2023-08-01_参保证明.png', 'insured_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_参保证明.png', 'incomeTax_file__id': 397, 'incomeTax_file__name': '李以权2023-08-01_所得税缴税证明.png', 'incomeTax_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_所得税缴税证明.png', 'accumulationFund_file__id': 398, 'accumulationFund_file__name': '李以权2023-08-01_公积金账户信息.png', 'accumulationFund_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_公积金账户信息.png', 'workPhotos_file__id': 396, 'workPhotos_file__name': '李以权2023-08-01_工作照片.png', 'workPhotos_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_工作照片.png', 'workVideo_file__id': 395, 'workVideo_file__name': '李以权2023-08-01_工作视频.mp4', 'workVideo_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_工作视频.mp4', 'dailyPhotos_file__id': 400, 'dailyPhotos_file__name': '李以权2023-08-01_日常照片.mp4', 'dailyPhotos_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_日常照片.mp4', 'dailyVideo_file__id': 399, 'dailyVideo_file__name': '李以权2023-08-01_日常视频.docx', 'dailyVideo_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_日常视频.docx', 'incumbency_file__id': 394, 'incumbency_file__name': '李以权2023-08-01_在职证明.png', 'incumbency_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_在职证明.png', 'noWork_file__id': 401, 'noWork_file__name': '李以权2023-08-01_无工作承诺函.docx', 'noWork_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_无工作承诺函.docx', 'cllBack_file__id': 402, 'cllBack_file__name': '李以权2023-08-01_电话回访录音.mp3', 'cllBack_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_电话回访录音.mp3', 'firstlivevideo_file__id': 403, 'firstlivevideo_file__name': '李以权2023-08-01_实时视频(第一次).mp4', 'firstlivevideo_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_实时视频(第一次).mp4', 'secondlivevideo_file__id': 404, 'secondlivevideo_file__name': '李以权2023-08-01_实时视频(第二次).mp4', 'secondlivevideo_file__url': 'static/competeRestrictionsFile/upload_file/2023-08-10/李以权_320924198611062130/李以权2023-08-01_实时视频(第二次).mp4'}]
# # # # # # # # # # # # #
# # # # # # # # # # # # # json_data = json.dumps(data,indent=4)
# # # # # # # # # # # # # print(json_data)
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # import datetime
# # # # # # # # # # # # # # # a = [{'id': 8314, 'expatriate_Begin': datetime.date(2023, 1, 15), 'expatriate_End': datetime.date(2023, 4, 15)}, {'id': 8313, 'expatriate_Begin': datetime.date(2023, 1, 11), 'expatriate_End': datetime.date(2023, 2, 28)}, {'id': 8312, 'expatriate_Begin': datetime.date(2023, 8, 1), 'expatriate_End': datetime.date(2023, 9, 30)}, {'id': 8267, 'expatriate_Begin': None, 'expatriate_End': None}, {'id': 6613, 'expatriate_Begin': datetime.date(2023, 1, 27), 'expatriate_End': datetime.date(2024, 1, 27)}, {'id': 6610, 'expatriate_Begin': datetime.date(2023, 1, 11), 'expatriate_End': datetime.date(2023, 2, 28)}, {'id': 6609, 'expatriate_Begin': None, 'expatriate_End': None}, {'id': 5817, 'expatriate_Begin': datetime.date(2023, 1, 15), 'expatriate_End': datetime.date(2023, 4, 14)}, {'id': 5816, 'expatriate_Begin': datetime.date(2023, 1, 19), 'expatriate_End': datetime.date(2023, 4, 18)}]
# # # # # # # # # # # # # # # b = [{'people__id': 6609, 'departure_time': datetime.datetime(2023, 8, 18, 17, 7, 52), 'arrival_time': datetime.datetime(2023, 8, 17, 17, 7, 56)}, {'people__id': 8313, 'departure_time': None, 'arrival_time': None}, {'people__id': 8313, 'departure_time': datetime.datetime(2023, 9, 9, 0, 0), 'arrival_time': datetime.datetime(2023, 8, 25, 0, 0)}, {'people__id': 8314, 'departure_time': None, 'arrival_time': None}, {'people__id': 5817, 'departure_time': datetime.datetime(2023, 8, 23, 0, 0), 'arrival_time': datetime.datetime(2023, 8, 10, 0, 0)}, {'people__id': 5816, 'departure_time': datetime.datetime(2023, 8, 23, 0, 0), 'arrival_time': datetime.datetime(2023, 8, 10, 0, 0)}]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for item in a:
# # # # # # # # # # # # # # #     max_arrival_time = None
# # # # # # # # # # # # # # #     for b_item in b:
# # # # # # # # # # # # # # #         if b_item['people__id'] == item['id']:
# # # # # # # # # # # # # # #             if item['expatriate_Begin'] and item['expatriate_End']:
# # # # # # # # # # # # # # #                 print(item['expatriate_Begin'] ,b_item['arrival_time'],item['expatriate_End'])
# # # # # # # # # # # # # # #                 if (
# # # # # # # # # # # # # # #                     item['expatriate_Begin'] <= b_item['arrival_time'] <= item['expatriate_End'] and (not max_arrival_time or b_item['arrival_time'] > max_arrival_time)
# # # # # # # # # # # # # # #                 ):
# # # # # # # # # # # # # # #                     max_arrival_time = b_item['arrival_time']
# # # # # # # # # # # # # # #     item['max_arrival_time'] = max_arrival_time
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # a = [{'id': 8314, 'expatriate_Begin': datetime.date(2023, 1, 15), 'expatriate_End': datetime.date(2023, 4, 15)},
# # # # # # # # # # # # # # #      {'id': 8313, 'expatriate_Begin': datetime.date(2023, 1, 11), 'expatriate_End': datetime.date(2023, 2, 28)},
# # # # # # # # # # # # # # #      {'id': 8312, 'expatriate_Begin': datetime.date(2023, 8, 1), 'expatriate_End': datetime.date(2023, 9, 30)},
# # # # # # # # # # # # # # #      {'id': 8267, 'expatriate_Begin': None, 'expatriate_End': None},
# # # # # # # # # # # # # # #      {'id': 6613, 'expatriate_Begin': datetime.date(2023, 1, 27), 'expatriate_End': datetime.date(2024, 1, 27)},
# # # # # # # # # # # # # # #      {'id': 6610, 'expatriate_Begin': datetime.date(2023, 1, 11), 'expatriate_End': datetime.date(2023, 2, 28)},
# # # # # # # # # # # # # # #      {'id': 6609, 'expatriate_Begin': None, 'expatriate_End': None},
# # # # # # # # # # # # # # #      {'id': 5817, 'expatriate_Begin': datetime.date(2023, 1, 15), 'expatriate_End': datetime.date(2023, 4, 14)},
# # # # # # # # # # # # # # #      {'id': 5816, 'expatriate_Begin': datetime.date(2023, 1, 19), 'expatriate_End': datetime.date(2023, 4, 18)}]
# # # # # # # # # # # # # # # b = [{'people__id': 6609, 'departure_time': datetime.datetime(2023, 8, 18, 17, 7, 52),
# # # # # # # # # # # # # # #       'arrival_time': datetime.datetime(2023, 8, 17, 17, 7, 56)},
# # # # # # # # # # # # # # #      {'people__id': 8313, 'departure_time': None, 'arrival_time': None},
# # # # # # # # # # # # # # #      {'people__id': 8313, 'departure_time': datetime.datetime(2023, 9, 9, 0, 0),
# # # # # # # # # # # # # # #       'arrival_time': datetime.datetime(2023, 8, 25, 0, 0)},
# # # # # # # # # # # # # # #      {'people__id': 8314, 'departure_time': None, 'arrival_time': None},
# # # # # # # # # # # # # # #      {'people__id': 5817, 'departure_time': datetime.datetime(2023, 8, 23, 0, 0),
# # # # # # # # # # # # # # #       'arrival_time': datetime.datetime(2023, 8, 10, 0, 0)},
# # # # # # # # # # # # # # #      {'people__id': 5816, 'departure_time': datetime.datetime(2023, 8, 23, 0, 0),
# # # # # # # # # # # # # # #       'arrival_time': datetime.datetime(2023, 8, 10, 0, 0)}]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # max_arrival_times = {}
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for dict_a in a:
# # # # # # # # # # # # # # #     id_a = dict_a['id']
# # # # # # # # # # # # # # #     max_arrival_time = None
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     for dict_b in b:
# # # # # # # # # # # # # # #         if dict_b['people__id'] == id_a:
# # # # # # # # # # # # # # #             arrival_time = dict_b['arrival_time']
# # # # # # # # # # # # # # #             if arrival_time is None:
# # # # # # # # # # # # # # #                 continue
# # # # # # # # # # # # # # #             if max_arrival_time is None or arrival_time > max_arrival_time:
# # # # # # # # # # # # # # #                 max_arrival_time = arrival_time
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     max_arrival_times[id_a] = max_arrival_time
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(max_arrival_times)
# # # # # # # # # # # # # # # print("+++++++++++++++++++")
# # # # # # # # # # # # # # # for item_a in a:
# # # # # # # # # # # # # # #     max_arrival_time = None
# # # # # # # # # # # # # # #     max_departure_time = None
# # # # # # # # # # # # # # #     for item_b in b:
# # # # # # # # # # # # # # #         if item_a['id'] == item_b['people__id']:
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #             if item_a['expatriate_Begin'] <= item_b['arrival_time'] <= item_a['expatriate_End']:
# # # # # # # # # # # # # # #                 max_arrival_time = max(max_arrival_time, item_b['arrival_time'])
# # # # # # # # # # # # # # #             if item_a['expatriate_Begin'] <= item_b['departure_time'] <= item_a['expatriate_End']:
# # # # # # # # # # # # # # #                 max_departure_time = max(max_departure_time, item_b['departure_time'])
# # # # # # # # # # # # # # #     item_a['max_arrival_time'] = max_arrival_time
# # # # # # # # # # # # # # #     item_a['max_departure_time'] = max_departure_time
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # for item_a in a:
# # # # # # # # # # # # # # #     max_arrival_time = None
# # # # # # # # # # # # # # #     max_departure_time = None
# # # # # # # # # # # # # # #     for item_b in b:
# # # # # # # # # # # # # # #         if item_a['id'] == item_b['people__id']:
# # # # # # # # # # # # # # #             if item_a['expatriate_Begin'] <= item_b['arrival_time'] <= item_a['expatriate_End']:
# # # # # # # # # # # # # # #                 if max_arrival_time is None or item_b['arrival_time'] > max_arrival_time:
# # # # # # # # # # # # # # #                     max_arrival_time = item_b['arrival_time']
# # # # # # # # # # # # # # #             if item_a['expatriate_Begin'] <= item_b['departure_time'] <= item_a['expatriate_End']:
# # # # # # # # # # # # # # #                 if max_departure_time is None or item_b['departure_time'] > max_arrival_time:
# # # # # # # # # # # # # # #                     max_departure_time = item_b['departure_time']
# # # # # # # # # # # # # # #     item_a['max_arrival_time'] = max_arrival_time
# # # # # # # # # # # # # # #     item_a['max_departure_time'] = max_departure_time
# # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # a = [{'id': 8314, 'expatriate_Begin': datetime.date(2023, 1, 15), 'expatriate_End': datetime.date(2023, 4, 15)}, {'id': 8313, 'expatriate_Begin': datetime.date(2023, 1, 11), 'expatriate_End': datetime.date(2023, 2, 28)}, {'id': 8312, 'expatriate_Begin': datetime.date(2023, 8, 1), 'expatriate_End': datetime.date(2023, 9, 30)}, {'id': 8267, 'expatriate_Begin': None, 'expatriate_End': None}, {'id': 6613, 'expatriate_Begin': datetime.date(2023, 1, 27), 'expatriate_End': datetime.date(2024, 1, 27)}, {'id': 6610, 'expatriate_Begin': datetime.date(2023, 1, 11), 'expatriate_End': datetime.date(2023, 2, 28)}, {'id': 6609, 'expatriate_Begin': None, 'expatriate_End': None}, {'id': 5817, 'expatriate_Begin': datetime.date(2023, 1, 15), 'expatriate_End': datetime.date(2023, 4, 14)}, {'id': 5816, 'expatriate_Begin': datetime.date(2023, 1, 19), 'expatriate_End': datetime.date(2023, 4, 18)}]
# # # # # # # # # # # # # # # b = [{'people__id': 6609, 'departure_time': datetime.datetime(2023, 8, 18, 17, 7, 52), 'arrival_time': datetime.datetime(2023, 8, 17, 17, 7, 56)}, {'people__id': 8313, 'departure_time': None, 'arrival_time': None}, {'people__id': 8313, 'departure_time': datetime.datetime(2023, 9, 9, 0, 0), 'arrival_time': datetime.datetime(2023, 8, 25, 0, 0)}, {'people__id': 8314, 'departure_time': None, 'arrival_time': None}, {'people__id': 5817, 'departure_time': datetime.datetime(2023, 8, 23, 0, 0), 'arrival_time': datetime.datetime(2023, 8, 10, 0, 0)}, {'people__id': 5816, 'departure_time': datetime.datetime(2023, 8, 23, 0, 0), 'arrival_time': datetime.datetime(2023, 8, 10, 0, 0)}]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for item_a in a:
# # # # # # # # # # # # # # #     id_a = item_a['id']
# # # # # # # # # # # # # # #     max_arrival_time = None
# # # # # # # # # # # # # # #     max_departure_time = None
# # # # # # # # # # # # # # #     for item_b in b:
# # # # # # # # # # # # # # #         if item_b['people__id'] == id_a:
# # # # # # # # # # # # # # #             if item_a['expatriate_Begin'] <= item_b['arrival_time'] <= item_a['expatriate_End']:
# # # # # # # # # # # # # # #                 if max_arrival_time is None or item_b['arrival_time'] > max_arrival_time:
# # # # # # # # # # # # # # #                     max_arrival_time = item_b['arrival_time']
# # # # # # # # # # # # # # #             if item_a['expatriate_Begin'] <= item_b['departure_time'] <= item_a['expatriate_End']:
# # # # # # # # # # # # # # #                 if max_departure_time is None or item_b['departure_time'] > max_departure_time:
# # # # # # # # # # # # # # #                     max_departure_time = item_b['departure_time']
# # # # # # # # # # # # # # #     item_a['arrival_time'] = max_arrival_time
# # # # # # # # # # # # # # #     item_a['departure_time'] = max_departure_time
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # a = [{'id': 8314, 'expatriate_Begin': datetime.datetime(2023, 1, 15), 'expatriate_End': datetime.datetime(2023, 4, 15)}, {'id': 8313, 'expatriate_Begin': datetime.datetime(2023, 1, 11), 'expatriate_End': datetime.datetime(2023, 2, 28)}, {'id': 8312, 'expatriate_Begin': datetime.datetime(2023, 8, 1), 'expatriate_End': datetime.datetime(2023, 9, 30)}, {'id': 8267, 'expatriate_Begin': None, 'expatriate_End': None}, {'id': 5817, 'expatriate_Begin': datetime.datetime(2023, 1, 15), 'expatriate_End': datetime.datetime(2023, 4, 14)}, {'id': 5816, 'expatriate_Begin': datetime.datetime(2023, 1, 19), 'expatriate_End': datetime.datetime(2023, 4, 18)}]
# # # # # # # # # # # # # # # b = [{'people__id': 6609, 'departure_time': datetime.datetime(2023, 8, 18, 17, 7, 52), 'arrival_time': datetime.datetime(2023, 8, 17, 17, 7, 56)}, {'people__id': 8313, 'departure_time': None, 'arrival_time': None},{'people__id': 5816, 'departure_time': datetime.datetime(2023, 8, 23, 0, 0), 'arrival_time': datetime.datetime(2023, 8, 10, 0, 0)}]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for item_b in b:
# # # # # # # # # # # # # # #     max_arrival_time = None
# # # # # # # # # # # # # # #     max_departure_time = None
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     for item_a in a:
# # # # # # # # # # # # # # #         if item_a['id'] == item_b['people__id']:
# # # # # # # # # # # # # # #             if item_a['expatriate_Begin'] and item_a['expatriate_End'] and item_b['arrival_time'] and item_b['departure_time']:
# # # # # # # # # # # # # # #                 if item_a['expatriate_Begin'] <= item_b['arrival_time'] <= item_a['expatriate_End']:
# # # # # # # # # # # # # # #                     if max_arrival_time is None or item_b['arrival_time'] > max_arrival_time:
# # # # # # # # # # # # # # #                         max_arrival_time = item_b['arrival_time']
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #                 if item_a['expatriate_Begin'] <= item_b['departure_time'] <= item_a['expatriate_End']:
# # # # # # # # # # # # # # #                     if max_departure_time is None or item_b['departure_time'] > max_departure_time:
# # # # # # # # # # # # # # #                         max_departure_time = item_b['departure_time']
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     item_b['max_arrival_time'] = max_arrival_time
# # # # # # # # # # # # # # #     item_b['max_departure_time'] = max_departure_time
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # # print("+++++++++++")
# # # # # # # # # # # # # # # a = [{'id': 8314, 'expatriate_Begin': datetime.date(2023, 1, 15), 'expatriate_End': datetime.date(2023, 4, 15)}, {'id': 8313, 'expatriate_Begin': datetime.date(2023, 1, 11), 'expatriate_End': datetime.date(2023, 2, 28)}, {'id': 8312, 'expatriate_Begin': datetime.date(2023, 8, 1), 'expatriate_End': datetime.date(2023, 9, 30)}, {'id': 8267, 'expatriate_Begin': None, 'expatriate_End': None}, {'id': 5817, 'expatriate_Begin': datetime.date(2023, 1, 15), 'expatriate_End': datetime.date(2023, 4, 14)}, {'id': 5816, 'expatriate_Begin': datetime.date(2023, 1, 19), 'expatriate_End': datetime.date(2023, 4, 18)}]
# # # # # # # # # # # # # # # b = [{'people__id': 6609, 'departure_time': datetime.datetime(2023, 8, 18, 17, 7, 52), 'arrival_time': datetime.datetime(2023, 8, 17, 17, 7, 56)}, {'people__id': 8313, 'departure_time': None, 'arrival_time': None},{'people__id': 5816, 'departure_time': datetime.datetime(2023, 8, 23, 0, 0), 'arrival_time': datetime.datetime(2023, 8, 10, 0, 0)}]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # result = {}
# # # # # # # # # # # # # # # for item_a in a:
# # # # # # # # # # # # # # #     item_id = item_a['id']
# # # # # # # # # # # # # # #     max_departure_time = None
# # # # # # # # # # # # # # #     max_arrival_time = None
# # # # # # # # # # # # # # #     for item_b in b:
# # # # # # # # # # # # # # #         if item_b['people__id'] == item_id:
# # # # # # # # # # # # # # #             departure_time = item_b['departure_time']
# # # # # # # # # # # # # # #             arrival_time = item_b['arrival_time']
# # # # # # # # # # # # # # #             if departure_time is None:
# # # # # # # # # # # # # # #                 max_departure_time = None
# # # # # # # # # # # # # # #             elif max_departure_time is None or departure_time > max_departure_time:
# # # # # # # # # # # # # # #                 max_departure_time = departure_time
# # # # # # # # # # # # # # #             if arrival_time is None:
# # # # # # # # # # # # # # #                 max_arrival_time = None
# # # # # # # # # # # # # # #             elif max_arrival_time is None or arrival_time > max_arrival_time:
# # # # # # # # # # # # # # #                 max_arrival_time = arrival_time
# # # # # # # # # # # # # # #     result[item_id] = {'max_departure_time': max_departure_time, 'max_arrival_time': max_arrival_time}
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(result)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # a=[{'code': '1010000433', 'name': '徐家杰', 'date_Of_Entry': datetime.datetime(2023, 3, 22, 0, 0), 'expatriate_Dept': '全球财务中心 审计监察中心 内审部（西南区域）', 'post': '内审专员', 'expatriate_jobRank': None, 'expatriate_Before_Base': '全球财务中心', 'expatriate_Before_Manage': '全球财务中心', 'expatriate_Before_Factory': '全球财务中心', 'resident_Dept': '全球财务中心 审计监察中心 内审部（西南区域）', 'expatriate_Cycle': '6月', 'expatriate_Begin': datetime.datetime(2023, 4, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 5, 0, 0), 'isCross_Division': 0, 'expatriate_After_Base': '全球财务中心', 'expatriate_After_Manage': '全球财务中心', 'expatriate_After_Factory': '全球财务中心', 'expatriate_Reason': '去云南基地开展工程审计工作', 'expatriate_Target': None, 'expatriate_Allowance': '按照公司规定发放', 'description_Allowance': '按照公司规定发放', 'expatriate_Type': '平级外派', 'expatriate_After_Cost': '全球财务中心', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 4, 1, 13, 30, 32, 717000)},
# # # # # # # # # # # # # # #    {'code': '1010000452', 'name': '余文飞', 'date_Of_Entry': datetime.datetime(2023, 3, 29, 0, 0), 'expatriate_Dept': '全球财务中心 审计监察中心 内审部（西南区域）', 'post': '内审中级专员', 'expatriate_jobRank': None, 'expatriate_Before_Base': '全球财务中心', 'expatriate_Before_Manage': '全球财务中心', 'expatriate_Before_Factory': '全球财务中心', 'resident_Dept': '全球财务中心 审计监察中心 内审部（西南区域）', 'expatriate_Cycle': '6月', 'expatriate_Begin': datetime.datetime(2023, 4, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 5, 0, 0), 'isCross_Division': 0, 'expatriate_After_Base': '全球财务中心', 'expatriate_After_Manage': '全球财务中心', 'expatriate_After_Factory': '全球财务中心', 'expatriate_Reason': '赴云南基地开展审计工作', 'expatriate_Target': None, 'expatriate_Allowance': '按照公司规定发放', 'description_Allowance': '按照公司规定发放', 'expatriate_Type': '平级外派', 'expatriate_After_Cost': '全球财务中心', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 4, 1, 13, 32, 0, 650000)},
# # # # # # # # # # # # # # #    {'code': '1010000450', 'name': '李智', 'date_Of_Entry': datetime.datetime(2023, 3, 29, 0, 0), 'expatriate_Dept': '全球财务中心 审计监察中心 内审部（西南区域）', 'post': '内审高级经理', 'expatriate_jobRank': None, 'expatriate_Before_Base': '全球财务中心', 'expatriate_Before_Manage': '全球财务中心', 'expatriate_Before_Factory': '全球财务中心', 'resident_Dept': '全球财务中心', 'expatriate_Cycle': '6月', 'expatriate_Begin': datetime.datetime(2023, 4, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 5, 0, 0), 'isCross_Division': 0, 'expatriate_After_Base': '全球财务中心', 'expatriate_After_Manage': '全球财务中心', 'expatriate_After_Factory': '全球财务中心', 'expatriate_Reason': '赴云南基地开展审计工作', 'expatriate_Target': None, 'expatriate_Allowance': '按照公司制度发放津贴', 'description_Allowance': '按照公司制度发放津贴', 'expatriate_Type': '平级外派', 'expatriate_After_Cost': '全球财务中心', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 4, 1, 13, 25, 33, 740000)},
# # # # # # # # # # # # # # #    {'code': '2060000515', 'name': '吴少政', 'date_Of_Entry': datetime.datetime(2023, 3, 31, 0, 0), 'expatriate_Dept': '组件事业部 润阳泰国四期组件 质量部（泰国四期组件）', 'post': ' 泰国四期IQC主管', 'expatriate_jobRank': None, 'expatriate_Before_Base': '组件事业部', 'expatriate_Before_Manage': '江苏海博瑞', 'expatriate_Before_Factory': '江苏海博瑞', 'resident_Dept': '组件事业部 润阳泰国四期组件 质量部（泰国四期组件）', 'expatriate_Cycle': '1年', 'expatriate_Begin': datetime.datetime(2023, 4, 10, 0, 0), 'expatriate_End': datetime.datetime(2024, 4, 10, 0, 0), 'isCross_Division': 0, 'expatriate_After_Base': '组件事业部', 'expatriate_After_Manage': '泰国P4组件厂', 'expatriate_After_Factory': '泰国P4组件厂', 'expatriate_Reason': '泰国四期新员工（外派时间以实际抵泰时间为准）\r\n', 'expatriate_Target': None, 'expatriate_Allowance': '10000元人民币', 'description_Allowance': 'SAL经理级以下;', 'expatriate_Type': '平级外派', 'expatriate_After_Cost': '泰国组件四期', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 4, 3, 18, 17, 36, 253000)},
# # # # # # # # # # # # # # #    {'code': '2060000235', 'name': '刘振', 'date_Of_Entry': datetime.datetime(2022, 12, 13, 0, 0), 'expatriate_Dept': '组件事业部 江苏海博瑞光伏科技有限公司 设备设施部', 'post': '设备倒班工程师', 'expatriate_jobRank': None, 'expatriate_Before_Base': '组件事业部', 'expatriate_Before_Manage': '江苏海博瑞', 'expatriate_Before_Factory': '江苏海博瑞', 'resident_Dept': '组件事业部 江苏海博瑞光伏科技有限公司 设备设施部', 'expatriate_Cycle': '1年', 'expatriate_Begin': datetime.datetime(2023, 4, 23, 0, 0), 'expatriate_End': datetime.datetime(2024, 4, 23, 0, 0), 'isCross_Division': 0, 'expatriate_After_Base': '组件事业部', 'expatriate_After_Manage': '江苏海博瑞', 'expatriate_After_Factory': '江苏海博瑞', 'expatriate_Reason': '支援泰国四期（外派时间以实际抵泰时间为准）', 'expatriate_Target': None, 'expatriate_Allowance': '10000', 'description_Allowance': '工程师：10000元/月', 'expatriate_Type': '平级外派', 'expatriate_After_Cost': '江苏海博瑞', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 4, 4, 8, 22, 50, 3000)},
# # # # # # # # # # # # # # #    {'code': '2060000490', 'name': '李栋', 'date_Of_Entry': datetime.datetime(2023, 3, 21, 0, 0), 'expatriate_Dept': '组件事业部 润阳泰国四期组件 设施部（泰国四期组件）', 'post': ' 电气倒班工程师', 'expatriate_jobRank': None, 'expatriate_Before_Base': '组件事业部', 'expatriate_Before_Manage': '江苏海博瑞', 'expatriate_Before_Factory': '江苏海博瑞', 'resident_Dept': '组件事业部 润阳泰国四期组件 设施部（泰国四期组件）', 'expatriate_Cycle': '1年', 'expatriate_Begin': datetime.datetime(2023, 3, 21, 0, 0), 'expatriate_End': datetime.datetime(2024, 3, 21, 0, 0), 'isCross_Division': 0, 'expatriate_After_Base': '组件事业部', 'expatriate_After_Manage': '泰国P4组件厂', 'expatriate_After_Factory': '泰国P4组件厂', 'expatriate_Reason': '泰国四期新员工，外派时间以实际抵泰时间为准。', 'expatriate_Target': None, 'expatriate_Allowance': '10000元人民币', 'description_Allowance': 'SAL经理级别以下;', 'expatriate_Type': '平级外派', 'expatriate_After_Cost': '泰国组件四期', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 4, 4, 17, 50, 33, 743000)},
# # # # # # # # # # # # # # #    {'code': '2060000523', 'name': '薛远航', 'date_Of_Entry': datetime.datetime(2023, 4, 3, 0, 0), 'expatriate_Dept': '组件事业部 润阳泰国四期组件 设备部（泰国四期组件）', 'post': '设备倒班工程师', 'expatriate_jobRank': None, 'expatriate_Before_Base': '组件事业部', 'expatriate_Before_Manage': '江苏海博瑞', 'expatriate_Before_Factory': '江苏海博瑞', 'resident_Dept': '组件事业部 润阳泰国四期组件 设备部（泰国四期组件）', 'expatriate_Cycle': '1年', 'expatriate_Begin': datetime.datetime(2023, 5, 4, 0, 0), 'expatriate_End': datetime.datetime(2024, 5, 3, 0, 0), 'isCross_Division': 0, 'expatriate_After_Base': '组件事业部', 'expatriate_After_Manage': '泰国P4组件厂', 'expatriate_After_Factory': '泰国P4组件厂', 'expatriate_Reason': '泰国四期组件新员工，外派时间以实际抵泰时间为准！', 'expatriate_Target': None, 'expatriate_Allowance': '10000元', 'description_Allowance': 'SAL经理级以下', 'expatriate_Type': '平级外派', 'expatriate_After_Cost': '泰国组件四期', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 4, 8, 21, 18, 57, 150000)},
# # # # # # # # # # # # # # #    {'code': '2060000235', 'name': '刘振', 'date_Of_Entry': datetime.datetime(2022, 12, 13, 0, 0), 'expatriate_Dept': '组件事业部 江苏海博瑞光伏科技有限公司 设备设施部', 'post': '设备倒班工程师', 'expatriate_jobRank': None, 'expatriate_Before_Base': '组件事业部', 'expatriate_Before_Manage': '江苏海博瑞', 'expatriate_Before_Factory': '江苏海博瑞', 'resident_Dept': '组件事业部 江苏海博瑞光伏科技有限公司 设备设施部', 'expatriate_Cycle': '1年', 'expatriate_Begin': datetime.datetime(2023, 5, 4, 0, 0), 'expatriate_End': datetime.datetime(2024, 5, 3, 0, 0), 'isCross_Division': 0, 'expatriate_After_Base': '组件事业部', 'expatriate_After_Manage': '泰国P4组件厂', 'expatriate_After_Factory': '泰国P4组件厂', 'expatriate_Reason': '支援泰国四期（外派时间以实际抵泰时间为准）', 'expatriate_Target': None, 'expatriate_Allowance': '10000元', 'description_Allowance': 'SAL经理级以下', 'expatriate_Type': '平级外派', 'expatriate_After_Cost': '泰国组件四期', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 4, 8, 21, 41, 43, 677000)},
# # # # # # # # # # # # # # #    {'code': '2060000058', 'name': '包小翠', 'date_Of_Entry': datetime.datetime(2022, 7, 12, 0, 0), 'expatriate_Dept': '组件事业部 江苏海博瑞光伏科技有限公司 生产部96', 'post': '生产班长', 'expatriate_jobRank': None, 'expatriate_Before_Base': '组件事业部', 'expatriate_Before_Manage': '江苏海博瑞', 'expatriate_Before_Factory': '江苏海博瑞', 'resident_Dept': '组件事业部 润阳泰国四期组件 生产部（泰国四期组件）', 'expatriate_Cycle': '1年', 'expatriate_Begin': datetime.datetime(2023, 4, 20, 0, 0), 'expatriate_End': datetime.datetime(2024, 4, 20, 0, 0), 'isCross_Division': 0, 'expatriate_After_Base': '组件事业部', 'expatriate_After_Manage': '江苏海博瑞', 'expatriate_After_Factory': '江苏海博瑞', 'expatriate_Reason': '\t工作需要', 'expatriate_Target': None, 'expatriate_Allowance': '7000', 'description_Allowance': '班长：7000元/月', 'expatriate_Type': '平级外派', 'expatriate_After_Cost': '江苏海博瑞', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 4, 12, 8, 4, 1, 787000)},
# # # # # # # # # # # # # # #    {'code': '2060000117', 'name': '顾笑', 'date_Of_Entry': datetime.datetime(2022, 11, 22, 0, 0), 'expatriate_Dept': '组件事业部 江苏海博瑞光伏科技有限公司 生产部96', 'post': '生产班长', 'expatriate_jobRank': None, 'expatriate_Before_Base': '组件事业部', 'expatriate_Before_Manage': '江苏海博瑞', 'expatriate_Before_Factory': '江苏海博瑞', 'resident_Dept': '组件事业部 润阳泰国四期组件 生产部（泰国四期组件）', 'expatriate_Cycle': '1年', 'expatriate_Begin': datetime.datetime(2023, 4, 20, 0, 0), 'expatriate_End': datetime.datetime(2024, 4, 20, 0, 0), 'isCross_Division': 0, 'expatriate_After_Base': '组件事业部', 'expatriate_After_Manage': '江苏海博瑞', 'expatriate_After_Factory': '江苏海博瑞', 'expatriate_Reason': '\t工作需要', 'expatriate_Target': None, 'expatriate_Allowance': '7000', 'description_Allowance': '班长：7000元/月', 'expatriate_Type': '平级外派', 'expatriate_After_Cost': '江苏海博瑞', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 4, 13, 8, 2, 30, 990000)},
# # # # # # # # # # # # # # #    {'code': '2060000154', 'name': '廖立胜', 'date_Of_Entry': datetime.datetime(2022, 11, 29, 0, 0), 'expatriate_Dept': '组件事业部 江苏海博瑞光伏科技有限公司 生产部96', 'post': '生产班长', 'expatriate_jobRank': None, 'expatriate_Before_Base': '组件事业部', 'expatriate_Before_Manage': '江苏海博瑞', 'expatriate_Before_Factory': '江苏海博瑞', 'resident_Dept': '组件事业部 润阳泰国四期组件 生产部（泰国四期组件）', 'expatriate_Cycle': '1年', 'expatriate_Begin': datetime.datetime(2023, 4, 20, 0, 0), 'expatriate_End': datetime.datetime(2024, 4, 20, 0, 0), 'isCross_Division': 0, 'expatriate_After_Base': '组件事业部', 'expatriate_After_Manage': '江苏海博瑞', 'expatriate_After_Factory': '江苏海博瑞', 'expatriate_Reason': '\t工作需要', 'expatriate_Target': None, 'expatriate_Allowance': '7000', 'description_Allowance': '班长：7000元/月', 'expatriate_Type': '平级外派', 'expatriate_After_Cost': '江苏海博瑞', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 4, 17, 10, 54, 15, 773000)},
# # # # # # # # # # # # # # #    {'code': '2060000381', 'name': '赵洋涛', 'date_Of_Entry': datetime.datetime(2023, 2, 20, 0, 0), 'expatriate_Dept': '组件事业部 江苏海博瑞光伏科技有限公司 生产部96', 'post': '生产班长', 'expatriate_jobRank': None, 'expatriate_Before_Base': '组件事业部', 'expatriate_Before_Manage': '江苏海博瑞', 'expatriate_Before_Factory': '江苏海博瑞', 'resident_Dept': '组件事业部 润阳泰国四期组件 生产部（泰国四期组件）', 'expatriate_Cycle': '1年', 'expatriate_Begin': datetime.datetime(2023, 4, 20, 0, 0), 'expatriate_End': datetime.datetime(2024, 4, 20, 0, 0), 'isCross_Division': 0, 'expatriate_After_Base': '组件事业部', 'expatriate_After_Manage': '江苏海博瑞', 'expatriate_After_Factory': '江苏海博瑞', 'expatriate_Reason': '工作需要', 'expatriate_Target': None, 'expatriate_Allowance': '7000', 'description_Allowance': '班长：7000元/月', 'expatriate_Type': '平级外派', 'expatriate_After_Cost': '江苏海博瑞', 'doc_status': '30', 'fd_ended_time': datetime.datetime(2023, 4, 12, 8, 2, 19, 547000)},
# # # # # # # # # # # # # # #    {'code': '1030000088', 'name': '高扬',  'expatriate_Begin': datetime.datetime(2023, 4, 20, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 20, 0, 0)},
# # # # # # # # # # # # # # #    {'code': '2050001360', 'name': '魏旭锦', 'expatriate_Begin': datetime.datetime(2023, 3, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 3, 1, 0, 0), },
# # # # # # # # # # # # # # #    {'code': '2010009608', 'name': '俞伟',   'expatriate_Begin': datetime.datetime(2023, 3, 23, 0, 0), 'expatriate_End': datetime.datetime(2024, 3, 22, 0, 0),}]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # import datetime
# # # # # # # # # # # # # # # a = [
# # # # # # # # # # # # # # #     {'code': '6030000532', 'name': '徐宇龙',  'expatriate_Begin': datetime.datetime(2023, 7, 12, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 11, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6030000585', 'name': '张雄虎', 'expatriate_Begin':None , 'expatriate_End': datetime.datetime(2024, 7, 11, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '1020000219', 'name': '赵越',  'expatriate_Begin': datetime.datetime(2023, 7, 12, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 11, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6010004073', 'name': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 1, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '1010000564', 'name': '司建东', 'expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 1, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6010004073', 'name': '阿连克沙',  'expatriate_Begin': datetime.datetime(2023, 7, 10, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 9, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6030000585', 'name': '张雄虎','expatriate_Begin': datetime.datetime(2023, 7, 4, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 3, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6030000603', 'name': '聂雨轩', 'expatriate_Begin': None, 'expatriate_End': datetime.datetime(2024, 6, 30, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '2010000566', 'name': '梁成才',  'expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 9, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6030000532', 'name': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023, 7, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 30, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6030000585', 'name': '张雄虎',  'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 13, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6010004073', 'name': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 13, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 31, 0, 0)},
# # # # # # # # # # # # # # #         {'code': '6010004073', 'name': '阿连克沙', 'expatriate_Begin':None, 'expatriate_End': datetime.datetime(2024, 7, 31, 0, 0)}
# # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # grouped_values = {}
# # # # # # # # # # # # # # # for item in a:
# # # # # # # # # # # # # # #     code = item['code']
# # # # # # # # # # # # # # #     expatriate_Begin = item['expatriate_Begin']
# # # # # # # # # # # # # # #     if code in grouped_values:
# # # # # # # # # # # # # # #         grouped_values[code].append(expatriate_Begin)
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         grouped_values[code] = [expatriate_Begin]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(grouped_values)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # from operator import itemgetter
# # # # # # # # # # # # # # # sorted_list = sorted(a, key=itemgetter('expatriate_Begin'), reverse=True)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Create a new list of dictionaries with the same 'code' and a list of 'expatriate_Begin' values
# # # # # # # # # # # # # # # expatriate_Begin_list = []
# # # # # # # # # # # # # # # for item in sorted_list:
# # # # # # # # # # # # # # #     code = item['code']
# # # # # # # # # # # # # # #     expatriate_Begin = item['expatriate_Begin']
# # # # # # # # # # # # # # #     for dict_item in expatriate_Begin_list:
# # # # # # # # # # # # # # #         if dict_item['code'] == code:
# # # # # # # # # # # # # # #             dict_item['begin_time_list'].append(expatriate_Begin)
# # # # # # # # # # # # # # #             break
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         expatriate_Begin_list.append({'code': code, 'begin_time_list': [expatriate_Begin]})
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(expatriate_Begin_list)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # expatriate_Begin_list = {}
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for item in a:
# # # # # # # # # # # # # # #     code = item['code']
# # # # # # # # # # # # # # #     expatriate_Begin = item['expatriate_Begin']
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     if code in expatriate_Begin_list:
# # # # # # # # # # # # # # #         if item['expatriate_Begin'] is not None:
# # # # # # # # # # # # # # #             expatriate_Begin_list[code]['time_list'].append(expatriate_Begin)
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         expatriate_Begin_list[code] = {'code': code, 'time_list': [expatriate_Begin]}
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for code in expatriate_Begin_list:
# # # # # # # # # # # # # # #     expatriate_Begin_list[code]['time_list'].sort(reverse=True)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(expatriate_Begin_list)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # expatriate_Begin_list = {}
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for item in a:
# # # # # # # # # # # # # # #     code = item['code']
# # # # # # # # # # # # # # #     expatriate_Begin = item['expatriate_Begin']
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     if expatriate_Begin is not None:
# # # # # # # # # # # # # # #         if code not in expatriate_Begin_list:
# # # # # # # # # # # # # # #             expatriate_Begin_list[code] = []
# # # # # # # # # # # # # # #         expatriate_Begin_list[code].append(expatriate_Begin)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for code in expatriate_Begin_list:
# # # # # # # # # # # # # # #     expatriate_Begin_list[code].sort(reverse=True)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(expatriate_Begin_list)
# # # # # # # # # # # # # # # [{'code':'6030000532','begin_list':[datetime.datetime(2023, 7, 12, 0, 0), datetime.datetime(2023, 7, 1, 0, 0)],'end_list':[]}]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # a = [
# # # # # # # # # # # # # # #     {'code': '6030000532', 'name': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023, 7, 12, 0, 0),
# # # # # # # # # # # # # # #      'expatriate_End': datetime.datetime(2024, 7, 11, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6030000585', 'name': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 4, 0, 0),
# # # # # # # # # # # # # # #      'expatriate_End': datetime.datetime(2023, 7, 3, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6030000603', 'name': '聂雨轩', 'expatriate_Begin': datetime.datetime(2023, 7, 1, 0, 0),
# # # # # # # # # # # # # # #      'expatriate_End': datetime.datetime(2024, 6, 30, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '2010000566', 'name': '梁成才', 'expatriate_Begin': None,
# # # # # # # # # # # # # # #      'expatriate_End': datetime.datetime(2023, 10, 9, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6030000532', 'name': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023, 7, 1, 0, 0),
# # # # # # # # # # # # # # #      'expatriate_End': datetime.datetime(2024, 6, 30, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6030000585', 'name': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0),
# # # # # # # # # # # # # # #      'expatriate_End': datetime.datetime(2024, 7, 13, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6010004073', 'name': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 13, 0, 0),
# # # # # # # # # # # # # # #      'expatriate_End': datetime.datetime(2024, 7, 31, 0, 0)},
# # # # # # # # # # # # # # #     {'code': '6010004073', 'name': '阿连克沙', 'expatriate_Begin': None,
# # # # # # # # # # # # # # #      'expatriate_End': datetime.datetime(2024, 7, 31, 0, 0)},
# # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # import datetime
# # # # # # # # # # # # # # # a = [
# # # # # # # # # # # # # # #     {'index': '1', 'name': '徐宇龙',  'expatriate_Begin': datetime.datetime(2024, 7, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 11, 0, 0),'create_time':datetime.datetime(2024, 6, 29, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '2', 'name': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023, 7, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 28, 0, 0),'create_time':datetime.datetime(2023, 6, 29, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '3', 'name': '张雄虎', 'expatriate_Begin':None , 'expatriate_End': None,'create_time':datetime.datetime(2023, 6, 29, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '4', 'name': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 4, 0, 0),'expatriate_End': datetime.datetime(2023, 7, 5, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '5', 'name': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0),'expatriate_End': datetime.datetime(2024, 7, 13, 0, 0), 'create_time': datetime.datetime(2023, 7, 7, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '6', 'name': '赵越',  'expatriate_Begin': datetime.datetime(2024, 7, 16, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 21, 0, 0),'create_time':datetime.datetime(2024, 7, 15, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '7', 'name': '司建东', 'expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 1, 0, 0),'create_time':datetime.datetime(2023, 6, 29, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '8', 'name': '聂雨轩', 'expatriate_Begin': None, 'expatriate_End': None,'create_time':datetime.datetime(2023, 6, 29, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '9', 'name': '梁成才',  'expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 9, 0, 0),'create_time':datetime.datetime(2023, 6, 29, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '10', 'name': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 10, 0, 0),'expatriate_End': datetime.datetime(2024, 7, 9, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '11', 'name': '阿连克沙', 'expatriate_Begin': datetime.datetime(2024, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8,2, 0, 0),'create_time':datetime.datetime(2024, 7, 29, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '12', 'name': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'expatriate_End': datetime.datetime(2023, 7,4, 0, 0),'create_time':datetime.datetime(2023, 6, 29, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '13', 'name': '阿连克沙', 'expatriate_Begin':None, 'expatriate_End':None,'create_time':datetime.datetime(2023, 6,8, 0, 0)}
# # # # # # # # # # # # # # # ]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # code_records = {}
# # # # # # # # # # # # # # # for record in a:
# # # # # # # # # # # # # # #     name=record['name']
# # # # # # # # # # # # # # #     index=record['index']
# # # # # # # # # # # # # # #     for line in a:
# # # # # # # # # # # # # # #         pass
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for i in range(len(a)):
# # # # # # # # # # # # # # #     current_record = a[i]
# # # # # # # # # # # # # # #     for j in range(i):
# # # # # # # # # # # # # # #         if a[j]['create_time'] < current_record['create_time']:
# # # # # # # # # # # # # # #             current_record['last'] = a[j]['index']
# # # # # # # # # # # # # # #             break
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         current_record['last'] = current_record['index']
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # z=[{'index': '1', 'name': '徐宇龙', 'expatriate_Begin': datetime.datetime(2024, 7, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 11, 0, 0), 'create_time': datetime.datetime(2024, 6, 29, 0, 0), 'last': '1'},
# # # # # # # # # # # # # # #    {'index': '2', 'name': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023, 7, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 28, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last': '2'},
# # # # # # # # # # # # # # #    {'index': '3', 'name': '张雄虎', 'expatriate_Begin': None, 'expatriate_End': None, 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last': '3'},
# # # # # # # # # # # # # # #    {'index': '4', 'name': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 4, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 5, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last': '4'},
# # # # # # # # # # # # # # #    {'index': '5', 'name': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 13, 0, 0), 'create_time': datetime.datetime(2023, 7, 7, 0, 0), 'last': '2'},
# # # # # # # # # # # # # # #    {'index': '6', 'name': '赵越', 'expatriate_Begin': datetime.datetime(2024, 7, 16, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 21, 0, 0), 'create_time': datetime.datetime(2024, 7, 15, 0, 0), 'last': '1'},
# # # # # # # # # # # # # # #    {'index': '7', 'name': '司建东', 'expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 1, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last': '7'},
# # # # # # # # # # # # # # #    {'index': '8', 'name': '聂雨轩', 'expatriate_Begin': None, 'expatriate_End': None, 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last': '8'},
# # # # # # # # # # # # # # #    {'index': '9', 'name': '梁成才', 'expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 9, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last': '9'},
# # # # # # # # # # # # # # #    {'index': '10', 'name': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 10, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 9, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last': '10'},
# # # # # # # # # # # # # # #    {'index': '11', 'name': '阿连克沙', 'expatriate_Begin': datetime.datetime(2024, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 2, 0, 0), 'create_time': datetime.datetime(2024, 7, 29, 0, 0), 'last': '1'},
# # # # # # # # # # # # # # #    {'index': '12', 'name': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 4, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last': '12'},
# # # # # # # # # # # # # # #    {'index': '13', 'name': '阿连克沙', 'expatriate_Begin': None, 'expatriate_End': None, 'create_time': datetime.datetime(2023, 6, 8, 0, 0), 'last': '13'}]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # b=[{'index': '1', 'name': '徐宇龙', 'expatriate_Begin': datetime.datetime(2024, 7, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 11, 0, 0), 'create_time': datetime.datetime(2024, 6, 29, 0, 0), 'last': '2'},
# # # # # # # # # # # # # # #    {'index': '2', 'name': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023, 7, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 28, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0),'last': '2'},
# # # # # # # # # # # # # # #    {'index': '3', 'name': '张雄虎', 'expatriate_Begin': None, 'expatriate_End': None, 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last': '3'},
# # # # # # # # # # # # # # #    {'index': '4', 'name': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 4, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 5, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0),'last':'4'},
# # # # # # # # # # # # # # #    {'index': '5', 'name': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 13, 0, 0), 'create_time': datetime.datetime(2023, 7, 7, 0, 0), 'last': '4'},
# # # # # # # # # # # # # # #    {'index': '6', 'name': '赵越', 'expatriate_Begin': datetime.datetime(2024, 7, 16, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 21, 0, 0), 'create_time': datetime.datetime(2024, 7, 15, 0, 0),'last':'6'},
# # # # # # # # # # # # # # #    {'index': '7', 'name': '司建东', 'expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 1, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0),'last':'7'},
# # # # # # # # # # # # # # #    {'index': '8', 'name': '聂雨轩', 'expatriate_Begin': None, 'expatriate_End': None, 'create_time': datetime.datetime(2023, 6, 29, 0, 0),'last':'8'},
# # # # # # # # # # # # # # #    {'index': '9', 'name': '梁成才', 'expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 9, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0),'last':'9'},
# # # # # # # # # # # # # # #    {'index': '10', 'name': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0),'expatriate_End': datetime.datetime(2023, 7, 4, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0),'last': '10'},
# # # # # # # # # # # # # # #    {'index': '11', 'name': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 10, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 13, 0, 0), 'create_time': datetime.datetime(2023, 7, 1, 0, 0), 'last': '10'},
# # # # # # # # # # # # # # #    {'index': '12', 'name': '阿连克沙', 'expatriate_Begin': datetime.datetime(2024, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 2, 0, 0), 'create_time': datetime.datetime(2024, 7, 29, 0, 0), 'last': '11'},
# # # # # # # # # # # # # # #    {'index': '13', 'name': '阿连克沙', 'expatriate_Begin': None, 'expatriate_End': None, 'create_time': datetime.datetime(2023, 6, 8, 0, 0), 'last': '13'}]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # import datetime
# # # # # # # # # # # # # # a = [
# # # # # # # # # # # # # #     {'index': '1', 'code': '徐宇龙',  'expatriate_Begin': datetime.datetime(2024, 7, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 11, 0, 0)},
# # # # # # # # # # # # # #     {'index': '2', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023,9, 21, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 28, 0, 0)},
# # # # # # # # # # # # # #     {'index': '3', 'code': '张雄虎', 'expatriate_Begin':None , 'expatriate_End': None,'create_time':datetime.datetime(2023, 6, 29, 0, 0)},
# # # # # # # # # # # # # #     {'index': '4', 'code': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 4, 0, 0),'expatriate_End': datetime.datetime(2023, 7, 5, 0, 0)},
# # # # # # # # # # # # # #     {'index': '5', 'code': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0),'expatriate_End': datetime.datetime(2024, 7, 13, 0, 0)},
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     {'index': '6', 'code': '赵越',  'expatriate_Begin': datetime.datetime(2024, 7, 16, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 21, 0, 0)},
# # # # # # # # # # # # # #     {'index': '7', 'code': '司建东', 'expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 1, 0, 0)},
# # # # # # # # # # # # # #     {'index': '8', 'code': '聂雨轩', 'expatriate_Begin': None, 'expatriate_End': None},
# # # # # # # # # # # # # #     {'index': '9', 'code': '梁成才',  'expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 9, 0, 0),},
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     {'index': '12', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0),'expatriate_End': datetime.datetime(2023, 7, 4, 0, 0), },
# # # # # # # # # # # # # #     {'index': '10', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 10, 0, 0),'expatriate_End': datetime.datetime(2024, 7, 9, 0, 0),},
# # # # # # # # # # # # # #     {'index': '11', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2024, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8,2, 0, 0),},
# # # # # # # # # # # # # #     {'index': '13', 'code': '阿连克沙', 'expatriate_Begin':None, 'expatriate_End':None,},
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     {'index': '12', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0),'expatriate_End': datetime.datetime(2023, 7, 24, 0, 0), },
# # # # # # # # # # # # # #     {'index': '10', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023,6, 14, 0, 0),'expatriate_End': datetime.datetime(2023, 7, 9, 0, 0), },
# # # # # # # # # # # # # #     {'index': '11', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0),'expatriate_End': datetime.datetime(2024, 8, 2, 0, 0), },
# # # # # # # # # # # # # #     {'index': '11', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 1, 1, 0, 0),'expatriate_End': datetime.datetime(2023, 1, 2, 0, 0), },
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     {'index': '12', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0),'expatriate_End': datetime.datetime(2024, 7, 14, 0, 0)},
# # # # # # # # # # # # # #     {'index': '10', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 6, 14, 0, 0),'expatriate_End': datetime.datetime(2024, 7, 14, 0, 0)},
# # # # # # # # # # # # # #     {'index': '11', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0),'expatriate_End': datetime.datetime(2024, 6, 14, 0, 0)},
# # # # # # # # # # # # # #     {'index': '13', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 1, 14, 0, 0),'expatriate_End':datetime.datetime(2023, 4, 14, 0, 0)},
# # # # # # # # # # # # # # ]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # from datetime import datetime
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # your_list = [(datetime(2023, 7, 2, 0, 0), datetime(2023, 7, 4, 0, 0)), (datetime(2023, 7, 10, 0, 0), datetime(2024, 7, 9, 0, 0))]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # max_datetime = None
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for item in your_list:
# # # # # # # # # # # # # # #     current_datetime = item[0]
# # # # # # # # # # # # # # #     if max_datetime is None or current_datetime > max_datetime:
# # # # # # # # # # # # # # #         max_datetime = current_datetime
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(max_datetime)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # import datetime
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # datetime_list = [(datetime.datetime(2023, 7, 14, 0, 0), datetime.datetime(2024, 7, 14, 0, 0)),
# # # # # # # # # # # # # # #                  (datetime.datetime(2023, 6, 14, 0, 0), datetime.datetime(2024, 7, 14, 0, 0)),
# # # # # # # # # # # # # # #                  (datetime.datetime(2023, 4, 14, 0, 0), datetime.datetime(2023, 6, 14, 0, 0)),
# # # # # # # # # # # # # # #                  (datetime.datetime(2024, 1,14, 0, 0), datetime.datetime(2023, 4, 14, 0, 0))]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # max_datetime = max(datetime_list, key=lambda x: x[0])
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(max_datetime)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # zj=[{'index': '1', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2024, 7, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 11, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 9, 21, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 6, 28, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '2', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023, 9, 21, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 28, 0, 0),  'last_expatriate_Begin': datetime.datetime(2023, 9, 21, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 6, 28, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '3', 'code': '张雄虎', 'expatriate_Begin': None, 'expatriate_End': None, 'last_expatriate_Begin': None, 'last_expatriate_End': None},
# # # # # # # # # # # # # # #     {'index': '4', 'code': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 4, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 5, 0, 0),  'last_expatriate_Begin': datetime.datetime(2023, 7, 4, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 7, 5, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '5', 'code': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 13, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 7, 4, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 7, 5, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '6', 'code': '赵越', 'expatriate_Begin': datetime.datetime(2024, 7, 16, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 21, 0, 0),  'last_expatriate_Begin': datetime.datetime(2024, 7, 16, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 7, 21, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '7', 'code': '司建东', 'expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 1, 0, 0),'last_expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 8, 1, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '8', 'code': '聂雨轩', 'expatriate_Begin': None, 'expatriate_End': None,  'last_expatriate_Begin': None, 'last_expatriate_End': None},
# # # # # # # # # # # # # # #     {'index': '9', 'code': '梁成才', 'expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 9, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 10, 9, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '12', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 4, 0, 0),  'last_expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 7, 4, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '10', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 10, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 9, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 7, 4, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '11', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2024, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 2, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 7, 10, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 7, 9, 0, 0)},
# # # # # # # # # # # # # # #     {'index': '13', 'code': '阿连克沙', 'expatriate_Begin': None, 'expatriate_End': None,  'last_expatriate_Begin': None, 'last_expatriate_End': None}]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # z=[{'index': '1', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2024, 7, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 11, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 9, 21, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 6, 28, 0, 0)},
# # # # # # # # # # # # # #    {'index': '2', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023, 9, 21, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 28, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 9, 21, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 6, 28, 0, 0)},
# # # # # # # # # # # # # #    {'index': '3', 'code': '张雄虎', 'expatriate_Begin': None, 'expatriate_End': None, 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last_expatriate_Begin': None, 'last_expatriate_End': None},
# # # # # # # # # # # # # #    {'index': '7', 'code': '司建东', 'expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 1, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 8, 1, 0, 0)},
# # # # # # # # # # # # # #    {'index': '8', 'code': '聂雨轩', 'expatriate_Begin': None, 'expatriate_End': None, 'last_expatriate_Begin': None, 'last_expatriate_End': None},
# # # # # # # # # # # # # #    {'index': '9', 'code': '梁成才', 'expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 9, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 10, 9, 0, 0)},
# # # # # # # # # # # # # #    {'index': '12', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 4, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 7, 4, 0, 0)},
# # # # # # # # # # # # # #    {'index': '13', 'code': '阿连克沙', 'expatriate_Begin': None, 'expatriate_End': None, 'last_expatriate_Begin': None, 'last_expatriate_End': None},
# # # # # # # # # # # # # #    {'index': '12', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 24, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 6, 14, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 7, 9, 0, 0)},
# # # # # # # # # # # # # #    {'index': '10', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 6, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 9, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 8, 2, 0, 0)},
# # # # # # # # # # # # # #    {'index': '11', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 2, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 1, 1, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 1, 2, 0, 0)},
# # # # # # # # # # # # # #    {'index': '11', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 1, 1, 0, 0), 'expatriate_End': datetime.datetime(2023, 1, 2, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 1, 1, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 1, 2, 0, 0)},
# # # # # # # # # # # # # #    {'index': '12', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 14, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 6, 14, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 7, 14, 0, 0)},
# # # # # # # # # # # # # #    {'index': '10', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 6, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 14, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 6, 14, 0, 0)},
# # # # # # # # # # # # # #    {'index': '11', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 14, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 1, 14, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 4, 14, 0, 0)},
# # # # # # # # # # # # # #    {'index': '13', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 1, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 4, 14, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 1, 14, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 4, 14, 0, 0)}]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # for index, item in enumerate(a):  #根据code找出所有的外派时间 然后遍历每一条 根据该条记录找出所有小于该条记录的外派起始时间中最大的外派起始时间就是该条的上次外派起始时间
# # # # # # # # # # # # # #     # print(index,item)
# # # # # # # # # # # # # #     last_begin=item['expatriate_Begin']
# # # # # # # # # # # # # #     last_end=item['expatriate_End']
# # # # # # # # # # # # # #     code=item['code']
# # # # # # # # # # # # # #     record={'code':code,'time_ls':[]}
# # # # # # # # # # # # # #     for line in a:
# # # # # # # # # # # # # #         if code==line['code']:
# # # # # # # # # # # # # #             record['time_ls'].append(tuple([line['expatriate_Begin'],line['expatriate_End']]))
# # # # # # # # # # # # # #     record['time_ls']=[t for t in record['time_ls'] if t[0] and last_begin and t[0] < last_begin]
# # # # # # # # # # # # # #     # for t in record['time_ls']:
# # # # # # # # # # # # # #     #     print(t)
# # # # # # # # # # # # # #         # if t[1] and last_begin and t[1] < last_begin:
# # # # # # # # # # # # # #         #     record['time_ls'].append(t[1])
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     # print(record)
# # # # # # # # # # # # # #     if len(record['time_ls']) >= 2:
# # # # # # # # # # # # # #         max_item = max(record['time_ls'], key=lambda x: x[0])
# # # # # # # # # # # # # #         record['time_ls'] = [max_item]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     if len(record['time_ls'])==0:  #第一次的
# # # # # # # # # # # # # #         item['last_expatriate_Begin']=last_begin
# # # # # # # # # # # # # #         item['last_expatriate_End']=last_end
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         item['last_expatriate_Begin']=record['time_ls'][0][0]
# # # # # # # # # # # # # #         item['last_expatriate_End']=record['time_ls'][0][1]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # j=[{'index': '1', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2024, 7, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 11, 0, 0), 'create_time': datetime.datetime(2024, 6, 29, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 9, 21, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 6, 28, 0, 0)}, {'index': '2', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023, 9, 21, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 28, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 9, 21, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 6, 28, 0, 0)}, {'index': '3', 'code': '张雄虎', 'expatriate_Begin': None, 'expatriate_End': None, 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last_expatriate_Begin': None, 'last_expatriate_End': None}, {'index': '4', 'code': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 4, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 5, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 7, 4, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 7, 5, 0, 0)}, {'index': '5', 'code': '张雄虎', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 13, 0, 0), 'create_time': datetime.datetime(2023, 7, 7, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 7, 4, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 7, 5, 0, 0)}, {'index': '6', 'code': '赵越', 'expatriate_Begin': datetime.datetime(2024, 7, 16, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 21, 0, 0), 'create_time': datetime.datetime(2024, 7, 15, 0, 0), 'last_expatriate_Begin': datetime.datetime(2024, 7, 16, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 7, 21, 0, 0)}, {'index': '7', 'code': '司建东', 'expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 1, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 8, 1, 0, 0)}, {'index': '8', 'code': '聂雨轩', 'expatriate_Begin': None, 'expatriate_End': None, 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last_expatriate_Begin': None, 'last_expatriate_End': None}, {'index': '9', 'code': '梁成才', 'expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 9, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 10, 9, 0, 0)}, {'index': '12', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 4, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 7, 4, 0, 0)}, {'index': '10', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 10, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 9, 0, 0), 'create_time': datetime.datetime(2023, 6, 29, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 7, 4, 0, 0)}, {'index': '11', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2024, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 2, 0, 0), 'create_time': datetime.datetime(2024, 7, 29, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 7, 10, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 7, 9, 0, 0)}, {'index': '13', 'code': '阿连克沙', 'expatriate_Begin': None, 'expatriate_End': None, 'create_time': datetime.datetime(2023, 6, 8, 0, 0), 'last_expatriate_Begin': None, 'last_expatriate_End': None},
# # # # # # # # # # # # # # #    {'index': '12', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 14, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 1, 14, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 4, 14, 0, 0)},
# # # # # # # # # # # # # # #    {'index': '10', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 6, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 14, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 1, 14, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 4, 14, 0, 0)},
# # # # # # # # # # # # # # #    {'index': '11', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 14, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0), 'last_expatriate_End': datetime.datetime(2024, 6, 14, 0, 0)},
# # # # # # # # # # # # # # #    {'index': '13', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 1, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 4, 14, 0, 0), 'last_expatriate_Begin': datetime.datetime(2023, 1, 14, 0, 0), 'last_expatriate_End': datetime.datetime(2023, 4, 14, 0, 0)}]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #     # print("++++++++")
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # recent_expatriate_begin = {}
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for person in a:
# # # # # # # # # # # # # # #     code = person['code']
# # # # # # # # # # # # # # #     filtered_list = [p for p in a if p['code'] == code]
# # # # # # # # # # # # # # #     sorted_list = sorted(filtered_list, key=lambda x: x['expatriate_Begin'], reverse=True)
# # # # # # # # # # # # # # #     most_recent = sorted_list[0]
# # # # # # # # # # # # # # #     recent_expatriate_begin[code] = most_recent['expatriate_Begin']
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(recent_expatriate_begin)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # result = {}
# # # # # # # # # # # # # # # for element in a:
# # # # # # # # # # # # # # #     code = element['code']
# # # # # # # # # # # # # # #     expatriate_Begin = element['expatriate_Begin']
# # # # # # # # # # # # # # #     expatriate_End = element['expatriate_End']
# # # # # # # # # # # # # # #     if code in result:
# # # # # # # # # # # # # # #         result[code]['begin_list'].append(expatriate_Begin)
# # # # # # # # # # # # # # #         result[code]['end_list'].append(expatriate_End)
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         result[code] = {'begin_list': [expatriate_Begin], 'end_list': [expatriate_End]}
# # # # # # # # # # # # # # # for code, values in result.items():
# # # # # # # # # # # # # # #     values['begin_list'] = sorted([x for x in values['begin_list'] if x is not None], reverse=True)
# # # # # # # # # # # # # # #     values['end_list'] = sorted([x for x in values['end_list'] if x is not None], reverse=True)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(result)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # #lbpm_process 每次流程的创建时间
# # # # # # # # # # # # # # # from operator import itemgetter
# # # # # # # # # # # # # # # sorted_list = sorted(resp['data'], key=itemgetter('expatriate_Begin'), reverse=True)
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # Create a new list of dictionaries with the same 'code' and a list of 'expatriate_Begin' values
# # # # # # # # # # # # # # # expatriate_Begin_list = []
# # # # # # # # # # # # # # # for item in sorted_list:
# # # # # # # # # # # # # # #     code = item['code']
# # # # # # # # # # # # # # #     expatriate_Begin = item['expatriate_Begin']
# # # # # # # # # # # # # # #     for dict_item in expatriate_Begin_list:
# # # # # # # # # # # # # # #         if dict_item['code'] == code:
# # # # # # # # # # # # # # #             dict_item['begin_time_list'].append(expatriate_Begin)
# # # # # # # # # # # # # # #             break
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         expatriate_Begin_list.append({'code': code, 'begin_time_list': [expatriate_Begin]})
# # # # # # # # # # # # # # # print(expatriate_Begin_list)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # a = [1, 1, 3, 2, 4]
# # # # # # # # # # # # # # # max_num = -float('inf')
# # # # # # # # # # # # # # # print(max_num)
# # # # # # # # # # # # # # # for num in a:
# # # # # # # # # # # # # # #     if num < 3 and num > max_num:
# # # # # # # # # # # # # # #         max_num = num
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # print(max_num)  # Output: 2
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # a = [1, 1, 3, 2, 4]
# # # # # # # # # # # # # # # smaller_than_three = [num for num in a if num < 3]
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # if smaller_than_three:
# # # # # # # # # # # # # # #     max_number = max(smaller_than_three)
# # # # # # # # # # # # # # #     print(f"The maximum number smaller than 3 is: {max_number}")
# # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # #     print("There are no numbers smaller than 3 in the list.")
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # # expatriate_time_list = {}  # 每个人的每次外派开始时间和外派结束时间
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for element in resp['data']:
# # # # # # # # # # # # # # #     code = element['code']
# # # # # # # # # # # # # # #     expatriate_Begin = element['expatriate_Begin']
# # # # # # # # # # # # # # #     expatriate_End = element['expatriate_End']
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # #     if code in expatriate_time_list:
# # # # # # # # # # # # # # #         expatriate_time_list[code]['begin_list'].append(expatriate_Begin)
# # # # # # # # # # # # # # #         expatriate_time_list[code]['end_list'].append(expatriate_End)
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         expatriate_time_list[code] = {'begin_list': [expatriate_Begin], 'end_list': [expatriate_End]}
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # for code, values in expatriate_time_list.items():
# # # # # # # # # # # # # # #     values['begin_list'] = sorted([x for x in values['begin_list'] if x is not None], reverse=True)
# # # # # # # # # # # # # # #     values['end_list'] = sorted([x for x in values['end_list'] if x is not None], reverse=True)
# # # # # # # # # # # # # # # print(expatriate_time_list)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # import datetime
# # # # # # # # # # # # #
# # # # # # # # # # # # # a=[
# # # # # # # # # # # # #     {'index': '1', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2024, 7, 12, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 28, 0, 0),},
# # # # # # # # # # # # #    {'index': '2', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023, 9, 21, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 12, 0, 0),},
# # # # # # # # # # # # #    {'index': '3', 'code': '张雄虎', 'expatriate_Begin': None, 'expatriate_End': None, },
# # # # # # # # # # # # #    {'index': '7', 'code': '司建东', 'expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 1, 0, 0),},
# # # # # # # # # # # # #    {'index': '8', 'code': '聂雨轩', 'expatriate_Begin': None, 'expatriate_End': None, },
# # # # # # # # # # # # #    {'index': '9', 'code': '梁成才', 'expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 9, 0, 0),},
# # # # # # # # # # # # #    {'index': '12', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 4, 0, 0), },
# # # # # # # # # # # # #    {'index': '13', 'code': '阿连克沙', 'expatriate_Begin': None, 'expatriate_End': None},
# # # # # # # # # # # # #    {'index': '15', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 24, 0, 0),},
# # # # # # # # # # # # #    {'index': '16', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 6, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 9, 0, 0), },
# # # # # # # # # # # # #    {'index': '17', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 2, 0, 0),},
# # # # # # # # # # # # #    {'index': '18', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 1, 1, 0, 0), 'expatriate_End': datetime.datetime(2023, 1, 2, 0, 0),},
# # # # # # # # # # # # #    {'index': '19', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 14, 0, 0), },
# # # # # # # # # # # # #    {'index': '20', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 6, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 14, 0, 0), },
# # # # # # # # # # # # #    {'index': '21', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 14, 0, 0), },
# # # # # # # # # # # # #    {'index': '22', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 1, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 4, 14, 0, 0),}
# # # # # # # # # # # # #
# # # # # # # # # # # # # ]
# # # # # # # # # # # # # """{
# # # # # # # # # # # # #
# # # # # # # # # # # # #     'code': {'index': '22', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 1, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 4, 14, 0, 0),}
# # # # # # # # # # # # # }
# # # # # # # # # # # # # """
# # # # # # # # # # # # # # dict=[]
# # # # # # # # # # # # # # for index, item in enumerate(a):  #根据code找出所有的外派开始时间
# # # # # # # # # # # # # #     begin=item['expatriate_Begin']
# # # # # # # # # # # # # #     end=item['expatriate_End']
# # # # # # # # # # # # # #     code=item['code']
# # # # # # # # # # # # # #     i=item['index']
# # # # # # # # # # # # # #     # print(index,item)
# # # # # # # # # # # # # # for line in a:
# # # # # # # # # # # # # #     if line['code'] in dict:
# # # # # # # # # # # # # #         if line['expatriate_Begin'] and line['expatriate_End'] and line['expatriate_Begin'] < dict[line['code']] <= line[
# # # # # # # # # # # # # #             'expatriate_End']:
# # # # # # # # # # # # # #             pass
# # # # # # # # # # # # # #         #
# # # # # # # # # # # # # #         # else:
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         dict[line['code']] = line
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #     #     if line['code']==code:
# # # # # # # # # # # # #     #         if begin and line['expatriate_Begin'] and line['expatriate_End'] and  line['expatriate_Begin']<begin<=line['expatriate_End']:
# # # # # # # # # # # # #     #             # print(i, line['index'])
# # # # # # # # # # # # #     #             item['expatriate_Begin']=min(line['expatriate_Begin'],item['expatriate_Begin'])
# # # # # # # # # # # # #     #             item['expatriate_End']=max(line['expatriate_End'],item['expatriate_End'])
# # # # # # # # # # # # #     #
# # # # # # # # # # # # #     # print(item)
# # # # # # # # # # # # #                 # print(i,line['index'])
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def mergeIntervals(intervals):
# # # # # # # # # # # # # #    intervals.sort(key=lambda x: x['expatriate_Begin'])
# # # # # # # # # # # # # #    stack = []
# # # # # # # # # # # # # #    stack.append(intervals[0])
# # # # # # # # # # # # # #    for i in range(1, len(intervals)):
# # # # # # # # # # # # # #       if stack[-1]['expatriate_Begin'] <= intervals[i]['expatriate_Begin'] <= stack[-1]['expatriate_End']:
# # # # # # # # # # # # # #          stack[-1]['expatriate_End'] = max(stack[-1]['expatriate_End'], intervals[i]['expatriate_End'])
# # # # # # # # # # # # # #       else:
# # # # # # # # # # # # # #          stack.append(intervals[i])
# # # # # # # # # # # # # #    print("The Merged Intervals are:", end=" ")
# # # # # # # # # # # # # #    for interval in stack:
# # # # # # # # # # # # # #       print(interval, end=" ")
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # a=[
# # # # # # # # # # # # #     {'index': '1', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2024, 7, 12, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 28, 0, 0),},
# # # # # # # # # # # # #    {'index': '2', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023, 9, 21, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 12, 0, 0),},
# # # # # # # # # # # # #    # {'index': '3', 'code': '张雄虎', 'expatriate_Begin': None, 'expatriate_End': None, },
# # # # # # # # # # # # #    {'index': '7', 'code': '司建东', 'expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 1, 0, 0),},
# # # # # # # # # # # # #    # {'index': '8', 'code': '聂雨轩', 'expatriate_Begin': None, 'expatriate_End': None, },
# # # # # # # # # # # # #    {'index': '9', 'code': '梁成才', 'expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 9, 0, 0),},
# # # # # # # # # # # # #    {'index': '12', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 4, 0, 0), },
# # # # # # # # # # # # #    # {'index': '13', 'code': '阿连克沙', 'expatriate_Begin': None, 'expatriate_End': None},
# # # # # # # # # # # # #    {'index': '15', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 24, 0, 0),},
# # # # # # # # # # # # #    {'index': '16', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 6, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 9, 0, 0), },
# # # # # # # # # # # # #    {'index': '17', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 2, 0, 0),},
# # # # # # # # # # # # #    {'index': '18', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 1, 1, 0, 0), 'expatriate_End': datetime.datetime(2023, 1, 2, 0, 0),},
# # # # # # # # # # # # #    {'index': '19', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 14, 0, 0), },
# # # # # # # # # # # # #    {'index': '20', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 6, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 14, 0, 0), },
# # # # # # # # # # # # #    {'index': '21', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 14, 0, 0), },
# # # # # # # # # # # # #    {'index': '22', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 1, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 4, 14, 0, 0),}
# # # # # # # # # # # # # ]
# # # # # # # # # # # # #
# # # # # # # # # # # # # z=[]
# # # # # # # # # # # # # for index, item in enumerate(a):  #根据code找出所有的外派开始时间
# # # # # # # # # # # # #     begin=item['expatriate_Begin']
# # # # # # # # # # # # #     end=item['expatriate_End']
# # # # # # # # # # # # #     code=item['code']
# # # # # # # # # # # # #     i=item['index']
# # # # # # # # # # # # #     record = {'code': code, 'ls': []}
# # # # # # # # # # # # #     for line in a:
# # # # # # # # # # # # #         if code==line['code']:
# # # # # # # # # # # # #             record['ls'].append(line)
# # # # # # # # # # # # #     z.append(record)
# # # # # # # # # # # # # # print(z)
# # # # # # # # # # # # #
# # # # # # # # # # # # # # for  i in z:
# # # # # # # # # # # # # #    print(i)
# # # # # # # # # # # # # import pandas as pd
# # # # # # # # # # # # # result = pd.Series(z).drop_duplicates().tolist()
# # # # # # # # # # # # # # print(result)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # jk=[
# # # # # # # # # # # # #     {'code': '徐宇龙', 'ls': [{'index': '1', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2024, 7, 12, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 28, 0, 0)}, {'index': '2', 'code': '徐宇龙', 'expatriate_Begin': datetime.datetime(2023, 9, 21, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 12, 0, 0)}]},
# # # # # # # # # # # # #     {'code': '司建东', 'ls': [{'index': '7', 'code': '司建东', 'expatriate_Begin': datetime.datetime(2023, 8, 1, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 1, 0, 0)}]},
# # # # # # # # # # # # #     {'code': '梁成才', 'ls': [{'index': '9', 'code': '梁成才', 'expatriate_Begin': datetime.datetime(2023, 7, 5, 0, 0), 'expatriate_End': datetime.datetime(2023, 10, 9, 0, 0)}]},
# # # # # # # # # # # # #     {'code': '阿连克沙', 'ls': [{'index': '12', 'code': '阿连克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 2, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 4, 0, 0)}]},
# # # # # # # # # # # # #     {'code': '克沙', 'ls': [{'index': '15', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 24, 0, 0)}, {'index': '16', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 6, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 7, 9, 0, 0)}, {'index': '17', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 8, 2, 0, 0)}, {'index': '18', 'code': '克沙', 'expatriate_Begin': datetime.datetime(2023, 1, 1, 0, 0), 'expatriate_End': datetime.datetime(2023, 1, 2, 0, 0)}]},
# # # # # # # # # # # # #     {'code': '陈烨', 'ls': [{'index': '19', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 7, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 14, 0, 0)},{'index': '20', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 6, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 7, 14, 0, 0)}, {'index': '21', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 4, 14, 0, 0), 'expatriate_End': datetime.datetime(2024, 6, 14, 0, 0)}, {'index': '22', 'code': '陈烨', 'expatriate_Begin': datetime.datetime(2023, 1, 14, 0, 0), 'expatriate_End': datetime.datetime(2023, 4, 14, 0, 0)}]}
# # # # # # # # # # # # #     ]
# # # # # # # # # # # # # for i in jk:
# # # # # # # # # # # # #     i['ls'].sort(key=lambda x: x['expatriate_Begin'])
# # # # # # # # # # # # #     print(i)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #    # sorted_data = sorted(i, key=lambda x: x['expatriate_Begin'], reverse=False)
# # # # # # # # # # # # #    # print(sorted_data)
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #    # if line['code'] in dict:
# # # # # # # # # # # # #    #         if line['expatriate_Begin'] and line['expatriate_End'] and line['expatriate_Begin'] < dict[line['code']] <= line[
# # # # # # # # # # # # #    #             'expatriate_End']:
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # # # # # # # # # # # # # def merge_ranges(ranges):
# # # # # # # # # # # # # #    # Sort the list by start date
# # # # # # # # # # # # # #    ranges.sort(key=lambda x: x['expatriate_Begin'])
# # # # # # # # # # # # # #    print(ranges)
# # # # # # # # # # # # # #    merged_ranges = []
# # # # # # # # # # # # # #    current_range = ranges[0]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #    for next_range in ranges[1:]:
# # # # # # # # # # # # # #       if current_range['expatriate_End'] >= next_range['expatriate_Begin']:
# # # # # # # # # # # # # #          # Merge the ranges by updating the end date
# # # # # # # # # # # # # #          current_range['expatriate_End'] = max(current_range['expatriate_End'], next_range['expatriate_End'])
# # # # # # # # # # # # # #       else:
# # # # # # # # # # # # # #          # Append the current range to the merged list and update current range
# # # # # # # # # # # # # #          merged_ranges.append(current_range)
# # # # # # # # # # # # # #          current_range = next_range
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #    # Append the last remaining range
# # # # # # # # # # # # # #    merged_ranges.append(current_range)
# # # # # # # # # # # # # #
# # # # # # # # # # # # # #    return merged_ranges
# # # # # # # # # # # # # # print(merge_ranges(a))
# # # # # # # # # # # # # # a.sort(key=lambda x: x['expatriate_Begin'])
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # stack = []
# # # # # # # # # # # # # # stack.append(a[0])
# # # # # # # # # # # # # # print(stack)
# # # # # # # # # # # # # # for i in range(1, len(a)):
# # # # # # # # # # # # # #    current = a[i]
# # # # # # # # # # # # # #    top = stack[-1]
# # # # # # # # # # # # # #    # Check for overlapping interval
# # # # # # # # # # # # # #    if top['expatriate_Begin'] <= current['expatriate_Begin'] <= top['expatriate_End']:
# # # # # # # # # # # # # #       top['expatriate_End'] = max(top['expatriate_End'], current['expatriate_End'])
# # # # # # # # # # # # # #    else:
# # # # # # # # # # # # # #       stack.append(current)
# # # # # # # # # # # # # # # Print the merged intervals
# # # # # # # # # # # # # # print("The Merged Intervals are:", end=" ")
# # # # # # # # # # # # # # for interval in stack:
# # # # # # # # # # # # # #    print(interval, end="")
# # # # # # # # # # # # # # mergeIntervals(a)
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # import base64
# # # # # # # # # # # # import hashlib
# # # # # # # # # # # # from Crypto import Random
# # # # # # # # # # # # from Crypto.Cipher import AES
# # # # # # # # # # # # from Crypto.Util import Padding
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # class AESCipher(object):
# # # # # # # # # # # #     def __init__(self, key):
# # # # # # # # # # # #         self.key = (hashlib.md5(key.encode('utf-8')).hexdigest()).encode('utf-8')
# # # # # # # # # # # #         print('key',self.key)
# # # # # # # # # # # #
# # # # # # # # # # # #     def encrypt(self, raw):
# # # # # # # # # # # #         iv = Random.get_random_bytes(AES.block_size)
# # # # # # # # # # # #         print('iv',iv)
# # # # # # # # # # # #         cipher = AES.new(self.key, AES.MODE_CBC, iv)
# # # # # # # # # # # #         data = Padding.pad(raw.encode('utf-8'), AES.block_size, 'pkcs7')
# # # # # # # # # # # #         return base64.b64encode(iv + cipher.encrypt(data)).decode('utf-8')
# # # # # # # # # # # #
# # # # # # # # # # # #     def decrypt(self, enc):
# # # # # # # # # # # #         enc = base64.b64decode(enc.encode('utf-8'))
# # # # # # # # # # # #         iv = enc[:AES.block_size]
# # # # # # # # # # # #         print('iv',iv)
# # # # # # # # # # # #         cipher = AES.new(self.key, AES.MODE_CBC, iv)
# # # # # # # # # # # #         data = Padding.unpad(cipher.decrypt(enc[AES.block_size:]), AES.block_size, 'pkcs7')
# # # # # # # # # # # #         return data.decode('utf-8')
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # cipher = AESCipher('455a0595071af6e2385c0ec556cb329c')
# # # # # # # # # # # #
# # # # # # # # # # # # # Encrypt a string
# # # # # # # # # # # # encrypted = cipher.encrypt('Hello, World!')
# # # # # # # # # # # # print(encrypted)  # Output: '...'
# # # # # # # # # # # #
# # # # # # # # # # # # # Decrypt the encrypted string
# # # # # # # # # # # # decrypted = cipher.decrypt(encrypted)
# # # # # # # # # # # # print(decrypted)  # Output: 'Hello, World!'
# # # # # # # # # # # import base64
# # # # # # # # # # #
# # # # # # # # # # # from Crypto.Cipher import AES
# # # # # # # # # # # from Crypto import Random
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # # def generate_key_and_iv():
# # # # # # # # # # # #     key = Random.new().read(AES.block_size)  # Generate a random key
# # # # # # # # # # # #     iv = Random.new().read(AES.block_size)  # Generate a random IV
# # # # # # # # # # # #     return key, iv
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # key, iv = generate_key_and_iv()
# # # # # # # # # # # # print(key,iv)
# # # # # # # # # # # # from Crypto.Cipher import AES
# # # # # # # # # # # # from Crypto import Random
# # # # # # # # # # # # import base64
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # def encrypt(data, key, iv):
# # # # # # # # # # # #     bs = AES.block_size
# # # # # # # # # # # #     pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
# # # # # # # # # # # #     cipher = AES.new(key, AES.MODE_CBC, iv)
# # # # # # # # # # # #     data = cipher.encrypt(pad(data))
# # # # # # # # # # # #     data = iv + data
# # # # # # # # # # # #     return base64.b64encode(data).decode('utf-8')
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # def decrypt(data, key, iv):
# # # # # # # # # # # #     bs = AES.block_size
# # # # # # # # # # # #     unpad = lambda s: s[0:-ord(s[-1])]
# # # # # # # # # # # #     data = base64.b64decode(data)
# # # # # # # # # # # #     iv = data[:bs]
# # # # # # # # # # # #     cipher = AES.new(key, AES.MODE_CBC, iv)
# # # # # # # # # # # #     data = unpad(cipher.decrypt(data[bs:])).decode('utf-8')
# # # # # # # # # # # #     return data
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # # Example usage:
# # # # # # # # # # # # data = 'Hello, World!'
# # # # # # # # # # # # encrypted_data = encrypt(data, key, iv)
# # # # # # # # # # # # decrypted_data = decrypt(encrypted_data, key, iv)
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # # from Crypto.Cipher import AES
# # # # # # # # # # # # from Crypto.Random import get_random_bytes
# # # # # # # # # # # # # 对应的模块
# # # # # # # # # # # # from Crypto.Util.Padding import pad
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # key = get_random_bytes(16)  # 16 bytes = 128 bits
# # # # # # # # # # # # iv = get_random_bytes(16)
# # # # # # # # # # # #
# # # # # # # # # # # # cipher = AES.new(key, AES.MODE_CBC, iv)
# # # # # # # # # # # #
# # # # # # # # # # # # plaintext = b'1234567812345678'
# # # # # # # # # # # # # 变为16的倍数
# # # # # # # # # # # # plaintext = pad(plaintext, 16)
# # # # # # # # # # # # print(plaintext)
# # # # # # # # # # # # ciphertext = cipher.encrypt(plaintext)
# # # # # # # # # # # #
# # # # # # # # # # # # print("Key:", key)
# # # # # # # # # # # # print("IV:", iv)
# # # # # # # # # # # # print("Ciphertext:", ciphertext)
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # # from Crypto.Cipher import AES
# # # # # # # # # # # # from Crypto.Util.Padding import pad
# # # # # # # # # # # # from Crypto.Random import get_random_bytes
# # # # # # # # # # # # key = get_random_bytes(16)  # 16 bytes key
# # # # # # # # # # # # iv = get_random_bytes(16)  # 16 bytes IV
# # # # # # # # # # # # data = '{"code":200,"data":{"apts":[]},"message":"","success":true}'  # Data to encrypt
# # # # # # # # # # # #
# # # # # # # # # # # # cipher = AES.new(key, AES.MODE_CBC, iv=iv)
# # # # # # # # # # # # ciphertext = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
# # # # # # # # # # # # import base64
# # # # # # # # # # # # encoded_key = base64.b64encode(key).decode('utf-8')
# # # # # # # # # # # # encoded_iv = base64.b64encode(iv).decode('utf-8')
# # # # # # # # # # # # print(encoded_key)
# # # # # # # # # # # # print(encoded_iv)
# # # # # # # # # # # # encoded_ciphertext = base64.b64encode(ciphertext).decode('utf-8')
# # # # # # # # # # # # print(encoded_ciphertext)
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # # from Crypto import Random
# # # # # # # # # # # #
# # # # # # # # # # # # key = Random.new().read(16)  # 16 bytes for AES-128, 24 bytes for AES-192, 32 bytes for AES-256
# # # # # # # # # # # # iv = Random.new().read(AES.block_size)  # 16 bytes
# iv = base64.b64decode(iv)
# # # # # # # # # # # from Crypto.Cipher import AES
# # # # # # # # # # # # import base64
# # # # # # # # # # # #
# # # # # # # # # # # # def encrypt(data, key, iv):
# # # # # # # # # # # #     bs = AES.block_size
# # # # # # # # # # # #     pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
# # # # # # # # # # # #     cipher = AES.new(key, AES.MODE_CBC, iv)
# # # # # # # # # # # #     data = cipher.encrypt(pad(data))
# # # # # # # # # # # #     data = iv + data
# # # # # # # # # # # #     return base64.b64encode(data)
# # # # # # # # # # # #
# # # # # # # # # # # # data = 'Hello, world!'
# # # # # # # # # # # # # print(type(data))
# # # # # # # # # # # # # # Method 2: Using bytes()
# # # # # # # # # # # # # string = "Hello, world!"  # Define a string
# # # # # # # # # # # # # bytes_result = bytes(string, 'utf-8')  # Convert string to bytes using UTF-8 encoding
# # # # # # # # # # # # # print(bytes_result,type(bytes_result))
# # # # # # # # # # # # # data=bytes(data,'utf-8')
# # # # # # # # # # # # # data=data.encode('utf-8')
# # # # # # # # # # # # print(data,type(data))
# # # # # # # # # # # # encrypted_data = encrypt(data, key, iv)
# # # # # # # # # # # # print("Encrypted data:", encrypted_data)
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # # from Crypto.Cipher import AES
# # # # # # # # # # # # from binascii import b2a_hex, a2b_hex
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # class PrpCrypt(object):
# # # # # # # # # # # #
# # # # # # # # # # # #     def __init__(self, key):
# # # # # # # # # # # #         self.key = key.encode('utf-8')
# # # # # # # # # # # #         print('key',self.key)
# # # # # # # # # # # #         self.mode = AES.MODE_CBC
# # # # # # # # # # # #
# # # # # # # # # # # #     # 加密函数，如果text不足16位就用空格补足为16位，
# # # # # # # # # # # #     # 如果大于16当时不是16的倍数，那就补足为16的倍数。
# # # # # # # # # # # #     def encrypt(self, text):
# # # # # # # # # # # #         text = text.encode('utf-8')
# # # # # # # # # # # #         cryptor = AES.new(self.key, self.mode, b'0000000000000000')
# # # # # # # # # # # #         # 这里密钥key 长度必须为16（AES-128）,
# # # # # # # # # # # #         # 24（AES-192）,或者32 （AES-256）Bytes 长度
# # # # # # # # # # # #         # 目前AES-128 足够目前使用
# # # # # # # # # # # #         length = 16
# # # # # # # # # # # #         count = len(text)
# # # # # # # # # # # #         if count < length:
# # # # # # # # # # # #             add = (length - count)
# # # # # # # # # # # #             # \0 backspace
# # # # # # # # # # # #             # text = text + ('\0' * add)
# # # # # # # # # # # #             text = text + ('\0' * add).encode('utf-8')
# # # # # # # # # # # #         elif count > length:
# # # # # # # # # # # #             add = (length - (count % length))
# # # # # # # # # # # #             # text = text + ('\0' * add)
# # # # # # # # # # # #             text = text + ('\0' * add).encode('utf-8')
# # # # # # # # # # # #         self.ciphertext = cryptor.encrypt(text)
# # # # # # # # # # # #         # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
# # # # # # # # # # # #         # 所以这里统一把加密后的字符串转化为16进制字符串
# # # # # # # # # # # #         return b2a_hex(self.ciphertext)
# # # # # # # # # # # #
# # # # # # # # # # # #     # 解密后，去掉补足的空格用strip() 去掉
# # # # # # # # # # # #     def decrypt(self, text):
# # # # # # # # # # # #         cryptor = AES.new(self.key, self.mode, b'0000000000000000')
# # # # # # # # # # # #         plain_text = cryptor.decrypt(a2b_hex(text))
# # # # # # # # # # # #         # return plain_text.rstrip('\0')
# # # # # # # # # # # #         return bytes.decode(plain_text).rstrip('\0')
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # # # #     pc = PrpCrypt('keyskeyskeyskeys')  # 初始化密钥
# # # # # # # # # # # #     e = pc.encrypt("testtesttest")  # 加密
# # # # # # # # # # # #     d = pc.decrypt(e)  # 解密
# # # # # # # # # # # #     print("加密:", e)
# # # # # # # # # # # #     print("解密:", d)
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # from Crypto.Cipher import AES
# # # # # # # # # # # # from Crypto.Util.Padding import pad, unpad
# # # # # # # # # # # # import os
# from Crypto import Random
# # # # # # # # # # # #
# # # # # # # # # # # # key = os.urandom(16)
# # # # # # # # # # # # iv = os.urandom(16)
# # # # # # # # # # # print(key,iv,type(key))
# # # # # # # # # # # # key=b'0123456789abcdef0123456789abcdef'
# # # # # # # # # # # # iv=b'abcdef9876543210abcdef9876543210'
# # # # # # # # # # # key=b'\xd85N\xb8\xf0vLp\xdd\x18\xb6\xd9\x02\x10b\x82='
# # # # # # # # # # # iv =b'\xd0v\xe8\x99\x0f\xbd\xbeu\x178\x02\\t\xc3uN\x9a=='
# # # # # # # # # # #
# # # # # # # # # # # print(len(iv))
# # # # # # # # # # # print(type(key))
# # # # # # # # # # # print(type(iv))
# # # # # # # # # # # # key = b'xSAU2gWfDhWusUPplf8RtWknJ0ZKZ+dqK23/go8i0ls='
# # # # # # # # # # # key = base64.b64decode(key)
# # # # # # # # # # #
# # # # # # # # # # # # iv = b'WmiBaaAuyX7YCSTTPj07/c=='
# # # # # # # # # # # iv = base64.b64decode(iv)
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # # import sys
# # # # # # # # # # # #
# # # # # # # # # # # # byte_string = b''
# # # # # # # # # # # # size = sys.getsizeof(byte_string)
# # # # # # # # # # # # print(size)  # Output: 37
# # # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # def encrypt(data, key, iv):
# # # # # # # # # # #     cipher = AES.new(key, AES.MODE_CBC, iv)
# # # # # # # # # # #     encrypted_data = cipher.encrypt(pad(data, AES.block_size))
# # # # # # # # # # #     return encrypted_data
# # # # # # # # # # #
# # # # # # # # # # #
# # # # # # # # # # # def decrypt(encrypted_data, key, iv):
# # # # # # # # # # #     cipher = AES.new(key, AES.MODE_CBC, iv)
# # # # # # # # # # #     decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
# # # # # # # # # # #     return decrypted_data
# # # # # # # # # # # # plaintext = b'This is the data to be encrypted'
# # # # # # # # # # # # print(plaintext,type(plaintext))
# # # # # # # # # # #
# # # # # # # # # # # a={
# # # # # # # # # # #     "code": 200,
# # # # # # # # # # #     "msg": "数据新增成功"
# # # # # # # # # # # }
# # # # # # # # # # # plaintext = bytes(str(a), 'utf-8')  # Convert string to bytes using UTF-8 encoding
# # # # # # # # # # # print(plaintext,type(plaintext))
# # # # # # # # # # # encrypted_data = encrypt(plaintext, key, iv)
# # # # # # # # # # # print(encrypted_data)
# # # # # # # # # # # encrypted_data=b'adYFCWJ7/DlCh1QbDJN6TtQGMEvJp/tMomF2Q7gMdrIpPyiz3x61EKz/ssvXk/Z0'
# # # # # # # # # # # decrypted_data = decrypt(encrypted_data, key, iv)
# # # # # # # # # # #
# # # # # # # # # # # print(decrypted_data.decode('utf-8'))
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # from base64 import b64encode
# # # # # # # # # # from Crypto.Cipher import AES
# # # # # # # # # # from Crypto.Util.Padding import pad
# # # # # # # # # # from Crypto.Random import get_random_bytes
# # # # # # # # # #
# # # # # # # # # # sensitive_data = b'========'
# # # # # # # # # # key = get_random_bytes(16)  # 密钥必须是16、24或32字节长
# # # # # # # # # # cipher = AES.new(key, AES.MODE_CBC)
# # # # # # # # # # ciphertext = cipher.encrypt(pad(sensitive_data, AES.block_size))
# # # # # # # # # #
# # # # # # # # # # print(f"iv: {b64encode(cipher.iv).decode('utf-8')}")
# # # # # # # # # # print(f"ciphertext: {b64encode(ciphertext).decode('utf-8')}")
# # # # # # # # # # print(f"key: {b64encode(key).decode('utf-8')}")
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # from Crypto.Cipher import AES
# # # # # # # # # from Crypto.Util.Padding import unpad
# # # # # # # # # from base64 import b64decode
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # def aes_decrypt(encrypted, key, iv):
# # # # # # # # #     # key = key.encode('utf-8')
# # # # # # # # #     # iv = iv.encode('utf-8')
# # # # # # # # #     key=key
# # # # # # # # #     iv=iv
# # # # # # # # #     print(key,iv)
# # # # # # # # #     cipher = AES.new(key, AES.MODE_CBC, iv)
# # # # # # # # #     decrypted = cipher.decrypt(b64decode(encrypted))
# # # # # # # # #     unpadded = unpad(decrypted, AES.block_size)
# # # # # # # # #
# # # # # # # # #     return unpadded.decode('utf-8')
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # # Use the generated key, iv and encrypted data from the frontend
# # # # # # # # # key = '8bae0fed898a315e2eedc383aac1e16d'
# # # # # # # # # iv = 'b0ca7b006129a80000000000000000000000000'
# # # # # # # # # # iv = "your_iv_here"
# # # # # # # # # print(len(key))
# # # # # # # # # if len(iv) == 16:
# # # # # # # # #     # Continue with decryption
# # # # # # # # #     pass
# # # # # # # # # else:
# # # # # # # # #     raise ValueError("Incorrect IV length (it must be 16 bytes long)")
# # # # # # # # #
# # # # # # # # # encrypted_data = 'encrypteData U2FsdGVkX1/v6Echz3MRzmF9hF9Pmy2YqMRF8jyr/so='
# # # # # # # # #
# # # # # # # # # # Decrypt the data
# # # # # # # # # decrypted_data = aes_decrypt(encrypted_data, key, iv)
# # # # # # # # # print(decrypted_data)
# # # # # # # #
# # # # # # # #
# # # # # # # # from Crypto.Cipher import AES
# # # # # # # # import base64
# # # # # # # #
# # # # # # # # message = b"U2FsdGVkX1/v6Echz3MRzmF9hF9Pmy2YqMRF8jyr/so="
# # # # # # # # message = base64.b64decode(message)
# # # # # # # #
# # # # # # # # key = b'8bae0fed898a315e2eedc383aac1e16d'
# # # # # # # # key = base64.b64decode(key)
# # # # # # # #
# # # # # # # # iv = b'1c6afc062ad97249569c4252d0b9abf6'
# # # # # # # # iv = base64.b64decode(iv)
# # # # # # # #
# # # # # # # # aes = AES.new(key, AES.MODE_CBC, iv)
# # # # # # # # decd = aes.decrypt(message)
# # # # # # # # print(decd)
# # # # # # # from Crypto.Cipher import AES
# # # # # # # from Crypto.Random import get_random_bytes
# # # # # # # from Crypto.Util.Padding import pad, unpad
# # # # # # # import base64
# # # # # # #
# # # # # # # # 要解密的数据和IV（需要与前端保持一致）
# # # # # # # encrypted_data = "U2FsdGVkX1/7TnFq4U+aIg=="
# # # # # # # iv = b'v3Jbf6*^$8^%jw2p'
# # # # # # #
# # # # # # # # 16字节的AES加密密钥（需要与前端保持一致）
# # # # # # # aes_key = b'1234567890123456'
# # # # # # #
# # # # # # # # 解码base64编码的加密数据
# # # # # # # encrypted_data = base64.b64decode(encrypted_data)
# # # # # # #
# # # # # # # # 创建AES解密器
# # # # # # # cipher = AES.new(aes_key, AES.MODE_CBC, iv)
# # # # # # #
# # # # # # # # 解密数据并去除填充
# # # # # # # decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
# # # # # # #
# # # # # # # print("Decrypted Data:", decrypted_data.decode('utf-8'))
# # # # # #
# # # # # # from Crypto.Cipher import AES
# # # # # # from Crypto.Util.Padding import unpad
# # # # # # import base64
# # # # # #
# # # # # # # 要解密的数据和IV（需要与前端保持一致）
# # # # # # encrypted_data = "U2FsdGVkX1/7TnFq4U+aIg=="
# # # # # # iv = b'v3Jbf6*^$8^%jw2p'
# # # # # #
# # # # # # # 16字节的AES加密密钥（需要与前端保持一致），以字节形式编码为UTF-8
# # # # # # aes_key = b'1234567890123456'
# # # # # #
# # # # # # # 解码base64编码的加密数据
# # # # # # encrypted_data = base64.b64decode(encrypted_data)
# # # # # # #
# # # # # # # 创建AES解密器，使用CBC模式和前端提供的IV
# # # # # # cipher = AES.new(aes_key, AES.MODE_CBC, iv)
# # # # # #
# # # # # # # 解密数据并去除填充
# # # # # # decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
# # # # # #
# # # # # # print("Decrypted Data:", decrypted_data.decode('utf-8'))
# # # # #
# # # # #
# # # # # from Crypto.Cipher import AES
# # # # # from Crypto.Util.Padding import unpad
# # # # # import base64
# # # # #
# # # # # # 要解密的数据和IV（需要与前端保持一致）
# # # # # encrypted_data = "U2FsdGVkX1/7TnFq4U+aIg=="
# # # # # iv = b'v3Jbf6*^$8^%jw2p'
# # # # #
# # # # # # 16字节的AES加密密钥（需要与前端保持一致），以字节形式编码为UTF-8
# # # # # aes_key = b'1234567890123456'
# # # # #
# # # # # # 解码base64编码的加密数据
# # # # # encrypted_data = base64.b64decode(encrypted_data)
# # # # #
# # # # # # 创建AES解密器，使用CBC模式和前端提供的IV
# # # # # cipher = AES.new(aes_key, AES.MODE_CBC, iv)
# # # # #
# # # # # # 解密数据并去除填充
# # # # # decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
# # # # #
# # # # # print("Decrypted Data:", decrypted_data.decode('utf-8'))
# # # #
# # # #
# # # # from Crypto.Cipher import AES
# # # # import base64
# # # #
# # # # # 要解密的数据和IV（需要与前端保持一致）
# # # # encrypted_data = "U2FsdGVkX1/7TnFq4U+aIg=="
# # # # iv = b'v3Jbf6*^$8^%jw2p'
# # # #
# # # # # 16字节的AES加密密钥（需要与前端保持一致），以字节形式编码为UTF-8
# # # # aes_key = b'1234567890123456'
# # # #
# # # # # 解码base64编码的加密数据
# # # # encrypted_data = base64.b64decode(encrypted_data)
# # # #
# # # # # 创建AES解密器，使用CBC模式和前端提供的IV
# # # # cipher = AES.new(aes_key, AES.MODE_CBC, iv)
# # # #
# # # # # 解密数据并去除填充
# # # # decrypted_data = cipher.decrypt(encrypted_data)
# # # #
# # # # # 去除PKCS7填充
# # # # padding_length = decrypted_data[-1]
# # # # decrypted_data = decrypted_data[:-padding_length]
# # # #
# # # # print("Decrypted Data:", decrypted_data.decode('utf-8'))
# # #
# # #
# # # from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# # # from cryptography.hazmat.primitives import padding
# # # from cryptography.hazmat.backends import default_backend
# # #
# # #
# # # def pkcs7_padding(data, block_size):
# # #     padder = padding.PKCS7(block_size * 8).padder()
# # #     padded_data = padder.update(data) + padder.finalize()
# # #     return padded_data
# # #
# # #
# # # def pkcs7_unpadding(data, block_size):
# # #     unpadder = padding.PKCS7(block_size * 8).unpadder()
# # #     unpadded_data = unpadder.update(data) + unpadder.finalize()
# # #     return unpadded_data
# # #
# # #
# # # block_size = 16  # AES block size
# # #
# # # # Example usage:
# # # cipher = Cipher(algorithms.AES(b"16-byte-key"), modes.ECB(), backend=default_backend())
# # # encryptor = cipher.encryptor()
# # # decryptor = cipher.decryptor()
# # #
# # # # Encrypt and pad data
# # # data = b"Sample data"
# # # padded_data = pkcs7_padding(data, block_size)
# # # encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
# # #
# # # # Decrypt and unpad data
# # # decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
# # # unpadded_data = pkcs7_unpadding(decrypted_data, block_size)
# # #
# # # print(unpadded_data)
# #
# #
# # from Crypto.Cipher import AES
# # import base64
# #
# # # 要解密的数据和IV（需要与前端保持一致）
# # encrypted_data = "U2FsdGVkX1/7TnFq4U+aIg=="
# # iv = b'v3Jbf6*^$8^%jw2p'
# #
# # # 16字节的AES加密密钥（需要与前端保持一致），以字节形式编码为UTF-8
# # aes_key = b'1234567890123456'
# #
# # # 解码base64编码的加密数据
# # encrypted_data = base64.b64decode(encrypted_data)
# #
# # # 创建AES解密器，使用CBC模式和前端提供的IV
# # cipher = AES.new(aes_key, AES.MODE_CBC, iv)
# #
# # # 解密数据
# # decrypted_data = cipher.decrypt(encrypted_data)
# #
# # # 去除PKCS7填充
# # padding_length = decrypted_data[-1]
# # decrypted_data = decrypted_data[:-padding_length]
# #
# # # 解码为字符串
# # decrypted_text = decrypted_data.decode('utf-8')
# #
# # print("Decrypted Data:", decrypted_text,len(decrypted_text))
#
#
# from Crypto.Cipher import AES
# import base64
#
# # 要解密的数据和IV（需要与前端保持一致）
# encrypted_data = "U2FsdGVkX1/7TnFq4U+aIg=="
# iv = b'v3Jbf6*^$8^%jw2p'
#
# # 16字节的AES加密密钥（需要与前端保持一致），以字节形式编码为UTF-8
# aes_key = b'1234567890123456'
#
# # 解码base64编码的加密数据
# encrypted_data = base64.b64decode(encrypted_data)
#
# # 创建AES解密器，使用CBC模式和前端提供的IV
# cipher = AES.new(aes_key, AES.MODE_CBC, iv)
#
# # 解密数据
# decrypted_data = cipher.decrypt(encrypted_data)
#
# # 去除PKCS7填充
# padding_length = decrypted_data[-1]
# decrypted_data = decrypted_data[:-padding_length]
#
# # 解码为字符串
# decrypted_text = decrypted_data.decode('utf-8')
#
# print("Decrypted Data:", decrypted_text)


# print("解密")
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import json
from Crypto import Random
from Crypto.Util.Padding import pad

# 要解密的数据
encrypted_data = "N3/a+8rdBarX51bYwLmLpq0njOFf2dry2V53mPJmC4rtXunRySxewLcB9kpvzumtENEKVAy8JTwh1dIefOm6tQ=="

# 16字节的AES加密密钥（需要与前端保持一致），以字节形式编码为UTF-8
aes_key = b'1234567890123456'

# 固定的初始化向量（与前端一致）
# fixed_iv = b'\x00' * 16

# 前端发送的IV字符串
iv_string_from_frontend = "8I/nyPSU0NMIceOtevV5vQ=="
# 解码base64编码的IV字符串
iv_bytes = base64.b64decode(iv_string_from_frontend)

print("IV Bytes:", iv_bytes)
fixed_iv=iv_bytes
print("fixed_iv",fixed_iv)


# # 前端发送的key字符串
# key_string_from_frontend = "cIXreJbM0ACb2OX9Ty8drg=="
# # 解码base64编码的IV字符串
# key_bytes = base64.b64decode(key_string_from_frontend)
#
# print("IV Bytes:", key_bytes)
# aes_key=key_bytes# # 前端发送的key字符串
# # key_string_from_frontend = "cIXreJbM0ACb2OX9Ty8drg=="
# # # 解码base64编码的IV字符串
# # key_bytes = base64.b64decode(key_string_from_frontend)
# #
# # print("IV Bytes:", key_bytes)
# print("ass_key",aes_key)




# 解码base64编码的加密数据
encrypted_data = base64.b64decode(encrypted_data)

# 创建AES解密器，使用CBC模式和前端提供的IV
cipher = AES.new(aes_key, AES.MODE_CBC, fixed_iv)

# 解密数据并去除填充
decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
print(decrypted_data,type(decrypted_data))
print("Decrypted Data:", decrypted_data.decode('utf-8'),eval(decrypted_data.decode('utf-8')),json.loads(decrypted_data.decode('utf-8')),type(eval(decrypted_data.decode('utf-8'))))







print("========================================")
#加密
# # # # # # # # # # # from Crypto.Util.Padding import pad, unpad
# # # # # # # # # # # import os
from Crypto import Random
#
# key = os.urandom(16)
# iv = os.urandom(16)
from Crypto.Util.Padding import pad
import json
# Data to be encrypted
data = {"code": "1010000087", "name": "王建", "idCard": "fsfsfdfs"}
data=json.dumps(data)
print(data,type(data))
# AES encryption key (16 bytes)
key = b'1234567890123456'

# iv = Random.new().read(AES.block_size)  # 16 bytes
# iv = base64.b64decode(iv)
# key = Random.new().read(16)  # 16 bytes for AES-128, 24 bytes for AES-192, 32 bytes for AES-256
iv = Random.new().read(AES.block_size)  # 16 bytes
print('iv',iv)
# Initialization Vector (16 bytes)
# iv = b'\xa7\x11\xc2\xd9\xad\x05\x14\xce\x7f\xc5\x05 3d\x9bf'

iv_data = base64.b64encode(iv)
print("iv_data",iv_data)


# key= Random.new().read(AES.block_size)  # 16 bytes
# print('key',key)
# # Initialization Vector (16 bytes)
# # iv = b'\xa7\x11\xc2\xd9\xad\x05\x14\xce\x7f\xc5\x05 3d\x9bf'
#
# key= base64.b64encode(key)
# print("key",key)



# Create AES cipher object using CBC mode and the provided key and IV
cipher = AES.new(key, AES.MODE_CBC, iv)

# Pad the data to match the block size of AES (16 bytes)
padded_data = pad(data.encode('utf-8'), AES.block_size)

# Encrypt the padded data
encrypted_data = cipher.encrypt(padded_data)

# Encode the encrypted data in base64
encoded_data = base64.b64encode(encrypted_data)
# print(encoded_data)
print("Encrypted Data:", encoded_data.decode('utf-8'))  #加密的数据






