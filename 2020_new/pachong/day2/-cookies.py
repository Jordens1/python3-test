#/usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib.request, urllib.parse
url = "https://space.bilibili.com/29213051"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
          "Cookie": "_uuid=60145FD6-9EC7-8451-FAC4-CB31F6B8855733365infoc; buvid3=6254505D-18CB-4B95-9152-691B808BA3B4190944infoc; LIVE_BUVID=AUTO9715744949492775; sid=ipwq80kn; im_notify_type_29213051=0; CURRENT_FNVAL=16; stardustvideo=1; rpdid=|(umRk)mR|~~0J'ul~Rl)|kkm; CURRENT_QUALITY=80; laboratory=1-1; DedeUserID=29213051; DedeUserID__ckMd5=a14a12949540f4a8; SESSDATA=ab03919c%2C1584695917%2C53c0de21; bili_jct=298ab4aba83954853728e7280305811b; INTVER=1; stardustpgcv=0606; bp_t_offset_29213051=363816753980093348"}

request = urllib.request.Request(url, headers=header)

reponse = urllib.request.urlopen(request)

with open("cook1.html", "wb") as f:
    f.write(reponse.read())


