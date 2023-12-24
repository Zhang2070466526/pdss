from wx.me.meClass import *
from rest_framework.decorators import api_view


# 获取待审批信息
@api_view(['POST'])
def get_me_page(request):
    me = Me(request)
    res = me.method_center('get_me_page')
    return res


# 获取待审批信息
@api_view(['POST'])
def get_notice_info(request):
    me = Me(request)
    res = me.method_center('get_notice_info')
    return res


# 删除审批信息
@api_view(['POST'])
def delete_notice_info(request):
    me = Me(request)
    res = me.method_center('delete_notice_info')
    return res
