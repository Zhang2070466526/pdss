import time

from django.core import signing
import hashlib
from django.core.cache import cache


class CreateToken():
    def __init__(self, KEY):
        self.HEADER = {'typ': 'JWP', 'alg': 'default'}
        self.TIME_OUT = 1440 * 60  # 30*60 30分钟
        self.KEY = KEY

    def encrypt(self, obj):
        """加密"""
        value = signing.dumps(obj)
        value = signing.b64_encode(value.encode()).decode()
        return value

    def create_token(self):
        """生成token信息"""
        # 1. 加密头信息
        header = self.encrypt(self.HEADER)
        # 2. 构造Payload
        payload = {"username": self.KEY, "iat": time.time()}
        payload = self.encrypt(payload)
        # 3. 生成签名
        md5 = hashlib.md5()
        md5.update(("%s.%s" % (header, payload)).encode())
        signature = md5.hexdigest()
        token = "%s.%s.%s" % (header, payload, signature)
        # 存储到缓存中
        cache.set(token, self.KEY, self.TIME_OUT)
        return token
