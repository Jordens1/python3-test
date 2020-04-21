#/usr/bin/env python
# _*_ coding:utf-8 _*_
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class mongoDB():
    def __init__(self, host, port=27017):
        self.host = host
        self.port = port
        # self.mydb = mydb
        # self.table = table
        self.collection = MongoClient("localhost", 27017)

    # def db_table(self, mydb, table):
    #     #     self.collection/.mydb/.table
    def insert(self, sql, mydb, table):
        sql1 = self.collection.mydb.table.insert_many(sql)
        # sql1 = self.db_table(mydb, table).insert_many(sql)
        #sql1 = self.collection.mydb.table.insert_many(sql)

    def remove(self):
        return

    def find(self):
        return

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    db = mongoDB("localhost")
    sql = [{"name":"jjj", "age":19, "gender":1, "address":"bejing", "idDelete":0},
            {"name":"bbb", "age":16, "gender":1, "address":"jiangxi", "idDelete":0},
            {"name":"ccc", "age":23, "gender":0, "address":"zhejiang", "idDelete":0}]
    a = db.insert(sql, "xishi", "table")
    db.close()








