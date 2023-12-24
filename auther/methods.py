from django.contrib.auth.hashers import check_password

from auther.models import AdminNavMenuList, AdminUser
from utils.check_token import CheckToken
from utils.create_token import CreateToken
from setup.models import *
class Login:
    # 校验用户名,密码
    def check_admin_info(self, username, password):
        return_data = {'code': "", "msg": ""}
        account = AdminUser.objects.filter(username=username,is_used=True).values("username", "password", "user", "is_superuser",'id')
        if account.exists():
            pwd_check = check_password(password, account[0]['password'])
            if pwd_check == True:
                # admin_token = CreateToken(username)
                admin_token = CreateToken(account[0]['id'])
                set_token = admin_token.create_token()
                return_data['code'] = 200
                return_data['msg'] = "登录成功"
                return_data['data'] = {}
                return_data['data']['token'] = set_token
                return_data['data']['userInfo'] = {}
                return_data['data']['userInfo']['user'] = account[0]['user']
                return_data['data']['userInfo']['is_superuser'] = account[0]['is_superuser']
                return return_data
            else:
                return_data['code'] = 401
                return_data['msg'] = "密码错误"
        else:
            return_data['code'] = 401
            return_data['msg'] = "用户名不存在"
        return return_data

    # 获取侧边栏
    def get_sidebar(self, token):
        return_data = {'code': "", 'data': "", "msg": ""}
        get_token = CheckToken()
        # print(get_token)
        # admin_username = get_token.check_token(token)
        admin_id = get_token.check_token(token)
        if admin_id is not None:
            admin_id = AdminUser.objects.filter(id=admin_id).values_list('user_menu__id',
                                                                                     'user_menu__nav_index',
                                                                                     'user_menu__nav_name',
                                                                                     'user_menu__nav_url',
                                                                                     'user_menu__nav_icon',
                                                                                     'user_menu__nav_component',
                                                                                     'user_menu__nav_parent_id',
                                                                                     'user_menu__nav_type').order_by('user_menu__nav_index')

            sidetree = {}
            for datas in admin_id:
                sidetree[datas[0]] = {}  # 创建一个以id创建的为主键的字典
                sidetree[datas[0]]['nav_index'] = datas[1]
                sidetree[datas[0]]['nav_name'] = datas[2]
                sidetree[datas[0]]['nav_url'] = datas[3]
                sidetree[datas[0]]['nav_icon'] = datas[4]
                sidetree[datas[0]]['nav_component'] = datas[5]
                sidetree[datas[0]]['nav_parent_id'] = datas[6]
                sidetree[datas[0]]['nav_type'] = datas[7]
            sidetree_list = []
            for key, value in list(sidetree.items()):
                pid = value.get('nav_parent_id')
                if pid is None:
                    sidetree_list.append(value)
                elif value.get('nav_type') == 1:
                    try:
                        sidetree[pid]['children'].append(value)
                    except KeyError:
                        sidetree[pid]['children'] = []
                        sidetree[pid]['children'].append(value)
            return_data['code'] = 200
            return_data['data'] = sidetree_list
            return_data['hidden'] = True
            return_data['msg'] = '获取数据成功'

            # print(return_data)
            return_data['data'] = [item for item in return_data['data'] if not all(value is None for value in item.values())]



            return return_data

    #获取导航
    def get_nav(self,token):
        return_data = {'code': "", 'data': "", "msg": ""}
        get_token = CheckToken()
        admin_id = get_token.check_token(token)
        # admin_id=2
        if admin_id is not None:
            admin_nav_list = list(AdminUser.objects.filter(id=admin_id,user_nav__menu_level__in=[1,2,3]).values('user_nav__id',
                                                                         # 'user_nav__menu_index',
                                                                         'user_nav__menu_icon',
                                                                         'user_nav__menu_complete_path',
                                                                         'user_nav__menu_name',
                                                                         'user_nav__menu_type',
                                                                         'user_nav__menu_parent_id',
                                                                         'user_nav__menu_level',
                                                                         'user_nav__menu_category_id',
                                                                         'user_nav__menu_category_name',
                                                                         ).order_by('user_nav__menu_index'))
            # print(admin_nav_list)
            # print(len(admin_nav_list))
            for line in admin_nav_list:
                line['id']=line['user_nav__id']
                line['parent_id'] = line['user_nav__menu_parent_id']
                line['icon'] = line['user_nav__menu_icon']
                line['path'] = line['user_nav__menu_complete_path']
                line['name'] = line['user_nav__menu_name']
                line['type'] = line['user_nav__menu_type']
                line['category_id']=line['user_nav__menu_category_id']
                line['category_name'] = line['user_nav__menu_category_name']
                line['level']=line['user_nav__menu_level']
                del line['user_nav__id']
                del line['user_nav__menu_parent_id']
                del line['user_nav__menu_icon']
                del line['user_nav__menu_complete_path']
                del line['user_nav__menu_name']
                del line['user_nav__menu_type']
                del line['user_nav__menu_category_id']
                del line['user_nav__menu_category_name']
                del line['user_nav__menu_level']

            def build_menu_tree(menu_items, parent_id=None):
                tree = []
                for item in menu_items:
                    if item['parent_id'] == parent_id:
                        children = build_menu_tree(menu_items, item['id'])
                        if children:
                            item['children'] = children
                        tree.append(item)
                return tree

            b = build_menu_tree(admin_nav_list)
            print(b)

            # parent_dict = {}
            # result = []
            #
            # for item in admin_nav_list:
            #     if item['user_nav__menu_level'] == 1:
            #         menu_item = {
            #             "icon": item['user_nav__menu_icon'],
            #             "name": item['user_nav__menu_name'],
            #             "path": item['user_nav__menu_complete_path'],
            #             "parent_id": None,
            #             "type": item['user_nav__menu_type'],
            #             "id": item['user_nav__id'],
            #             "children": []
            #         }
            #         result.append(menu_item)
            #         parent_dict[item['user_nav__id']] = menu_item
            #     else:
            #         if item['user_nav__menu_type'] == 1:
            #             menu_item = {
            #                 "icon": item['user_nav__menu_icon'],
            #                 "name": item['user_nav__menu_name'],
            #                 "path": item['user_nav__menu_complete_path'],
            #                 "parent_id": item['user_nav__menu_parent_id'],
            #                 "type": item['user_nav__menu_type'],
            #                 "id": item['user_nav__id'],
            #                 'category_id':item['user_nav__menu_category_id'],
            #                 'category_name': item['user_nav__menu_category_name']
            #             }
            #             parent_dict[item['user_nav__menu_parent_id']]['children'].append(menu_item)




            return_data['code'] =200
            return_data['hidden'] = True
            return_data['msg'] = '获取数据成功'
            return_data['data']=b
