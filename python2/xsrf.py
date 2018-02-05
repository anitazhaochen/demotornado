#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.ioloop
from tornado.web import RequestHandler
from tornado.options import optins, define

define("port", default=9000, type=int, help="")

class IndexHandler(RequestHandler):

