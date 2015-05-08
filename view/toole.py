# -*-coding: utf-8-*-

__author__ = 'wangyu'

from datetime import time

from flask import render_template
from urlparse import urljoin
from flask import request,g
from werkzeug.contrib.atom import AtomFeed

from model.blog import Blog
from lib.decorator import GMT1,get_time

def make_external(url):
    return urljoin(request.url_root, url)




def google():
    return render_template("googlefad2f2add41d5dac.html")



def recent_feed():
    feed = AtomFeed('Recent Articles',
                    feed_url=request.url, url=request.url_root)
    articles = Blog.rss_blog(g.db)
    for article in articles:
        print article.date
        dir(article.date)
        data = get_time(article.date)

        feed.add(article.title, unicode(article.content_html),
                 content_type='html',
                 author="22too",
                 url=make_external("http://www.22too.com/blog/"+str(article.id)),
                 updated=time(1,1,1,tzinfo=GMT1()))
    return feed.get_response()
