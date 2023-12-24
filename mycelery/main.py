from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
# 设置Celery默认的Django settings模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pdss.settings')

# 创建Celery实例对象
celery_app = Celery('pdss')

# 使用Django配置
celery_app.config_from_object('mycelery.config') #指定配置文件的位置,配置Celery，使用Redis作为消息队列
celery_app.conf.broker_connection_retry = True
# 自动发现异步任务
celery_app.autodiscover_tasks('mycelery.migrate')#自动从settings的配置installed_apps的应用目录下加载task.py

