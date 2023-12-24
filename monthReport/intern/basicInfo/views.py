from monthReport.intern.basicInfo.methods import *
from rest_framework.views import APIView


def upload_basic_info(request):
    zgz = internBasicInfoClass(request)
    zgz.add_meth()
    res = zgz.method_center('upload_basic_info')
    return res


def get_basic_info(request):
    zgz = internBasicInfoClass(request)
    zgz.add_meth()
    res = zgz.method_center('get_basic_info')
    return res


class basicInfo(APIView):
    def __init__(self):
        self.zgz = internBasicInfoClass(None)
        self.zgz.add_meth()

    def post(self, request):
        """
        查询
        :param request:
        :return:
        """
        self.zgz.request = request
        return self.zgz.method_center('search')

    def put(self, request):
        """
        新增
        检测创建重复放在前端，使用查询完成
        :param request:
        :return:
        """
        self.zgz.request = request
        return self.zgz.method_center('create')

    def patch(self, request):
        """
        修改
        :param request:
        :return:
        """
        self.zgz.request = request
        return self.zgz.method_center('update')

    def delete(self, request):
        """
        删除
        :param request:
        :return:
        """
        self.zgz.request = request
        return self.zgz.method_center('delete')


class fileInfo(APIView):
    def __init__(self):
        self.obj = internBasicInfoFileClass(None)
        self.obj.add_meth()

    # 下载
    def post(self, request):
        self.obj.request = request
        return self.obj.method_center('download')

    # 上传
    def put(self, request):
        self.obj.request = request
        return self.obj.method_center('upload')
