#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
"C:\Program Files\MongoDB\Server\4.2\bin\mongod.exe" --dbpath="c:\data\db"
mongochef 可视化管理mongoDB  直接上官网就行了
mongoDB的基本操作
文档的操作（表里的一行）
db.student.insert([{name:xishi,age:23},{同上}])   一个列表里是多个文档插入多个文档
还有一个save方法，除了指定ID不同（可以替换，可以插入）
db.student.drop()    # db就是指代的当前库
db.student.update(条件，操作，限制范围 )参数较多
db.student.remove(query,{justone:boolean,writeCincern:document})
用remove先使用find  可以查询文档和指定的列   .pretty()使用格式化的形式查询
    大于小于之类的：find.({age:{$gt:67}})
    db.student.find({"_id":ObjectId{"id值"}})
    还可以有 and or 联合使用
    find({},{},{})     find({$or:[{},{},{}]})
    limit 和  skip 实现翻页的功能   sort  排序方式

'''
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId


#连接服务器
conn = MongoClient("localhost", 27017)
#连接数据库
db = conn.mydb
#获取集合
collection = db.student
#添加文档
collection.insert_many([{"name":"leilei", "age":19, "gender":1, "address":"bejing", "idDelete":0},
                        {"name":"xishi", "age":16, "gender":1, "address":"jiangxi", "idDelete":0},
                       {"name":"meimei", "age":23, "gender":0, "address":"zhejiang", "idDelete":0}])
#查询文档  查询的时候需要 bson 这个标准库
    #查询部分文档
#res = collection.find({})
res = collection.find({"age":{"$gt":18}}).sort("age", pymongo.DESCENDING)
for row in res:
    print(row, type(row))
    #查询所有的文档    直接find()
    #统计查询   find().count()
    #根据id查询  res = collection.find({"_id":ObjectId("id号")})
    #排序   find().sort()  默认升序  降序   find.sort("age", pymongo.DESCENDING)
    #分页  find().skip().limit()      从开头跳几个，显示几个   做一个循环就行了
# res1 = collection.find({}).skip(2).limit(2)
# for row in res1:
#     print(row, type(row))
#更新文档
#collection.update_one({"name":"xishi"}, {"$set":{"age":19}})
    # 删除    collection.remove({"name":"lilei"})


#断开
conn.close()



























