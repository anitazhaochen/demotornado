#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.httpserver
from tornado.web import RequestHandler
from tornado.options import options, define

define("port", default=8000, type=int, help="run server on given port")


class IndexHandler(RequestHandler):
    def get(self):
        self.write("调用了 get")

    def initialize(self):
        print("调用了initialize")

    def prepare(self):
        print("调用了 prepare")

    def set_default_headers(self):
        print("调用了set_default_headers")

    def write_error(self, status_code, **kwargs):
        print("调用了write_error")
        self.send_error(200)

    def post(self):
        print("调用了post")

    def on_finish(self):
        print("调用了on_finish")

if __name__ == "__main__":
    options.parse_command_line()
    
    app = tornado.web.Application([
        (r'/', IndexHandler),

        ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


