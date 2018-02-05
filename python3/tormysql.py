#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import tornado.httpserver
from tornado.web import RequestHandler
from tornado.options import options, define
import torndb

define("port", default=8000, type=int, help="run server on given port")

class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = torndb.Connection(
                host = "127.0.0.1",
                database = "test2",
                user = "root",
                password = "root"
                )
    
class IndexHandler(RequestHandler):
    def get(self):
        self.write("hello")



if __name__ == "__main__":
    app = Application([
        (r'/', IndexHandler),
        ], **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

        
