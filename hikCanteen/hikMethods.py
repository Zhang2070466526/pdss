import base64
import hashlib
import hmac
import json
import os
import time
import datetime as dt
import uuid
from base64 import encode
from ftplib import FTP
from hashlib import md5, sha256
import pytz
import numpy as np
from dateutil import parser
# from datetime import datetime

import cv2
import requests
import arrow
import urllib3

from hikCanteen.sql import *
from utils.sqlServerConnect import EhrConnect

urllib3.disable_warnings()


def if_None(val):
    if val is None:
        return 0
    else:
        return val


def get_sign(key, data):
    data = data.encode('utf-8')
    return base64.b64encode(hmac.new(key.encode('utf-8'), data, digestmod=sha256).digest())


def ftpconnect(host, port, username, password):
    ftp = FTP()
    # 打开调试级别2，显示详细信息
    ftp.connect(host, port)
    ftp.login(username, password)
    return ftp


# 从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    # 设置的缓冲区大小
    bufsize = 1024
    fp = open(localpath, 'wb')
    try:
        ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)  # 接受服务器上文件并写入本地文件
        ftp.set_debuglevel(0)  # 参数为0，关闭调试模式
        fp.close()
        return True
    except Exception as e:
        print(e)
        return False


def get_photo(code):
    if not os.path.exists("static/hikPhotos"):
        os.makedirs("static/hikPhotos")
    if not os.path.exists("static/hikPhotos/photos"):
        os.makedirs("static/hikPhotos/photos")
    ftp = ftpconnect("172.16.6.131", 2123, "admin", "123456")
    try:
        print(ftp.nlst('/%s' % code))
        flag = True
    except Exception as a:
        print(a)
        flag = False
    if flag is True:
        return downloadfile(ftp, '/%s/%s.jpg' % (code, code), 'static/hikPhotos/photos/%s.jpg' % code)
    else:
        return False


def change_pic_size(path):
    """
    循环压缩图片，使得它的大小保持在其中
    :param path:
    :return:
    """
    image = cv2.imread(path)
    original_size = os.path.getsize(path) // 1024
    # 计算压缩比例
    scale = 1.0
    quality = 90
    result = True
    while original_size > 195 or original_size < 15:
        if original_size > 195:
            scale *= 0.9  # 缩小比例为当前的90%
            quality -= 5
        if original_size < 15:
            scale *= 1.1
            quality += 5
        if quality > 100 or quality < 30:
            result = False
            break
        resized_image = cv2.resize(image, None, fx=scale, fy=scale)
        cv2.imwrite(path, resized_image, [cv2.IMWRITE_JPEG_QUALITY, quality])

        compressed_size = os.path.getsize(path) // 1024
        original_size = compressed_size
    return result


def save_file(file, code):
    if not os.path.exists("static/hikPhotos"):
        os.makedirs("static/hikPhotos")
    if not os.path.exists("static/hikPhotos/photos"):
        os.makedirs("static/hikPhotos/photos")
    path = "static/hikPhotos/photos/{0}.jpg".format(code)
    with open(path, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)
    image = cv2.imread(path)
    height, width = image.shape[0], image.shape[1]
    if width > height:
        image = cv2.imread(path)
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)  # 顺时针旋转90度
        cv2.imwrite(path, rotated_image)
    status = change_pic_size(path)
    if status is False:
        path = 0

    # if os.path.getsize(path) / 1024 > 200 or os.path.getsize(path) / 1024 < 10:
    #     image = cv2.imread(path)
    #     height, width = image.shape[0], image.shape[1]
    #     scale = os.path.getsize(path) / 1024 / 200
    #     image_resize = cv2.resize(image, (round(width / scale), round(height / scale)))
    #     path = "static/hikPhotos/photos/1010000401.jpg"
    #     cv2.imwrite(path, image_resize, [cv2.IMWRITE_JPEG_QUALITY, 95])
    #
    #     image = cv2.imread(path)
    #     height, width = image.shape[0], image.shape[1]
    #     print("压缩后的图像")
    #     print("size:", os.path.getsize(path) / 1024)
    #     print("height:", height)
    #     print("width:", width)

    return path


