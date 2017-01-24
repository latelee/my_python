#!/usr/bin/python3
# encoding: utf-8
# Author: Late Lee

# 天干地支示例
# 年份最后一个数字对应的天干
# 甲、乙、丙、丁、戊、己、庚、辛、壬、 癸
# 4、 5、 6、 7、 8、 9、 0、 1 、 2、 3
# 如2017最后一位是7，则天干是“丁”
#
#子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥
#4、 5、 6 、7、 8、 9、10、11、 0、 1、 2、3


import os
import datetime
import base64

tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
td = [] # 天干地支

# 计算天干地支
def tiangdi():
    for i in range(len(tiangan)*len(dizhi)//2):
        td.append(tiangan[i%len(tiangan)] + dizhi[i%len(dizhi)])
    #for i in td:
    #    print(i);

# 年份换算成天干地支，公式：(year - 3) % 总数 (列表要减去1)
def y2td(year = datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day, hour=datetime.datetime.now().hour):
    print("%04d-%02d-%02d %02d" % (year, month, day, hour))
    # 年份
    t = (year - 3) % 10
    d = (year - 3) % 12
    y_dt = tiangan[t-1]+dizhi[d-1]
    # 月份
    d = (t * 2 + month) % 10 # 月干
    t =  month % 12 + 2# 月支
    m_dt = tiangan[d-1]+dizhi[t-1]
    
    # 日
    x = year/100
    y = year%100
    print("x: %d y: %d" % (x, y));
    G=int(5*(x+y)+x/4+y/4+(month+1)*3/5+day-3-x) % 10
    i = 0
    if month%2 == 0:
        i = 6
    Z=int(G+4*x+10+i) % 12
    d_dt = tiangan[G-2]+dizhi[Z]

    print("year %d 年干: %s" % (year, y_dt))
    print("month: %d 月干 %s" % (month, m_dt));
    print("day: %d 日干 %s" % (day, d_dt));

def now_test():
    y2td(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour)
    
#### main
if __name__ == '__main__':
    tiangdi()
    y2td(2016, 6, 13)
    y2td(2016, 7, 16)
    print(datetime.datetime.now());
