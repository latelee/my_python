#!/usr/bin/python3
# encoding: utf-8
# Author: Late Lee
# 2017.1.26
# linux+python3

# 抓取HK农历数据
# 地址：
# http://data.weather.gov.hk/gts/time/calendar/text/

#　算法
#
#
#
#
#
#


import os
import sys
import re

import urllib.request

mydict = {'正月': 13, '一月': 1, '二月': 2, '三月': 3, '四月': 4, '五月': 5, '六月': 6, '七月': 7, '八月': 8, '九月': 9, '十月': 10, '十一月': 11, '十二月': 12}

# 大小月
monthdict = {'廿九': 0, '三十': 1}

gl = "" # 公历日期
yue = "" # 月份
jieqi = "" #节气
y, m, d = 0, 0, 0 # 数字形式

leapmonth_m, leapmonth_d, leapmonth_is = 0, 0, 0
lichun_d = 0
chunjie_m, chunjie_d = 0, 0
day_cnt = 1
y_nl = 0
monthlist=[0]*33

binary_data = 0

def get_nongli(url, year1, year2):
    for year in range(year1, year2+1):
        aaaa(url, year)
def aaaa(url, year):
    global leapmonth_m, leapmonth_d, leapmonth_is
    global lichun_d
    global chunjie_m, chunjie_d
    global day_cnt
    global y, m, d
    global yy_nl
    global monthlist
    global binary_data

    new_url = url + "T%dc.txt" % year
    request = urllib.request.Request(new_url)
    response = urllib.request.urlopen(request)
    src = response.read().decode('big5')
    tmp = src.split('\n')

    start_row = 3 # 第三行才是真正的数据
    if year == 1901:
        for i in range(start_row, len(tmp)-start_row):
            start_row += 1
            tmpp = tmp[i].split()
            gl = tmpp[0]
            y, m, d = int(gl[:4]), int(gl[5:7]), int(gl[8:10])
            yy_nl = y
            yue = tmpp[1]
            if yue != "正月":
                continue
            else:
                chunjie_m = m
                chunjie_d = d
                print("计算农历%d年日历" % (yy_nl), end='')
                print("  --春节：%d年%d月%d日" % (yy_nl, m, d))
                break;

    #leapmonth_is = 0
    #leapmonth_m = 0
    leap_flag = 0
    # 确定起始计算位置
    for i in range(start_row, len(tmp)): # len(tmp)-3
        tmpp = tmp[i].split() # 格式：1903年01月01日 初三 星期四 [节气]
        if (len(tmpp)) == 0:
            break;
        gl = tmpp[0]
        y, m, d = int(gl[:4]), int(gl[5:7]), int(gl[8:10])
        #print(y, m, d)
        if len(tmpp) == 4:
            jieqi = tmpp[3]
            #print(jieqi, end='')
            if (jieqi == "立春"):
                lichun_d = d
        yue = tmpp[1]
        #print(gl, yue)
        if yue == "正月":
            day_cnt = monthdict[tmp[i-1].split()[1]]
            yy_nl = y - 1
            monthlist[0] = yy_nl
            monthlist[mydict[yue[0:]]-1] = day_cnt
            i = 13
            monthlist[i] = chunjie_d
            i+=1
            monthlist[i] = chunjie_m
            i+=1
            monthlist[i] = lichun_d
            i+=1
            monthlist[i] = leapmonth_is
            i+=1
            monthlist[i] = leapmonth_d
            i+=1
            monthlist[i] = leapmonth_m
            i+=1
            print("%d月 有%d天" % (mydict[yue[0:]]-1, day_cnt))
            print("农历%d年日历小结　" % (yy_nl))
            print("  --春节：%d年%d月%d日" % (yy_nl, chunjie_m, chunjie_d))
            print("  --立春：2月%d日" % (lichun_d))
            if leapmonth_is != 0:
                print("  --闰%d月 (大小月 %d)" % (leapmonth_m, leapmonth_d))
            print("数据: ", monthlist)
            
            #　转换成二进制
            for j in range(1, 13):
                binary_data |= monthlist[j] << (j-1) # 月份
            j = 13
            binary_data |= monthlist[j] << 12
            j+=1
            binary_data |= monthlist[j] << 17
            j+=1
            binary_data |= monthlist[j] << 19
            j+=1
            binary_data |= monthlist[j] << 23
            j+=1
            binary_data |= monthlist[j] << 24
            j+=1
            binary_data |= monthlist[j] << 25
            print("二进制数据：0x%08x" % binary_data)
            monthlist=[0]*33
            binary_data = 0
            #print("-------------------\n计算农历%d年日历" % (y))
            chunjie_m = m
            chunjie_d = d
            #print("    -- new春节：%d年%d月%d日" % (y, chunjie_m, chunjie_d))
        elif yue.find('月') != -1:
            day_cnt = monthdict[tmp[i-1].split()[1]]
            if yue.find('閏') != -1:
                leap_flag = 1
                leapmonth_is = 1
                leapmonth_m = mydict[yue[1:]]
                leapmonth_d = day_cnt
                #if day_cnt == 30:
                #    leapmonth_d = 1
                monthlist[mydict[yue[1:]]-1] = day_cnt
                print("闰%d月 有%d天 %d %d %d" % (mydict[yue[1:]], day_cnt, leapmonth_is, leapmonth_d, leapmonth_m))
            else:
                monthlist[mydict[yue[0:]]-1] = day_cnt
                print("%d月 有%d天" % (mydict[yue[0:]]-1, day_cnt))
    # 由于计算月份日期是在次月方知，所以闰月与非闰月是相反的 (如得到的闰五月日期数实为五月日期数)，这里调换
    # 此处还有问题
    if leapmonth_m != 0:
        changed_tmp = leapmonth_d
        leapmonth_d = monthlist[leapmonth_m]
        monthlist[leapmonth_m] = changed_tmp

    # 消掉全局变量的——全年没有闰月时，清零
    if leap_flag != 1:
        leapmonth_m, leapmonth_d, leapmonth_is = 0, 0, 0

def init_python_env():
    if sys.version_info.major == 2:
       reload(sys)
       sys.setdefaultencoding('utf8')


#### main
if __name__ == '__main__':
    init_python_env()

    # add here
    get_nongli("http://data.weather.gov.hk/gts/time/calendar/text/", 1901, 1907) # 2100