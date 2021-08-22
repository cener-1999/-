# -*-coding:utf-8-*-
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# 创建连接引擎
engine = create_engine('mysql+pymysql://root:nbuser@localhost:3306/winbupt?charset=utf8', echo=True)

# 声明映射
Base = declarative_base()

# 定义Course对象，课程表对象
class Projects(Base):
    # 表的名字
    __tablename__ = 'Projects'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), default=None, nullable=False, comment='name')
    department = Column(String(20), default=None, nullable=False, comment='department')
    date = Column(String(20), default=0, nullable=False, comment='date')

class Project_ifo(Base):
    # 表的名字
    __tablename__ = 'Project_ifo'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), default=None, nullable=False, comment='name')
    department = Column(String(20), default=None, nullable=False, comment='department')
    date = Column(String(20), default=0, nullable=False, comment='date')
    procontent=Column(String(500), default=None)
    goal=Column(String(500))
    achievements= Column(String(500))
    requests=Column(String(500))

#Base.metadata.create_all(engine)
