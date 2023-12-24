from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
from competeRestrictions.restrictions.restrictionsClass import *


class RestrictionsView(GenericViewSet):
    def get_list(self, request):
        obj = infoMgmt(request, "get_list")
        res = obj.meth_center()
        return res

    def get_upload(self, request):
        obj = infoMgmt(request, "get_upload")
        res = obj.meth_center()
        return res

    def patch_data(self, request):
        obj = infoMgmt(request, "patch_data")
        res = obj.meth_center()
        return res

    def delete_data(self, request):
        obj = infoMgmt(request, "delete_data")
        res = obj.meth_center()
        return res

    def download_file(self, request):
        obj = infoMgmt(request, "download_file")
        res = obj.meth_center()
        return res
    def delete_other_file(self, request):
        obj = infoMgmt(request, "delete_other_file")
        res = obj.meth_center()
        return res


    def get_systemUpload(self, request):
        obj = infoMgmt(request, "get_systemUpload")
        res = obj.meth_center()
        return res
    def verify(self, request):
        obj = infoMgmt(request, "verify")
        res = obj.meth_center()
        return res
    # def get_location(self, request):
    #     obj = infoMgmt(request, "get_location")
    #     res = obj.meth_center()
    #     return res
    def get_location(self,request):
        longitude = request.GET.get("longitude", None)  # 经度
        latitude = request.GET.get("latitude", None)  # 纬度
        if longitude is None or latitude is None:
            return HttpResponse('')
        url = "https://restapi.amap.com/v3/geocode/regeo?output=json&location={0},{1}&key=5ac9f355f8489931303f20f73fd05ed7&radius=50&extensions=all&batch=false&extensions=base".format(
            longitude, latitude)
        resp = requests.get(url).content
        resp = json.loads(resp)
        return HttpResponse(json.dumps(resp))

    def get_isExpiration(self,request):
        obj = infoMgmt(request, "get_isExpiration")
        res = obj.meth_center()
        return res

    def post_annex_file(self,request):
        obj = infoMgmt(request, "post_annex_file")
        res = obj.meth_center()
        return res
    def delete_annex_file(self,request):
        obj = infoMgmt(request, "delete_annex_file")
        res = obj.meth_center()
        return res

    # def upload_other_file(self, request):
    #     obj = infoMgmt(request, "upload_other_file")
    #     res = obj.meth_center()
    #     return res