#             return_data['data'] = [
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
#       {
#         "icon": None,
#         "name": "入职管理",
#         "path": "/employeeInformation/PreEntry",
#         "parent_id": 1,
#         "type": 1,
#         "id": 4,
#         "category_id": 1,
#         "category_name": "组织员工"
#       },
#       {
#         "icon": None,
#         "name": "外派信息",
#         "path": "/expatriateRecord/expatriateLedger",
#         "parent_id": 1,
#         "type": 1,
#         "id": 5,
#         "category_id": 1,
#         "category_name": "组织员工"
#       },
#       {
#         "icon": None,
#         "name": "竞业限制",
#         "path": "/competeRestrictions/record",
#         "parent_id": 1,
#         "type": 1,
#         "id": 6,
#         "category_id": 1,
#         "category_name": "组织员工"
#       },
#       {
#         "icon": None,
#         "name": "数据分析",
#         "path": None,
#         "parent_id": 1,
#         "type": 1,
#         "id": 7,
#         "category_id": 1,
#         "category_name": "组织员工"
#       },
#       {
#         "icon": None,
#         "name": "档案管理",
#         "path": "1111",
#         "parent_id": 1,
#         "type": 1,
#         "id": 8,
#         "category_id": 1,
#         "category_name": "组织员工"
#       }
#     ]
#   },
#   {
#     "icon": "/icon/kaoqin.png",
#     "name": "假勤管理",
#     "path": None,
#     "parent_id": None,
#     "type": 1,
#     "id": 11,
#     "children": [
#       {
#         "icon": None,
#         "name": "离岗分析",
#         "path": "1111",
#         "parent_id": 11,
#         "type": 1,
#         "id": 12,
#         "category_id": 2,
#         "category_name": "假勤管理"
#       }
#     ]
#   },
#   {
#     "icon": "/icon/kaoqin.png",
#     "name": "人力月报",
#     "path": None,
#     "parent_id": None,
#     "type": 1,
#     "id": 31,
#     "children": [
#       {
#         "icon": None,
#         "name": "公司大事记",
#         "path": "memorabilia/Record",
#         "parent_id": 31,
#         "type": 1,
#         "id": 32,
#         "category_id": 4,
#         "category_name": "人力月报"
#       }
#     ]
#   },
#   {
#     "icon": "/icon/peixun.png",
#     "name": "培训",
#     "path": None,
#     "parent_id": None,
#     "type": 1,
#     "id": 41,
#     "children": [
#       {
#         "icon": 'el-icon-data-line',
#         "name": "讲师库",
#         "path": None,
#         "parent_id": 41,
#         "type": 1,
#         "id": 42,
#         "category_id": 41,
#         "category_name": "培训",
#         "children":[{
#                          "icon": None,
#                          "name": "讲师明细",
#                          "path": "/offlineTraining/LecturerDetail",
#                          "parent_id": 42,
#                          "type": 1,
#                          "id": 43,
#                          "category_id": 41,
#                          "category_name": "培训",
#                      },
#                      {
#                          "icon": None,
#                          "name": "讲师分析",
#                          "path": "/offlineTraining/SummaryDetail",
#                          "parent_id": 42,
#                          "type": 1,
#                          "id": 44,
#                          "category_id": 41,
#                          "category_name": "培训",
#                      },
#                      {
#                          "icon": None,
#                          "name": "卸任/离职讲师明细",
#                          "path": "/offlineTraining/OutgoingLecturer",
#                          "parent_id":42,
#                          "type": 1,
#                          "id": 45,
#                          "category_id":41,
#                          "category_name": "培训",
#                      }]
#
#       },
#       {
#         "icon": 'el-icon-data-line',
#         "name": "培训报表",
#         "path": "/offlineTraining/TrainingReport",
#         "parent_id": 41,
#         "type": 1,
#         "id": 46,
#         "category_id":41,
#         "category_name": "培训"
#       },
#         {
#             "icon": 'el-icon-data-line',
#             "name": "培训类型",
#             "path": "/offlineTraining/TrainingType",
#             "parent_id": 41,
#             "type": 1,
#             "id": 47,
#             "category_id": 41,
#             "category_name": "培训"
#         },
#         {
#             "icon": 'el-icon-data-line',
#             "name": "培训记录",
#             "path": "/offlineTraining/TrainingSignIn",
#             "parent_id": 41,
#             "type": 1,
#             "id": 48,
#             "category_id": 41,
#             "category_name": "培训"
#         },
#         {
#             "icon": 'el-icon-data-line',
#             "name": "本月汇总分析",
#             "path": "/offlineTraining/SummaryAnalysis",
#             "parent_id": 41,
#             "type": 1,
#             "id": 49,
#             "category_id": 41,
#             "category_name": "培训"
#         },
#         {
#             "icon": 'el-icon-data-line',
#             "name": "本月人均课时",
#             "path": "/offlineTraining/TrainingPeriod",
#             "parent_id": 41,
#             "type": 1,
#             "id": 50,
#             "category_id": 41,
#             "category_name": "培训"
#         },
#     ]
#   }
# ]


