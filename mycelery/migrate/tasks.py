

from mycelery.main import celery_app
import logging,time
log=logging.getLogger('django')
@celery_app.task
def send_sms(mobile):
    print("想手机号{}发送短信成功".format(mobile))
    time.sleep(5)
    return 'send_sms OK'

@celery_app.task
def send_sms2(mobile):
    print("想手机号{}发送短信成功2".format(mobile))
    time.sleep(5)
    return 'send_sms2 OK'
