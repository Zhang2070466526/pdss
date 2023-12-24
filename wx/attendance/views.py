from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ViewSet, GenericViewSet

from rest_framework.decorators import APIView
from wx.attendance.attendanceClass import *


class Attendance(APIView):
    def post(self, request):
        print(request.data)
        req_data = request.data
        attendance_data = AttendanceInfo()
        return JsonResponse(attendance_data.get_daliy_data(req_data['code'], req_data['month'], req_data['language']))
        # return JsonResponse(attendance_data.get_daliy_data(req_data['code'], req_data['month']))
