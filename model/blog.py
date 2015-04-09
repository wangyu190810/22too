# -*-coding: utf-8-*-

__author__ = 'wangyu'

from datetime import date

import markdown2
from sqlalchemy import Column, Integer, String, TEXT, Date

from .base import Base


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

    @classmethod
    def add_blog(cls, connection, title, content_md, classify, tag, img):
        content_html = markdown2.markdown(content_md)
        blog = Blog(title=title, classify=classify, content_md=content_md, tag=tag, content_html=content_html, img=img)
        print blog
        connection.add(blog)
        connection.commit()
    
    @classmethod
    def index(cls, connection):
        return connection.query(Blog).filter_by().order_by(Blog.id.desc()).limit(1)
    
    @classmethod
    def blog_list(cls, connection):
        return connection.query(Blog).filter_by(status=1).order_by(Blog.id.desc()).all()

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
    def get_classify(cls, connection, name):
        return connection.query(Blog).filter_by(classify=name)

    @classmethod
    def blog_change(cls, connection, blog_id, title, classify, content_md, tag, img, status):
        content_html = markdown2.markdown(content_md)
        connection.query(Blog).filter(Blog.id == blog_id).update({
            "title": title,
            "classify": classify,
            "content_md": content_md,
            "content_html": content_html,
            "status": status,
            "tag": tag,
            "img": img
        })
        connection.commit()
