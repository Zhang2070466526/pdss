from rest_framework.views import APIView
from .methods import *


class basicDepartInfo(ViewBasicTemplate):
    def __init__(self):
        super().__init__(internDepartInfoClass)
        # self.obj = internDepartInfoClass(None)
        # self.obj.add_meth()


class fileDepartInfo(ViewBasicTemplate):
    def __init__(self):
        super().__init__(internDepartFileInfoClass)
        # self.obj = internDepartInfoClass(None)
        # self.obj.add_meth()

# class fileDepartInfo(APIView):
#     def __init__(self):
#         self.obj = internBasicInfoFileClass(None)
#         self.obj.add_meth()
#
#     # 下载
#     def post(self, request):
#         self.obj.request = request
#         return self.obj.method_center('download')
#
#     # 上传
#     def put(self, request):
#         self.obj.request = request
#         return self.obj.method_center('upload')
