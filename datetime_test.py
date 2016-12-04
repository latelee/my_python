#!/usr/bin/python3
# encoding: utf-8

# 日期时间测试示例

import time
from datetime import date

import datetime

def datetime_test():
    buffer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("now: %s" % buffer)

#### main
if __name__ == '__main__':
    print("date time test")
    datetime_test()
