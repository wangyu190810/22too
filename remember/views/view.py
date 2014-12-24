#--coding:utf-8--
__author__ = 'iTianpin'
from remember.models.blog import Blog
from sqlalchemy.sql import select
import time
from markdown import markdown
#首页
def _get_timestamp():
    get_time = time.time()
    style = "%Y-%m-%d %H:%M:%S"
    value = time.localtime(get_time)
    timestamp = time.strftime(style,value)
    return timestamp

def mk_to_html(content):
    content_html = markdown(content)
    return content_html

def _get_blog():
    blog = Blog()
    return blog

#
# def index(self):
#     conn = engine.connect()
#     B = select([blog.c.title,blog.c.html,blog.c.time,blog.c.tag,blog.c.id]).order_by(
#         blog.c.time.desc()).limit(1)
#     results = conn.execute(B)
#     self.render("index.html",results=results)
#     conn.close()

def index(self):
    blog_list =Blog.all_blog()
    self.render("index.html",results=blog_list)
    return 0
# def tag(self,tagname):
#     print tagname
#     conn = engine.connect()
#     B = select([blog.c.title,blog.c.html,blog.c.time,blog.c.tag,blog.c.id]).\
#         where(blog.c.tag == tagname).order_by(blog.c.time.desc())
#     results = conn.execute(B)
#     self.render("list.html",results=results)
#     conn.close()
#
#
#编写blog
def edit(self):
    self.set_header("Content-Type", "application/json")
    title = self.get_argument("title")
    content = self.get_argument("content")
    tag = self.get_argument("tag")
    print title
    print content
    html = mk_to_html(content)
    print html
    dt = _get_timestamp()
    Blog.insert_blog(title=title,content=content,html=html,tag=tag,timestamp=dt)
    return 0
#     if title is None:
#         return self.write("None title")
#
#     ins = blog.insert().values(title=title,
#                                content=content,
#                                time=dt,
#                                tag=tag,
#                                html=html,
#                          )
#     print ins
#     conn = engine.connect()
#     conn.execute(ins)
#
#     self.write("success")
#
#     conn.close()
#     self.redirect("/")
#     return
#
# def login(self):
#     if not self.current_user:
#         email = self.get_argument("email")
#         password = self.get_argument("password")
#         if email == "wo190810401@gmail.com" and password == "12345678":
#             self.set_secure_cookie("email",email)
#         else:
#             return self.redirect("/")
#     return  self.redirect("/edit")
#
#
# #阅读blog
# def read(self, blog_id):
#     id = blog_id
#     change = 0
#     if self.current_user:
#         change = 1
#
#     print id
#     conn = engine.connect()
#     B = select([blog.c.title,blog.c.html,blog.c.time,blog.c.tag,blog.c.id]).\
#         where(blog.c.id == id)
#     results = conn.execute(B)
#     self.render("remember.html",results=results, change=change)
#
# def pull(self,blog_id):
#     id = blog_id
#     print id
#     print id
#     conn = engine.connect()
#     B = select([blog.c.title,blog.c.content]).\
#         where(blog.c.id == id)
#     results = conn.execute(B)
#     for result in results:
#         title = result[0]
#         content = result[1]
#     self.render("change.html", title=title, content=content)
#
#
# def push(self,blog_id):
#     id = blog_id
#     title = self.get_argument("title")
#     tag = self.get_argument("tag")
#     content= self.get_argument("content")
#
#
