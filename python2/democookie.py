#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torndb
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.web import RequestHandler
from tornado.options import options, define


define("port", default=8000, type=int, help="run server on given port")

class CookieHandler(RequestHandler):
    def get(self):
        count = self.get_secure_cookie("page_count")
        if not count:
            self.set_secure_cookie("page_count","1", expires_days=1)
        else:
            count = int(count)
            count +=1
            self.set_secure_cookie("page_count",str(count),expires_days=1)
        self.write(str(count))


class Application(tornado.web.Application):
    def __init__(self,*args, **kwargs):
        super(Application,self).__init__(*args, **kwargs)
        self.db = torndb.Connection(
                host="127.0.0.1",
                user="root",
                password="root",
                database="tornado"
                )
            

class IndexHandler(RequestHandler):
    def get(self):
        self.write("hello index")



if __name__ == "__main__":
    tornado.options.parse_command_line()

    app = Application([
        (r'/', IndexHandler),
        (r'/cookie',CookieHandler),
        
        ], cookie_secret='H5d2GiwmQIO9a1Fc7/caZKGsZz2J5kwLvjO/Jr3SVwI=')

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
