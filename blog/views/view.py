#--coding:utf-8--
__author__ = 'iTianpin'
from models.DB import blog, comment,engine
from sqlalchemy.sql import select
import time
from markdown import markdown
#首页
def timestamp_datetime(value):
    style = "%Y-%m-%d %H:%M:%S"
    value = time.localtime(value)
    dt = time.strftime(style,value)
    return dt

def mk_to_html(content):
    content_html = markdown(content)
    return content_html

def index(self):
    conn = engine.connect()
    B = select([blog.c.title,blog.c.html,blog.c.time,blog.c.tag,blog.c.id]).order_by(
        blog.c.time.desc()).limit(1)
    results = conn.execute(B)
    self.render("index.html",results=results)
    conn.close()


def tag(self,tagname):
    print tagname
    conn = engine.connect()
    B = select([blog.c.title,blog.c.html,blog.c.time,blog.c.tag,blog.c.id]).\
        where(blog.c.tag == tagname).order_by(blog.c.time.desc())
    results = conn.execute(B)
    self.render("list.html",results=results)
    conn.close()


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
    settime = time.time()
    dt = timestamp_datetime(settime)

    if title is None:
        return self.write("None title")

    ins = blog.insert().values(title=title,
                               content=content,
                               time=dt,
                               tag=tag,
                               html=html,
                         )
    print ins
    conn = engine.connect()
    conn.execute(ins)

    self.write("success")

    conn.close()
    self.redirect("/")
    return

def login(self):
    if not self.current_user:
        email = self.get_argument("email")
        password = self.get_argument("password")
        if email == "wo190810401@gmail.com" and password == "12345678":
            self.set_secure_cookie("email",email)
        else:
            return self.redirect("/")
    return  self.redirect("/edit")


#阅读blog
def read(self, blog_id):
    id = blog_id
    change = 0
    if self.current_user:
        change = 1

    print id
    conn = engine.connect()
    B = select([blog.c.title,blog.c.html,blog.c.time,blog.c.tag,blog.c.id]).\
        where(blog.c.id == id)
    results = conn.execute(B)
    self.render("blog.html",results=results, change=change)

def pull(self,blog_id):
    id = blog_id
    print id
    print id
    conn = engine.connect()
    B = select([blog.c.title,blog.c.content]).\
        where(blog.c.id == id)
    results = conn.execute(B)
    for result in results:
        title = result[0]
        content = result[1]
    self.render("change.html", title=title, content=content)


def push(self,blog_id):
    id = blog_id
    title = self.get_argument("title")
    tag = self.get_argument("tag")
    content= self.get_argument("content")
    update = blog.update()
    conn = engine.connect()

