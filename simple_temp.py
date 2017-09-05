#!/usr/bin/python3
# encoding: utf-8
# Author: Late Lee
# 2017.1.26
# linux+python3


import os
import sys

def init_python_env():
    if sys.version_info.major == 2:
       reload(sys)
       sys.setdefaultencoding('utf8')

#### main
if __name__ == '__main__':
    init_python_env()
    # add here
    if (len(sys.argv) < 3):
        print("usage: %s " % (sys.argv[0]))
        quit()
    #for arg in sys.argv:   
    #    print(arg) 



