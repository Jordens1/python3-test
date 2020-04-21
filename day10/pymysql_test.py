import pymysql

conn = pymysql.connect(host='172.16.38.133',
                       port=3306,
                       user='u2',
                       passwd='Ying1@123',
                       db='db1',
                       charset='utf8')

cursor = conn.cursor()

# create_table_sql = """create table t1
#                 (id int auto_increment primary key,
#                  name varchar(10) not null,
#                  age int not null)"""
#
#
# cursor.execute(create_table_sql)

#row = cursor.execute(r'insert into t1(name, age) values(%s, %s);', ('xishi', 18))
row = cursor.executemany(r'insert into t1(name, age) values(%s, %s);', [('wuhao', 18),('kunkun', 20)])
new_id = cursor.lastrowid
print(new_id)
#cursor = conn.cursor(cursor = pymysql.cursors.SSDictCursor)

row_nums = cursor.execute('select id,name,age from t1 where name=%s;', ('kunkun'))
one_data = cursor.fetchone()
print(one_data)


conn.commit()

cursor.close()
conn.close()




