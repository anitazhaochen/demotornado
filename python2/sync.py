#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def long_io():
    print "start sleep "
    time.sleep(5)
    print "end sleep"
    result = "io result"
    return result

def req_a():
    print "start deal with a "
    ret = long_io()
    print ret
    print "end deal with a"
    
def req_b():
    print "start deal with b "
    print "end deal with b"


def main():
    req_a()
    req_b()


if __name__ == "__main__":
    main()
