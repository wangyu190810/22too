__author__ = 'iTianpin'
from sqlalchemy import create_engine
from sqlalchemy import Table, Integer, MetaData, Column,\
    TEXT, CHAR, TIMESTAMP

DB_CONNECT_STRING = "mysql+mysqldb://root:@localhost/blog?charset=utf8"
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
            )

comment = Table("comment", m,
                Column("id", Integer, primary_key=True, autoincrement=True),
                Column("blog_id", Integer),
                Column("content", TEXT),
                Column("html", TEXT),
                Column("user", CHAR),
                Column("time", TIMESTAMP),
                )


def init_db():
    m.create_all(engine)

def drop_db():
    m.drop_all(engine)

