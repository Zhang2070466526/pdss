# authentication/utils.py
import random
import string
import redis
from django.conf import settings
from django.http import JsonResponse
import redis,json
from redis import ConnectionPool

# 连接到 Redis
redis_client_connection = redis.StrictRedis(
    host='localhost',
    port=6379,
    db=1,
    password="8023",
    # connection_pool=settings.REDIS_POOL,#连接池
    decode_responses=True  #设置为 True，将返回的数据解码为字符串
)


def save_data(user_id, token):   #保存数据到redis
    redis_client_connection.set(token, user_id)
    redis_client_connection.expire(token, 10*365*24*60 * 60 * 1)#单位是秒   10年


def save_list_data_to_redis(key, data): #列表内嵌字典   覆盖
    # serialized_data = [json.dumps(item) for item in data] #字典转字符串  (时间不能序列化)
    serialized_data = [str(item) for item in data]  # 字典转字符串
    # print(serialized_data)
    if redis_client_connection.exists(key):    #存在数据 删除
        redis_client_connection.delete(key)
    if serialized_data==[]:
        serialized_data=[0,0]
    redis_client_connection.rpush(key, *serialized_data) #无数据 新增


def get_list_data_from_redis(key):  #取出数据
    import json
    import datetime
    request_data = redis_client_connection.lrange(key, 0, -1)   #将范围指定为“0”到“-1”来检索列表中的所有元素，其中包括所有元素。
    # response_data = [eval(item) for item in request_data]  # 列表推导 时间格式会有问题
    # response_data = [json.loads(item) for item in request_data]   #格式有问题
    response_data = []
    for item in request_data:
        # print(type(item),item)
        try:
            dict = eval(item)
        except:
            dict=item
        response_data.append(dict)
    return response_data

'''
redis-server 启动服务

redis-cli 启动客户端
config set requirepass 8023 设置密码
'''