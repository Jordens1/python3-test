import sqlalchemy
from sqlalchemy import create_engine
from MyTable import Title
from sqlalchemy.orm import sessionmaker
from config import *
class Ormd():
    def __init__(self,url):
        #mysql+pymysql(使用的api接口)://账号:密码@host:端口/db名称
        engine=create_engine(url,echo=False,encoding='utf-8')
        # url为配置文件，echo调试参数，值为为true打印整个sql执行过程
        session = sessionmaker(bind=engine)
        # # 采用工厂模式，获取session
        self.session_Obj = session()
        # # 创建session对象，绑定了数据库引擎，为关联对象模型
    def Select(self,clo,record='all',start=None,end=None):
        # result = engine.execute('select * from user')  # 测试代码
        # print(result.fetchall())  # 测试代码
        # result = self.session_Obj.query(Title).first()  #测试打印第一条记录的from_date字段
        # print(result.from_date)
        if record == 'all':
            data = []
            result = self.session_Obj.query(Title).filter(Title.emp_no==f'{clo}').all()
            for i in result:
                data.append([i.emp_no,i.title,i.from_date,i.to_date])
        elif record == 'first':
            i = self.session_Obj.query(Title).filter(Title.emp_no == f'{clo}').first()
            data = [i.emp_no,i.title,i.from_date,i.to_date]
        return data
    def Inster(self,e,t):
        new = Title(emp_no=e,title=t,from_date='1925-02-18',to_date='1927-02-22')
        self.session_Obj.add(new)
        self.session_Obj.commit()
    def Update(self):
        self.session_Obj.query(Title).filter(Title.emp_no==100001).update({'title':'ssssss'})
        self.session_Obj.commit()
if __name__ == '__main__':
    s = Ormd(database_url)
    s.Update()