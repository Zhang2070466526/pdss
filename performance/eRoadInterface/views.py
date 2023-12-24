from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from auther.models import AdminUser
# Create your views here.
from utils.check_token import *
from performance.eRoadInterface.models import *
from rest_framework import status
import json
from django.http import JsonResponse
from datetime import datetime
from django.contrib.auth.hashers import check_password

from utils.create_token import CreateToken


class Push_Performance_Data_POST_RecordView(APIView):
    def post(self, request, **kwargs):
        new_token = CheckToken()
        try:
            check_token = new_token.check_token(request.headers['Authorization'])
        except:
            check_token = None
        return_data = {'code': status.HTTP_403_FORBIDDEN, "msg": '没有权限访问!'}
        if check_token:
            try:
                info_data=json.loads(request.body)['data'] #批量数据
                if len(info_data)==0:
                    return_data = {'code': status.HTTP_401_UNAUTHORIZED, "msg": '数据为空，无法推送!'}
                else:
                    for line in info_data:
                        if 'eroad_indicator_code' not in line.keys():
                            return_data = {'code': status.HTTP_404_NOT_FOUND, "msg": '指标代码缺失,无法推送'}
                            break
                        elif 'eroad_indicator_name' not in line.keys():
                            return_data = {'code': status.HTTP_404_NOT_FOUND, "msg": '指标名称缺失,无法推送'}
                            break
                        elif 'eroad_month' not in line.keys():
                            return_data = {'code': status.HTTP_404_NOT_FOUND, "msg": '月份缺失,无法推送'}
                            break
                        elif 'eroad_code' not in line.keys():
                            return_data = {'code': status.HTTP_404_NOT_FOUND, "msg": '提供人工号缺失,无法推送'}
                            break
                        elif 'eroad_name' not in line.keys():
                            return_data = {'code': status.HTTP_404_NOT_FOUND, "msg": '提供人姓名缺失,无法推送'}
                            break
                        elif all(key in list(line.keys()) for key in ['eroad_indicator_code','eroad_indicator_name','eroad_month','eroad_code','eroad_name']):  #这5个参数都在里面
                            if type(line['eroad_month']) == str and len(line['eroad_month']) == 7:
                                params={
                                    'eroad_month':datetime.strptime(line['eroad_month'] + '-01', "%Y-%m-%d"),
                                    'eroad_create_id':check_token,
                                    'eroad_indicator_code':line['eroad_indicator_code'],
                                    'eroad_indicator_name':line['eroad_indicator_name'],
                                    'eroad_code': line['eroad_code'],
                                    'eroad_name': line['eroad_name'],
                                }
                                EroadInterface.objects.update_or_create(defaults=params,eroad_month=params['eroad_month'],eroad_indicator_code=params['eroad_indicator_code'])
                                return_data = {'code': status.HTTP_200_OK, "msg": '数据推送成功'}
                            else:
                                return_data = {'code': status.HTTP_401_UNAUTHORIZED, "msg": '日期格式错误，应为%Y-%m'}
                                break
                        else:
                            return_data = {'code': status.HTTP_401_UNAUTHORIZED, "msg": '未知错误'}
                            break
            except:
                return_data = {'code': status.HTTP_401_UNAUTHORIZED, "msg": '未知错误'}
        else:
            return_data = {'code': status.HTTP_403_FORBIDDEN, "msg": '没有权限访问!'}
        return JsonResponse(return_data)




class Create_Token_POST_RecordView(APIView):
    def post(self, request, **kwargs):
        info=json.loads(request.body)
        return_data={}

        if len(info) < 2 :
            if 'username' not in info.keys():
                return_data = {'code': status.HTTP_404_NOT_FOUND, "msg": '用户名缺失,token获取失败'}

            if 'password' not in info.keys():
                return_data = {'code': status.HTTP_404_NOT_FOUND, "msg": '密码缺失，token获取失败'}

        elif len(info)>=2 and 'username'in info.keys() and 'password' in info.keys():
            account = AdminUser.objects.filter(username=info['username'], is_used=True).first()
            if account:
                pwd_check = check_password(info['password'], account.password)
                if pwd_check == True:
                    admin_token = CreateToken(account.id)
                    set_token = admin_token.create_token()
                    return_data = {'code': status.HTTP_200_OK, "msg": 'token获取成功','token':set_token}
                else:
                    return_data = {'code': status.HTTP_401_UNAUTHORIZED, "msg": '密码错误,token获取失败'}
            else:
                return_data = {'code': status.HTTP_401_UNAUTHORIZED, "msg": '用户名错误,token获取失败'}
        else:
            return_data = {'code': status.HTTP_401_UNAUTHORIZED, "msg": '未知错误'}
        return JsonResponse(return_data)

