

import json,requests
class Enterprise_WeChat():
    def __init__(self):
        self.corpid = 'wwf09e52651b8a677d'    #企业id
        self.corpsecret ='V969I7dACKRAcFs2M-jr1sdfYb9rFKwwtC8gYyDganQ'  # 应用的凭证密钥

    def get_wx_access_token(self):    #获取access_token
        """
        :return: access_token
        """
        corpid =self.corpid
        corpsecret = self.corpsecret
        response = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(corpid, corpsecret))
        response_dict = json.loads(response.text)
        if response_dict['errcode'] == 0:
            access_token = response_dict['access_token']
        else:
            access_token = None
        return access_token

    def post_wx_message(self, access_token, **params):    #发送消息
        """
        :param access_token:     access_token
        :param params:  发送的参数,字典类型,例如{'code':'1010000407','name':'张优'}
        :return:
        """
        payload = {
            'touser': params['code'],
            'agentid': 1000073,
            'msgtype': 'text',
            'text': {
                'content': params['content']
            },
            'safe': 0,
            'enable_id_trans': 0,
            'enable_duplicate_check': 0
        }
        response = requests.post("https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token), json=payload)
        return response
