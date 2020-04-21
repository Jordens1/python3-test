#/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib.request, urllib.parse

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
word = input("输入")
date = {"from": "en",
    "to": "zh",
    "query": word,
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": "814534.560887",
    "token": "884f2f81d45d10f65dbf088febd77d08",
    "domain": "common"}

date = urllib.parse.urlencode(date)
headers = {"authority": "fanyi.baidu.com",
"method": "POST",
"path": "/v2transapi?from=en&to=zh",
"scheme": "https",
"accept": "*/*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
#"content-length": "135",
"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
"cookie": "BAIDUID=4AF31140B675845AB1E3EAEF36CABCC4:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=noxVWZqZmhUaW1YSTVNQkZGSE5MY0p5aDRKWlJwV2pXLWdqY0NTSkZDVDJiUDlkSVFBQUFBJCQAAAAAAAAAAAEAAACCWms-tO3Jz9lctLJ0d2ljZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPbf113239ddf; BIDUPSID=4AF31140B675845AB1E3EAEF36CABCC4; PSTM=1574481182; pgv_pvi=2670401536; APPGUIDE_8_2_2=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1427_21090_30788_30909_30940_30823; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1582278813,1582536761,1582634892,1583071160; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1583111614; yjs_js_security_passport=cf9f5bdb2b8c84e28ee6c535ed5c23a40ee4cef8_1583111615_js; session_name=cn.bing.com; session_id=1583129492829; from_lang_often=%5B%7B%22value%22%3A%22fra%22%2C%22text%22%3A%22%u6CD5%u8BED%22%7D%2C%7B%22value%22%3A%22dan%22%2C%22text%22%3A%22%u4E39%u9EA6%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D",
"origin": "https://fanyi.baidu.com",
"referer": "https://fanyi.baidu.com/",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
"x-requested-with": "XMLHttpRequest"}
request = urllib.request.Request(url=url, headers=headers)
reponse = urllib.request.urlopen(request, data=date.encode())

#报错：UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte
import gzip
from Logger import logger
#print(reponse.read().decode("utf8"))

#进行解压缩  或者注释注释掉压缩的请求语句
f = gzip.GzipFile(fileobj=reponse)
reponse_finall = f.read().decode()
#print(reponse_finall)
a = logger()
a.warning(reponse_finall)




