
from django.core.cache import cache


class CheckToken():
    # 检查token
    def check_token(self, token):
        last_token = cache.get(token)
        return last_token
