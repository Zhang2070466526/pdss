from django.core.cache import cache


class DelToken():
    def clear_token(self, token):
        cache.delete(token)
        return True
