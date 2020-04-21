#!/usr/bin/python3
#coding:utf8
import pymysql

'''
pip install -U pip
pip freeze > yilai.txt     pip install -r yilai.txt


'''

class mysqld():
	def __init__(self,host,passwd,db,port=3306,user='root'):
		self.host = host
		self.passwd = passwd
		self.db = db
		self.port = port
		self.user = user
		self.conn = pymysql.connect(host=host,
						port=port,
						user=user,
						passwd=passwd,
						db=db,
						charset='utf8')
		self.cursor=self.conn.cursor()
	def select(self,sql,num=0):
		data = self.cursor.execute(sql)
		num = int(num)
		if num > 1:
			all_data = self.cursor.fetchmany(num)
		elif num == 1:
			all_data = self.cursor.fetchone()
		else:
			all_data = self.cursor.fetchall()
		for i in all_data:
			print(i)
		return f"查询结果共{data}条"
	def change(self,sql):
		try:
			data = self.cursor.execute(sql)
			self.conn.commit()
			return data
		except Exception as e:
			self.conn.rollback()
			print(e)
	def delete(self):

	def close(self):
		self.cursor.close()
		self.conn.close()

if __name__ == '__main__':
	db = mysqld('192.168.115.128','Xishi@123','test',user="xishi")
	s = db.change('insert into t1(name,age) values("xiaoming",16)')
	#d = db.select('select * from user',3)
	#d = db.delete('delete * from user where a=%s',(no, yes))     这里是可以（）当作是元组的就算只有一个元素（no, ） 尽量不要用，sql注射攻击
	#print(d)
	print(s)
	db.close()
