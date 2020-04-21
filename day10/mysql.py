import pymysql

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
	def close(self):
		self.cursor.close()
		self.conn.close()

if __name__ == '__main__':
	db = mysqld('localhost','Ying1@123','db1')
	s = db.change('insert into t1(name,age) values("xishi", 18)')
	#d = db.select('select * from user',3)
	print(s)
	db.close()