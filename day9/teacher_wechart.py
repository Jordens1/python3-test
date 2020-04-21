import urllib.request
import json
import sys
import time

# 此为企业的ID号
CorpID = 'wwf463042e4fcc909e'

# 应用的ID
Agentid = 1000003

# 认证信息，企业ID+认证信息可获取tokent，获取之后向此tokent发送内容
Secret = 'FCF6kq1cMjxzwe5lpnBQTE03Q3D9YPEWdABjqiF9gSA'

localtime = time.strftime("[%H:%M:%S]", time.localtime())
class Tencent(object):
    def __init__(self,user,title,msg):
        # 格式化输出内容：标题+内容
        self.MSG = localtime+title+msg
        self.User = user
        self.url = 'https://qyapi.weixin.qq.com'
        self.send_msg = json.dumps({
            'touser': self.User,
            'msgtype': 'text',
            'agentid': Agentid,
            'text': {'content': self.MSG},
            'safe': 0
        })
    # 获取tokent
    def get_token(self):
        token_url = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (self.url, CorpID, Secret)
        token = json.loads(urllib.request.urlopen(token_url).read())['access_token']
        return token

    # 发送信息
    def send_message(self):
        send_url = r'%s/cgi-bin/message/send?access_token=%s' % (self.url,self.get_token())

        respone = urllib.request.urlopen(url=send_url, data=self.send_msg.encode('utf-8')).read()
        x = json.loads(respone.decode())['errcode']
        if x == 0:
            print ('Succesfully')
        else:
            print ('Failed')

if __name__ == '__main__':
    # 创建对象
    send_obj = Tencent('WangMingYu','test','hello world')
    # 调用发送函数
    send_obj.send_message()