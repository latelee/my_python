#!/usr/bin/python3
# encoding: utf-8
# Author: Late Lee
# 2017.1.26
# linux+python3

# 抓取HK农历数据
# 地址：
# http://data.weather.gov.hk/gts/time/calendar/text/

import os
import sys
import re

import urllib.request

mydict= {'正月': 1, '一月': 1, '二月': 2, '三月': 3, '四月': 4, '五月': 5, '六月': 6, '七月': 7, '八月': 8, '九月': 9, '十月': 10, '十一月': 11, '十二月': 12}

gl = "" # 公历日期
yue = "" # 月份
jieqi = "" #节气
y, m, d = 0, 0, 0 # 数字形式

bit23, bit22, bit21 = 0, 0, 0
bit19 = 0
bit17, bit12 = 0, 0
bit0 = 0
day_cnt = 1

def get_nongli(url, year1, year2):
    for year in range(year1, year2+1):
        aaaa(url, year)
def aaaa(url, year):
    global bit23, bit22, bit21
    global bit19
    global bit17, bit12
    global bit0
    global day_cnt

    new_url = url + "T%dc.txt" % year
    request = urllib.request.Request(new_url)
    response = urllib.request.urlopen(request)
    src = response.read().decode('big5')
    tmp = src.split('\n')

    start_row = 3 # 第三行才是真正的数据
    if year == 1901:
        for i in range(start_row, len(tmp)-start_row):
            tmpp = tmp[i].split()
            gl = tmpp[0]
            y, m, d = int(gl[:4]), int(gl[5:7]), int(gl[8:10])
            yue = tmpp[1]
            if yue != "正月":
                start_row += 1
                continue
            else:
                bit17 = m
                bit12 = d
                break;
    else:
        for i in range(start_row, len(tmp)-start_row):
            tmpp = tmp[i].split()
            gl = tmpp[0]
            y, m, d = int(gl[:4]), int(gl[5:7]), int(gl[8:10])
            yue = tmpp[1]
            if yue != "正月":
                continue
            else:
                bit17 = m
                bit12 = d
                break;
        print("春节：%d年%d月%d日 立春：2月%d日  " % (y, bit17, bit12, bit19), end="")
        if bit21:
            l_day=29
            if bit22:
                l_day=30
            print("闰%d月有%d天" % (bit23, l_day), end='')
        else:
            print("无闰月", end='')
        print("\n=====================")
    
    
    print("计算农历%d年日历" % (y))
    
    bit21 = 0
    # 确定起始计算位置
    for i in range(start_row, len(tmp)): # len(tmp)-3
        day_cnt += 1
        tmpp = tmp[i].split()
        if (len(tmpp)) == 0:
            break;
        gl = tmpp[0]
        y, m, d = int(gl[:4]), int(gl[5:7]), int(gl[8:10])
        #print(y, m, d)
        yue = tmpp[1]
        
        if yue == "正月" and i == start_row:
            bit17 = m
            bit12 = d
            print("  --春节：%d年%d月%d日" % (y, m, d))
            #continue
        #print(gl, yue, end='')
        if (len(tmpp) == 4):
            jieqi = tmpp[3]
            #print(jieqi, end='')
            if (jieqi == "立春"):
                bit19 = d
                #print(" -- ", bit19, end='')
        if yue.find('月') != -1:
            if yue.find('閏') != -1:
                bit21 = 1
                bit23 = mydict[yue[1:]]
                print("闰%d月 有%d天 %d %d" % (mydict[yue[1:]], day_cnt, bit21, bit23))
            else:
                print("%d月 有%d天 " % (mydict[yue[0:]], day_cnt))
            day_cnt = 0
        #print("")
        
def aaaa11(url, year):
    global bit23, bit22, bit21
    global bit19
    global bit17, bit12
    global bit0
    global day_cnt

    new_url = url + "T%dc.txt" % year
    request = urllib.request.Request(new_url)
    response = urllib.request.urlopen(request)
    src = response.read().decode('big5')
    tmp = src.split('\n')

    start_row = 3 # 第三行才是真正的数据
    if year == 1901:
        for i in range(start_row, len(tmp)-start_row):
            tmpp = tmp[i].split()
            gl = tmpp[0]
            y, m, d = int(gl[:4]), int(gl[5:7]), int(gl[8:10])
            yue = tmpp[1]
            if yue != "正月":
                start_row += 1
                continue
            else:
                bit17 = m
                bit12 = d
                break;
    else:
        for i in range(start_row, len(tmp)-start_row):
            tmpp = tmp[i].split()
            gl = tmpp[0]
            y, m, d = int(gl[:4]), int(gl[5:7]), int(gl[8:10])
            yue = tmpp[1]
            if yue != "正月":
                continue
            else:
                bit17 = m
                bit12 = d
                break;
        print("春节：%d年%d月%d日 立春：2月%d日  " % (y, bit17, bit12, bit19), end="")
        if bit21:
            l_day=29
            if bit22:
                l_day=30
            print("闰%d月有%d天" % (bit23, l_day), end='')
        else:
            print("无闰月", end='')
        print("\n=====================")
    
    
    print("计算农历%d年日历" % (y))
    
    bit21 = 0
    # 确定起始计算位置
    for i in range(start_row+1, len(tmp)): # len(tmp)-3
        tmpp = tmp[i].split()
        if (len(tmpp)) == 0:
            break;
        gl = tmpp[0]
        y, m, d = int(gl[:4]), int(gl[5:7]), int(gl[8:10])
        #print(y, m, d)
        yue = tmpp[1]

        if yue == "正月":
            bit17 = m
            bit12 = d
            print("  --春节：%d年%d月%d日" % (y, m, d))
        #print(gl, yue, end='')
        if (len(tmpp) == 4):
            jieqi = tmpp[3]
            #print(jieqi, end='')
            if (jieqi == "立春"):
                bit19 = d
                #print(" -- ", bit19, end='')
        day_cnt += 1
        if yue.find('月') != -1:
            if yue.find('閏') != -1:
                bit21 = 1
                bit23 = mydict[yue[1:]]
                print("闰%d月 有%d天 %d %d" % (mydict[yue[1:]], day_cnt, bit21, bit23))
            else:
                print("%d月 有%d天 " % (mydict[yue[0:]], day_cnt))
            day_cnt = 0
        #print("")

def init_python_env():
    if sys.version_info.major == 2:
       reload(sys)
       sys.setdefaultencoding('utf8')


#### main
if __name__ == '__main__':
    init_python_env()
    
    # add here
    get_nongli("http://data.weather.gov.hk/gts/time/calendar/text/", 1901, 1903) # 2100