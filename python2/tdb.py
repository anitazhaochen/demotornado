#!/usr/bin/env python
# -*- coding: utf-8 -*-
import torndb
import tornado.web
from tornado.web import RequestHandler
import tornado.httpserver
from tornado.options import options, define

define("port", default=8000, type=int, help="run server on given port")

class IndexHandler(RequestHandler):
    def get(self):
        print "get come"
        ret = self.application.db.get("select * from bookinfo")
        if ret:
            self.write("ok")
        else:
            self.write("no ok")
        


class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = torndb.Connection(
                host="127.0.0.1",
                database="test2",
                user="root",
                password="root",
                )


if __name__ == '__main__':
    tornado.options.parse_command_line()
    
    app = Application([
        (r'/',IndexHandler),
        ],debug=True)
            

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
