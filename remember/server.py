#--coding:utf-8--
__author__ = 'iTianpin'
import tornado.web
import tornado.ioloop
from views.view import index, edit#, #tag, login, read,pull,push
import os

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("email")

class IndexHandler(BaseHandler):
    def get(self):
        index(self)

class EditHandler(BaseHandler):
    #@tornado.web.authenticated
    def get(self):
        self.render("edit.html")
    def post(self):
        self.set_header("templates/Content-Type","text/palin")
        edit(self)

# class TagHandler(BaseHandler):
#     def get(self,tagname):
#         self.set_header("templates/Content-Type","text/palin")
#         print tag
#         tag(self,tagname)
#
# class LoginHandler(BaseHandler):
#     def get(self):
#         self.render("login.html")
#
#     def post(self):
#         login(self)
# # class MainHandler(BaseHandler):
# #     @tornado.web.authenticated
# #     def get(self):
# #         name = tornado.escape.xhtml_escape(self.current_user)
# #         self.render("/edit")
# class BlogHandler(BaseHandler):
#     def get(self, blog_id):
#         print blog_id
#         read(self, blog_id)
#
# class ChangeHandler(BaseHandler):
#     def get(self,blog_id):
#         pull(self,blog_id)
#     def post(self,blog_id):
#         push(self,blog_id)

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": True,
    "template_path": "templates",
}

application = tornado.web.Application([
    #统一的portal入口
    (r"/",IndexHandler),
    (r"/edit",EditHandler),
    # (r"/tag/(\w+)",TagHandler),
    # (r"/login",LoginHandler),
    # (r"/remember/([0-9]+)",BlogHandler),
    # (r"/change/([0-9]+)",ChangeHandler),

], **settings)


if __name__ == "__main__":
    application.listen(9999, address="127.0.0.1")
    tornado.ioloop.IOLoop.instance().start()
