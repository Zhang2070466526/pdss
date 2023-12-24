import json
from django.http import HttpResponse

from auther.methods import Login
from utils.del_token import DelToken
from django.contrib.auth.hashers import make_password, check_password
from utils.check_token import CheckToken
from auther.models import *
from setup.models import *


def admin_login(request):
    # print(request.body)
    request_data = json.loads(request.body)
    new_admin = Login()
    admin = new_admin.check_admin_info(request_data['username'], request_data['password'])
    # print(admin)
    return HttpResponse(json.dumps(admin))


def admin_logout(request):
    token = request.headers['Authorization']
    del_token = DelToken()
    delete_token = del_token.clear_token(token)  # 注销后删除redis中的token
    if delete_token == True:
        return_data = {'code': 200, "msg": "Token清除成功", 'hidden': True}
        return HttpResponse(json.dumps(return_data))


def admin_sidebar(request):
    token = request.headers['Authorization']
    new_admin = Login()
    admin_username = new_admin.get_sidebar(token)
    return HttpResponse(json.dumps(admin_username))

def admin_getnav(request):
    token = request.headers['Authorization']
    new_admin = Login()
    admin_username = new_admin.get_nav(token)
    return HttpResponse(json.dumps(admin_username))
def admin_getsidebar(request):   #最新的获取侧边栏
    token = request.headers['Authorization']
    new_admin = Login()
    admin_username = new_admin.get_sidebat_new(token)
    return HttpResponse(json.dumps(admin_username))

def admin_editpwd(request):
    return_data = {
        'code': 200, "msg": "密码修改成功"
    }
    request_data = json.loads(request.body)
    # print(request.check_token)
    pwd = AdminUser.objects.filter(id=request.check_token).values_list('password', flat=True)  # 数据库中加密后的密码
    if check_password(request_data['originalPassword'], pwd[0]):  # 密码一样
        if request_data['newPassword'] != request_data['newPassword2']:
            return_data = {
                'code': 400, "msg": "两次密码不一致，修改失败!"
            }
        else:
            # print("+++++++++++++")
            password_encrypt = make_password(request_data['newPassword'])  # 加密密碼
            AdminUser.objects.filter(id=request.check_token).update(password=password_encrypt)
            # return_data = {
            #     'code': 200, "msg": "修改成功!"
            # }
    else:  # 旧密码和数据库中的密码不一样
        return_data = {
            'code': 400, "msg": "不是原有密码，修改失败!"
        }
    # print(return_data)
    return HttpResponse(json.dumps(return_data))


def admin_picbk(request):
    obj = PicManage.objects.filter(pic_status=True).order_by('-create_time').values_list('url', flat=True)
    index = 1
    data = []
    for i in obj:
        d = {}
        d['index'] = index
        d['url'] = i
        index += 1
        data.append(d)
    # print(data)
    return_data = {'picList': data}
    return HttpResponse(json.dumps(return_data))