#             return_data['data']=[
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
#       {
#         "icon": None,
#         "name": "入职管理",
#         "path": "/employeeInformation/PreEntry",
#         "parent_id": 1,
#         "type": 1,
#         "id": 4,
#         "category_id": 1,
#         "category_name": "组织员工"
#       },
#       {
#         "icon": None,
#         "name": "外派信息",
#         "path": "/expatriateRecord/expatriateLedger",
#         "parent_id": 1,
#         "type": 1,
#         "id": 5,
#         "category_id": 1,
#         "category_name": "组织员工"
#       },
#       {
#         "icon": None,
#         "name": "竞业限制",
#         "path": "/competeRestrictions/record",
#         "parent_id": 1,
#         "type": 1,
#         "id": 6,
#         "category_id": 1,
#         "category_name": "组织员工"
#       },
#       {
#         "icon": None,
#         "name": "数据分析",
#         "path": "111",
#         "parent_id": 1,
#         "type": 1,
#         "id": 7,
#         "category_id": 1,
#         "category_name": "组织员工"
#       },
#       {
#         "icon": None,
#         "name": "档案管理",
#         "path": " 111",
#         "parent_id": 1,
#         "type": 1,
#         "id": 8,
#         "category_id": 1,
#         "category_name": "组织员工"
#       }
#     ]
#   },
#   {
#     "icon": "/icon/kaoqin.png",
#     "name": "假勤管理",
#     "path": " ",
#     "parent_id": None,
#     "type": 1,
#     "id": 11,
#     "children": [
#       {
#         "icon": None,
#         "name": "离岗分析",
#         "path": "1111",
#         "parent_id": 11,
#         "type": 1,
#         "id": 12,
#         "category_id": 2,
#         "category_name": "假勤管理"
#       }
#     ]
#   },
#   {
#     "icon": "/icon/kaoqin.png",
#     "name": "人力月报",
#     "path": None,
#     "parent_id": None,
#     "type": 1,
#     "id": 31,
#     "children": [
#       {
#         "icon": None,
#         "name": "公司大事记",
#         "path": "memorabilia/Record",
#         "parent_id": 31,
#         "type": 1,
#         "id": 32,
#         "category_id": 4,
#         "category_name": "人力月报"
#       }
#     ]
#   },
#   {
#     "icon": "/icon/peixun.png",
#     "name": "培训",
#     "path": None,
#     "parent_id": None,
#     "type": 1,
#     "id": 41,
#     "children": [
#       {
#         "icon": None,
#         "name": "线下培训",
#         "path": None,
#         "parent_id": 41,
#         "type": 1,
#         "id": 42,
#         "category_id": 5,
#         "category_name": "培训",
#          "children": [
#              {
#                  "icon": None,
#                  "name": "讲师库",
#                  "path": "/offlineTraining",
#                  "parent_id": 42,
#                  "type": 1,
#                  "id": 43,
#                  "category_id": 5,
#                  "category_name": "培训",
#                  "children": [
#                      {
#                          "icon": None,
#                          "name": "讲师明细",
#                          "path": "/offlineTraining/LecturerDetail",
#                          "parent_id": 43,
#                          "type": 1,
#                          "id": 44,
#                          "category_id": 5,
#                          "category_name": "培训",
#                      },
#                      {
#                          "icon": None,
#                          "name": "讲师分析",
#                          "path": "/offlineTraining/SummaryDetail",
#                          "parent_id": 43,
#                          "type": 1,
#                          "id": 45,
#                          "category_id": 5,
#                          "category_name": "培训",
#                      },
#                      {
#                          "icon": None,
#                          "name": "卸任/离职讲师明细",
#                          "path": "/offlineTraining/OutgoingLecturer",
#                          "parent_id": 43,
#                          "type": 1,
#                          "id": 46,
#                          "category_id": 5,
#                          "category_name": "培训",
#                      }
#                  ]
#              },
#             {
#               "icon": None,
#               "name": "培训报表",
#               "path": '/offlineTraining/TrainingReport',
#               "parent_id": 42,
#               "type": 1,
#               "id": 47,
#               "category_id": 5,
#               "category_name": "培训",
#             },
#
#           ]
#
#       }
#     ]
#   }
# ]

            # print(result)

        return return_data

    #获取侧边栏（新）
    def get_sidebat_new(self,token):
        return_data = {'code': "", 'data': "", "msg": ""}
        get_token = CheckToken()
        admin_id = get_token.check_token(token)

        if admin_id is not None:
            admin_nav_list = list(AdminUser.objects.filter(id=admin_id,user_nav__menu_level__gt=1).values('user_nav__id',
                                                          'user_nav__menu_index',
                                                          'user_nav__menu_icon',
                                                          'user_nav__menu_path',
                                                          'user_nav__menu_name',
                                                          'user_nav__menu_type',
                                                          'user_nav__menu_parent_id',
                                                          'user_nav__menu_level',
                                                          'user_nav__menu_category_id',
                                                          'user_nav__menu_category_name',
                                                           'user_nav__menu_secondary_category_id'
                                                          ).order_by('user_nav__menu_index'))
            # for line in admin_nav_list:
            #     print(line)
            print(admin_nav_list)

            result_data = self.transform_data(admin_nav_list)
            return_data['code'] =200
            return_data['hidden'] = True
            return_data['msg'] = '获取数据成功'
            return_data['data']=result_data
