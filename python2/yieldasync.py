#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import thread

gen = None

def long_io():
    def fun():
        global gen
        print "start sleep "
        time.sleep(5)
        print "end sleep"
        result = "io result"
        try:
            gen.send(result)
        except StopIteration:
            pass
    thread.start_new_thread(fun, ())




def req_a():
    print "start deal with a "
    ret = yield long_io()
    print "leave  deal with a"
    
def req_b():
    print "start deal with b "
    time.sleep(2)
    print "end deal with b"


def main():
    global gen
    gen = req_a()
    gen.next()
    req_b()
    while True:
        pass


if __name__ == "__main__":
        main()
