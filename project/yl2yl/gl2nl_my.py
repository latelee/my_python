#!/usr/bin/python3
# encoding: utf-8
# Author: Late Lee
# 2017.2.11

#
# 阴历数据 每个元素的存储格式如下：
#   26~25   24~23   22~18   17~14   13        12              11~0
#   立春日  春节月  春节日 闰几月 闰月日数  是否闰月    1~12月份农历日数

# new...
#    26~23   22        21      20~19   18~17   16~12        11~0
#   闰几月 闰月日数  是否闰月  立春日  春节月  春节日   1~12月份农历日数

# 注：1、bit0表示农历1月份日数，为1表示30天，为0表示29天。bit1表示农历2月份日数，依次类推。
#     2、bit12表示该年是否有闰月，bit13表示闰月日数，1为30天，0为29天。bit17~bit14表示第几月是闰月
#
# 数据来源：http://data.weather.gov.hk/gts/time/conversion1_text_c.htm
my_g_lunar_month_day = [
    0x752, 0xea5, 0x2a00b2a, 0x64b,
]

#==================================================================================

from datetime import date, datetime
from calendar import Calendar as Cal

START_YEAR = 1901

LM_BIT = 21
LM_DAY_BIT = 22
LM_NUM_BIT = 23

yuefeng = ["正月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "冬月", "腊月"]
riqi = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", 
    "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "廿十", 
    "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"]

xingqi = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

tiangan   = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
shengxiao = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
dizhi     = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

jieqi = ["小寒", "大寒", 
    "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
    "立夏", "小满", "芒种", "夏至", "小暑", "大暑",
    "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
    "立冬", "小雪", "大雪", "冬至"]

def change_year(num):
    dx = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    tmp_str = ""
    for i in str(num):
        tmp_str += dx[int(i)]
    return tmp_str

def week_str(tm):
    return xingqi[tm.weekday()]

def d_lunar(ld):
    return riqi[(ld - 1) % 30]

def m_lunar(lm):
    leap = (lm>>4)&0xf
    m = lm&0xf
    month = yuefeng[(m - 1) % 12]
    if leap == m:
        month = "闰" + month
    return month

def y_lunar(ly):
    return tiangan[(ly - 4) % 10] + dizhi[(ly - 4) % 12] + u' ' + shengxiao[(ly - 4) % 12]

def date_diff(tm):
    return (tm - datetime(1901, 1, 1)).days

# 返回：
# a b c
# 闰几月，该月多少天 传入月份多少天
def lunar_month_days(lunar_year, lunar_month):
    if (lunar_year < START_YEAR):
        return 30

    leap_month, leap_day, month_day = 0, 0, 0 # 闰几月，该月多少天 传入月份多少天
    
    tmp = my_g_lunar_month_day[lunar_year - START_YEAR]
    
    if tmp & (1<<(lunar_month-1)):
        month_day = 30
    else:
        month_day = 29
    
    # 闰月
    if (tmp & (1<<LM_BIT)):
        if (tmp & (1<<LM_DAY_BIT)):
            leap_day = 30
        else:
            leap_day = 29
        leap_month = (tmp >> LM_NUM_BIT) & 0xf

        #print("!!!we have leap month: ", leap_month, leap_day)

    #print("debug: year: %d month: %d (%d %d)0x%x" % (lunar_year, lunar_month, leap_day, month_day, my_g_lunar_month_day[lunar_year - START_YEAR]));
    return (leap_month, leap_day, month_day)

# 获取某一年有多少个农历日
def lunar_year_days(year):
    days = 0
    tmp = my_g_lunar_month_day[year - START_YEAR]
    # 1~12月
    for i in range(0, 12):
        if tmp & (1<<i):
            days += 30
        else:
            days += 29
    # 闰月
    if (tmp & (1<<LM_BIT)):
        if (tmp & (1<<LM_DAY_BIT)):
            lm_days = 30
        else:
            lm_days = 29
        days += lm_days
        leap_month = (tmp >> LM_NUM_BIT) & 0xf
        #print("%d has leap month %d %d" % (year, leap_month, lm_days))
    #print("%d total day: %d" % (year, days))
    return days

# 算农历日期
# 返回的月份中，高4bit为闰月月份，低4bit为其它正常月份
def get_ludar_date(tm):
    span_days = date_diff(tm)
    #print("span_days %d" % span_days)
    #阳历1901年2月19日为阴历1901年正月初一
    #阳历1901年1月1日到2月19日共有49天
    if (span_days <49):
        year = START_YEAR - 1
        if (span_days <19):
          month = 11;
          day = 11 + span_days
        else:
            month = 12;
            day = span_days - 18
        return (year, month, day)

    #下面从阴历1901年正月初一算起
    span_days -= 49
    year, month, day = START_YEAR, 1, 1 # 从1901.1.1开始计算
    #计算年
    tmp = lunar_year_days(year)
    #print("year1: %d span: %d tmp: %d 0x%x" % (year, span_days, tmp, g_lunar_month_day[year - START_YEAR]))
    # 如果间隔大于1901年，则要继续循环计算时间，否则在1901年
    while span_days >= tmp:
        span_days -= tmp
        year += 1
        tmp = lunar_year_days(year)
        #print("year11: %d span: %d tmp: %d 0x%x" % (year, span_days, tmp, g_lunar_month_day[year - START_YEAR]))
    # span还有，说明是下一年之内的，则计算月
    #计算月
    (leap_month, foo, tmp) = lunar_month_days(year, month)
    #print(" month %d span: %d tmp: %d" % (month, span_days, tmp))
    while span_days >= tmp:
        span_days -= tmp
        if (month == leap_month):
            (leap_month, tmp, foo) = lunar_month_days(year, month)
            if (span_days < tmp): # 指定日期在闰月中
                month = (leap_month<<4) | month
                break
            span_days -= tmp
        month += 1 # 此处累加得到当前是第几个月
        (leap_month, foo, tmp) = lunar_month_days(year, month)

    #计算日
    day += span_days
    return (year, month, day)

def simple_test():
    lunar_year_days(1901)
    lunar_year_days(1902)
    lunar_year_days(1903)
    print('=============')

def show_month(tm):
    (ly, lm, ld) = get_ludar_date(tm)
    print("%d年%d月%d日" % (tm.year, tm.month, tm.day), week_str(tm), end='')
    print("\t农历 %s年 %s年%s%s " % (y_lunar(ly), change_year(ly), m_lunar(lm), d_lunar(ld))) # 根据数组索引确定

def _show_month(year, month, day):
    tmp = datetime(year, month, day)
    show_month(tmp)
    print('==========================================')

def this_month():
    _show_month(datetime.now().year, datetime.now().month, datetime.now().day)

#simple_test()
_show_month(1901, 1, 1)
_show_month(1901, 2, 18)
_show_month(1901, 2, 19)
_show_month(1902, 4, 1)
_show_month(1903, 6, 24)
_show_month(1903, 6, 25)
_show_month(1903, 6, 26)
_show_month(1903, 12, 28)
#_show_month(1903, 4, 1)

