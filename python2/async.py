#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import thread

def long_io(cb):
    def fun(callback):
        print "start sleep "
        time.sleep(5)
        print "end sleep"
        result = "io result"
        callback(result)
    thread.start_new_thread(fun, (cb,))

def on_finish(ret):
    print "start deal with callback"
    print ret
    print "end deal with callback"



def req_a():
    print "start deal with a "
    ret = long_io(on_finish)
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
