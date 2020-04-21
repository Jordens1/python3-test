from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String

class Title(Base):
    # 表名称
    __tablename__ = 'titles'
    # 表里id字段
    emp_no = Column(Integer, primary_key=True, autoincrement=True)
    # 表里title字段
    title = Column(String(length=255), nullable=False)
    # 表里from_date字段
    from_date = Column(String(length=255),nullable=False)
    to_date = Column(String(length=255), nullable=False)