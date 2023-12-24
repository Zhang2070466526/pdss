import json, os,arrow,openpyxl,time,requests

from django.db.models import Q,F
from rest_framework import status
from django.http import JsonResponse

from auther.models import AdminUser
from employee.models import *

from datetime import datetime, date,timedelta

from socialSecurity.Anomalies.models import *
from pdss.settings import BASE_DIR
from socialSecurity.publicMethods import *
from utils.wechat_interface import *

class Anomalies:
    def __init__(self, request,meth):
        self.request = request
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功'
        }
        self.meth = meth
        self.now = arrow.now()
        self.t1 = self.now.format('YYYY-MM-DD')
        self.t2 = self.now.timestamp()
        self.methods = {
            'get_anomalies_info': self.get_anomalies_info,        #社保增员信息 查询
            'batch_anomalies_info':self.batch_anomalies_info,     #社保增员信息上传
            'down_anomalies_info':self.down_anomalies_info,      #社保增员信息 下载
            'post_dispose_gather':self.post_dispose_gather,       #收集员工处理结果   手机端
            'post_dispose_overrule':self.post_dispose_overrule,   #驳回员工处理结果   平台端
            'timing_employee_reminders':self.timing_employee_reminders,#定时任务 员工未提醒
        }
        self.Enterprise_WeChat=Enterprise_WeChat()   #企业微信的接口
    def method_center(self):
        if self.meth in ['post_dispose_gather','timing_employee_reminders']:
            pass
        else:
            if self.request.check_token is None:
                self.return_data = {'code': status.HTTP_403_FORBIDDEN, "msg": '没有权限访问!'}
                return JsonResponse(self.return_data)

        self.methods[self.meth]()
        return JsonResponse(self.return_data)

    # 获取信息列表
    def get_anomalies_info(self):
        columnList = [{'label': 'index', 'value': '序号', 'width': 60},
                      {'label': 'anomalies_people__employee_code', 'value': '工号', 'width': 100},
                      {'label': 'anomalies_people__employee_name', 'value': '姓名', 'width':100},
                      {'label': 'anomalies_people__employee_identity_no', 'value': '身份证号', 'width': ""},
                      {'label': 'anomalies_people__employee_job_rank__job_rank_name', 'value': '合同归属', 'width': ""},
                      {'label': 'anomalies_people__employee_department__department_manage', 'value': '管理归属', 'width': ""},
                      {'label': 'anomalies_people__employee_department__department_first_name', 'value': '一级部门', 'width': ""},
                      {'label': 'anomalies_people__employee_department__department_second_name', 'value': '二级部门','width': ""},
                      {'label': 'anomalies_people__employee_department__department_third_name', 'value': '三级部门','width': ""},
                      {'label': 'anomalies_insurance_type__insurance_type_name', 'value': '险种', 'width': ""},
                      {'label': '_anomalies_month', 'value': '月份', 'width': ""},
                      {'label': 'anomalies_fail_reason', 'value': '增员失败原因','width': ""},
                      {'label': 'anomalies_return_reason', 'value': '返回原因', 'width': ""},
                      {'label': 'anomalies_dispose', 'value': '需如何处理', 'width': ""},
                      {'label': 'anomalies_process_results', 'value': '员工处理结果', 'width': ""},
                      ]
        currentPage = json.loads(self.request.body).get('currentPage')
        pageSize = json.loads(self.request.body).get('pageSize')

        totalNumber = SocialSecurityAnomalies.objects.filter(anomalies_status=True).count()
        tableList = list(
            SocialSecurityAnomalies.objects.filter(anomalies_status=True).values('id',
                                                                                 'anomalies_people_id',
                                                                        'anomalies_people__employee_name',
                                                                        'anomalies_people__employee_code',
                                                                        'anomalies_people__employee_identity_no',
                                                                        'anomalies_people__employee_job_rank__job_rank_name',
                                                                        'anomalies_people__employee_department__department_manage',
                                                                        'anomalies_people__employee_department__department_first_name',
                                                                        'anomalies_people__employee_department__department_second_name',
                                                                        'anomalies_people__employee_department__department_third_name',

                                                                        'anomalies_fail_reason',    #失败原因唯一
                                                                        'anomalies_insurance_type__insurance_type_name',  #险种唯一
                                                                        'anomalies_month',         #月份唯一

                                                                        # 'anomalies_return_reason',
                                                                        # 'anomalies_dispose',
                                                                        # 'anomalies_process_results',
                                                            )[(currentPage - 1) * pageSize:currentPage * pageSize])

        all_id = [item['id'] for item in tableList]     #所有记录的id
        results_list=list(SocialSecurityAnomaliesResults.objects.filter(results_anomalies_id__in=all_id,results_status=True).values('id','results_people_id','results_anomalies_id','return_dispose','return_cause','results_process'))
        fils_list=list(SocialSecurityFiles.objects.filter(anomalies_file_id__in=all_id,file_status=True).values('id','file_type','file_name','file_url','anomalies_file_id'))


        anomalies_file = {}  # 员工凭证表

        for item in fils_list:  # 查找每份提案对应的文件
            anomalies_file_id = item.get('anomalies_file_id')
            if item['file_type'] == 1:  # 活动照片
                if anomalies_file_id not in anomalies_file:
                    anomalies_file[anomalies_file_id] = []
                anomalies_file[anomalies_file_id].append(item)
        for index, item in enumerate(tableList):
            item['index'] = (currentPage - 1) * pageSize + index + 1
            item['return_cause'] =','.join([line['return_cause'] for line in results_list if line['results_anomalies_id'] == item['id'] and line['results_people_id']==item['anomalies_people_id'] and line['return_cause'] is not None ])
            item['return_dispose'] = ','.join([line['return_dispose'] for line in results_list if line['results_anomalies_id'] == item['id'] and line['results_people_id'] == item['anomalies_people_id']  and line['return_dispose'] is not None])
            item['results_process'] =','.join([line['results_process'] for line in results_list if line['results_anomalies_id'] == item['id'] and line['results_people_id']==item['anomalies_people_id'] and line['results_process'] is not None])
            if item['id'] in anomalies_file:
                item['anomalies_file_ls'] = anomalies_file[item['id']]
                item['anomalies_file_num'] = len(anomalies_file[item['id']])
            else:
                item['anomalies_file_ls'] = []
                item['anomalies_file_num'] = 0


        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "信息返回成功",
            "data": {
                'columnList': columnList,
                'tableList': tableList,
                'totalNumber': totalNumber,
            }
        }


    def batch_anomalies_info(self):
        file = self.request.FILES.get("file", None)

        dummy_path = os.path.join(BASE_DIR, 'static', 'socialSecurityFile', 'upload_file', self.t1,'社保增员提醒文件上传')  # 创建文件夹
        mkdir(dummy_path)
        file_url, file_name, file_suffix = createPath(file, '社保增员提醒文件上传','socialSecurityFile', '培训增员提醒' + str(self.t2))
        saveFile(file_url, file)
        exc = openpyxl.load_workbook(file_url, data_only=True)
        sheet = exc.active
        access_token=self.Enterprise_WeChat.get_wx_access_token()   #access_token
        for line in range(1, sheet.max_row):  # 每行数据
            print(line)
            code = sheet.cell(line+1, 2).value
            name = sheet.cell(line+1, 3).value
            anomalies_insurance_type = sheet.cell(line + 1, 10).value  # 险种
            anomalies_fail_reason = sheet.cell(line+1, 11).value   #失败原因
            return_dispose = sheet.cell(line+1, 12).value    #如何处理
            return_cause = sheet.cell(line + 1, 13).value  # 退回原因
            anomalies_month=sheet.cell(line+1,14).value #月份
            print(name,code,anomalies_fail_reason,return_cause,return_dispose)

            hr_employee_obj = HrEmployee.objects.filter(employee_code=code).first()

            anomalies_params={
                'anomalies_people_id':hr_employee_obj.id,
                'anomalies_fail_reason':anomalies_fail_reason,   #失败原因
                'anomalies_insurance_type':anomalies_insurance_type,  #险种
                'anomalies_month':anomalies_month
            }
           #失败原因 险种唯一
            anomalies_obj=SocialSecurityAnomalies.objects.update_or_create(defaults=anomalies_params,
                                                             anomalies_people_id=anomalies_params['anomalies_people_id'],
                                              anomalies_insurance_type=anomalies_params['anomalies_insurance_type'], anomalies_status=True)
            print(anomalies_obj)

            result_obj=SocialSecurityAnomaliesResults.objects.filter(results_people_id=hr_employee_obj.id,results_anomalies_id=anomalies_obj[0].id).order_by('-results_createTime').first()
            print(result_obj)
                # if flag <= 1:
                #    content= '工号：{}\n姓名：{}\n险种：{}\n增员失败原因：{}\n需如何处理：{}<a href=\"http://work.weixin.qq.com\">一刀99999</a>'.format(params['code'],params['name'],params['anomalies_insurance_type'],params['anomalies_fail_reason'],params['return_dispose'])
                # else:
                #     content='工号：{}\n姓名：{}\n险种：{}\n增员退回原因：{}\n需如何处理：{}<a href=\"http://work.weixin.qq.com\">一刀99999</a>'.format(params['code'],params['name'],params['anomalies_insurance_type'],params['return_cause'],params['return_dispose'])

            if result_obj:   #print('有驳回记录')   会加上增员退回原因
                result_params={
                    'results_people_id':hr_employee_obj.id,
                    'results_anomalies_id':anomalies_obj[0].id,   #记录id
                    'return_dispose':return_dispose,    #需如何处理
                    'return_cause': return_cause,  # 退回原因
                    'results_frequency':  result_obj.results_frequency+1
                }
                push_info = {
                    'code': code,
                    'name': name,
                    'anomalies_insurance_type': anomalies_insurance_type,  # 险种
                    'return_dispose': return_dispose,  # 需如何处理
                    'return_cause':return_cause,#退回原因
                    'content': '工号：{}\n姓名：{}\n险种：{}\n增员退回原因：{}\n需如何处理：{}<a href=\"http://work.weixin.qq.com\">一刀99999</a>'.format(code,name,anomalies_insurance_type,return_cause,return_dispose)

                }
            else:
                result_params={
                    'results_people_id':hr_employee_obj.id,
                    'results_anomalies_id':anomalies_obj[0].id,   #记录id
                    'return_dispose':return_dispose,    #需如何处理
                    'results_frequency':1
                }
                push_info={
                    'code':code,
                    'name':name,
                    'anomalies_insurance_type':anomalies_insurance_type,   #险种
                    'anomalies_fail_reason':anomalies_fail_reason,  #增员失败原因
                    'return_dispose':return_dispose,   #需如何处理
                    'content':'工号：{}\n姓名：{}\n险种：{}\n增员失败原因：{}\n需如何处理：{}<a href=\"http://work.weixin.qq.com\">一刀99999</a>'.format(code,name,anomalies_insurance_type,anomalies_fail_reason,return_dispose)

                }

            SocialSecurityAnomaliesResults.objects.update_or_create(defaults=result_params,results_people_id=result_params['results_people_id'],
                                                                    results_anomalies_id=result_params['results_anomalies_id'],results_frequency=result_params['results_frequency'],results_status=True )
            print(push_info)
            self.Enterprise_WeChat.post_wx_message(access_token,**push_info)



        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "上传成功·!"
        }

    def down_anomalies_info(self):
        dummy_path = os.path.join(BASE_DIR, 'static', 'socialSecurityFile', 'download_file', self.t1, str(self.t2))  # 创建文件夹
        mkdir(dummy_path)
        file_ls = [
            "序号","工号","姓名","身份证号","合同归属","管理归属","一级部门","二级部门", "三级部门", "险种", "月份", "增员失败原因", "需如何处理","增员退回原因","处理结果"
        ]
        print(file_ls)
        path =createExcelPath('社保增员信息.xlsx','socialSecurityFile',str(self.t2),'社保增员信息', 25,'A1:N1', *file_ls)
        print(path)
        info=json.loads(self.request.body)
        downloadAll=info['downloadAll']
        idList=info['idList']
        row_data=[]
        if downloadAll == True:  # 是下载全部   有条件
            row_data = []

            kwargs = {}
            tableList = list(
                SocialSecurityAnomalies.objects.filter(anomalies_status=True).values('id',
                                                                                    'anomalies_people_id',
                                                                                     'anomalies_people__employee_name',
                                                                                     'anomalies_people__employee_code',
                                                                                     'anomalies_people__employee_identity_no',
                                                                                     'anomalies_people__employee_job_rank__job_rank_name',
                                                                                     'anomalies_people__employee_department__department_manage',
                                                                                     'anomalies_people__employee_department__department_first_name',
                                                                                     'anomalies_people__employee_department__department_second_name',
                                                                                     'anomalies_people__employee_department__department_third_name',

                                                                                     'anomalies_fail_reason',  # 失败原因唯一
                                                                                     'anomalies_insurance_type',  # 险种唯一
                                                                                     'anomalies_month',  # 月份唯一
                                                                                     ))

            all_id = [item['id'] for item in tableList]  # 所有记录的id
            results_list = list(SocialSecurityAnomaliesResults.objects.filter(results_anomalies_id__in=all_id,
                                                                              results_status=True).values('id',
                                                                                                          'results_people_id',
                                                                                                          'results_anomalies_id',
                                                                                                          'return_dispose',
                                                                                                          'return_cause',
                                                                                                          'results_process'))

            for index, item in enumerate(tableList):
                item['return_cause'] = ','.join([line['return_cause'] for line in results_list if
                                                 line['results_anomalies_id'] == item['id'] and line[
                                                     'results_people_id'] == item['anomalies_people_id'] and line[
                                                     'return_cause'] is not None])
                item['return_dispose'] = ','.join([line['return_dispose'] for line in results_list if
                                                   line['results_anomalies_id'] == item['id'] and line[
                                                       'results_people_id'] == item['anomalies_people_id'] and line[
                                                       'return_dispose'] is not None])
                item['results_process'] = ','.join([line['results_process'] for line in results_list if
                                                    line['results_anomalies_id'] == item['id'] and line[
                                                        'results_people_id'] == item['anomalies_people_id'] and line[
                                                        'results_process'] is not None])
            tableList = self.sort_list_of_dicts(tableList)
            index = 1
            for line in tableList:
                line_data = []
                for k, v in line.items():
                    if k not in ('id','anomalies_people_id'):
                        line_data.append(v)
                row_data.append(line_data)
                line_data.insert(0, index)
                if len(line_data) == 0:
                    index = index
                index += 1

        else:
            tableList = list(
                SocialSecurityAnomalies.objects.filter(anomalies_status=True,id__in=idList).values('id',
                                                                                     'anomalies_people_id',
                                                                                     'anomalies_people__employee_name',
                                                                                     'anomalies_people__employee_code',
                                                                                     'anomalies_people__employee_identity_no',
                                                                                     'anomalies_people__employee_job_rank__job_rank_name',
                                                                                     'anomalies_people__employee_department__department_manage',
                                                                                     'anomalies_people__employee_department__department_first_name',
                                                                                     'anomalies_people__employee_department__department_second_name',
                                                                                     'anomalies_people__employee_department__department_third_name',
                                                                                     'anomalies_fail_reason',  # 失败原因唯一
                                                                                     'anomalies_insurance_type',  # 险种唯一
                                                                                     'anomalies_month',  # 月份唯一
                                                                                     ))

            all_id = [item['id'] for item in tableList]  # 所有记录的id
            results_list = list(SocialSecurityAnomaliesResults.objects.filter(results_anomalies_id__in=all_id,
                                                                              results_status=True).values('id',
                                                                                                          'results_people_id',
                                                                                                          'results_anomalies_id',
                                                                                                          'return_dispose',
                                                                                                          'return_cause',
                                                                                                          'results_process'))

            for index, item in enumerate(tableList):
                item['return_cause'] = ','.join([line['return_cause'] for line in results_list if
                                                 line['results_anomalies_id'] == item['id'] and line[
                                                     'results_people_id'] == item['anomalies_people_id'] and line[
                                                     'return_cause'] is not None])
                item['return_dispose'] = ','.join([line['return_dispose'] for line in results_list if
                                                   line['results_anomalies_id'] == item['id'] and line[
                                                       'results_people_id'] == item['anomalies_people_id'] and line[
                                                       'return_dispose'] is not None])
                item['results_process'] = ','.join([line['results_process'] for line in results_list if
                                                    line['results_anomalies_id'] == item['id'] and line[
                                                        'results_people_id'] == item['anomalies_people_id'] and line[
                                                        'results_process'] is not None])
            tableList = self.sort_list_of_dicts(tableList)
            index = 1
            for line in tableList:
                line_data = []
                for k, v in line.items():
                    if k not in ('id','anomalies_people_id'):
                        line_data.append(v)
                row_data.append(line_data)
                line_data.insert(0, index)
                if len(line_data) == 0:
                    index = index
                index += 1
        exc = openpyxl.load_workbook(path)  # 打开整个excel文件
        sheet = exc.worksheets[0]  # 打开第0张工作表(也就是第一张)
        for row in row_data:
            sheet.append(row)  # 在工作表中添加一行
        exc.save(path)  # 指定路径,保存文件

        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "下载成功",
            "downloadUrl": path
        }
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "下载成功",
            "downloadUrl": path
        }

    def post_dispose_gather(self):
        code = self.request.POST.get('code', None)
        results_process = self.request.POST.get('results_process', None)  #员工处理结果
        anomalies_insurance_type = self.request.POST.get('anomalies_insurance_type', None)  # 险种
        employee_obj = HrEmployee.objects.filter(employee_code=code, employee_status='1').first()
        file_ls = self.request.FILES.getlist("file", None)  # 凭证
        filtered_files = []
        for file in file_ls:
            if file.content_type != 'text/html':
                filtered_files.append(file)
        if employee_obj:
            anomalies_obj = SocialSecurityAnomalies.objects.filter(anomalies_people_id=employee_obj.id,anomalies_insurance_type=anomalies_insurance_type,anomalies_status=True).first()
            results_obj=SocialSecurityAnomaliesResults.objects.filter(results_people_id=employee_obj.id,results_anomalies_id=anomalies_obj.id,results_status=True).order_by('-results_create').first()
            SocialSecurityAnomaliesResults.objects.filter(id=results_obj.id).update(results_process=results_process)
            dummy_path = os.path.join(BASE_DIR, 'static', 'socialSecurityFile', 'upload_file', self.t1, '员工凭证文件上传')# 创建文件夹
            mkdir(dummy_path)
            for file_obj in filtered_files:
                file_url, file_name, suffix =createPath(file_obj, '员工凭证文件上传', 'socialSecurityFile', str(code)+'_凭证_' + str(self.t2)[:-7])
                saveFile(file_url, file_obj)  # 保存文件
                social_security_files_kwargs = {
                    'file_name': file_name,
                    'file_url': file_url,
                    'file_type': 1,
                    'anomalies_file_id':anomalies_obj.id,
                }
                file_dbobj = SocialSecurityFiles.objects.create(**social_security_files_kwargs)
                self.return_data = {
                    'code': status.HTTP_200_OK,
                    'msg': '提交成功',
                }
        else:
            self.return_data = {
                'code': status.HTTP_401_UNAUTHORIZED,
                'msg': '您不是公司员工,无法提交',
            }

    def post_dispose_overrule(self):
        info=json.loads(self.request.body)
        print(info)
        employee_obj = HrEmployee.objects.filter(employee_code=info['code'], employee_status='1').first()
        anomalies_obj = SocialSecurityAnomalies.objects.filter(id=info['id'], anomalies_status=True).first()
        results_obj=SocialSecurityAnomaliesResults.objects.filter(results_anomalies_id=info['id'],results_status=True,results_people_id=employee_obj.id).order_by('-results_create').first()
        print(results_obj)

        results_params={
            'results_people_id':employee_obj.id,
            'results_anomalies_id':info['id'],
            'return_dispose':info['return_dispose'],  #需如何处理
            'return_cause':info['return_cause'],       #  增员退回原因
            'results_frequency':results_obj.results_frequency+1
        }
        SocialSecurityAnomaliesResults.objects.update_or_create(defaults=results_params,results_people_id=results_params['results_people_id'],
                                                                results_anomalies_id=results_params['results_anomalies_id'],
                                                                results_frequency=results_params['results_frequency']
                                                                )
        push_info = {
            'code': info['code'],
            'content': '工号：{}\n姓名：{}\n险种：{}\n增员退回原因：{}\n需如何处理：{}<a href=\"http://work.weixin.qq.com\">一刀99999</a>'.format(
                info['code'], employee_obj.employee_name, anomalies_obj.anomalies_insurance_type, info['return_cause'], info['return_dispose'])

        }

        # print(push_info)
        access_token=self.Enterprise_WeChat.get_wx_access_token()
        self.Enterprise_WeChat.post_wx_message(access_token, **push_info)

    def timing_employee_reminders(self):
        now=datetime.now()
        seven_days_ago = now -timedelta(days=7)#当前日期的前7天日期
        #当前日期2023-10-23  创建日期 2023-10-10  和 2023-10-22  前7天内的不发即大于等于2023-10-16的不发
        #记录创建日期小于等于当前日期的前7天日期的发送
        employee_code_list=list(SocialSecurityAnomalies.objects.filter(anomalies_status=True,anomalies_approval_status__in=[2,3],anomalies_createTime__lte=seven_days_ago).values_list('anomalies_people__employee_code',flat=True))
        for code in employee_code_list:
            push_info = {
                'code': code,
                'content': '请关注HRSSC发送的信息,及时填写社保增员失败提醒的相关结果,感谢您的回复!'
            }
            access_token = self.Enterprise_WeChat.get_wx_access_token()
            self.Enterprise_WeChat.post_wx_message(access_token, **push_info)
        self.return_data = {
            'code': status.HTTP_200_OK,
            'msg': '发送成功',
        }


    @staticmethod
    def sort_list_of_dicts(list_of_dicts):
        """
        对列表中的字典按照指定的顺序排序。

        Args:
        list_of_dicts (list): 包含多个字典的列表。
        order (list): 指定排序顺序的键的列表。

        Returns:
        list: 排序后的列表中的字典。
        """
        # 对列表中的每个字典按照指定的顺序排序
        # 指定排序顺序
        order = [
            'anomalies_people__employee_name',
            'anomalies_people__employee_code',
            'anomalies_people__employee_identity_no',
            'anomalies_people__employee_job_rank__job_rank_name',
            'anomalies_people__employee_department__department_manage',
            'anomalies_people__employee_department__department_first_name',
            'anomalies_people__employee_department__department_second_name',
            'anomalies_people__employee_department__department_third_name',
            'anomalies_insurance_type',#险种
            'anomalies_month',#月份
            'anomalies_fail_reason',  # 失败原因唯一
            'return_dispose',#需如何处理
            'return_cause',#退回原因
            'results_process',#处理结果
            'id','anomalies_people_id'
        ]

        '''
            "序号","工号","姓名","身份证号","合同归属","管理归属","一级部门","二级部门", "三级部门", "险种", "月份", "增员失败原因", "需如何处理","增员退回原因"
        '''
        sorted_list_of_dicts = [dict(sorted(d.items(), key=lambda x: order.index(x[0]))) for d in list_of_dicts]
        return sorted_list_of_dicts

