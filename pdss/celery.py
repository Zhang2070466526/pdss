
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from pdss import settings

# 设置环境变量，以便在项目中使用 settings 模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pdss.settings')

# # 创建 Celery 实例
# app = Celery('pdss')
#
# # 配置 Celery 使用 Django settings
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# # 自动加载异步任务定义
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#
# # 定义 Redis 连接信息
# # app.conf.broker_url = 'redis://:8023@localhost:6379/2'
# app.conf.broker_url = 'redis://:372169zw..@172.16.6.89:6379/2'


import os
from celery import Celery

# 设置默认的Django settings模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pdss.settings')

app = Celery('pdss')

# 使用Django配置
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动加载任务
app.autodiscover_tasks()

