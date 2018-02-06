#!/usr/bin/env python
# -*- coding: utf-8 -*-
import torndb
import tornado.web
from tornado.web import RequestHandler
import tornado.httpserver
from tornado.options import options, define
from tornado.httpclient import AsyncHTTPClient
import json

define("port", default=8000, type=int, help="run server on given port")

class IndexHandler(RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        client = AsyncHTTPClient()
        client.fetch("http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=110.200.158.197",callback=self.on_response)
        
    def on_response(self, resp):
        json_data = resp.body
        data = json.loads(json_data)
        self.write(data.get("city"," "))
        self.finish()
        

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
