#-*-coding:utf-8-*-
__author__ = 'iTianpin'
from sqlalchemy import func
from sqlalchemy.schema import Column
from sqlalchemy.types import Unicode, Integer, String, DateTime,TEXT,TIMESTAMP
from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.schema import MetaData


metadata = MetaData()

def _get_connect():
    DB_CONNECT_STRING = "mysql+mysqldb://22too:123456@localhost/22too?charset=utf8"
    engine = create_engine(DB_CONNECT_STRING,echo=True)
    sessionDB = sessionmaker(_get_connect())
    session = sessionDB()
    return session



class Blog():
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, autoincrement=True),
    title = Column(Unicode(40))
    content = Column(TEXT)
    html = Column(TEXT)
    tag = Column(Unicode(30))
    time =  Column(TIMESTAMP)
    user =  Column(Integer)
    skim =  Column(Integer)
    comment =  Column(Integer)

    @classmethod
    def update_blog(cls, blog_id=None, title=None,content=None,tag=None):
        sessionDB = sessionmaker(_get_connect())
        session = sessionDB()
        update_blog=session.query(cls.Blog).filter_by(id=blog_id)
        update_blog.title = title
        update_blog.content = content
        update_blog.tag = tag
        session.commit()
        session.close()

    @classmethod
    def all_blog(cls):
        session = sessionmaker(_get_connect())
        list_blog = session.query(cls.blog).order_by(cls.blog.time).desc()
        session.close()
        return list_blog

    @classmethod
    def insert_blog(cls,title=None,content=None,
                    html=None,tag=None,timestamp=None):

        session = _get_connect()
        blog = Blog(title=title,
                        content=content,
                        html=html,
                        tag=tag,
                        time=timestamp
                        )
        session.add(blog)
        session.commit()
        session.close()







#初始化数据库
def init_db():
    MetaData.create_all(_get_connect())
#清空数据库
def drop_db():
    MetaData.drop_all(_get_connect())

