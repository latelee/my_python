#!/usr/bin/python3
# encoding: utf-8
# python调用C动态库演示

import ctypes
from ctypes import *

class foo_info(Structure):
    _fields_ = [
        ("id",c_long),
        ("num",c_int),
        ("info",c_char*100)
        ]

def struct_test():
    foo = foo_info(100, 250, b"hello")
    print("%d %d %s" % (foo.id, foo.num, foo.info))
def hello():
    #so = ctypes.cdll("./libhello.so")
    so = cdll.LoadLibrary("./libhello.so")
    #so = cdll("./libhello.so")
    ret = so.hello(b"fuck..."); # 字符串用b""
    print("c return: %d" % ret);
#### main
if __name__ == '__main__':
    print("foo test")
    hello()
    struct_test()



