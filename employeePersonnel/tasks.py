# tasks.py
#定义异步任务
from celery import shared_task
from django.http import JsonResponse
from rest_framework import status

from employee.models import HrEmployee
from employeePersonnel.models import HrEmployeeHistory
from utils.save_data_to_redis import save_list_data_to_redis

'''

celery -A pdss flower

celery -A pdss worker --loglevel=info


'''



# from celery import shared_task
#
# @shared_task
# def my_async_task(arg1, arg2):
#     # 执行异步任务的代码
#     result = arg1 + arg2
#     return result
from mycelery.main import celery_app
from celery import shared_task
import logging,time
log=logging.getLogger('django')
# @celery_app.task
# @shared_task
# def send_sms(mobile):
#     print("想手机号{}发送短信成功".format(mobile))
#     time.sleep(5)
#     return 'send_sms OK'
#
# # @celery_app.task
# @shared_task
# def send_sms2(mobile):
#     print("想手机号{}发送短信成功2".format(mobile))
#     time.sleep(5)
#     return 'send_sms2 OK'
#
#
#





# @celery_app.task
@shared_task
def migrate_data_week(begin_date,end_date):
    """
    :param begin_date:
    :param end_date:
    :return:
    """
    print("{}-{}时间段周数据开始同步".format(begin_date,end_date))
    source_data = HrEmployee.objects.values()
    index=0
    for line in source_data:
        del line['id']
        line['employee_record_begin_time']=begin_date
        line['employee_record_end_time'] = end_date
        line['employee_record_type']='1'
        HrEmployeeHistory.objects.update_or_create(defaults=line,employee_record_begin_time=begin_date,employee_record_end_time=end_date,employee_record_type='1',employee_code=line['employee_code'],employee_name=line['employee_name'])
        index+=1
        # print(index)

    print('周数据同步',index)
    all_employee_data=list(HrEmployeeHistory.objects.filter(employee_record_begin_time=begin_date,employee_record_end_time=end_date,employee_record_type='1').values())

    save_list_data_to_redis('{}_{}_1'.format(begin_date,end_date),all_employee_data)  # 存储数据到redis中

    # hr_employee_history = [HrEmployee(**row) for row in source_data]
    # HrEmployeeHistory.objects.bulk_create(hr_employee_history)


    return_data = {
        "code": status.HTTP_200_OK,
        "msg": "同步成功"
    }
    # return JsonResponse(return_data)





    return '迁移成功'

@shared_task
def migrate_data_month(begin_date,end_date):
    """
    :param begin_date:
    :param end_date:
    :return:
    """
    print("{}-{}时间段月数据开始同步".format(begin_date, end_date))
    source_data = HrEmployee.objects.values()
    for line in source_data:
        del line['id']
        line['employee_record_begin_time'] = begin_date
        line['employee_record_end_time'] = end_date
        line['employee_record_type'] = '2'
        HrEmployeeHistory.objects.update_or_create(defaults=line,employee_record_begin_time=begin_date,employee_record_end_time=end_date,employee_record_type='2',employee_code=line['employee_code'],employee_name=line['employee_name'])
    all_employee_data=list(HrEmployeeHistory.objects.filter(employee_record_begin_time=begin_date,employee_record_end_time=end_date,employee_recprd_type='2').values())
    save_list_data_to_redis('{}_{}_2'.format(begin_date,end_date),all_employee_data)  # 存储数据到redis中


    return_data = {
        "code": status.HTTP_200_OK,
        "msg": "同步成功"
    }
    return '迁移成功'