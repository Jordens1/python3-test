


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

msg = MIMEText('are yuou ok today ?', 'plain', 'utf-8')
msg['From'] = formataddr(["darnell",'18270938391@163.com'])
msg['To'] = formataddr(["me",'1285389644@qq.com'])
msg['Subject'] = "A letter from your little cute lover"

server = smtplib.SMTP("smtp.163.com", 25)
server.login("18270938391@163.com", "yxsyxs123")
server.sendmail('18270938391@163.com', ['1285389644@qq.com',], msg.as_string())
server.quit()

