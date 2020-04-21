
import yagmail

yag = yagmail.SMTP(user='18270938391@163.com',
                   host='smtp.163.com',
                   port=465)
                   smtp_ssl=False
yag.send(to='18270938391@163.com',
         subject='a gift for you',
         contents='hello my friend !',
         attachments='/root/PycharmProjects/darnell/venv/python3test/day6/test.jpg')



# html = '''
# <html>
# 	<head>
#     	<meta charset="utf-8">
#     	<title>make friend.com</title>
# </head>
# <body>
#     <center><img src="test.jpg" alt="xiao hong" width="500px" height="900px" /></center>
# </body>
# </html>
# '''


# html = '''
# <html>
# <head>
#     <meta charset="utf-8">
#     <title>qf.com</title>
# </head>
# <body style="background-color:red;">
#     <img src="http://10.30.161.84"/>
# </body>
# </html>
# '''
# yag.send(to='18270938391@163.com',
#          subject='a gift for you',
#          contents=['nihao',html])






















