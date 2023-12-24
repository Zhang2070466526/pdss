from rest_framework.generics import GenericAPIView

from employeePersonnel.archives.archive import *
from rest_framework.views import APIView
import calendar
from datetime import date, datetime, timedelta, time
from employeePersonnel.tasks import *
from datetime import time


def get_week_begin_end(flag=0):  # 跟据flag获取不同周的周一00:00:00和周日的23:59:59   flag=0默认即这周 flag=1即上周
    # 获取当前日期
    today = date.today()
    if flag == 1:
        days_until_monday = today.weekday() + 7 * flag  # 计算上周的周一
    else:
        days_until_monday = today.weekday()  # 计算这周的周一
    monday = today - timedelta(days=days_until_monday)
    days_until_sunday = 6 - days_until_monday  # 计算日期差值以获取周日
    sunday = today + timedelta(days=days_until_sunday)
    begin_time = time(0, 0, 0)  # 创建时间对象并设置时间为00:00:00
    end_time = time(23, 59, 59)  # 创建时间对象并设置时间为23:59:59
    begin_date = datetime.combine(monday, begin_time)
    end_date = datetime.combine(sunday, end_time)
    return begin_date, end_date


def get_month_begin_end(flag=0):  # 跟据flag获取不同月的第一天00:00:00和最后一天的的23:59:59   flag=0默认即这月 flag=1即上月,2即下月
    today = datetime.today()
    if flag == 1:
        year, month = today.year, today.month - 1
        if month == 0:
            year, month = year - 1, 12
    elif flag == 0:
        year, month = today.year, today.month
    elif flag == 2:
        year, month = today.year, today.month + 1
        if month == 13:
            year, month = year + 1, 1
    else:
        raise ValueError("错误")
    _, num_days = calendar.monthrange(year, month)
    first_day = datetime(year, month, 1)
    last_day = datetime(year, month, num_days)
    begin_date = datetime.combine(first_day, time(0, 0, 0))
    end_date = datetime.combine(last_day, time(23, 59, 59))
    return begin_date, end_date


# 触发异步任务
def test_celery(request):
    print('启动')
    begin_week, end_week = get_week_begin_end()  # 这周的
    begin_month, end_month = get_month_begin_end()  # 这个月的
    result = migrate_data_week.delay(begin_week, end_week)
    result = migrate_data_month.delay(begin_month, end_month)
    # task_result = result.get()
    # print(task_result)

    print('111111111111111111111111')
    return JsonResponse({'test': '数据同步启动'})


'''
    celery -A mycelery.main worker --loglevel=info
    celery -A pdss worker --pool=solo -l info
'''


def history_basic_sync_week(request):
    begin_week, end_week = get_week_begin_end()  # 这周的






    # result = migrate_data_week.delay(begin_week, end_week)
    # return JsonResponse({'msg': '周数据同步启动'})


def history_basic_sync_month(request):
    begin_month, end_month = get_month_begin_end()  # 这个月的
    result = migrate_data_month.delay(begin_month, end_month)
    return JsonResponse({'msg': '月数据同步启动'})

def test_threading_file(request):
    import threading

    uploaded_files = request.FILES.getlist('file')
    # print(uploaded_files)
    import time
    def save_file_to_disk(uploaded_file):
        file_name = uploaded_file.name
        file_content = uploaded_file.read()
        print(file_name)
        # print(file_content)
        time.sleep(5)

        file_url, file_name, suffix = createPath(uploaded_file, str('wwwwww'),
                                                      str(random.random())[-5:] + '_签到表')
        saveFile(file_url, uploaded_file)  # 保存文件

        with open(file_name, 'wb') as file:
            file.write(file_content)
    #     file_model = FileModel(name=file_name)
    #     file_model.save()
    #
    threads = []
    for uploaded_file in uploaded_files:
        thread = threading.Thread(target=save_file_to_disk, args=(uploaded_file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return JsonResponse({'msg': '月数据同步启动'})