from wx.login.loginClass import Login


def login_judge(request):
    login = Login(request)
    res = login.method_center('login_judge')
    return res


def get_login_page(request):
    login = Login(request)
    res = login.method_center('get_login_page')
    return res
