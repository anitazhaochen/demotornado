#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import thread


def long_io():
        print "start sleep "
        time.sleep(5)
        print "end sleep"
        result = "io result"
        yield result

def gen_coroutine(f):
    def wrapper():
        gen = f()
        gen_login_io = gen.next()
        def fun():
            ret = gen_login_io.next()
            try:
                gen.send(ret)
            except StopIteration:
                pass
        thread.start_new_thread(fun, ())
    return wrapper


@gen_coroutine
def req_a():
    print "start deal with a "
    ret = yield long_io()
    print "leave  deal with a"
    
def req_b():
    print "start deal with b "
    time.sleep(2)
    print "end deal with b"


def main():
    req_a()
    req_b()
    while True:
        pass


if __name__ == "__main__":
        main()
