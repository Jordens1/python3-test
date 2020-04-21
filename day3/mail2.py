import subprocess,os

#在python里使用sheel命令
#yxsyxs123

# os.system('ls /root')
# print('*****')
# a = subprocess.getoutput('ls /opt')
# print(a)


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail(strd):
    msg = MIMEText(strd, 'plain', 'utf-8')     # nei rong   ge shi
    msg['From'] = formataddr(["darnell", '18270938391@163.com'])  #who send
    msg['To'] = formataddr(["me", '1285389644@qq.com'])       #who resive
    msg['Subject'] = "邮箱账号"          # zhu ti

    server = smtplib.SMTP("smtp.163.com", 25)
    server.login("18270938391@163.com", "yxsyxs123")
    server.sendmail('18270938391@163.com', ['1285389644@qq.com', ], msg.as_string())
    server.quit()

mail('邮箱账号')


