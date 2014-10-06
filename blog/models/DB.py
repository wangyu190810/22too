#-*-coding:utf-8-*-
__author__ = 'iTianpin'

from sqlalchemy import create_engine
from sqlalchemy import Table, Integer, MetaData, Column,\
    TEXT, CHAR, TIMESTAMP

DB_CONNECT_STRING = "mysql+mysqldb://22too:123456@localhost/22too?charset=utf8"
engine = create_engine(DB_CONNECT_STRING,echo=True)
m = MetaData()

blog = Table("blog", m,
             Column("id", Integer, primary_key=True, autoincrement=True),
             Column("title", CHAR(20)),
             Column("content", TEXT),
             Column("html",TEXT),
             Column("tag", CHAR(20)),
             Column("time", TIMESTAMP),
             Column("user", CHAR(20)),
             Column("skim", Integer),
             Column("comment_nums",Integer),
            )

comment = Table("comment", m,
                Column("id", Integer, primary_key=True, autoincrement=True),
                Column("blog_id", Integer),
                Column("content", TEXT),
                Column("html", TEXT),
                Column("email", CHAR(40)),
                Column("username",CHAR(20)),
                Column("time", TIMESTAMP),
                )

#初始化数据库
def init_db():
    m.create_all(engine)
#清空数据库
def drop_db():
    m.drop_all(engine)

