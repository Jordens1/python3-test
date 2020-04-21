#/usr/bin/env python
# _*_ coding:utf-8 _*_
import pymysql
'''
可以自己将mysql语句封装好，直接调用
'''

db = pymysql.connect()
cursor1 = db.cursor()    #游标用了需要关闭，还有一种自动关的写法
with db.cursor() as cursor:
    cursor.execute("use local")
    db.commit()

# 检查表是否存在
cursor1.execute("drop if exits")   #建表的时候

#建表
sql = "create table bandcard(id int auto_increment prinmarykey, money int not null)"
cursor1.execute(sql)

#插入
try:
    sql = ""
    cursor1.execute(sql)
    db.commit()     #从缓存进去
except:
    db.rollback()     #回滚


#查询
'''
fetchone()   获取下一个查询的结果集，结果集是一个对象
fetchmany(self, size)
fetchall()  接收全部的返回的行返回元组     
rowcount：是一个只读属性，返回execute()方法影响的行数

而且上面的使用了之后，游标会向后漂移，就像是read文本一样
如果不想对元组进行操作，可以将他的返回值改为字典类型(更好操作)的：db = pymysql.connect(cursorcalss=pymysql.cursors.DictCursor)


'''
sql  = ""
try:
    cursor1.execute(sql)
    reslist = cursor1.fetchall()
    for row in reslist:
        print("%s--%s" % (row[0], row[1]))
except:
    import time
    time.sleep()


cursor1.close()
db.close()
