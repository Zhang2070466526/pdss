from wx.myArchives.archivesClass import *


#
def get_file_info(request):
    arc = Archives(request)
    res = arc.method_center('get_file_info')
    return res


def get_file_info_page(request):
    arc = Archives(request)
    res = arc.method_center('get_file_info_page')
    return res


def upload_file_apply(request):
    arc = Archives(request)
    res = arc.method_center('upload_file_apply')
    return res
