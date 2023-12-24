# import asyncio,time
#
#
# async def foo():
#     print("这是一个协程")
#
#     return "返回值"
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         print("开始运行协程")
#         coro = foo()
#         print("进入事件循环")
#
#         print('1')
#         time.sleep(5)
#         result = loop.run_until_complete(coro)
#         time.sleep(5)
#         print(f"run_until_complete可以获取协程的{result}，默认输出None")
#     finally:
#         print("关闭事件循环")
#         loop.close()


import json
from websocket import create_connection

# 1、建立连接
ws = create_connection("ws://8x.xxx.74.26:9088/pinter/imserver/1")

# 2、获取连接状态
print("获取连接状态：", ws.getstatus())

# 3、发送请求参数
# ws.send('hello')
params = '{"msgId":"admin","type":"match","from":"admin","to":"system"}'
ws.send(json.dumps(params))

# 4、获取返回结果
result = ws.recv()
print("接收结果：", result)

# 5、关闭连接
ws.close()











