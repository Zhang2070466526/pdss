from wx.myInfo.myinfoClass import Info
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class InfoView(APIView):

    def get(self, request):
        info = Info(request)
        res = info.method_center('get_info')
        return res

    def post(self, request):
        info = Info(request)
        res = info.method_center('commit_edit')
        return res


def edit_info(request):
    info = Info(request)
    res = info.method_center('edit_info')
    return res


@api_view(['POST'])
def get_info(request):
    info = Info(request)
    res = info.method_center('get_info')
    return res


@api_view(['POST'])
def drop_down_menu(request):
    info = Info(request)
    res = info.method_center('drop_down_menu')
    return res


@api_view(['POST'])
def upload_menu(request):
    info = Info(request)
    res = info.method_center('upload_menu')
    return res


@api_view(['POST'])
def get_index_bar(request):
    info = Info(request)
    res = info.method_center('get_index_bar')
    return res


# 获取待审批信息
@api_view(['POST'])
def get_approve_list(request):
    info = Info(request)
    res = info.method_center('get_approve_list')
    return res


# 获取待审批信息
@api_view(['POST'])
def edit_approve_list(request):
    info = Info(request)
    res = info.method_center('edit_approve_list')
    return res
