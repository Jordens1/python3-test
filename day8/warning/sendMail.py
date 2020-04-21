

# 两种发送方式  1 钉钉(no)  2 email

def mail(strd):
    # import subprocess, os
    # import smtplib
    # from email.mime.text import MIMEText
    # from email.utils import formataddr
    # msg = MIMEText(strd, 'plain', 'utf-8')
    # msg['From'] = formataddr(["darnell", '18270938391@163.com'])
    # msg['To'] = formataddr(["xishi", '18270938391@163.com'])
    # msg['Subject'] = "系统报警"
    #
    # server = smtplib.SMTP("smtp.163.com", 25)
    # server.login("18270938391@163.com", "yxsyxs123")
    # server.sendmail('18270938391@163.com', ['18270938391@163.com', ], msg.as_string())
    # server.quit()

    import yagmail

    yag = yagmail.SMTP(user='18270938391@163.com',
                       host='smtp.163.com',
                       port=465)
    # smtp_ssl=False
    yag.send(to='18270938391@163.com',
             subject='a tip to you',
             contents='systemctl walling',
             attachments=strd)