#             return_data['data']=[
#   {
#       'nav_id':2,
#     'nav_index': '1-1',
#     'nav_name': '花名册',
#     'nav_url': '/employeeInformation/Roster',
#     'nav_icon': '',
#     'nav_component': 'layout/index',
#     'nav_parent_id': None,
#     'nav_type': 1,
#     'nav_level':2,
#       'nav_category_id': 1,
#       'nav_category_name': '组织员工',
#       'nav_secondary_category_id':None
#   },
#
#   {
#       'nav_id': 3,
#     'nav_index': '1-2',
#     'nav_name': '追光者信息',
#     'nav_url': '/volumeContracts/Record',
#     'nav_icon': '',
#     'nav_component': 'layout/index',
#     'nav_parent_id': None,
#     'nav_type': 1,
#     'nav_level': 2,
#       'nav_category_id': 1,
#       'nav_category_name': '组织员工',
#       'nav_secondary_category_id': None
#   },
#   {
#       'nav_id': 42,
#     'nav_index': '5-1',
#     'nav_name': '线下培训',
#     'nav_url': '/offlineTraining',
#     'nav_icon': '',
#     'nav_component': 'layout/index',
#     'nav_parent_id': None,
#     'nav_type': 1,
#     'nav_level': 2,
#       'nav_category':5,
#       'nav_category_name': '培训',
#       'nav_secondary_category_id': None,
#     'children': [
#         {
#             'nav_id': 47,
#             'nav_index': '5-1-2',
#             'nav_name': '培训报表',
#             'nav_url': '/TrainingReport',
#             'nav_icon': '',
#             'nav_component': '/views/offlineTraining/TrainingReport',
#             'nav_parent_id': 42,
#             'nav_type': 1,
#             'nav_level': 3,
#             'nav_category': 5,
#             'nav_category_name': '培训',
#             'nav_secondary_category_id': 42
#         },
#       {
#           'nav_id': 43,
#         'nav_index': '5-1-1',
#         'nav_name': '讲师库',
#         'nav_url': '/offlineTraining',
#         'nav_icon': '',
#         'nav_component': '/views/offlineTraining',
#         'nav_parent_id': 42,
#         'nav_type': 1,
#     	'nav_level': 3,
#           'nav_category': 5,
#           'nav_category_name': '培训',
#           'nav_secondary_category_id': 42,
#         'children': [
#           {
#               'nav_id': 44,
#             'nav_index': '5-1-1-2',
#             'nav_name': '讲师明细',
#             'nav_url': '/LecturerDetail',
#             'nav_icon': '',
#             'nav_component': '/views/offlineTraining/LecturerDetail',
#             'nav_parent_id': 43,
#             'nav_type': 1,
#           	'nav_level': 4,
#               'nav_category': 5,
#               'nav_category_name': '培训',
#               'nav_secondary_category_id': 42
#           },
#           {
#               'nav_id': 45,
#             'nav_index': '5-1-1-2',
#             'nav_name': '讲师分析',
#             'nav_url': '/SummaryDetail',
#             'nav_icon': '',
#             'nav_component': '/views/offlineTraining/SummaryDetail',
#             'nav_parent_id': 43,
#             'nav_type': 1,
#             'nav_level': 4,
#               'nav_category': 5,
#               'nav_category_name': '培训',
#               'nav_secondary_category_id': 42
#           },
#           {
#               'nav_id': 46,
#             'nav_index': '5-1-1-3',
#             'nav_name': '卸任/离职讲师明细',
#             'nav_url': '/OutgoingLecturer',
#             'nav_icon': '',
#             'nav_component': '/views/offlineTraining/OutgoingLecturer',
#             'nav_parent_id': 43,
#             'nav_type': 1,
#     				'nav_level': 4,
#               'nav_category': 5,
#               'nav_category_name': '培训',
#               'nav_secondary_category_id': 42
#           }
#         ]
#       },
#
#
#     ]
#   },
#
# ]


            # print(return_data['data'])
            return return_data
    @staticmethod
    def transform_data(data):
        nav_map = {}
        root_items = []

        for item in data:
            nav_id = item['user_nav__id']
            parent_id = item['user_nav__menu_parent_id']

            nav_item = {
                'nav_id': nav_id,
                'nav_index': item['user_nav__menu_index'],
                'nav_name': item['user_nav__menu_name'],
                'nav_url': item['user_nav__menu_path'],
                'nav_icon': item['user_nav__menu_icon'],
                'nav_component': 'layout/index',
                'nav_type': item['user_nav__menu_type'],
                'nav_level': item['user_nav__menu_level'],
                'nav_category_id': item['user_nav__menu_category_id'],
                'nav_category_name': item['user_nav__menu_category_name'],
                'nav_secondary_category_id': item['user_nav__menu_secondary_category_id']
            }

            nav_map[nav_id] = nav_item

            if parent_id in nav_map:
                if 'children' not in nav_map[parent_id]:
                    nav_map[parent_id]['children'] = []
                nav_map[parent_id]['children'].append(nav_item)
            else:
                root_items.append(nav_item)

        return root_items
