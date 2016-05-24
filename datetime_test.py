#!/usr/bin/python3
# encoding: utf-8
# 日期时间使用示例

import time

def show_datetime(s):
    print("tm_year: %s" % s.tm_year)
    print("tm_mon: %s" % s.tm_mon)
    print("tm_mday: %s" % s.tm_mday)
    print("tm_hour: %s" % s.tm_hour)
    print("tm_min: %s" % s.tm_min)
    print("tm_sec: %s" % s.tm_sec)
    print("tm_wday: %s" % s.tm_wday)
    print("tm_yday: %s" % s.tm_yday)
    print("tm_isdst: %s" % s.tm_isdst)
    print("time: %04d-%02d-%02d %d:%02d:%02d" % (s.tm_year, s.tm_mon, s.tm_mday, s.tm_hour, s.tm_min, s.tm_sec))
    
def time_test():
    print("time is: %s" % time.time())
    print("gmt time:")
    show_datetime(time.gmtime())
    print("local time:")
    show_datetime(time.localtime())
    
    print("mktime: %s" % time.mktime(time.localtime()))
    
    now = time.ctime()
    print("ctime: %s" % now)
    parsed = time.strptime(now)
    
    print("formatted: %s" % time.strftime("%a %b %d %H:%M:%S %Y", parsed))
    
# main...
if __name__ == '__main__':  
    time_test()