class HikvisonInterface:
    """
    与海康智慧园区平台交互接口
    1、同步组织
    2、删除组织
    3、新增人员和人脸
    4、删除人员
    5、充值
    """

    def __init__(self):
        # 总部智慧园区系统
        self.host = 'https://172.16.6.84'
        self.port = '444'
        self.appKey = '27139717'
        self.appSecret = 'b324yhWlgERdZKm4z5mF'
        # 建湖二期智慧园区系统
        # self.host = 'https://10.70.81.1'
        # self.port = '8443'
        # self.appKey = '23120519'
        # self.appSecret = 'cpXW0sDLKpvvvOpFFL5t'
        self.artemis = 'artemis'
        self.access_token_url = '/api/v1/oauth/token'
        self.get_region_list_url = '/api/irds/v2/region/nodesByParams'
        self.get_org_list_url = '/api/resource/v1/org/orgList'
        self.add_org_url = '/api/resource/v1/org/batch/add'
        self.add_person_url = '/api/resource/v2/person/single/add'
        self.delete_person_batch_url = '/api/resource/v1/person/batch/delete'
        self.search_person_by_code_url = '/api/resource/v1/person/condition/personInfo'
        self.add_picture_by_code_url = '/api/resource/v1/face/single/add'
        self.update_picture_url = '/api/resource/v1/face/single/update'
        self.entry_add_money_url = '/api/cems/v1/account/recharge'
        self.select_expenses_record_url = '/api/cems/v1/consume/log/search'
        self.report_loss_url = '/api/cis/v1/card/batch/loss'
        self.report_unloss_url = '/api/cis/v1/card/batch/unLoss'
        self.select_person_cards_url = '/api/irds/v1/card/advance/cardList'
        self.select_balance_url = '/api/cems/v1/account/balance/search'
        self.test_photo_url = '/api/frs/v1/face/picture/check'
        self.search_person_photo = "/api/resource/v1/person/picture"
        self.select_person_list_v2 = "/api/resource/v2/person/advance/personList"
        self.ehr = EhrConnect()

    # 获取token
    def get_access_token(self):
        method = "POST"
        t = time.time()
        nowTime = lambda: int(round(t * 1000))
        timestamp = nowTime()
        timestamp = str(timestamp)
        # uuid
        nonce = str(uuid.uuid1())
        message = str(
            method + '\n*/*\napplication/json\nx-ca-key:' + self.appKey + '\nx-ca-nonce:' + nonce + '\nx-ca-timestamp:' + timestamp + '\n/' + self.artemis + self.access_token_url).encode(
            'utf-8')
        signature = base64.b64encode(
            hmac.new(self.appSecret.encode('utf-8'), message, digestmod=hashlib.sha256).digest())
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'X-Ca-timestamp': timestamp,
            'X-Ca-Key': self.appKey,
            'X-Ca-nonce': nonce,
            'X-Ca-Signature': signature,
            'X-Ca-Signature-Headers': 'x-ca-key,x-ca-nonce,x-ca-timestamp'
        }

        res = requests.post(headers=headers,
                            url=self.host + ':' + self.port + '/' + self.artemis + self.access_token_url, verify=False)
        # print(res.content.decode('utf-8'))
        return json.loads(res.content.decode('utf-8'))

    # 查询区域
    def get_region_list(self):
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        content = {
            'resourceType': 'region',
            'pageSize': 1000,
            'pageNo': 1
        }
        res = requests.post(headers=headers,
                            url=self.host + ':' + self.port + '/' + self.artemis + self.get_region_list_url,
                            json=content, verify=False)
        print(json.loads(res.content.decode('utf-8')))

    # 查询部门
    def get_org_list(self):
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        content = {
            'pageSize': 1000,
            'pageNo': 1
        }
        res = requests.post(headers=headers,
                            url=self.host + ':' + self.port + '/' + self.artemis + self.get_org_list_url, json=content,
                            verify=False)
        print(json.loads(res.content.decode('utf-8')))

    # 新增部门
    def add_org(self):
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        # 获取ehr 中部门信息
        select_department_sql = """
            SELECT
                    b.DepartmentCode as code1,
                    b.DepartmentName as name1,
                    a.DepartmentCode as code2,
                    a.DepartmentName as name2
                FROM
                    T_HR_Department AS a
                    INNER JOIN T_HR_Department AS b ON b.ParentID = a.ID
                WHERE
                    b.ExpiryDate IS NULL
                ORDER BY
                    b.DeptLeve
        """
        ehr = EhrConnect()
        department_list = ehr.select(select_department_sql)
        if department_list:
            for department_info in department_list:
                print(department_info['code1'], department_info['name1'])
                content = []
                content.append({
                    'orgIndexCode': department_info['code1'],
                    'orgName': department_info['name1'],
                    'parentIndexCode': department_info['code2']
                })
                res = requests.post(headers=headers,
                                    url=self.host + ':' + self.port + '/' + self.artemis + self.add_org_url,
                                    json=content, verify=False)
                print(json.loads(res.content.decode('utf-8')))

    # 新增人员
    def add_person(self, company):
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        if company == 'zongbu':
            employee_list = self.ehr.select(select_zongbu_new_person)
        else:
            employee_list = self.ehr.select(select_jianhuerqi_new_person)
        for employee_info in employee_list:
            print(employee_info['code'])
            if get_photo(employee_info['code']):
                try:
                    result = change_pic_size("static/hikPhotos/photos/%s.jpg" % employee_info['code'])
                    # if os.path.getsize("static/hikPhotos/photos/%s.jpg" % employee_info[
                    #     'code']) / 1024 > 200 or os.path.getsize(
                    #     "static/hikPhotos/photos/%s.jpg" % employee_info['code']) / 1024 < 10:
                    #     image = cv2.imread("static/hikPhotos/photos/%s.jpg" % employee_info['code'])
                    #     height, width = image.shape[0], image.shape[1]
                    #     scale = os.path.getsize(
                    #         "static/hikPhotos/photos/%s.jpg" % employee_info['code']) / 1024 / 200
                    #     image_resize = cv2.resize(image, (round(width / scale), round(height / scale)))
                    #     cv2.imwrite("static/hikPhotos/photos/%s.jpg" % employee_info['code'],
                    #                 image_resize, [cv2.IMWRITE_JPEG_QUALITY, 80])
                    try:
                        with open("static/hikPhotos/photos/%s.jpg" % employee_info['code'],
                                  "rb") as f:  # 转为二进制格式
                            base64_data = base64.b64encode(f.read()).decode('utf-8')  # 使用base64进行加密
                    except Exception as e:
                        print(e)
                        base64_data = ''
                except Exception as e:
                    print(e)
                    base64_data = ''
            else:
                base64_data = ''
            content = {
                'personId': employee_info['code'],
                'jobNo': employee_info['code'],
                'personName': employee_info['name'],
                'orgIndexCode': employee_info['DepartmentCode'],
                'certificateType': '111',
                'certificateNo': employee_info['IdentityNumber'],
                'gender': employee_info['Sex'],
            }
            if base64_data != '':
                content['faces'] = [{
                    'faceData': base64_data
                }]
            res = requests.post(headers=headers,
                                url=self.host + ':' + self.port + '/' + self.artemis + self.add_person_url,
                                json=content, verify=False)
            res_data = json.loads(res.content.decode('utf-8'))
            print(res_data)
            print(res_data['data'])
            # 如果返回信息带有faceId，则更新到ehr里
            if res_data['data'] is not None:
                if res_data['data']['faceId'] is not None:
                    if company == 'zongbu':
                        self.ehr.update(update_zongbu_face_status(employee_info['code']))
                    else:
                        self.ehr.update(update_jianhuerqi_face_status(employee_info['code']))

    # 批量删除人员
    def delete_person_batch(self):
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        # 获取ehr 中部门信息
        select_leave_person_sql = """
            select code,name from T_HR_Employee where _lztbrq = '%s'
        """ % str(arrow.now().shift(days=-2).date()) + ' 00:00:00'
        ehr = EhrConnect()
        leave_person_list = ehr.select(select_leave_person_sql)
        if leave_person_list:
            personIds = []
            for leave_person_info in leave_person_list:
                personIds.append(leave_person_info['code'])
            res = requests.post(headers=headers,
                                url=self.host + ':' + self.port + '/' + self.artemis + self.delete_person_batch_url,
                                json=personIds, verify=False)
            print(json.loads(res.content.decode('utf-8')))

    # 查询人员(根据工号查询personid)
    def search_person_by_code(self, code):
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        content = {
            "paramName": "jobNo",
            "paramValue": [
                code
            ]
        }
        res = requests.post(headers=headers,
                            url=self.host + ':' + self.port + '/' + self.artemis + self.search_person_by_code_url,
                            json=content, verify=False)
        return json.loads(res.content.decode('utf-8'))['data']['list'][0]['personId']
        # if len(json.loads(res.content.decode('utf-8'))['data']['list']) > 0 and len(json.loads(res.content.decode('utf-8'))['data']['list'][0]['personPhoto']) > 0:
        #     if 'personPhotoIndexCode' in json.loads(res.content.decode('utf-8'))['data']['list'][0]['personPhoto'][0]:
        #         return json.loads(res.content.decode('utf-8'))['data']['list'][0]['personPhoto'][0]['personPhotoIndexCode']
        # else:
        #     return False

    # 手动增加人员照片
    def add_picture_by_code(self, company):
        method = "POST"
        t = time.time()
        nowTime = lambda: int(round(t * 1000))
        timestamp = nowTime()
        timestamp = str(timestamp)
        # uuid
        nonce = str(uuid.uuid1())
        message = str(
            method + '\n*/*\napplication/json\nx-ca-key:' + self.appKey + '\nx-ca-nonce:' + nonce + '\nx-ca-timestamp:' + timestamp + '\n/' + self.artemis + self.add_picture_by_code_url).encode(
            'utf-8')
        signature = base64.b64encode(
            hmac.new(self.appSecret.encode('utf-8'), message, digestmod=hashlib.sha256).digest())
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'X-Ca-timestamp': timestamp,
            'X-Ca-Key': self.appKey,
            'X-Ca-nonce': nonce,
            'X-Ca-Signature': signature,
            'X-Ca-Signature-Headers': 'x-ca-key,x-ca-nonce,x-ca-timestamp'
        }
        if company == 'zongbu':
            employee_list = self.ehr.select(select_zongbu_no_face_employee)
        else:
            employee_list = self.ehr.select(select_jianhuerqi_no_face_employee)
        if employee_list:
            for employee_info in employee_list:
                print(employee_info['code'])
                if get_photo(employee_info['code']):
                    try:
                        result = change_pic_size("static/hikPhotos/photos/%s.jpg" % employee_info['code'])

                        # if os.path.getsize("static/hikPhotos/photos/%s.jpg" % employee_info[
                        #     'code']) / 1024 > 200 or os.path.getsize(
                        #     "static/hikPhotos/photos/%s.jpg" % employee_info['code']) / 1024 < 10:
                        #     image = cv2.imread("static/hikPhotos/photos/%s.jpg" % employee_info['code'])
                        #     height, width = image.shape[0], image.shape[1]
                        #     scale = os.path.getsize(
                        #         "static/hikPhotos/photos/%s.jpg" % employee_info['code']) / 1024 / 200
                        #     image_resize = cv2.resize(image, (round(width / scale), round(height / scale)))
                        #     cv2.imwrite("static/hikPhotos/photos/%s.jpg" % employee_info['code'],
                        #                 image_resize, [cv2.IMWRITE_JPEG_QUALITY, 80])

                        try:
                            with open("static/hikPhotos/photos/%s.jpg" % employee_info['code'],
                                      "rb") as f:  # 转为二进制格式
                                base64_data = base64.b64encode(f.read()).decode('utf-8')  # 使用base64进行加密
                        except Exception as e:
                            print(e)
                            base64_data = ''
                    except Exception as e:
                        print(e)
                        base64_data = ''
                else:
                    base64_data = ''
                content = {
                    "personId": employee_info['code'],
                    "faceData": base64_data
                }
                res = requests.post(headers=headers,
                                    url=self.host + ':' + self.port + '/' + self.artemis + self.add_picture_by_code_url,
                                    json=content, verify=False)
                print(res)
                res_data = json.loads(res.content.decode('utf-8'))
                print(res_data)
                # 如果返回信息带有faceId，则更新到ehr里
                if res_data['data'] is not None:
                    if res_data['data']['faceId'] is not None:
                        if company == 'zongbu':
                            self.ehr.update(update_zongbu_face_status(employee_info['code']))
                        else:
                            self.ehr.update(update_jianhuerqi_face_status(employee_info['code']))
                # elif res_data['code'] == '0x00072001':
                #     if company == 'zongbu':
                #         self.ehr.update(update_zongbu_face_status(employee_info['code']))
                #     else:
                #         self.ehr.update(update_jianhuerqi_face_status(employee_info['code']))

    def daliy_entry_person_to_oa(self):
        """
        查询每日新增人员，根据合同归属分别取不同金额生成oa首充流程
        :return:
        """
        daliy_person_list = self.ehr.select(
            daliy_entry_job_rank_person_sql(str(arrow.now().date()) + ' 00:00:00'))
        # 遍历生成字典
        person_obj = {}
        for daliy_person_info in daliy_person_list:
            if daliy_person_info['JobRankName'] not in person_obj.keys():
                person_obj[daliy_person_info['JobRankName']] = [daliy_person_info]
            else:
                person_obj[daliy_person_info['JobRankName']].append(daliy_person_info)
        print(person_obj)
        for job_rank, job_rank_person_list in person_obj.items():
            entry_date = []
            name = []
            code = []
            department = []
            amount = []
            position = []
            remark = []
            for person_info in job_rank_person_list:
                name.append(person_info['name'])
                entry_date.append(str(person_info['_jtrzrq'])[:10])
                code.append(person_info['code'])
                department.append(person_info['DepartmentName'])
                amount.append(person_info['entryCanteenAmount'])
                position.append(person_info['PostName'])
                remark.append('')
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
                                                    <docCreator>{"LoginName":"2010009598"}</docCreator>
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
                                                    <fdTemplateId>188b7c60014351056752b284eee89421</fdTemplateId>
                                                    <!--Optional:--><flowParam>{}</flowParam>
                                                    <!--Optional:-->
                                                    <formValues>{"fd_3bec8b27bc5dac":"%s","fd_3bed78fa065f82":"%s","fd_3bec9afaf0d078.fd_3bec9b4cc31f76":%s,"fd_3bec9afaf0d078.fd_3bec9b5f14d078":%s,"fd_3bec9afaf0d078.fd_3bec9b6000ce3e":%s,"fd_3bec9afaf0d078.fd_3bed78fe477f34":%s,"fd_3bec9afaf0d078.fd_3bec9b61904556":%s,"fd_3bec9afaf0d078.fd_3bec9bf778452e":%s,"fd_3bec9afaf0d078.fd_3bec9bf8c8ef0e":%s}</formValues>
                                                </arg0>
                                            </web:addReview>
                                        </soapenv:Body>
                                    </soapenv:Envelope>
                            """ % (
                str(arrow.now().date()) + job_rank + '新入职人员餐补申请流程',
                str(arrow.now().date()) + job_rank + '新入职人员餐补申请流程',
                job_rank,
                entry_date,
                department,
                code, name, position, amount, remark)
            response = requests.request("POST", url, headers=headers, data=payload.replace("'", '"'))
            print(response.text)

        # 遍历字典发送流程

    def oa_entry_add_money(self, oa_data):
        """
        新入职人员首充接口，承接oa流程数据
        :param oa_data: oa流程数据
        :return:
        """
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        for oa_person_info in oa_data:
            if oa_person_info['entry_money'] == 0:
                # 金额为0则记录在ehr人员表中
                self.ehr.update(update_not_need_canteen_person_sql(oa_person_info['code']))
            else:
                self.ehr.update(update_need_canteen_person_sql(oa_person_info['code']))
                content = {
                    "personId": oa_person_info['code'],
                    "money": int(oa_person_info['entry_money']) * 100,
                    "accountType": 1,
                    "rechargeId": str(uuid.uuid1()).replace('-', '')
                }
                res = requests.post(headers=headers,
                                    url=self.host + ':' + self.port + '/' + self.artemis + self.entry_add_money_url,
                                    json=content, verify=False)
                print(json.loads(res.content.decode('utf-8')))

    def month_money_to_oa(self):
        """
        每月7号发起流程审批上月餐补
        :return:
        """
        month_meal_allowance_obj = self.ehr.select(
            month_meal_allowance_sql('2023-02-01 00:00:00', '2023-02-28 00:00:00'))
        if month_meal_allowance_obj:
            department_month_meal_allowance = {}
            for month_meal_allowance in month_meal_allowance_obj:
                print(month_meal_allowance)
                # 写入部门
                if month_meal_allowance['DepartmentCode'] not in department_month_meal_allowance:
                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']] = {}
                # 写入部门下的人员工号和初始数据
                if month_meal_allowance['code'] not in department_month_meal_allowance[
                    month_meal_allowance['DepartmentCode']]:
                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                        month_meal_allowance['code']] = {
                        'chuqin': 0,
                        'butie': 0,
                        'zhoumojiaban': 0,
                        'jiaban>2': 0,
                        'jiaban>5': 0,
                        'jiaban>7.5': 0,
                        'jiaban>10': 0,
                        'jiaban>12.5': 0,
                        'yeban': 0,
                        'qingjia>4': 0
                    }

                # **************************************************************
                # 宁夏
                if month_meal_allowance['job_rank_id'] in (27, 45, 48, 49):
                    # 根据joblevel判断是否是经理级以上
                    # 经理级以上就添加应出勤日期
                    if month_meal_allowance['JobLevelCode'] == 'ZJ010' or month_meal_allowance[
                        'JobLevelCode'] == 'ZJ020' or month_meal_allowance['JobLevelCode'][-1] in ('5', '6', '7', '8'):
                        if month_meal_allowance['BiaoZhun'] is not None:
                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                month_meal_allowance['code']]['chuqin'] += 1
                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                month_meal_allowance['code']]['butie'] += 45
                    # 不是经理级，需要根据出勤计算餐补
                    else:
                        # 工作日
                        if month_meal_allowance['BiaoZhun'] is not None:
                            # 夜班
                            if month_meal_allowance['night'] == 1:
                                # 没有请假、调休加起来4小时
                                if if_None(month_meal_allowance['njxs']) + if_None(
                                        month_meal_allowance['sjxs']) + if_None(month_meal_allowance['bjxs']) + if_None(
                                    month_meal_allowance['hjxs']) + if_None(month_meal_allowance['njxs']) + if_None(
                                    month_meal_allowance['cjxs']) + if_None(month_meal_allowance['gsxs']) + if_None(
                                    month_meal_allowance['txxs']) + if_None(
                                    month_meal_allowance['sajxs']) + if_None(month_meal_allowance['pcjxs']) + if_None(
                                    month_meal_allowance['cjjxs']) + if_None(month_meal_allowance['hljxs']) + if_None(
                                    month_meal_allowance['brjxs']) + if_None(month_meal_allowance['ccxs']) + if_None(
                                    month_meal_allowance['yejxs']) <= 4:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['chuqin'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 55
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['yeban'] += 1
                                else:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['qingjia>4'] += 1
                            else:
                                # 没有请假、调休加起来4小时
                                if if_None(month_meal_allowance['njxs']) + if_None(
                                        month_meal_allowance['sjxs']) + if_None(month_meal_allowance['bjxs']) + if_None(
                                    month_meal_allowance['hjxs']) + if_None(month_meal_allowance['njxs']) + if_None(
                                    month_meal_allowance['cjxs']) + if_None(month_meal_allowance['gsxs']) + if_None(
                                    month_meal_allowance['txxs']) + if_None(
                                    month_meal_allowance['sajxs']) + if_None(month_meal_allowance['pcjxs']) + if_None(
                                    month_meal_allowance['cjjxs']) + if_None(month_meal_allowance['hljxs']) + if_None(
                                    month_meal_allowance['brjxs']) + if_None(month_meal_allowance['ccxs']) + if_None(
                                    month_meal_allowance['yejxs']) <= 4:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['chuqin'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 45
                                else:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['qingjia>4'] += 1
                        # 非工作日
                        else:
                            # 加班4小时以上补贴
                            if month_meal_allowance['_ctxxs'] >= 4:
                                department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                    month_meal_allowance['code']]['zhoumojiaban'] += 1
                                department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                    month_meal_allowance['code']]['butie'] += 45
                # 不是宁夏
                else:
                    # 副经理及以上（后续需要单独处理+4的补贴）
                    if month_meal_allowance['JobLevelCode'] in (
                            'ZJ010', 'ZDM8', 'ZDM7', 'ZDM6', 'ZDT6', 'ZDT7', 'ZDP6', 'ZDM5', 'ZDT5', 'ZDP5', 'JYRC'):
                        if month_meal_allowance['BiaoZhun'] is not None:
                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                month_meal_allowance['code']]['chuqin'] += 1
                            department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                month_meal_allowance['code']]['butie'] += 24
                    # 副经理以下
                    else:
                        # 责任制
                        if month_meal_allowance['PayTypeID'] == 2:
                            # 工作日
                            if month_meal_allowance['BiaoZhun'] is not None:
                                # 请假时长小于4小时
                                if if_None(month_meal_allowance['njxs']) + if_None(
                                        month_meal_allowance['sjxs']) + if_None(month_meal_allowance['bjxs']) + if_None(
                                    month_meal_allowance['hjxs']) + if_None(month_meal_allowance['njxs']) + if_None(
                                    month_meal_allowance['cjxs']) + if_None(month_meal_allowance['gsxs']) + if_None(
                                    month_meal_allowance['txxs']) + if_None(
                                    month_meal_allowance['sajxs']) + if_None(month_meal_allowance['pcjxs']) + if_None(
                                    month_meal_allowance['cjjxs']) + if_None(month_meal_allowance['hljxs']) + if_None(
                                    month_meal_allowance['brjxs']) + if_None(month_meal_allowance['ccxs']) + if_None(
                                    month_meal_allowance['yejxs']) <= 4:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['chuqin'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 12
                                else:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['qingjia>4'] += 1
                                    # 加班
                                # 2小时补贴12， 7.5小时补贴12， 12.5小时补贴6元
                                if month_meal_allowance['_ctxxs'] >= 2:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>2'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 12
                                if month_meal_allowance['_ctxxs'] >= 7.5:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>7.5'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 12
                                if month_meal_allowance['_ctxxs'] >= 12.5:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>12.5'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 12
                            # 周末节假日
                            else:
                                # 加班4小时以上有补贴
                                if month_meal_allowance['_ctxxs'] >= 4:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['zhoumojiaban'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 12
                        # 计时制
                        else:
                            # 夜班
                            if month_meal_allowance['IfNight'] == 1:
                                # 请假4小时以内
                                if if_None(month_meal_allowance['njxs']) + if_None(
                                        month_meal_allowance['sjxs']) + if_None(month_meal_allowance['bjxs']) + if_None(
                                    month_meal_allowance['hjxs']) + if_None(month_meal_allowance['njxs']) + if_None(
                                    month_meal_allowance['cjxs']) + if_None(month_meal_allowance['gsxs']) + if_None(
                                    month_meal_allowance['txxs']) + if_None(
                                    month_meal_allowance['sajxs']) + if_None(month_meal_allowance['pcjxs']) + if_None(
                                    month_meal_allowance['cjjxs']) + if_None(month_meal_allowance['hljxs']) + if_None(
                                    month_meal_allowance['brjxs']) + if_None(month_meal_allowance['ccxs']) + if_None(
                                    month_meal_allowance['yejxs']) <= 4:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['chuqin'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 18
                                else:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['qingjia>4'] += 1

                                # 加班5小时补贴12，加班10小时补贴6
                                if month_meal_allowance['_ctxxs'] >= 5:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>5'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 12
                                if month_meal_allowance['_ctxxs'] >= 10:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>10'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 6
                            # 白班
                            else:
                                # 请假4小时以内
                                if if_None(month_meal_allowance['njxs']) + if_None(
                                        month_meal_allowance['sjxs']) + if_None(month_meal_allowance['bjxs']) + if_None(
                                    month_meal_allowance['hjxs']) + if_None(month_meal_allowance['njxs']) + if_None(
                                    month_meal_allowance['cjxs']) + if_None(month_meal_allowance['gsxs']) + if_None(
                                    month_meal_allowance['txxs']) + if_None(
                                    month_meal_allowance['sajxs']) + if_None(month_meal_allowance['pcjxs']) + if_None(
                                    month_meal_allowance['cjjxs']) + if_None(month_meal_allowance['hljxs']) + if_None(
                                    month_meal_allowance['brjxs']) + if_None(month_meal_allowance['ccxs']) + if_None(
                                    month_meal_allowance['yejxs']) <= 4:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['chuqin'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 24
                                else:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['qingjia>4'] += 1

                                # 加班5小时补贴12，加班10小时补贴12
                                if month_meal_allowance['_ctxxs'] >= 5:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>5'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 12
                                if month_meal_allowance['_ctxxs'] >= 10:
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['jiaban>10'] += 1
                                    department_month_meal_allowance[month_meal_allowance['DepartmentCode']][
                                        month_meal_allowance['code']]['butie'] += 12

            print(department_month_meal_allowance)

    def select_expenses_record(self, begin_time, end_time, person_id):
        """
        查询消费记录
        :return:
        """
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        content = {
            'startTime': begin_time,
            'endTime': end_time,
            'personId': person_id,
            'pageNo': 1,
            'pageSize': 1000
        }
        res = requests.post(headers=headers,
                            url=self.host + ':' + self.port + '/' + self.artemis + self.select_expenses_record_url,
                            json=content, verify=False)
        res = json.loads(res.content.decode('utf-8'))
        if res['code'] != '0':
            res = {
                'code': 200,
                'msg': res['msg']
            }
        else:
            res['msg'] = "查询成功"
            for i in res['data']['rows']:
                china_tz = pytz.timezone("Asia/Shanghai")
                dateObject = parser.isoparse(i['debitTime'])
                i['debitTime'] = dateObject.astimezone(tz=china_tz)
                i['debitTime'] = i['debitTime'].strftime('%Y-%m-%d %H:%M:%S')
                if "preAccount" in i:
                    i['preAccount'] = str(i['preAccount'])[:-2] + "." + str(i['preAccount'])[-2:] + "元"
                if "deduction" in i:
                    i['deduction'] = str(i['deduction'])[:-2] + "." + str(i['deduction'])[-2:] + "元"
                if "balance" in i:
                    i['balance'] = str(i['balance'])[:-2] + "." + str(i['balance'])[-2:] + "元"
        return res

    def select_person_cards(self, code):
        """
               查询卡号
               :return:
               """
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        content = {
            "pageNo": 1,
            "pageSize": 1000,
            "personIds": self.search_person_by_code(code),
            # 'useStatus': 1 # 卡片状态
        }
        res = requests.post(headers=headers,
                            url=self.host + ':' + self.port + '/' + self.artemis + self.select_person_cards_url,
                            json=content, verify=False)
        res_data = json.loads(res.content.decode('utf-8'))
        if res_data['data']['list']:
            return {
                'code': 200,
                'msg': '查询成功',
                'cardList': [{'no': data['cardNo'], 'createTime': data['createTime'][:10].replace('T', ' '),
                              'status': data['useStatus'], "cardType": "正常使用" if data['useStatus'] == 1 else "已挂失",
                              "cardStyle": {"backgroundColor": '#55ff00'} if data['useStatus'] == 1 else {
                                  "backgroundColor": '#ff0000'}} for
                             data in res_data['data']['list']]
            }
        else:
            return {
                'code': 200,
                'msg': '您还没有卡',
                'cardList': []
            }

    def report_loss_card(self, card_no):
        """
        卡挂失，先要获取卡号
        :return:
        """
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        content = {
            "cardList": [
                {
                    "cardNumber": card_no
                }
            ]
        }
        res = requests.post(headers=headers,
                            url=self.host + ':' + self.port + '/' + self.artemis + self.report_loss_url, json=content,
                            verify=False)
        res = json.loads(res.content.decode('utf-8'))
        if res['code'] == '0':
            return {
                'code': 200,
                'msg': '挂失成功',
            }
        else:
            return {
                'code': 200,
                'msg': res['msg'],
            }

    def report_unloss_card(self, card_no):
        """
        卡解挂，先要获取卡号
        :return:
        """
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        content = {
            "cardList": [
                {
                    "cardNumber": card_no
                }
            ]
        }
        res = requests.post(headers=headers,
                            url=self.host + ':' + self.port + '/' + self.artemis + self.report_unloss_url, json=content,
                            verify=False)
        res = json.loads(res.content.decode('utf-8'))
        if res['code'] == '0':
            return {
                'code': 200,
                'msg': '解挂成功',
            }
        else:
            return {
                'code': 200,
                'msg': res['msg'],
            }

    def select_balance(self, code):
        """
        查询余额
        :return:
        """
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        try:
            content = {
                "personId": self.search_person_by_code(code)
            }
        except:
            return {
                'code': 200,
                'balance': 0
            }
        res = requests.post(headers=headers,
                            url=self.host + ':' + self.port + '/' + self.artemis + self.select_balance_url,
                            json=content, verify=False)
        res = json.loads(res.content.decode('utf-8'))
        if res['data']:
            return {
                'code': 200,
                'balance': str(res['data']['totalAccount'] / 100.0)
            }
        else:
            return {
                'code': 200,
                'msg': res['msg']
            }

    # 更新所有人脸信息
    def update_face(self):
        """
               查询卡号
               :return:
               """
        for i in range(1, 13):
            access_token_obj = self.get_access_token()
            access_token = access_token_obj['data']['access_token']
            headers = {
                'Content-Type': 'application/json',
                'access_token': access_token
            }
            print('i=', i)
            content = {
                "pageSize": 1000,
                "pageNo": i
            }
            res = requests.post(headers=headers,
                                url=self.host + ':' + self.port + '/' + self.artemis + '/api/resource/v2/person/personList',
                                json=content, verify=False)
            employee_list = json.loads(res.content.decode('utf-8'))
            for employee_info in employee_list['data']['list']:
                print(employee_info['jobNo'])
                if get_photo(employee_info['jobNo']):
                    try:
                        if os.path.getsize("static/hikPhotos/photos/%s.jpg" % employee_info[
                            'jobNo']) / 1024 > 200 or os.path.getsize(
                            "static/hikPhotos/photos/%s.jpg" % employee_info['jobNo']) / 1024 < 10:
                            image = cv2.imread("static/hikPhotos/photos/%s.jpg" % employee_info['jobNo'])
                            height, width = image.shape[0], image.shape[1]
                            scale = os.path.getsize(
                                "static/hikPhotos/photos/%s.jpg" % employee_info['jobNo']) / 1024 / 200
                            image_resize = cv2.resize(image, (round(width / scale), round(height / scale)))
                            cv2.imwrite("static/hikPhotos/photos/%s.jpg" % employee_info['jobNo'],
                                        image_resize, [cv2.IMWRITE_JPEG_QUALITY, 80])

                        try:
                            with open("static/hikPhotos/photos/%s.jpg" % employee_info['jobNo'],
                                      "rb") as f:  # 转为二进制格式
                                base64_data = base64.b64encode(f.read()).decode('utf-8')  # 使用base64进行加密
                        except Exception as e:
                            print(e)
                            base64_data = ''
                    except Exception as e:
                        print(e)
                        base64_data = ''
                else:
                    base64_data = ''
                if 'personPhoto' in employee_info:
                    content = {
                        "faceId": employee_info['personPhoto'][0]['personPhotoIndexCode'],
                        "faceData": base64_data
                    }
                    dd = requests.post(headers=headers,
                                       url=self.host + ':' + self.port + '/' + self.artemis + '/api/resource/v1/face/single/update',
                                       json=content, verify=False)
                    res_data = json.loads(dd.content.decode('utf-8'))
                    print(res_data)
                    if res_data['msg'] == 'success':
                        self.ehr.update(update_zongbu_face_status(employee_info['jobNo']))
        return 1

    def temp(self):
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        sql = """
                select code  from T_HR_Employee where EmployeeStatusID = 1 and zongbu_photo is NULL        """
        employee_obj = self.ehr.select(sql)
        for employee_info in employee_obj:
            person_face_id = self.search_person_by_code(employee_info['code'])
            if person_face_id:
                print(employee_info['code'])
                if get_photo(employee_info['code']):
                    try:
                        if os.path.getsize("static/hikPhotos/photos/%s.jpg" % employee_info[
                            'code']) / 1024 > 200 or os.path.getsize(
                            "static/hikPhotos/photos/%s.jpg" % employee_info['code']) / 1024 < 10:
                            image = cv2.imread("static/hikPhotos/photos/%s.jpg" % employee_info['code'])
                            height, width = image.shape[0], image.shape[1]
                            scale = os.path.getsize(
                                "static/hikPhotos/photos/%s.jpg" % employee_info['code']) / 1024 / 200
                            image_resize = cv2.resize(image, (round(width / scale), round(height / scale)))
                            cv2.imwrite("static/hikPhotos/photos/%s.jpg" % employee_info['code'],
                                        image_resize, [cv2.IMWRITE_JPEG_QUALITY, 80])

                        try:
                            with open("static/hikPhotos/photos/%s.jpg" % employee_info['code'],
                                      "rb") as f:  # 转为二进制格式
                                base64_data = base64.b64encode(f.read()).decode('utf-8')  # 使用base64进行加密
                        except Exception as e:
                            print(e)
                            base64_data = ''
                    except Exception as e:
                        print(e)
                        base64_data = ''
                else:
                    base64_data = ''
                content = {
                    "faceId": person_face_id,
                    "faceData": base64_data
                }
                dd = requests.post(headers=headers,
                                   url=self.host + ':' + self.port + '/' + self.artemis + '/api/resource/v1/face/single/update',
                                   json=content, verify=False)
                res_data = json.loads(dd.content.decode('utf-8'))
                if res_data['msg'] == 'success':
                    self.ehr.update(update_zongbu_face_status(employee_info['code']))

    def search_person_by_code2(self, code):
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        content = {
            "paramName": "jobNo",
            "paramValue": [
                code
            ]
        }
        res = requests.post(headers=headers,
                            url=self.host + ':' + self.port + '/' + self.artemis + self.search_person_by_code_url,
                            json=content, verify=False)
        if len(json.loads(res.content.decode('utf-8'))['data']['list']) > 0 and len(
                json.loads(res.content.decode('utf-8'))['data']['list'][0]['personPhoto']) > 0:
            if 'personPhotoIndexCode' in json.loads(res.content.decode('utf-8'))['data']['list'][0]['personPhoto'][0]:
                return json.loads(res.content.decode('utf-8'))['data']['list'][0]['personPhoto'][0][
                    'personPhotoIndexCode']
        else:
            return False

    # 修改个人的照片
    def update_single_person_face(self, file_path, code):
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        person_face_id = self.search_person_by_code2(code)
        try:
            # if os.path.getsize(file_path) / 1024 > 200 or os.path.getsize(file_path) / 1024 < 10:
            #     image = cv2.imread(file_path)
            #     height, width = image.shape[0], image.shape[1]
            #     scale = os.path.getsize(file_path) / 1024 / 200
            #     image_resize = cv2.resize(image, (round(width / scale), round(height / scale)))
            #     cv2.imwrite(file_path, image_resize, [cv2.IMWRITE_JPEG_QUALITY, 80])
            try:
                with open(file_path, "rb") as f:
                    base64_data = base64.b64encode(f.read()).decode('utf-8')
            except Exception as e:
                print("1075行", e)
                return {
                    "code": 200,
                    "msg": "照片解码失败！"
                }

        except Exception as e:
            print("1080行", e)
            return {
                "code": 200,
                "msg": "照片解析失败！"
            }

        content = {
            "faceId": person_face_id,
            "faceData": base64_data
        }
        dd = requests.post(headers=headers,
                           url=self.host + ':' + self.port + '/' + self.artemis + '/api/resource/v1/face/single/update',
                           json=content, verify=False)
        res_data = json.loads(dd.content.decode('utf-8'))
        if res_data['msg'] == 'success':
            self.ehr.update(update_zongbu_face_status(code))

        return res_data

    def add_single_picture_by_code(self, file_path, code):
        method = "POST"
        t = time.time()
        nowTime = lambda: int(round(t * 1000))
        timestamp = nowTime()
        timestamp = str(timestamp)
        # uuid
        nonce = str(uuid.uuid1())
        message = str(
            method + '\n*/*\napplication/json\nx-ca-key:' + self.appKey + '\nx-ca-nonce:' + nonce + '\nx-ca-timestamp:' + timestamp + '\n/' + self.artemis + self.add_picture_by_code_url).encode(
            'utf-8')
        signature = base64.b64encode(
            hmac.new(self.appSecret.encode('utf-8'), message, digestmod=hashlib.sha256).digest())
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'X-Ca-timestamp': timestamp,
            'X-Ca-Key': self.appKey,
            'X-Ca-nonce': nonce,
            'X-Ca-Signature': signature,
            'X-Ca-Signature-Headers': 'x-ca-key,x-ca-nonce,x-ca-timestamp'
        }
        try:
            if os.path.getsize(file_path) / 1024 > 200 or os.path.getsize(file_path) / 1024 < 10:
                image = cv2.imread(file_path)
                height, width = image.shape[0], image.shape[1]
                scale = os.path.getsize(file_path) / 1024 / 200
                image_resize = cv2.resize(image, (round(width / scale), round(height / scale)))
                cv2.imwrite(file_path, image_resize, [cv2.IMWRITE_JPEG_QUALITY, 80])
            try:
                with open(file_path, "rb") as f:
                    base64_data = base64.b64encode(f.read()).decode('utf-8')
            except Exception as e:
                print("1075行", e)
                return {
                    "code": 200,
                    "msg": "照片解码失败！"
                }

        except Exception as e:
            print("1080行", e)
            return {
                "code": 200,
                "msg": "照片解析失败！"
            }
        content = {
            "personId": code,
            "faceData": base64_data
        }
        res = requests.post(headers=headers,
                            url=self.host + ':' + self.port + '/' + self.artemis + self.add_picture_by_code_url,
                            json=content, verify=False)
        res_data = json.loads(res.content.decode('utf-8'))
        # 如果返回信息带有faceId，则更新到ehr里
        if res_data['data'] is not None:
            if res_data['data']['faceId'] is not None:
                self.ehr.update(update_zongbu_face_status(code))
                self.ehr.update(update_jianhuerqi_face_status(code))
        # elif res_data['code'] == '0x00072001':
        #     self.ehr.update(update_zongbu_face_status(code))
        #     self.ehr.update(update_jianhuerqi_face_status(code))
        #     res_data = {
        #         "code": 200,
        #         "msg": res_data['msg']
        #     }
        return res_data

    def test_photo(self, file_path):
        """
        人脸质量测试
        :return:
        """
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        with open(file_path, "rb") as f:  # 转为二进制格式
            base64_data = base64.b64encode(f.read()).decode('utf-8')  # 使用base64进行加密
        content = {
            "facePicBinaryData": base64_data
        }
        res = requests.post(headers=headers, url=self.host + ':' + self.port + '/' + self.artemis + self.test_photo_url,
                            json=content, verify=False)
        res = json.loads(res.content)
        # 如果图像检测不通过，则返回
        if res['code'] != "0":
            res = {
                "code": 400,
                "msg": res['msg']
            }

        else:
            res = {
                "code": 200,
                "msg": res['msg']
            }
        return res

    def update_one_face(self, file, code):
        path = save_file(file, code)
        if path == 0:
            return {
                "code": 200,
                "msg": "图像不符合，请重新选择后上传"
            }
        result = self.test_photo(path)
        if result['code'] == 400:
            res = {
                "code": 400,
                "msg": "照片不合格，请重新选择",
                "error": result['msg']
            }
            return res
        res = self.search_person_by_code2(code)
        if res:
            # 照片存在，修改
            result = self.update_single_person_face(path, code)
            if result['code'] == "0":
                result = {
                    "code": 200,
                    "msg": "照片更新成功"
                }
        else:
            # 照片不存在，新增
            result = self.add_single_picture_by_code(path, code)
            if result['code'] == "0":
                result = {
                    "code": 200,
                    "msg": "照片上传成功"
                }

        return result

    def get_one_person_info_v2(self, personID):
        access_token_obj = self.get_access_token()
        access_token = access_token_obj['data']['access_token']
        headers = {
            'Content-Type': 'application/json',
            'access_token': access_token
        }
        content = {
            "personIds": personID,
            "pageNo": 1,
            "pageSize": 10,
        }
        res = requests.post(headers=headers,
                            url=self.host + ':' + self.port + '/' + self.artemis + self.select_person_list_v2,
                            json=content, verify=False)
        employee_list = json.loads(res.content.decode('utf-8'))
        return employee_list

    def get_face_pic(self, code):
        # 查找person的唯一标示ID
        url = "https://218.92.177.146:19444"
        personID = self.search_person_by_code(code)
        # 通过person的表示找到个人信息，需要照片的秘钥
        person_info = self.get_one_person_info_v2(personID)
        # 查找失败
        if person_info['code'] != "0":
            res = {
                "code": 400,
                "msg": "个人信息获取失败",
                "url": '/'
            }
            return res
        if person_info['data']['total'] != 1:
            res = {
                "code": 400,
                "msg": "身份信息不唯一",
                "url": '/'
            }
            return res
        url += person_info['data']['list'][0]['personPhoto'][0]['picUri']
        res = {
            "code": 200,
            "msg": "照片获取成功",
            "url": url
        }
        return res
