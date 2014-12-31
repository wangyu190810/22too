#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: commit.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-12-29
#Description: 

from sqlalchemy import Column,Integer,String,TEXT,Date,DateTime
from flask import g
import markdown2
from datetime import date

from mysite.model.base import Base

class Blog(Base):
    __tablename__ = "comment"
    id = Column(Integer,primary_key=True,autoincrement=True)
    content = Column(TEXT)
    user_name = Column()
