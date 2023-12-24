import arrow
from rest_framework.status import HTTP_403_FORBIDDEN

from general.models import center_base
from hikCanteen.sql import month_meal_allowance_sql
from rayongAttendance.sql import *
from utils.check_token import CheckToken
from utils.pssqlConnect import connect_to_postgresql
from utils.sqlServerConnect import EhrConnect
from ..models import *
from django.db.models import Q


def get_attendance_data(startTime, endTime):
    conn = connect_to_postgresql()
    sql = select_Rayong_Attendance_sql(startTime, endTime)
    compare_data = {}
    data_obj = conn.select(sql)
    for i in data_obj:
        name = i[0] + "__" + i[2]
        if name in compare_data:
            diff = i[1] - compare_data[name][-1]
            if diff.total_seconds() > 60:
                compare_data[name].append(i[1])
        else:
            compare_data[name] = [i[1]]
    # for key,value in compare_data.items():
    #     print(key)
    #     print(value)
    return compare_data


def transform_data(data):  # sql转换函数
    if len(data) == 0:
        return []
    transformed_data = {}
    transformed_data['Code'] = data[0]['Code']
    transformed_data['Name'] = data[0]['Name']
    transformed_data['DepartmentCode'] = data[0]['DepartmentCode']
    transformed_data['DepartmentName'] = data[0]['DepartmentName']
    transformed_data['job_time'] = data[0]['job_time']

    time_intervals = []
    for item in data:
        start_time = item['startTime']
        end_time = item['endTime']
        time_intervals.append([start_time, end_time])
    transformed_data['time'] = time_intervals
    return transformed_data


def get_rayong_shift(code, startTime, endTime):
    ehr = EhrConnect()
    ehr.database = 'T9IMS_TG'
    rayong_shift = ehr.select(select_ehr_workNumber_sql(code, startTime, endTime))
    rayong_data = transform_data(rayong_shift)
    return rayong_data


# 生成详细的外出数据
def generate_data(request):
    startTime = request.GET.get("startTime", None)
    endTime = request.GET.get("endTime", None)
    if startTime is None or startTime == '' or endTime is None or endTime:
        endTime = arrow.now()
        startTime = endTime.shift(weeks=-1, days=-1)
        startTime = startTime.format("YYYY-MM-DD")
        endTime = endTime.format("YYYY-MM-DD")
    compare_data = get_attendance_data(startTime, endTime)
    try:
        for key, value in compare_data.items():
            key = key.split("__")
            res = get_rayong_shift(key[0], startTime + " 00:00:00", endTime + " 00:00:00")
            if len(res) != 0:
                kwargs = {
                    'pin': res['Code'],
                    'name': res['Name'],
                    'dept_code': res['DepartmentCode'],
                    'dept_name': res['DepartmentName'],
                    'job_time': res['job_time'],

                }
                obj = AttendanceDetailRecord.objects.update_or_create(defaults=kwargs, pin=res['Code'])[0]
                pk = obj.id
                for time in value:
                    for p in res['time']:
                        if p[0] <= time < p[1]:
                            AttendanceTimeRecord.objects.update_or_create(
                                defaults={"event_time": time, "person_id": pk, 'render_name': key[1]},
                                event_time=time, person_id=pk)
    except Exception as e:
        print(e)


def get_person_data(request):
    new_token = CheckToken()
    check_token = new_token.check_token(request.headers['Authorization'])
    if check_token is not None:
        kwargs = {
            "status": 1
        }
        args = ()
        searchName = request.GET.get("searchName", None)
        startTime = request.GET.get("startTime", None)
        endTime = request.GET.get("endTime", None)
        currentPage = request.GET.get("currentPage", None)
        pageSize = request.GET.get("pageSize", None)
        deptName = request.GET.get("deptName", None)
        dept_list = AttendanceDetailRecord.objects.filter(status=1).values("dept_name").distinct()
        dept_list = [{"label": i['dept_name'], "value": i['dept_name']} for i in dept_list]
        if currentPage == '' or currentPage is None:
            currentPage = 1
        else:
            currentPage = int(currentPage)
        if pageSize == '' or pageSize is None:
            pageSize = 25
        else:
            pageSize = int(pageSize)
        if searchName is not None and searchName != "":
            args += Q(person__name__contains=searchName) | Q(person__pin__contains=searchName),
        if startTime != "" and startTime is not None:
            kwargs["event_time__gte"] = startTime + " 00:00:00"
        if endTime != "" and endTime is not None:
            kwargs["event_time__lte"] = endTime + " 00:00:00"
        if deptName is not None and deptName != '':
            kwargs['person__dept_name'] = deptName
        obj = AttendanceTimeRecord.objects.filter(*args, **kwargs).values \
                  ("id", "person__name", "person__dept_name", "person__pin", "render_name", "event_time",
                   "person__job_time").order_by("-event_time")[
              (currentPage - 1) * pageSize:currentPage * pageSize]
        # print(kwargs)
        totalNumber = AttendanceTimeRecord.objects.filter(*args, **kwargs).count()
        for i in obj:
            i['event_time'] = arrow.get(i['event_time']).format("YYYY-MM-DD HH:mm:ss")
        columnList = [
            {
                "value": "姓名",
                "label": "person__name",
                "width": 200
            }, {
                "value": "部门",
                "label": "person__dept_name",
                "width": 300
            }, {
                "value": "工号",
                "label": "person__pin",
                "width": 120
            },
            {
                "value": "出门时间",
                "label": "event_time",
                "width": ""
            },
            {
                "value": "班制",
                "label": "person__job_time",
                "width": 120
            },
        ]
        return_data = {
            "code": 200,
            "msg": "信息返回成功",
            "data": {
                "tableList": [i for i in obj],
                "currentPage": currentPage,
                "pageSize": pageSize,
                "totalNumber": totalNumber,
                "columnList": columnList,
                "deptList": dept_list,
            }
        }
        return return_data
    else:
        return_data = {
            "code": HTTP_403_FORBIDDEN,
            "msg": "没有权限访问",
            'hidden': False
        }
        return return_data
