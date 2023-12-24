import json, os,arrow,openpyxl
from random import random

from django.db.models import Q,F
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from rest_framework.status import HTTP_200_OK

from IeProposal.models import *
# from employee.models import *
from rest_framework.response import Response
from datetime import datetime, date
import requests

# from employee.models import HrEmployee
from pdss.settings import BASE_DIR
import base64
from utils.sqlServerConnect import EhrConnect,OAConnect

class ResetProposal:
    def __init__(self, request,meth):
        self.request = request
        self.now=arrow.now().format('YYYY-MM-DD')
        self.return_data = {
            'code': 200,
            'msg': '信息返回成功'
        }
        self.meth = meth
        self.methods = {
            'phone_post_proposal': self.phone_post_proposal,  #手机端上传
            'download_file':self.download_file,#保存文件
            'get_proposal':self.get_proposal,#电脑端查看
            'proposal_options':self.proposal_options,
            'get_confirm_proposal':self.get_confirm_proposal,  #已确认和未确认
            'get_detailed_proposal':self.get_detailed_proposal,   #第二级
            # 'select_oa':self.select_oa,
            'down_proposal':self.down_proposal,#下载
        }

    def method_center(self):
        if self.meth in ['phone_post_proposal','phone_get_proposal','proposal_options','get_confirm_proposal','get_detailed_proposal','download_file']:
            pass
        else:
            if self.request.check_token is None:
                self.return_data = {'code': status.HTTP_403_FORBIDDEN, "msg": '没有权限访问!'}
                return JsonResponse(self.return_data)
        self.methods[self.meth]()
        return JsonResponse(self.return_data)

    # def phone_post_proposal(self):
    #     code = self.request.POST.get('code', None)
    #     ie_proposal_type_id=self.request.POST.get('ie_proposal_type_id', None)  #id
    #     ie_proposal_type_obj = IeProposalType.objects.filter(id=ie_proposal_type_id, ie_proposal_type_status=1).first()
    #     ie_proposal_type_name=ie_proposal_type_obj.ie_proposal_type_name
    #
    #     # ie_proposal_type_name= self.request.POST.get('ie_proposal_type_id', None)#文本
    #     # ie_proposal_type_obj = IeProposalType.objects.filter(ie_proposal_type_name=ie_proposal_type_name, ie_proposal_type_status=1).first()
    #     # ie_proposal_type_id=ie_proposal_type_obj.id
    #
    #     ie_proposal_feedback_on_workshop_issues=self.request.POST.get('ie_proposal_feedback_on_workshop_issues', None)
    #     ie_proposal_sane_proposal=self.request.POST.get('ie_proposal_sane_proposal', None)
    #     file_ls = self.request.FILES.getlist("file", None)
    #     filtered_files=[]
    #     for file in file_ls:
    #         if file.content_type != 'text/html':
    #             filtered_files.append(file)
    #     employee_obj_list=HrEmployee.objects.filter(employee_code=code,employee_status=1).values('id','employee_name','employee_job_duty__job_duty_name').first()
    #     file_s=""
    #     if employee_obj_list:
    #         proposal_info={
    #             'ie_proposal_employee_id':employee_obj_list['id'],
    #             'ie_proposal_type_id':ie_proposal_type_id,
    #             'ie_proposal_feedback_on_workshop_issues':ie_proposal_feedback_on_workshop_issues,
    #             'ie_proposal_sane_proposal':ie_proposal_sane_proposal
    #         }
    #         proposal_obj=IeProposalRecord.objects.create(**proposal_info)
    #         now = arrow.now().format('YYYY-MM-DD')
    #         if filtered_files:
    #
    #             dummy_path = os.path.join(BASE_DIR, 'static', 'IeProposalFile', 'upload_file', now,employee_obj_list['employee_name'])  # 创建文件夹
    #             self.mkdir(dummy_path)
    #             for file_obj in filtered_files:
    #                 file_url, file_name, suffix = self.createPath(file_obj,employee_obj_list['employee_name'],  str(employee_obj_list['employee_name'])+str(random())[-5:]+'_问题照片','IeProposalFile')
    #                 self.saveFile(file_url, file_obj)  # 保存文件
    #
    #                 with open(file_url, 'rb') as file_object:
    #                     # 读取文件内容
    #                     file_contents = file_object.read()
    #                 # 将文件内容编码为Base64字符串
    #                 base64_encoded = base64.b64encode(file_contents).decode('utf-8')
    #                 file_s+='<attachmentForms><fdKey>fd_3c2d1e41dc1784</fdKey><fdFileName>{}</fdFileName><fdAttachment>{}</fdAttachment></attachmentForms>'.format(file_name,base64_encoded)
    #
    #
    #                 proposal_employee_kwargs = {
    #                     'ie_proposal_file_name': file_name,
    #                     'ie_proposal_file_url': file_url,
    #                     'ie_proposal_type': 1,
    #                     'ie_proposal_employee_id':proposal_obj.id
    #                 }
    #                 file_dbobj = IeProposalFile.objects.create(**proposal_employee_kwargs)
    #
    #             title=str(employee_obj_list['employee_name'])+'_'+str(now)+'_'+'提案申请流程'
    #             url = "http://ekp.runergy.cn:28080/sys/webservice/kmReviewWebserviceService?wsdl"
    #             headers = {'Content-Type': 'application/xml'}
    #             payload = """
    #                                                     <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservice.review.km.kmss.landray.com/">
    #                                                         <soapenv:Header/>
    #                                                         <soapenv:Body>
    #                                                             <web:addReview>
    #                                                                 <!--Optional:-->
    #                                                                 <arg0>
    #                                                                     <!--Zero or more repetitions:-->
    #                                                                     <!--Optional:-->
    #                                                                     <attachmentValues></attachmentValues>
    #                                                                     <!--Optional:-->
    #                                                                     <authAreaId></authAreaId>
    #                                                                     <!--Optional:-->
    #                                                                     <docContent></docContent>
    #                                                                     <!--Optional:-->
    #                                                                     <docCreator>{"LoginName":"%s"}</docCreator>
    #                                                                     <!--Optional:-->
    #                                                                     <docProperty></docProperty>
    #                                                                     <!--Optional:-->
    #                                                                     <docStatus>10</docStatus>
    #                                                                     <!--Optional:-->
    #                                                                     <docSubject>%s</docSubject>
    #                                                                     <!--Optional:-->
    #                                                                     <fdId></fdId>
    #                                                                     <!--Optional:-->
    #                                                                     <fdKeyword></fdKeyword>
    #                                                                     <!--Optional:-->
    #                                                                     <fdSource></fdSource>
    #                                                                     <!--Optional:-->
    #                                                                     <fdTemplateId>18a4a207e56f3ad44de69a64fd2ba0db</fdTemplateId>
    #                                                                     <!--Optional:--><flowParam>{}</flowParam>
    #                                                                     <!--Optional:-->
    #                                                                     <formValues>
    #                                                                     {
    #                                                                         "fd_3b850713360d54":"%s",
    #                                                                         "fd_3c2d1db9377260":"%s",
    #                                                                         "fd_3c2d1e0306c51c":"%s",
    #                                                                         "fd_3c3018fd3012b2":"%s",
    #                                                                         "fd_38ee4f140210f6":"%s",
    #                                                                     }
    #                                                                     </formValues>
    #                                                                     %s
    #                                                                 </arg0>
    #                                                             </web:addReview>
    #                                                         </soapenv:Body>
    #                                                     </soapenv:Envelope>
    #                                                                             """ % (code,
    #                                                                                    title,title,
    #                                                                                    ie_proposal_type_name,
    #                                                                                    ie_proposal_feedback_on_workshop_issues,
    #                                                                                    ie_proposal_sane_proposal,
    #                                                                                    employee_obj_list['employee_job_duty__job_duty_name'],
    #                                                                                    file_s)
    #
    #             response = requests.post(url, headers=headers, data=payload.replace("'", '"').encode('utf-8'))
    #             # print(response.text,type(response.text))
    #             ie_process_id=response.text.split('<return>')[1].split('</return>')[0]
    #             # print(proposal_obj.id)
    #             proposal_obj = IeProposalRecord.objects.filter(pk=proposal_obj.id).update(ie_process_id=ie_process_id)
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
    #         self.return_data = {
    #             'code': 200,
    #             'msg': '提案提交成功',
    #         }
    #     else:
    #         self.return_data = {
    #             'code': 401,
    #             'msg': '您不是公司员工,无法提交',
    #         }
    def phone_post_proposal(self):
        code = self.request.POST.get('code', None)
        ie_workshop_section = self.request.POST.get('ie_workshop_section', None)
        ie_proposal_type_id=self.request.POST.get('ie_proposal_type_id', None)  #id    #类型id
        ie_proposal_type_obj = IeProposalType.objects.filter(id=ie_proposal_type_id, ie_proposal_type_status=1).first()
        ie_proposal_type_name=ie_proposal_type_obj.ie_proposal_type_name    #类型文本
        ie_proposal_feedback_on_workshop_issues=self.request.POST.get('ie_proposal_feedback_on_workshop_issues', None)
        ie_proposal_sane_proposal=self.request.POST.get('ie_proposal_sane_proposal', None)
        file_ls = self.request.FILES.getlist("file", None)
        filtered_files=[]
        for file in file_ls:
            if file.content_type != 'text/html':
                filtered_files.append(file)

        ehr_connect = EhrConnect()
        ehr_ie_data = ehr_connect.select("""
            SELECT
            b.id,
                 b.Name as employee_name,
                 j.JobName as employee_job_duty__job_duty_name
             FROM
                 T_HR_Employee AS b 
                 LEFT JOIN T_HR_Department AS d ON b.DeptID = d.id
                 LEFT JOIN  T_HR_Job AS j ON b.JobID=j.id

             WHERE
                  d.IfUse= 1 
                 AND b.code LIKE '{}'
                """.format(code))
        print(ehr_ie_data)
        # employee_obj_list=HrEmployee.objects.filter(employee_code=code,employee_status=1).values('id','employee_name','employee_job_duty__job_duty_name').first()
        employee_obj_list=ehr_ie_data[0]
        file_s=""
        ie_proposal_file_id_all=[]   #所有照片的id
        if employee_obj_list:
            dummy_path = os.path.join(BASE_DIR, 'static', 'IeProposalFile', 'upload_file', self.now,employee_obj_list['employee_name'])  # 创建文件夹
            self.mkdir(dummy_path)
            for file_obj in filtered_files:
                file_url, file_name, suffix = self.createPath(file_obj,employee_obj_list['employee_name'],  str(employee_obj_list['employee_name'])+str(random())[-5:]+'_问题照片','IeProposalFile')
                self.saveFile(file_url, file_obj)  # 保存文件
                proposal_employee_kwargs = {
                    'ie_proposal_file_name': file_name,
                    'ie_proposal_file_url': file_url,
                    'ie_proposal_type': 1,
                    # 'ie_proposal_employee_id':proposal_obj.id
                }
                file_dbobj = IeProposalFile.objects.create(**proposal_employee_kwargs)
                ie_proposal_file_id_all.append(file_dbobj.id)

                with open(file_url, 'rb') as file_object:
                    # 读取文件内容
                    file_contents = file_object.read()
                # 将文件内容编码为Base64字符串
                base64_encoded = base64.b64encode(file_contents).decode('utf-8')
                file_s+='<attachmentForms><fdKey>fd_3c2d1e41dc1784</fdKey><fdFileName>{}</fdFileName><fdAttachment>{}</fdAttachment></attachmentForms>'.format(file_name,base64_encoded)
            title = str(employee_obj_list['employee_name']) + '_' + str(self.now) + '_' + '提案申请流程'
            url = "http://ekp.runergy.cn:28080/sys/webservice/kmReviewWebserviceService?wsdl"
            headers = {'Content-Type': 'application/xml'}
            payload = """
                                                    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservice.review.km.kmss.landray.com/">
                                                        <soapenv:Header/>
                                                        <soapenv:Body>
                                                            <web:addReview>
                                                                <!--Optional:-->
                                                                <arg0>
                                                                    <!--Zero or more repetitions:-->
                                                                    <!--Optional:-->
                                                                    <attachmentValues></attachmentValues>
                                                                    <!--Optional:-->
                                                                    <authAreaId></authAreaId>
                                                                    <!--Optional:-->
                                                                    <docContent></docContent>
                                                                    <!--Optional:-->
                                                                    <docCreator>{"LoginName":"%s"}</docCreator>
                                                                    <!--Optional:-->
                                                                    <docProperty></docProperty>
                                                                    <!--Optional:-->
                                                                    <docStatus>20</docStatus>
                                                                    <!--Optional:-->
                                                                    <docSubject>%s</docSubject>
                                                                    <!--Optional:-->
                                                                    <fdId></fdId>
                                                                    <!--Optional:-->
                                                                    <fdKeyword></fdKeyword>
                                                                    <!--Optional:-->
                                                                    <fdSource></fdSource>
                                                                    <!--Optional:-->
                                                                    <fdTemplateId>18a4a207e56f3ad44de69a64fd2ba0db</fdTemplateId>
                                                                    <!--Optional:--><flowParam>{}</flowParam>
                                                                    <!--Optional:-->
                                                                    <formValues>
                                                                    {
                                                                        "fd_3c38e7225c6092":"%s",
                                                                        "fd_3b850713360d54":"%s",
                                                                        "fd_3c2d1db9377260":"%s",
                                                                        "fd_3c2d1e0306c51c":"%s",
                                                                        "fd_3c3018fd3012b2":"%s",
                                                                        "fd_38ee4f140210f6":"%s",
                                                                    }
                                                                    </formValues>
                                                                    %s
                                                                </arg0>
                                                            </web:addReview>
                                                        </soapenv:Body>
                                                    </soapenv:Envelope>
                                                                            """ % (code,
                                                                                   title,ie_workshop_section, title,
                                                                                   ie_proposal_type_name,
                                                                                   ie_proposal_feedback_on_workshop_issues,
                                                                                   ie_proposal_sane_proposal,
                                                                                   employee_obj_list['employee_job_duty__job_duty_name'],
                                                                                   file_s)

            response = requests.post(url, headers=headers, data=payload.replace("'", '"').encode('utf-8'))
            # print(response.text,type(response.text))
            ie_process_id = response.text.split('<return>')[1].split('</return>')[0]
            # print(ie_process_id)
            proposal_obj = IeProposalFile.objects.filter(id__in=ie_proposal_file_id_all).update(ie_proposal_employee_id=ie_process_id)
            self.return_data = {
                'code': 200,
                'msg': '提案提交成功',
            }
        else:
            self.return_data = {
                'code': 401,
                'msg': '您不是公司员工,无法提交',
            }

    def download_file(self):
        oa_connect = OAConnect()
        oa_ie_file_Data= oa_connect.select("""
              SELECT
                c.fd_id as ie_fd_id,
                a.fd_id as f_fd_id,
                        a.fd_key,
                        a.fd_file_name,
                        a.doc_Create_Time ,
                        d.fd_38ee4f12ab860a as code
                FROM
                        sys_att_main AS a
                        INNER JOIN sys_att_file AS b ON a.fd_file_id = b.fd_id
                        INNER JOIN km_review_main AS c ON a.fd_model_id = c.fd_id
                        INNER JOIN ekp_18a644a0e38b4aaa8979 AS d ON d.fd_id = c.fd_id
                where  a.fd_key='fd_3c2d1ed162e6a2'  --完成照片'
                AND a.doc_Create_Time BETWEEN DATEADD(hour,-2, GETDATE()) AND GETDATE()   --前2小时的数据 
               """)

        # all_ie_id = [item['ie_fd_id'] for item in oa_ie_file_Data]

        for file in oa_ie_file_Data:
            file_fd_id=file['f_fd_id']   #流程中文件的id
            file_fd_file_name = file['fd_file_name']   #流程文件的名字
            code=file['code']   #工号
            proposal_id=file['ie_fd_id']    #流程的id
            file_file_path = os.path.join(BASE_DIR, 'static', 'IeProposalFile', 'oa_ie_file', self.now, code)
            self.mkdir(file_file_path)
            import time
            time=int(time.time() * 1000)
            session_url='http://ekp.runergy.cn:28080/api/sys-authentication/loginService/getLoginSessionId?loginName={}'.format(code)
            session_response = requests.post(session_url)
            session_r_text=json.loads(session_response.text)

            sessionId=session_r_text['sessionId']
            cookie_url='http://ekp.runergy.cn:28080/sys/authentication/sso/login_auto.jsp?sessionId={}'.format(sessionId)
            cookie_response = requests.get(cookie_url)
            cookie_r_text=cookie_response.text
            cookie=cookie_r_text.split("cookie = '")[1].split(';domainekp')[0]
            header={
                'Cookie':cookie
            }
            down_url="http://ekp.runergy.cn:28080/sys/attachment/sys_att_main/sysAttMain.do?method=download&fdId={}&downloadType=manual&downloadFlag={}".format(file_fd_id,time)
            file_response = requests.get(down_url,headers=header)
            file_path = os.path.join('static', 'IeProposalFile', 'oa_ie_file', self.now, code,file_fd_file_name)  # 文件路径
            file_path = file_path.replace('\\', '/')

            with open(file_path, "wb") as f:
                f.write(file_response.content)

            proposal_employee_kwargs = {
                'ie_proposal_file_name': file_fd_file_name,
                'ie_proposal_file_url': file_path,
                'ie_proposal_type':2,
                'ie_proposal_employee_id': proposal_id
            }

            file_dbobj = IeProposalFile.objects.update_or_create(defaults=proposal_employee_kwargs,ie_proposal_type=2,ie_proposal_employee_id=proposal_employee_kwargs['ie_proposal_employee_id'],ie_proposal_file_name=proposal_employee_kwargs['ie_proposal_file_name'],ie_proposal_file_url=proposal_employee_kwargs['ie_proposal_file_url'])




    def get_proposal(self):
        column_list = [
            {'label': 'index', 'value': '序号', 'width': 60},
            {'label': 'ie_proposal_employee__employee_name', 'value': '姓名', 'width': 100},
            {'label': 'ie_proposal_employee__employee_code', 'value': '工号', 'width': 100},
            {'label': 'bumen', 'value': '申请部门', 'width': 200},
            {'label': 'gongduan', 'value': '工段', 'width': 100},
            {'label': 'ie_proposal_type__ie_proposal_type_name', 'value': '提案类型', 'width': 100},
            {'label': 'ie_proposal_feedback_on_workshop_issues', 'value': '车间异常问题反馈', 'width': 300},
            {'label': 'file1_num', 'value': '问题照片', 'width': 100},
            {'label': 'ie_proposal_sane_proposal', 'value': '合理化建议', 'width':300 },
            {'label': 'ie_proposal_create_time', 'value': '提案时间', 'width': 150},
            {'label': 'ie_proposal_superior_examine_time', 'value': '直接上级审批时间', 'width': 150},
            {'label': 'ie_proposal_ie_examine_time', 'value': 'IE审批时间', 'width': 150},
            {'label': 'ie_proposal_ie_superior_examine_time', 'value': 'IE主管审批时间', 'width': 150},
            {'label': 'ie_proposal_effect_department', 'value': '实施部门', 'width': 200},
            {'label': 'ie_proposal_effect_head', 'value': '实施负责人', 'width': 100},
            {'label': 'ie_proposal_effect_superior_examine_time', 'value': '实施单位主管审批时间', 'width': 150},
            # {'label': 'ie_proposal_expected_start_time', 'value': '预计开始时间', 'width': 150},
            # {'label': 'ie_proposal_expected_end_time', 'value': '预计结束时间', 'width': 150},
            {'label': 'ie_proposal_ie_confirm_examine_time', 'value': 'IE效果确认审核时间', 'width': 150},
            {'label': 'ie_proposal_reality_start_time', 'value': '实际开始时间', 'width': 150},
            {'label': 'ie_proposal_reality_end_time', 'value': '实际结束时间', 'width':150},
            {'label': 'fd_shiShiKeXingXingPingGu', 'value': '实施可行性评估', 'width': 150},
            {'label': 'file2_num', 'value': '实施完成照片', 'width':110},
            {'label': 'ie_proposal_accept', 'value': '是否验收', 'width': 110},
            {'label': 'ie_proposal_remark', 'value': '备注', 'width': ''}
        ]
        currentPage = eval(self.request.GET.get("currentPage", None)) if self.request.GET.get("currentPage",None) != "" else 1
        pageSize = eval(self.request.GET.get("pageSize", None)) if self.request.GET.get("pageSize", None) != "" else 25
        searchName = self.request.GET.get('searchName', None)
        # print(searchName)
        kwargs = {}
        ie_proposal_type_name_tuple=()   #提案类型  (查询条件)
        if "ie_proposal_type_id[]" in self.request.GET:
            ie_proposal_type = self.request.GET.getlist('ie_proposal_type_id[]', None)
            ie_proposal_type_obj = tuple(IeProposalType.objects.filter(id__in=ie_proposal_type,ie_proposal_type_status=1).values_list('ie_proposal_type_name',flat=True))
            ie_proposal_type_name_tuple=ie_proposal_type_obj

        is_confirm=self.request.GET.get("is_confirm", None)
        if is_confirm=='1':
            is_confirm=30    #已确认
        elif is_confirm=='0':
            is_confirm=20    #未确认
        else:
            pass
        begin_date_create_time = self.request.GET.get('begin_date_create_time', None)
        end_date_create_time = self.request.GET.get('end_date_create_time', None)
        begin_date_ie_confirm_examine_time = self.request.GET.get('begin_date_ie_confirm_examine_time', None)
        end_date_ie_confirm_examine_time = self.request.GET.get('end_date_ie_confirm_examine_time', None)

        if len(ie_proposal_type_name_tuple)==1:
            ie_proposal_type_name_tuple="('"+str(ie_proposal_type_name_tuple[0])+"')"
        oa_connect = OAConnect()
        select_sql="""
            SELECT
            a.fd_process_id,
            a.fd_fact_node_name,
            a.fd_create_time,
            b.doc_status,
            f.fd_name AS 'name',
            c.fd_38ee4f12ab860a as 'gonghao',
            c.fd_3c2d1db9377260 as 'tianleixing',
            c.fd_3c2d1e0306c51c as 'wentifankui',
            c.fd_heLiHuaJianYi as 'helihuajianyi',
            d.fd_name as 'shishibumen',
            e.fd_name as 'shishifuzeren',
            c.fd_shiShiKeXingXingPingGu as 'shishikexingxingpinggu',
            c.fd_yuanYinShuoMing as 'yuanyinshuoming',
            c.fd_3c2d1eaf80eaac as 'shishikaishishijian',
            c.fd_3c2d1ebdbbeb86 as 'shishijieshushijian',
            c.fd_yanShou as 'yanshou',
            c.fd_3c2d1f1b610ff8 as 'beizhu',
            c.fd_gongDuan as 'gongduan',
            c.fd_38ee4f117f56c8 as 'bumen'
            FROM
              lbpm_audit_note AS a
              LEFT JOIN lbpm_process AS b ON a.fd_process_id = b.fd_id
              LEFT JOIN ekp_18a644a0e38b4aaa8979 as c on b.fd_id = c.fd_id
              LEFT JOIN sys_org_element as d on c.fd_3c2d1e6c6c197c = d.fd_id
              LEFT JOIN sys_org_element as e on c.fd_3c2d1e7ce45706 = e.fd_id
              INNER JOIN sys_org_element AS f ON c.fd_38ee4f15e85c90 = f.fd_id
            where a.fd_create_time>'2021-09-27' AND (c.fd_38ee4f12ab860a= '{}' or f.fd_name='{}')  AND c.fd_3c2d1db9377260 IN {} AND b.doc_status ={}
                     """.format(searchName,searchName,ie_proposal_type_name_tuple,is_confirm)
        # print(select_sql)
        if len(ie_proposal_type_name_tuple)==0:
            select_sql = select_sql.replace("AND c.fd_3c2d1db9377260 IN ()", "")
        if searchName is None or len(searchName)==0:
            select_sql = select_sql.replace("AND (c.fd_38ee4f12ab860a= '' or f.fd_name='')", "")
        if is_confirm is None or is_confirm not in (20,30):
            select_sql = select_sql.replace("AND b.doc_status =", "")
        # print(select_sql)

        oa_ie_data = oa_connect.select(select_sql)

        sorted_oa_ie_data = sorted(oa_ie_data, key=lambda x: (-x['fd_create_time'].timestamp(), x['fd_process_id'], self.custom_sort(x)),reverse=True)

        ie_proposal_record = {}

        # ehr_connect = EhrConnect()

        for line in sorted_oa_ie_data:
            # ehr_ie_data = ehr_connect.select("""
            #     SELECT
            #          b.Name as employee_name
            #      FROM
            #          T_HR_Employee AS b
            #      WHERE
            #           b.code = '{}'
            #         """.format(line['gonghao']))

            fd_process_id = line['fd_process_id']
            ie_proposal_record[fd_process_id] = {
                'id':fd_process_id,
                'ie_proposal_employee__employee_code': line['gonghao'],
                # 'ie_proposal_employee__employee_name':HrEmployee.objects.filter(employee_code=line['gonghao'],employee_status=1).values('employee_name').first()['employee_name'],
                # 'ie_proposal_employee__employee_name': ehr_ie_data[0]['employee_name'],
                'ie_proposal_employee__employee_name':line['name'],
                'bumen': line['bumen'],
                'gongduan': line['gongduan'],
                'ie_proposal_type__ie_proposal_type_name': line['tianleixing'],  # 提案类型
                'ie_proposal_feedback_on_workshop_issues': line['wentifankui'],  # 问题反馈
                'ie_proposal_sane_proposal': line['helihuajianyi'],  # 合理化建议
                'ie_proposal_effect_department': line['shishibumen'],  # 实施部门
                'ie_proposal_effect_head': line['shishifuzeren'],  # 实施负责人
                'fd_shiShiKeXingXingPingGu': line['shishikexingxingpinggu'],  # 实施可行性评估
                'ie_proposal_reason': line['yuanyinshuoming'],  # 原因说明
                'ie_proposal_reality_start_time': line['shishikaishishijian'],  # 实施开始时间
                'ie_proposal_reality_end_time': line['shishijieshushijian'],  # 实施结束时间
                'ie_proposal_accept': line['yanshou'],  # 是否验收
                'ie_proposal_remark': line['beizhu'],  # 备注
            }

        for line in sorted_oa_ie_data:
            fd_process_id = line['fd_process_id']
            if line['fd_fact_node_name']=='起草节点':
                ie_proposal_record[fd_process_id]['ie_proposal_create_time']=line['fd_create_time']
            else:
                ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] =None

            if line['fd_fact_node_name']=='直接上级审批':
                ie_proposal_record[fd_process_id]['ie_proposal_superior_examine_time'] = line['fd_create_time']
            else:
                ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] =None
            if line['fd_fact_node_name']=='IE审批':
                ie_proposal_record[fd_process_id]['ie_proposal_ie_examine_time'] = line['fd_create_time']
            else:
                ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] =None
            if line['fd_fact_node_name']=='IE主管':
                ie_proposal_record[fd_process_id]['ie_proposal_ie_superior_examine_time'] = line['fd_create_time']
            else:
                ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] =None
            if line['fd_fact_node_name']=='实施单位主管':
                ie_proposal_record[fd_process_id]['ie_proposal_effect_superior_examine_time'] = line['fd_create_time']
            else:
                ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] =None
            if line['fd_fact_node_name']=='效果确认':
                ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] = line['fd_create_time']
            else:
                ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] =None

        table_list = list(ie_proposal_record.values())
        if begin_date_create_time != "" and end_date_create_time != "":
            if type(begin_date_create_time)==str:
                begin_date_create_time = datetime.strptime(begin_date_create_time, "%Y-%m-%d")
            if type(end_date_create_time)==str:
                end_date_create_time = datetime.strptime(end_date_create_time, "%Y-%m-%d")
            table_list = [item for item in table_list if begin_date_create_time <= item['ie_proposal_create_time'] <= end_date_create_time]
        if begin_date_ie_confirm_examine_time != "" and end_date_ie_confirm_examine_time != "":
            if type(begin_date_ie_confirm_examine_time) == str:
                begin_date_ie_confirm_examine_time = datetime.strptime(begin_date_ie_confirm_examine_time, "%Y-%m-%d")
            if type(end_date_ie_confirm_examine_time) == str:
                end_date_ie_confirm_examine_time = datetime.strptime(end_date_ie_confirm_examine_time, "%Y-%m-%d")
            table_list = [item for item in table_list if 'ie_proposal_ie_confirm_examine_time' in item and
                             begin_date_ie_confirm_examine_time <= item['ie_proposal_ie_confirm_examine_time'] <= end_date_ie_confirm_examine_time ]


        total_number=len(table_list)
        try:
            table_list = sorted(table_list, key=lambda x: x.get('ie_proposal_create_time'), reverse=True)
        except:
            pass
        table_list=table_list[(currentPage - 1) * pageSize:currentPage * pageSize]

        all_id = [item['id'] for item in table_list]
        # print('all_id',all_id)
        file_list = list(IeProposalFile.objects.filter(ie_proposal_employee_id__in=all_id).values('id','ie_proposal_type',
                                                                                                                   'ie_proposal_file_name',
                                                                                                                   'ie_proposal_file_url',
                                                                                                                   'ie_proposal_employee_id'))
        file_dict1 = {}#问题照片
        file_dict2 = {} #实施完成照片
        for item in file_list:  #查找每份提案对应的文件
            ie_proposal_employee_id = item.get('ie_proposal_employee_id')
            if item['ie_proposal_type']=='1':   #问题照片
                if ie_proposal_employee_id not in file_dict1:
                    file_dict1[ie_proposal_employee_id] = []
                file_dict1[ie_proposal_employee_id].append(item)
            elif item['ie_proposal_type']=='2':#实施完成照片
                if ie_proposal_employee_id not in file_dict2:
                    file_dict2[ie_proposal_employee_id] = []
                file_dict2[ie_proposal_employee_id].append(item)
        for index, item in enumerate(table_list):
            # item['index'] = (currentPage - 1) * pageSize + index + 1
            try:
                item['ie_proposal_create_time'] = item['ie_proposal_create_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_create_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_superior_examine_time'] = item['ie_proposal_superior_examine_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_superior_examine_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_ie_examine_time'] = item['ie_proposal_ie_examine_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_ie_examine_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_ie_superior_examine_time'] = item['ie_proposal_ie_superior_examine_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_ie_superior_examine_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_effect_superior_examine_time'] = item['ie_proposal_effect_superior_examine_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_effect_superior_examine_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_ie_confirm_examine_time'] = item['ie_proposal_ie_confirm_examine_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_ie_confirm_examine_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_reality_start_time'] = item['ie_proposal_reality_start_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_reality_start_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_reality_end_time'] = item['ie_proposal_reality_end_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_reality_end_time'] is not None else None
            except:
                pass

            ie_proposal_id = item.get('id')
            if ie_proposal_id in file_dict1:
                item['file1_ls'] = file_dict1[ie_proposal_id]
                item['file1_num'] = len(file_dict1[ie_proposal_id])
            else:
                item['file1_ls'] = []
                item['file1_num'] = 0
            if ie_proposal_id in file_dict2:
                item['file2_ls'] = file_dict2[ie_proposal_id]
                item['file2_num'] = len(file_dict2[ie_proposal_id])
            else:
                item['file2_ls'] = []
                item['file2_num'] = 0



        # print(len(table_list))
        # try:
        #     table_list = sorted(table_list, key=lambda x: x.get('ie_proposal_create_time'), reverse=True)
        # except:
        #     pass
        for index, item in enumerate(table_list):
            item['index'] = (currentPage - 1) * pageSize + index + 1
        print(table_list)
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "信息返回成功",
            "data": {
                'columnList': column_list,
                'tableList': table_list,
                'totalNumber': total_number,

            },
        }

    def down_proposal(self):
        now = arrow.now()
        t1 = now.format('YYYY-MM-DD')
        t2 = now.timestamp()
        dummy_path = os.path.join(BASE_DIR, 'static', 'IeProposalFile', 'download_file', t1, str(t2))  # 创建文件夹
        self.mkdir(dummy_path)

        template_path = os.path.join(BASE_DIR, 'static', 'IeProposalFile', 'template_file','IE提案模板.xlsx')  # 创建文件夹
        import shutil
        # 指定原始文件路径和目标路径
        source_path = template_path  # 例如：C:\\原始文件夹\\文件名.xlsx
        destination_path = os.path.join(BASE_DIR, 'static', 'IeProposalFile', 'download_file', t1, str(t2),'IE提案.xlsx')  # 例如：D:\\目标文件夹\\文件名.xlsx
        # 使用shutil库进行复制操作
        shutil.copy(source_path, destination_path)
        id_list = json.loads(self.request.body).get('idList')
        download_all = json.loads(self.request.body).get('downloadAll')
        print(id_list,download_all)
        self.get_proposal()
        table_list = self.sort_list_of_dicts(self.return_data['data']['tableList'])
        # print(table_list)
        # print(len(table_list))
        row_data = []
        if download_all == True:  # 是下载全部   有条件

            searchName = self.request.GET.get('searchName', None)
            kwargs = {}
            ie_proposal_type_name_tuple = ()  # 提案类型  (查询条件)
            if "ie_proposal_type_id[]" in self.request.GET:
                ie_proposal_type = self.request.GET.getlist('ie_proposal_type_id[]', None)
                ie_proposal_type_obj = tuple(
                    IeProposalType.objects.filter(id__in=ie_proposal_type, ie_proposal_type_status=1).values_list(
                        'ie_proposal_type_name', flat=True))
                ie_proposal_type_name_tuple = ie_proposal_type_obj

            is_confirm = self.request.GET.get("is_confirm", None)
            if is_confirm == '1':
                is_confirm = 30  # 已确认
            elif is_confirm == '0':
                is_confirm = 20  # 未确认
            else:
                pass
            begin_date_create_time = self.request.GET.get('begin_date_create_time', None)
            end_date_create_time = self.request.GET.get('end_date_create_time', None)
            begin_date_ie_confirm_examine_time = self.request.GET.get('begin_date_ie_confirm_examine_time', None)
            end_date_ie_confirm_examine_time = self.request.GET.get('end_date_ie_confirm_examine_time', None)

            if len(ie_proposal_type_name_tuple) == 1:
                ie_proposal_type_name_tuple = "('" + str(ie_proposal_type_name_tuple[0]) + "')"
            oa_connect = OAConnect()
            select_sql = """
                       SELECT
                       a.fd_process_id,
                       a.fd_fact_node_name,
                       a.fd_create_time,
                       b.doc_status,
                       f.fd_name AS 'name',
                       c.fd_38ee4f12ab860a as 'gonghao',
                       c.fd_3c2d1db9377260 as 'tianleixing',
                       c.fd_3c2d1e0306c51c as 'wentifankui',
                       c.fd_heLiHuaJianYi as 'helihuajianyi',
                       d.fd_name as 'shishibumen',
                       e.fd_name as 'shishifuzeren',
                       c.fd_shiShiKeXingXingPingGu as 'shishikexingxingpinggu',
                       c.fd_yuanYinShuoMing as 'yuanyinshuoming',
                       c.fd_3c2d1eaf80eaac as 'shishikaishishijian',
                       c.fd_3c2d1ebdbbeb86 as 'shishijieshushijian',
                       c.fd_yanShou as 'yanshou',
                       c.fd_3c2d1f1b610ff8 as 'beizhu',
                       c.fd_gongDuan as 'gongduan',
                       c.fd_38ee4f117f56c8 as 'bumen'
                       FROM
                         lbpm_audit_note AS a
                         LEFT JOIN lbpm_process AS b ON a.fd_process_id = b.fd_id
                         LEFT JOIN ekp_18a644a0e38b4aaa8979 as c on b.fd_id = c.fd_id
                         LEFT JOIN sys_org_element as d on c.fd_3c2d1e6c6c197c = d.fd_id
                         LEFT JOIN sys_org_element as e on c.fd_3c2d1e7ce45706 = e.fd_id
                         INNER JOIN sys_org_element AS f ON c.fd_38ee4f15e85c90 = f.fd_id
                       where a.fd_create_time>'2021-09-27' AND (c.fd_38ee4f12ab860a= '{}' or f.fd_name='{}')  AND c.fd_3c2d1db9377260 IN {} AND b.doc_status ={}
                                """.format(searchName, searchName, ie_proposal_type_name_tuple, is_confirm)
            # print(select_sql)
            if len(ie_proposal_type_name_tuple) == 0:
                select_sql = select_sql.replace("AND c.fd_3c2d1db9377260 IN ()", "")
            if searchName is None or len(searchName) == 0:
                select_sql = select_sql.replace("AND (c.fd_38ee4f12ab860a= '' or f.fd_name='')", "")
            if is_confirm is None or is_confirm not in (20, 30):
                select_sql = select_sql.replace("AND b.doc_status =", "")
            # print(select_sql)

            oa_ie_data = oa_connect.select(select_sql)

            sorted_oa_ie_data = sorted(oa_ie_data, key=lambda x: (
            -x['fd_create_time'].timestamp(), x['fd_process_id'], self.custom_sort(x)), reverse=True)

            ie_proposal_record = {}

            # ehr_connect = EhrConnect()

            for line in sorted_oa_ie_data:
                fd_process_id = line['fd_process_id']
                ie_proposal_record[fd_process_id] = {
                    'id': fd_process_id,
                    'ie_proposal_employee__employee_code': line['gonghao'],
                    'ie_proposal_employee__employee_name': line['name'],
                    'bumen': line['bumen'],
                    'gongduan': line['gongduan'],
                    'ie_proposal_type__ie_proposal_type_name': line['tianleixing'],  # 提案类型
                    'ie_proposal_feedback_on_workshop_issues': line['wentifankui'],  # 问题反馈
                    'ie_proposal_sane_proposal': line['helihuajianyi'],  # 合理化建议
                    'ie_proposal_effect_department': line['shishibumen'],  # 实施部门
                    'ie_proposal_effect_head': line['shishifuzeren'],  # 实施负责人
                    'fd_shiShiKeXingXingPingGu': line['shishikexingxingpinggu'],  # 实施可行性评估
                    'ie_proposal_reason': line['yuanyinshuoming'],  # 原因说明
                    'ie_proposal_reality_start_time': line['shishikaishishijian'],  # 实施开始时间
                    'ie_proposal_reality_end_time': line['shishijieshushijian'],  # 实施结束时间
                    'ie_proposal_accept': line['yanshou'],  # 是否验收
                    'ie_proposal_remark': line['beizhu'],  # 备注
                }

            for line in sorted_oa_ie_data:
                fd_process_id = line['fd_process_id']
                if line['fd_fact_node_name'] == '起草节点':
                    ie_proposal_record[fd_process_id]['ie_proposal_create_time'] = line['fd_create_time']
                else:
                    ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] = None

                if line['fd_fact_node_name'] == '直接上级审批':
                    ie_proposal_record[fd_process_id]['ie_proposal_superior_examine_time'] = line['fd_create_time']
                else:
                    ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] = None
                if line['fd_fact_node_name'] == 'IE审批':
                    ie_proposal_record[fd_process_id]['ie_proposal_ie_examine_time'] = line['fd_create_time']
                else:
                    ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] = None
                if line['fd_fact_node_name'] == 'IE主管':
                    ie_proposal_record[fd_process_id]['ie_proposal_ie_superior_examine_time'] = line['fd_create_time']
                else:
                    ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] = None
                if line['fd_fact_node_name'] == '实施单位主管':
                    ie_proposal_record[fd_process_id]['ie_proposal_effect_superior_examine_time'] = line[
                        'fd_create_time']
                else:
                    ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] = None
                if line['fd_fact_node_name'] == '效果确认':
                    ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] = line['fd_create_time']
                else:
                    ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] = None



            table_list = list(ie_proposal_record.values())
            if begin_date_create_time != "" and end_date_create_time != "":
                if type(begin_date_create_time) == str:
                    begin_date_create_time = datetime.strptime(begin_date_create_time, "%Y-%m-%d")
                if type(end_date_create_time) == str:
                    end_date_create_time = datetime.strptime(end_date_create_time, "%Y-%m-%d")
                table_list = [item for item in table_list if
                              begin_date_create_time <= item['ie_proposal_create_time'] <= end_date_create_time]
            if begin_date_ie_confirm_examine_time != "" and end_date_ie_confirm_examine_time != "":
                if type(begin_date_ie_confirm_examine_time) == str:
                    begin_date_ie_confirm_examine_time = datetime.strptime(begin_date_ie_confirm_examine_time,
                                                                           "%Y-%m-%d")
                if type(end_date_ie_confirm_examine_time) == str:
                    end_date_ie_confirm_examine_time = datetime.strptime(end_date_ie_confirm_examine_time, "%Y-%m-%d")
                table_list = [item for item in table_list if 'ie_proposal_ie_confirm_examine_time' in item and
                              begin_date_ie_confirm_examine_time <= item[
                                  'ie_proposal_ie_confirm_examine_time'] <= end_date_ie_confirm_examine_time]

            total_number = len(table_list)
            try:
                table_list = sorted(table_list, key=lambda x: x.get('ie_proposal_create_time'), reverse=True)
            except:
                pass

            # print(table_list)

            table_list = self.sort_list_of_dicts(table_list)



            index = 1
            for line in table_list:
                line_data = []
                for k, v in line.items():
                    if k not in ('ie_proposal_reason','id','file1_ls','file1_num','file2_ls','file2_num','index'):
                        line_data.append(v)
                line_data.insert(0,index)
                index += 1
                row_data.append(line_data)

        else:
            index = 1
            for line in table_list:
                if line['id'] in id_list:
                    print('line',line)
                    line_data = []
                    for k, v in line.items():
                        if k not in ('ie_proposal_reason','id','file1_ls','file1_num','file2_ls','file2_num','index'):
                            line_data.append(v)
                    print(line_data)
                    line_data.insert(0,index)
                    index += 1
                    row_data.append(line_data)
        exc = openpyxl.load_workbook(destination_path)  # 打开整个excel文件
        sheet = exc.worksheets[0]  # 打开第0张工作表(也就是第一张)
        for row in row_data:
            sheet.append(row)  # 在工作表中添加一行
        exc.save(destination_path)  # 指定路径,保存文件

        # 使用字符串替换将\替换为/
        destination_path = destination_path.replace('\\', '/')
        destination_path = 'static/' + destination_path.split('static/')[1]
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "下载成功",
            "downloadUrl": destination_path
        }


    def get_detailed_proposal(self):   #详细的
        id = self.request.GET.get('id', None)#流程id
        oa_connect = OAConnect()
        oa_ie_data = oa_connect.select("""
                            SELECT
                                a.fd_process_id,
                                a.fd_fact_node_name,
                                a.fd_create_time,
                                b.doc_status,
                                c.fd_38ee4f12ab860a as 'gonghao',
                                c.fd_3c2d1db9377260 as 'tianleixing',
                                c.fd_3c2d1e0306c51c as 'wentifankui',
                                c.fd_heLiHuaJianYi as 'helihuajianyi',
                                d.fd_name as 'shishibumen',
                                e.fd_name as 'shishifuzeren',
                                c.fd_shiShiKeXingXingPingGu as 'shishikexingxingpinggu',
                                c.fd_yuanYinShuoMing as 'yuanyinshuoming',
                                c.fd_3c2d1eaf80eaac as 'shishikaishishijian',
                                c.fd_3c2d1ebdbbeb86 as 'shishijieshushijian',
                                c.fd_yanShou as 'yanshou',
                                c.fd_3c2d1f1b610ff8 as 'beizhu'
                                FROM
                                        lbpm_audit_note AS a
                                        LEFT JOIN lbpm_process AS b ON a.fd_process_id = b.fd_id
                                        LEFT JOIN ekp_18a644a0e38b4aaa8979 as c on b.fd_id = c.fd_id
                                        LEFT JOIN sys_org_element as d on c.fd_3c2d1e6c6c197c = d.fd_id
                                        LEFT JOIN sys_org_element as e on c.fd_3c2d1e7ce45706 = e.fd_id
                             
                                where a.fd_process_id='{}'
                       """.format(id))
        # sorted_oa_ie_data = sorted(oa_ie_data, key=self.custom_sort_key)  # 排序
        sorted_oa_ie_data = sorted(oa_ie_data, key=lambda x: (-x['fd_create_time'].timestamp(), x['fd_process_id'], self.custom_sort(x)),reverse=True)  #,reverse=True
        ie_proposal_record = {}
        file_dict1 = {}#问题照片
        file_dict2 = {} #实施完成照片
        # 遍历原始数据列表
        ehr_connect = EhrConnect()




        for line in sorted_oa_ie_data:
            ehr_ie_data = ehr_connect.select("""
                SELECT
                     b.Name as employee_name
                 FROM
                     T_HR_Employee AS b 
                 WHERE
                      b.code = '{}'
                    """.format(line['gonghao']))
            fd_process_id = line['fd_process_id']
            ie_proposal_record[fd_process_id] = {
                'id':fd_process_id,
                'ie_proposal_employee': line['gonghao'],
                'ie_proposal_employee__employee_code': line['gonghao'],
                # 'ie_proposal_employee__employee_name':HrEmployee.objects.filter(employee_code=line['gonghao'], employee_status=1).values('employee_name').first()['employee_name'],
                'ie_proposal_employee__employee_name':ehr_ie_data[0]['employee_name'],
                'ie_proposal_type__ie_proposal_type_name': line['tianleixing'],#提案类型
                'ie_proposal_feedback_on_workshop_issues': line['wentifankui'],#问题反馈
                'ie_proposal_sane_proposal':line['helihuajianyi'],#合理化建议
                'ie_proposal_effect_department':line['shishibumen'],#实施部门
                'ie_proposal_effect_head':line['shishifuzeren'],#实施负责人
                'fd_shiShiKeXingXingPingGu':line['shishikexingxingpinggu'],#实施可行性评估
                'ie_proposal_reason':line['yuanyinshuoming'],#原因说明
                'ie_proposal_reality_start_time':line['shishikaishishijian'],#实施开始时间
                'ie_proposal_reality_end_time':line['shishijieshushijian'],#实施结束时间
                'ie_proposal_accept':line['yanshou'],#是否验收
                'ie_remark':line['beizhu'],#备注
            }
        ls = []
        for line in sorted_oa_ie_data:
            fd_process_id = line['fd_process_id']
            if line['fd_fact_node_name']=='起草节点':
                ie_proposal_record[fd_process_id]['ie_proposal_create_time']=line['fd_create_time']
            if line['fd_fact_node_name']=='直接上级审批':
                ie_proposal_record[fd_process_id]['ie_proposal_superior_examine_time'] = line['fd_create_time']
            if line['fd_fact_node_name']=='IE审批':
                ls.append(line['fd_create_time'])
                ie_proposal_record[fd_process_id]['ie_proposal_ie_examine_time'] = line['fd_create_time']
            if line['fd_fact_node_name']=='IE主管':
                ie_proposal_record[fd_process_id]['ie_proposal_ie_superior_examine_time'] = line['fd_create_time']
            if line['fd_fact_node_name']=='实施单位主管':
                ie_proposal_record[fd_process_id]['ie_proposal_effect_superior_examine_time'] = line['fd_create_time']
            if line['fd_fact_node_name']=='效果确认':
                ie_proposal_record[fd_process_id]['ie_proposal_ie_confirm_examine_time'] = line['fd_create_time']
            if line['fd_fact_node_name']=='结束节点':
                ie_proposal_record[fd_process_id]['ie_proposal_ie_end_time'] = line['fd_create_time']

        table_list = list(ie_proposal_record.values())
        file_list = list(IeProposalFile.objects.filter(ie_proposal_employee_id=id).values('id','ie_proposal_type',
                                                                                                                   'ie_proposal_file_name',
                                                                                                                   'ie_proposal_file_url',
                                                                                                                'ie_proposal_employee_id'))

        for item in file_list:  #查找每份提案对应的文件
            ie_proposal_employee_id = item.get('ie_proposal_employee_id')
            if item['ie_proposal_type']=='1':   #问题照片
                if ie_proposal_employee_id not in file_dict1:
                    file_dict1[ie_proposal_employee_id] = []
                file_dict1[ie_proposal_employee_id].append(item)
            elif item['ie_proposal_type']=='2':#实施完成照片
                if ie_proposal_employee_id not in file_dict2:
                    file_dict2[ie_proposal_employee_id] = []
                file_dict2[ie_proposal_employee_id].append(item)
        #
        for item in table_list:
            try:
                item['ie_proposal_create_time'] = item['ie_proposal_create_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_create_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_superior_examine_time'] = item['ie_proposal_superior_examine_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_superior_examine_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_ie_examine_time'] = item['ie_proposal_ie_examine_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_ie_examine_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_ie_superior_examine_time'] = item['ie_proposal_ie_superior_examine_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_ie_superior_examine_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_effect_superior_examine_time'] = item['ie_proposal_effect_superior_examine_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_effect_superior_examine_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_ie_confirm_examine_time'] = item['ie_proposal_ie_confirm_examine_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_ie_confirm_examine_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_reality_start_time'] = item['ie_proposal_reality_start_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_reality_start_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_reality_end_time'] = item['ie_proposal_reality_end_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_reality_end_time'] is not None else None
            except:
                pass
            try:
                item['ie_proposal_ie_end_time'] = item['ie_proposal_ie_end_time'].strftime("%Y-%m-%d %H:%M:%S") if item['ie_proposal_ie_end_time'] is not None else None
            except:
                pass
            ie_proposal_id = item.get('id')
            if ie_proposal_id in file_dict1:
                item['file1_ls'] = file_dict1[ie_proposal_id]
                item['file1_num'] = len(file_dict1[ie_proposal_id])
            else:
                item['file1_ls'] = []
                item['file1_num'] = 0
            if ie_proposal_id in file_dict2:
                item['file2_ls'] = file_dict2[ie_proposal_id]
                item['file2_num'] = len(file_dict2[ie_proposal_id])
            else:
                item['file2_ls'] = []
                item['file2_num'] = 0

        print(table_list)
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "信息返回成功",
            "data":  table_list[0],
        }

    def get_confirm_proposal(self):
        is_confirm=self.request.GET.get("is_confirm", None)
        code = self.request.GET.get('code', None)
        if is_confirm=='1':
            is_confirm=30    #已确认
        elif is_confirm=='0':
            is_confirm=20    #未确认
        oa_connect = OAConnect()
        oa_ie_data = oa_connect.select("""
                    SELECT
                        a.fd_process_id as id,
                        a.fd_fact_node_name,
                        a.fd_create_time,
                        b.doc_status,
                        c.fd_38ee4f12ab860a as 'gonghao',
                        c.fd_3c2d1db9377260 as 'tianleixing',
                        c.fd_3c2d1e0306c51c as 'wentifankui'
                    FROM
                        lbpm_audit_note AS a
                        LEFT JOIN lbpm_process AS b ON a.fd_process_id = b.fd_id
                        LEFT JOIN ekp_18a644a0e38b4aaa8979 as c on b.fd_id = c.fd_id
                        LEFT JOIN sys_org_element as d on c.fd_3c2d1e6c6c197c = d.fd_id
                        LEFT JOIN sys_org_element as e on c.fd_3c2d1e7ce45706 = e.fd_id
                     where b.doc_status={} AND c.fd_38ee4f12ab860a={}
               """.format(is_confirm,code))
        # sorted_oa_ie_data = sorted(oa_ie_data, key=self.custom_sort_key)#排序
        sorted_oa_ie_data = sorted(oa_ie_data, key=lambda x: (-x['fd_create_time'].timestamp(), x['id'], self.custom_sort(x)))
        ie_proposal_record = {}

        # 遍历原始数据列表
        for line in sorted_oa_ie_data:
            # fd_process_id = line['fd_process_id']
            fd_process_id = line['id']
            ie_proposal_record[fd_process_id] = {
                'id':line['id'],
                'ie_proposal_employee': line['gonghao'],
                'ie_proposal_type__ie_proposal_type_name': line['tianleixing'],
                'ie_proposal_feedback_on_workshop_issues': line['wentifankui'],
                'ie_proposal_create_time': line['fd_create_time']
            }


        # 将合并后的结果转换为列表
        table_list = list(ie_proposal_record.values())
        for item in table_list:
            item['ie_proposal_create_time']=item['ie_proposal_create_time'].strftime("%Y-%m-%d %H:%M:%S")
        self.return_data = {
            "code": status.HTTP_200_OK,
            "msg": "信息返回成功",
            "data": {
                'tableList': table_list,
            },
        }

    def proposal_options(self):
        code=self.request.GET.get('code',None)
        print(code)
        ie_proposal_type_list = list(IeProposalType.objects.filter(ie_proposal_type_status=True).values('id', 'ie_proposal_type_name'))

        new_list=[]
        if code is not None :
            ehr_connect = EhrConnect()
            ehr_ie_data = ehr_connect.select("""
                      SELECT
                           d.Dept3
                       FROM
                           T_HR_Employee AS b 
                           LEFT JOIN T_HR_Department AS d ON b.DeptID = d.id
                       WHERE
                            d.IfUse= 1 
                           AND b.code LIKE '{}'
                          """.format(code))
            print(ehr_ie_data)

            # dept_name=HrEmployee.objects.filter(employee_code=code,employee_status = '1').values_list( 'employee_department__department_name',flat=True).first()
            dept_name = ehr_ie_data[0]['Dept3']
            print(dept_name)
            # print(dept_name)
            gongduan_all = [
                {
                    "value": 'C1生产C区-高温',
                    "text": "C1生产C区-高温"
                },
                {
                    "value": 'C1生产C区-湿法',
                    "text": "C1生产C区-湿法"
                },

                {
                    "value": 'C1生产B区',
                    "text": "C1生产B区"
                },
                {
                    "value": 'C1生产丝网',
                    "text": "C1生产丝网"
                },
                {
                    "value": 'C1生产测试',
                    "text": "C1生产测试"
                },
                {
                    "value": 'C1生产无',
                    "text": "C1生产无"
                },
                {
                    "value": 'C2生产C区-湿法',
                    "text": "C2生产C区-湿法"
                },
                {
                    "value": 'C2生产C区-高温',
                    "text": "C2生产C区-高温"
                },
                {
                    "value": 'C2生产丝网',
                    "text": "C2生产丝网"
                },
                {
                    "value": 'C2生产B区',
                    "text": "C2生产B区"
                },
                {
                    "value": 'C2生产测试',
                    "text": "C2生产测试"
                },
                {
                    "value": 'C2生产无',
                    "text": "C2生产无"
                },
                {
                    "value": 'C1设备C区-湿法',
                    "text": "C1设备C区-湿法"
                },
                {
                    "value": 'C1设备C区-高温',
                    "text": "C1设备C区-高温"
                },
                {
                    "value": 'C1设备B区',
                    "text": "C1设备B区"
                },
                {
                    "value": 'C1设备丝网',
                    "text": "C1设备丝网"
                },
                {
                    "value": 'C1设备测试',
                    "text": "C1设备测试"
                },
                {
                    "value": 'C1设备无',
                    "text": "C1设备无"
                },

                {
                    "value": 'C2设备C区-湿法',
                    "text": "C2设备C区-湿法"
                },
                {
                    "value": 'C2设备C区-高温',
                    "text": "C2设备C区-高温"
                },
                {
                    "value": 'C2设备B区',
                    "text": "C2设备B区"
                },
                {
                    "value": 'C2设备丝网',
                    "text": "C2设备丝网"
                },
                {
                    "value": 'C2设备测试',
                    "text": "C2设备测试"
                },
                {
                    "value": 'C2设备无',
                    "text": "C2设备无"
                },

                {
                    "value": 'C1工艺C区-湿法',
                    "text": "C1工艺C区-湿法"
                },
                {
                    "value": 'C1工艺C区-高温',
                    "text": "C1工艺C区-高温"
                },
                {
                    "value": 'C1工艺B区',
                    "text": "C1工艺B区"
                },
                {
                    "value": 'C1工艺丝网',
                    "text": "C1工艺丝网"
                },
                {
                    "value": 'C1工艺测试',
                    "text": "C1工艺测试"
                },
                {
                    "value": 'C1工艺无',
                    "text": "C1工艺无"
                },

                {
                    "value": 'C2工艺C区-湿法',
                    "text": "C2工艺C区-湿法"
                },
                {
                    "value": 'C2工艺C区-高温',
                    "text": "C2工艺C区-高温"
                },
                {
                    "value": 'C2工艺B区',
                    "text": "C2工艺B区"
                },
                {
                    "value": 'C2工艺丝网',
                    "text": "C2工艺丝网"
                },
                {
                    "value": 'C2工艺测试',
                    "text": "C2工艺测试"
                },
                {
                    "value": 'C2工艺无',
                    "text": "C2工艺无"
                },
                {
                    "value": '工业工程部',
                    "text": "工业工程部"
                },
                {
                    "value": '信息技术部',
                    "text": "信息技术部"
                },
                {
                    "value": '行政部',
                    "text": "行政部"
                },
                {
                    "value": '安环部',
                    "text": "安环部"
                },
                # {
                #     "value": '设施部',
                #     "text": "设施部"
                # },
                # {
                #     "value": '质量部',
                #     "text": "质量部"
                # },

                {
                    "value": '人力资源部',
                    "text": "人力资源部"
                },
                {
                    "value": '财务中心',
                    "text": "财务中心"
                },
                {
                    "value": '计划部',
                    "text": "计划部"
                },
                {
                    "value": '总经办',
                    "text": "总经办"
                },
            ]
            for item in gongduan_all:
                if item['value'][:3]==dept_name[:3]:
                    # print(item['value'][:3], dept_name[:3])
                    new_list.append(item)
                # if dept_name=='仓库模块（润阳世纪）' or   dept_name=='计划模块（润阳世纪）':
                #     new_list=[
                #         {
                #     "value": '计划部',
                #     "text": "计划部"
                # }]
        # print(new_list)

        self.return_data = {
            'data': {
                'ie_proposal_type_list': [
                    {"value": item["id"], "text": item["ie_proposal_type_name"]}
                    for item in ie_proposal_type_list
                ],
                'gongduan_list':new_list
            },
            'code': HTTP_200_OK,
            'msg': '查询成功'
        }

    @staticmethod
    def mkdir(path):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)
        else:
            pass
    @staticmethod
    def createPath(pic, path, fileName, father_file):  # 生成路径     文件对象  文件上一级目录名称 文件名称   static下面的目录名称（父目录）
        now = arrow.now().format('YYYY-MM-DD')
        file_suffix = str(pic).split(".")[-1]  # 文件后缀
        file_name = f"{fileName}.{file_suffix}"  # 文件名称
        file_path = os.path.join('static', father_file, 'upload_file', now, path, file_name)  # 文件路径
        file_path = file_path.replace('\\', '/')
        return (file_path, file_name, file_suffix)  # 文件路径   文件名字  文件后缀
    @staticmethod
    def saveFile(file_path, file_obj):  # 文件名,图像对象   文件保存
        with open(str(file_path), 'wb+') as f:
            for dot in file_obj.chunks():
                f.write(dot)

    # @staticmethod
    # def custom_sort_key(item):# 自定义排序键函数
    #     node_order = ['起草节点', '直接上级审批', '部门负责人', 'IE审批', 'IE主管', 'IE负责人', '实施单位主管','实施部门负责人','效果确认','结束节点']# 定义节点顺序
    #     return (item['fd_process_id'], node_order.index(item['fd_fact_node_name']))

    # 自定义排序规则函数
    @staticmethod
    def custom_sort(item):
        process_order = {
            '起草节点': 0,
            '直接上级审批': 1,
            '部门负责人': 2,
            'IE审批': 3,
            'IE主管': 4,
            'IE负责人': 5,
            '实施单位主管': 6,
            '实施部门负责人': 7,
            '效果确认': 8,
            '结束节点': 9
        }
        return process_order.get(item['fd_fact_node_name'], 10)



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
            'ie_proposal_employee__employee_name',
            'ie_proposal_employee__employee_code',
            'bumen',
            'gongduan',
            'ie_proposal_type__ie_proposal_type_name',
            'ie_proposal_feedback_on_workshop_issues',
            'ie_proposal_sane_proposal',
            'ie_proposal_create_time',
            'ie_proposal_superior_examine_time',
            'ie_proposal_ie_examine_time',
            'ie_proposal_ie_superior_examine_time',
            'ie_proposal_effect_department',
            'ie_proposal_effect_head',
            'ie_proposal_effect_superior_examine_time',
            'ie_proposal_ie_confirm_examine_time',
            'ie_proposal_reality_start_time',
            'ie_proposal_reality_end_time',
            'fd_shiShiKeXingXingPingGu',
            'ie_proposal_accept',
            'ie_proposal_remark',
            'ie_proposal_reason',
            'id','file1_ls','file1_num','file2_ls','file2_num','index'
        ]
        sorted_list_of_dicts = [dict(sorted(d.items(), key=lambda x: order.index(x[0]))) for d in list_of_dicts]
        return sorted_list_of_dicts

