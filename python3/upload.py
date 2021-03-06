#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import RequestHandler


define("port", default=8000, type=int, help="run server on given port.")

class IndexHandler(RequestHandler):
    def get(self):
        self.write("hello world")

class UploadHandler(RequestHandler):
    def post(self):
        files = self.request.files
        img_files = files.get('img')
        if img_files:
            img_file = img_files[0]["body"]
            file = open("./hello","w+")
            file.write(img_file)
            file.close()
        self.write("OK")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r'/',IndexHandler),
        (r'/upload', UploadHandler),
        ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
