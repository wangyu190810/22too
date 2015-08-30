# -*-coding: utf-8-*-

__author__ = 'wangyu'

from datetime import date

import markdown2
from sqlalchemy import Column, Integer, String, TEXT, Date,func
import sqlalchemy

sqlalchemy.func.yearmonth()

from base import Base


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(80))
    content_md = Column(TEXT)
    tag = Column(String(80), doc=u"使用|||作为多个标签的分隔")
    classify = Column(TEXT)
    content_html = Column(TEXT)
    status = Column(Integer, default=1, doc=u"默认为1，删除为0")
    img = Column(String(80), default="")
    readNum = Column(Integer, nullable=False, default=0)
    commentNum = Column(Integer, nullable=False, default=0)
    date = Column(Date, default=lambda: date.today())
    tag_title = Column(String(80))

    @classmethod
    def add_blog(cls, connection, title, content_md, classify, tag, img,tag_title):
        content_html = markdown2.markdown(content_md)
        blog = Blog(title=title, classify=classify, content_md=content_md,
                    tag=tag, content_html=content_html, img=img,
                    tag_title=tag_title)
        print blog
        connection.add(blog)
        connection.commit()

    @classmethod
    def admin_index(cls,connection):
        return connection.query(Blog)

    @classmethod
    def get_classify(cls, connection, name):
        return connection.query(Blog).filter_by(classify=name).order_by(Blog.id.desc())

    @classmethod
    def set_blog_status(cls,connection,blog_id,status):
        connection.query(Blog).filter(Blog.id == blog_id).\
            update({Blog.status:status})
        connection.commit()
        return True

    @classmethod
    def get_arch_dates(cls, connection):
        return connection.query(Blog.date).filter(Blog.status == 1).order_by(Blog.date.desc()).distinct()

    @classmethod
    def get_blog_form_data(cls, connection, date):
        return connection.query(Blog).filter(Blog.status == 1).filter(Blog.date >= date)

    @classmethod
    def index(cls, connection):
        return connection.query(Blog).filter_by(status=1).order_by(Blog.id.desc()).limit(5)

    @classmethod
    def blog(cls, connection, blog_id, status=None):
        if status is None:
            return connection.query(Blog).filter_by(id=blog_id)
        return connection.query(Blog).filter_by(id=blog_id, status=status)

    @classmethod
    def blog_tag(cls, connection, name):
        tag_name = "%s" + name + "%s"
        return connection.query(Blog).filter(Blog.tag.like(tag_name)).order_by(Blog.id.desc())

    @classmethod
    def blog_change(cls, connection, blog_id, title, classify, content_md, tag, img, status,tag_title):
        content_html = markdown2.markdown(content_md)
        connection.query(Blog).filter(Blog.id == blog_id).update({
            "title": title,
            "classify": classify,
            "content_md": content_md,
            "content_html": content_html,
            "status": status,
            "tag": tag,
            "img": img,
            "tag_title":tag_title
        })
        connection.commit()

    @classmethod
    def rss_blog(cls,connection):
        return connection.query(Blog).order_by(Blog.id.desc())

    @classmethod
    def blog_tag_title(cls,connection,name):
        return connection.query(Blog).filter(Blog.tag_title == name,Blog.status==1)
