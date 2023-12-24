from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from sendEmail.sendEmailMethod.sendClass import sendClass


# Create your views here.


class sendEmail(GenericViewSet):

    def get_dept(self, request):
        obj = sendClass(request, 'get_dept')
        res = obj.token_center_method()
        return res

    def post_person(self, request):
        obj = sendClass(request, 'post_person')
        res = obj.token_center_method()
        return res

    def add_dept(self, request):
        obj = sendClass(request, 'add_dept')
        res = obj.token_center_method()
        return res

    def del_data(self, request):
        obj = sendClass(request, 'del_data')
        res = obj.token_center_method()
        return res

    def patch_data(self, request):
        obj = sendClass(request, 'patch_data')
        res = obj.token_center_method()
        return res

    def get_attendance_list(self, request):
        obj = sendClass(request, 'get_attendance_list')
        res = obj.token_center_method()
        return res

    def get_dimissweek_list(self, request):
        obj = sendClass(request, 'get_dimissweek_list')
        res = obj.token_center_method()
        return res

    def get_attendance_data(self, request):
        obj = sendClass(request, 'get_everyWeek_attendance_data')
        res = obj.center_method()
        return res

    def get_everyday_leave_data(self, request):
        obj = sendClass(request, 'get_everyday_leave_data')
        res = obj.center_method()
        return res

    def get_everyweek_leave_data(self, request):
        obj = sendClass(request, 'get_everyWeek_leave_data')
        res = obj.center_method()
        return res

    def delete_one_dept_apt(self, request):
        obj = sendClass(request, 'delete_one_dept_apt')
        res = obj.center_method()
        return res

    def test_send(self, request):
        obj = sendClass(request, 'test_send')
        res = obj.center_method()
        return res

