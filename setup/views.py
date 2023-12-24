from rest_framework.viewsets import GenericViewSet
from setup.userClass.userClass import userMgmt, picMgmt,baseMgmt


# Create your views here.

class AdminUserMgmt(GenericViewSet):

    def add_user(self, request):
        obj = userMgmt(request, "add_user")
        res = obj.center_meth()
        return res

    def update_user(self, request):
        obj = userMgmt(request, "update_user")
        res = obj.center_meth()
        return res

    def get_list(self, request):
        obj = userMgmt(request, "get_list")
        res = obj.center_meth()
        return res

    def delete_user(self, request):
        obj = userMgmt(request, "delete_user")
        res = obj.center_meth()
        return res


class PicManageView(GenericViewSet):
    def get_pic(self, request):
        obj = picMgmt(request, "get_pic")
        res = obj.center_meth()
        # print("res",res)
        return res

    def add_pic(self, request):
        obj = picMgmt(request, "add_pic")
        res = obj.center_meth()

        return res

    def delete_pic(self, request):
        obj = picMgmt(request, "delete_pic")
        res = obj.center_meth()
        return res

class BaseManageView(GenericViewSet):
    def get_base(self, request):
        obj =baseMgmt(request, "get_base")
        res = obj.center_meth()
        return res
    def add_base(self, request):
        obj = baseMgmt(request, "add_base")
        res = obj.center_meth()
        return res
    def delete_base(self, request):
        obj = baseMgmt(request, "delete_base")
        res = obj.center_meth()
        return res
    def patch_base(self, request):
        obj = baseMgmt(request, "patch_base")
        res = obj.center_meth()
        return res