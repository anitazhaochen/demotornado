#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import RequestHandler

define("port",default=8000, type=int, help="run server on given port")

class IndexHandler(RequestHandler):
    def get(self):
        self.write("hello world")

class SubjectDateHandler(RequestHandler):
    def get(self, date, subject):
        self.write("Date:%s<br/>Subject:%s"%(date,subject))

class SubjectCityHandler(RequestHandler):
    def get(self, subject,city):
        self.write("Subject:%s<br/>City:%s"%(subject,city))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/sub-city/(.+)/([a-z]+)',SubjectCityHandler),
        (r'/sub-date/(?P<subject>.+)/(?P<date>\d+)',SubjectDateHandler),
        ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
