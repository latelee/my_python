#!/usr/bin/python3
# encoding: utf-8
# Author: Late Lee
# Linux + python3
# 2017.2.14

# 2033年有闰十一月

#农历数据 每个元素的存储格式如下：
#   26~25   24~20   19~17    16~13    12          11~0
#   春节月  春节日  立春日  闰几月 闰月日数  1~12月份农历日数

#  27~25   24~23   22~18    17~14   13        12              11~0
#  立春日  春节月  春节日 闰几月 闰月日数  是否闰月    1~12月份农历日数

#    ~13          12~7         6~5    4~0
# 农历有多少天 离元旦多少天  春节月  春节日



#####################################################################################
# 1901~2099年农历数据表
# powered by Late Lee, http://www.latelee.org 
# 2017-02-20 09:51:33.487610 
#农历数据 每个元素的存储格式如下： 
#      ~23      22~17   16~13    12          11~0  
# 农历总天数 离元旦天数 闰几月 闰月天数  1~12月份农历天数  
# 注：1、bit0表示农历1月份天数，为1表示30天，为0表示29天。bit1表示农历2月份天数，依次类推。 
#     2、bit12表示闰月天数，1为30天，0为29天。bit13~bit17表示第几月是闰月(注：为0表示该年无闰月) 
# 数据来源: http://data.weather.gov.hk/gts/time/conversion1_text_c.htm 
# 由Jim Kent编写python爬虫强力收集并分析
#####################################################################################
g_lunar_month_day = [
	0xb1620752, 0xb1cc0ea5, 0xbfb8ab2a, 0xb15c064b, 0xb1c40a9b, 0xc0309aa6, 0xb156056a, 0xb1c00b59, 0xc02a4baa, 0xb1500752, # 1901 ~ 1910 
	0xc03acda5, 0xb1600b25, 0xb1480a4b, 0xc032ba4b, 0xb15802ad, 0xb1c2056b, 0xc02c45b5, 0xb1d20da9, 0xc03efe92, 0xb1640e92, # 1911 ~ 1920 
	0xb14c0d25, 0xc036ad2d, 0xb15c0a56, 0xb14602b6, 0xc0ae9ad5, 0xb15606d4, 0xb1c00ea9, 0xc02c4f4a, 0xb1500e92, 0xbfbac6a6, # 1921 ~ 1930 
	0xb15e052b, 0xb1c80a57, 0xc032b956, 0xb1d80b5a, 0xb14406d4, 0xc02e7761, 0xb1520749, 0xc03cfb13, 0xb1620a93, 0xb14c052b, # 1931 ~ 1940 
	0xc034d51b, 0xb1da0aad, 0xb146056a, 0xc0b09da5, 0xb1560ba4, 0xb1400b49, 0xc02a4d4b, 0xb1500a95, 0xc038eaad, 0xb15e0536, # 1941 ~ 1950 
	0xb1c80aad, 0xc034baca, 0xb15805b2, 0xb1c20da5, 0xc02e7ea2, 0xb1540d4a, 0xbfbd0595, 0xb1e00a97, 0xb14c0556, 0xc036c575, # 1951 ~ 1960 
	0xb1da0ad5, 0xb14606d2, 0xc0308755, 0xb1d60ea5, 0xb0c0064a, 0xc028664f, 0xb1ce0a9b, 0xc03aeada, 0xb15e056a, 0xb1c80b69, # 1961 ~ 1970 
	0xc034abb2, 0xb15a0b52, 0xb1420b25, 0xc02c8b2b, 0xb1520a4b, 0xc03d0aab, 0xb16002ad, 0xb1ca056d, 0xc036d5a9, 0xb1dc0da9, # 1971 ~ 1980 
	0xb1460d92, 0xc0308e95, 0xb1560d25, 0xc0414e4d, 0xb1640a56, 0xb14e02b6, 0xc038c2f5, 0xb1de06d5, 0xb1c80ea9, 0xc034af52, # 1981 ~ 1990 
	0xb15a0e92, 0xb1440d26, 0xbfac652e, 0xb1d00a57, 0xc03d0ad6, 0xb162035a, 0xb1ca06d5, 0xc036ab69, 0xb15c0749, 0xb1460693, # 1991 ~ 2000 
	0xc02e8a9b, 0xb154052b, 0xb1be0a5b, 0xc02a4aae, 0xb14e056a, 0xc0b8edd5, 0xb1600ba4, 0xb14a0b49, 0xc032ad53, 0xb1580a95, # 2001 ~ 2010 
	0xb142052d, 0xc02c855d, 0xb1d00ab5, 0xc03d2baa, 0xb16205d2, 0xb1cc0da5, 0xc036de8a, 0xb15c0d4a, 0xb1460c95, 0xc0308a9e, # 2011 ~ 2020 
	0xb1540556, 0xb1be0ab5, 0xc02a4ada, 0xb15006d2, 0xc038c765, 0xb15e0725, 0xb148064b, 0xc032a657, 0xb1d60cab, 0xb142055a, # 2021 ~ 2030 
	0xc02c656e, 0xb1d20b69, 0xc03d6f52, 0xb1620b52, 0xb14c0b25, 0xc036dd0b, 0xb15a0a4b, 0xb14404ab, 0xc02ea2bb, 0xb1d405ad, # 2031 ~ 2040 
	0xb1be0b6a, 0xc02a4daa, 0xb1500d92, 0xc03aeea5, 0xb15e0d25, 0xb1480a55, 0xc032ba4d, 0xb15804b6, 0xb1c005b5, 0xc02c76d2, # 2041 ~ 2050 
	0xb1d20ec9, 0xc03f0f92, 0xb1620e92, 0xb14c0d26, 0xbfb6d516, 0xb1da0a57, 0xb1440556, 0xc02e9365, 0xb1d40755, 0xb1400749, # 2051 ~ 2060 
	0xc028674b, 0xb14e0693, 0xc038eaab, 0xb15e052b, 0xb1c60a5b, 0xc032aaba, 0xb158056a, 0xb1c20b65, 0xc02c8baa, 0xb1520b4a, # 2061 ~ 2070 
	0xc03d0d95, 0xb1620a95, 0xb14a052d, 0xc034c56d, 0xb1da0ab5, 0xb14605aa, 0xc02e85d5, 0xb1d40da5, 0xb1400d4a, 0xc02a6e4d, # 2071 ~ 2080 
	0xb14e0c96, 0xc038ecce, 0xb15e0556, 0xb1c80ab5, 0xc032bad2, 0xb15806d2, 0xb1c20ea5, 0xbfae872a, 0xb150068b, 0xc03b0697, # 2081 ~ 2090 
	0xb16004ab, 0xb1ca055b, 0xc034d556, 0xb1da0b6a, 0xb1460752, 0xc0308b95, 0xb1540b45, 0xb13e0a8b, 0xc0284a4f, ]

#==================================================================================

from datetime import date, datetime
import calendar

START_YEAR = 1901

MONTH_DAY_BIT = 12
MONTH_NUM_BIT = 13
YD_DAY_BIT = 17

#　todo：正月初一 == 春节   腊月二十九/三十 == 除夕
yuefeng = ["正月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "冬月", "腊月"]
riqi = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
    "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "廿十",
    "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"]

xingqi = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

tiangan   = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhi     = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
shengxiao = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]

# todo：添加节气
jieqi = [
    "小寒", "大寒",  # 1月
    "立春", "雨水",  # 2月
    "惊蛰", "春分",  # 3月
    "清明", "谷雨",  # 4月
    "立夏", "小满",  # 5月
    "芒种", "夏至",  # 6月
    "小暑", "大暑",  # 7月
    "立秋", "处暑",  # 8月
    "白露", "秋分",  # 9月
    "寒露", "霜降",  # 10月
    "立冬", "小雪",  # 11月
    "大雪", "冬至"]  # 12月

def change_year(num):
    dx = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    tmp_str = ""
    for i in str(num):
        tmp_str += dx[int(i)]
    return tmp_str

def week_str(tm):
    return xingqi[tm.weekday()]

def lunar_day(day):
    return riqi[(day - 1) % 30]

def lunar_day1(month, day):
    if day == 1:
        return lunar_month(month)
    else:
        return riqi[day - 1]

def lunar_month(month):
    leap = (month>>4)&0xf
    m = month&0xf
    month = yuefeng[(m - 1) % 12]
    if leap == m:
        month = "闰" + month
    return month

def lunar_year(year):
    return tiangan[(year - 4) % 10] + dizhi[(year - 4) % 12] + '[' + shengxiao[(year - 4) % 12] + ']'

# 返回：
# a b c
# 闰几月，该闰月多少天 传入月份多少天
def lunar_month_days(lunar_year, lunar_month):
    if (lunar_year < START_YEAR):
        return 30

    leap_month, leap_day, month_day = 0, 0, 0 # 闰几月，该月多少天 传入月份多少天

    tmp = g_lunar_month_day[lunar_year - START_YEAR]

    if tmp & (1<<(lunar_month-1)):
        month_day = 30
    else:
        month_day = 29

    # 闰月
    leap_month = (tmp >> MONTH_NUM_BIT) & 0xf
    if leap_month:
        if (tmp & (1<<MONTH_DAY_BIT)):
            leap_day = 30
        else:
            leap_day = 29

    return (leap_month, leap_day, month_day)

# 算农历日期
# 返回的月份中，高4bit为闰月月份，低4bit为其它正常月份
def get_ludar_date(tm):
    year, month, day = tm.year, 1, 1
    code_data = g_lunar_month_day[year - START_YEAR]
    days_tmp = (code_data >> YD_DAY_BIT) & 0x3f
    days_tmp2 = (tm - datetime(year, 1, 1)).days # 当前日期离该年元旦多少天
    span_days = days_tmp2-days_tmp # 差值即为农历日期(注：正数即是，负数则要倒算)
    #print("span_day: ", days_tmp, days_tmp2, span_days)
    
    # 日期在该年农历之后
    if (span_days >= 0):
        (leap_month, foo, tmp) = lunar_month_days(year, month)
        while span_days >= tmp:
            span_days -= tmp
            if (month == leap_month):
                (leap_month, tmp, foo) = lunar_month_days(year, month) # 注：tmp变为闰月日数
                if (span_days < tmp): # 指定日期在闰月中
                    month = (leap_month<<4) | month
                    break
                span_days -= tmp
            month += 1 # 此处累加得到当前是第几个月
            (leap_month, foo, tmp) = lunar_month_days(year, month)
        day += span_days
        return year, month, day
    # 倒算日历
    else:
        month = 12
        year -= 1
        (leap_month, foo, tmp) = lunar_month_days(year, month)
        while abs(span_days) >= tmp:
            span_days += tmp
            month -= 1
            if (month == leap_month):
                (leap_month, tmp, foo) = lunar_month_days(year, month)
                if (abs(span_days) < tmp): # 指定日期在闰月中
                    month = (leap_month<<4) | month
                    break
                span_days += tmp
            (leap_month, foo, tmp) = lunar_month_days(year, month)
        day += (tmp + span_days) # 从月份总数中倒扣 得到天数
        return year, month, day

def _show_month(tm):
    (year, month, day) = get_ludar_date(tm)
    print("%d年%d月%d日" % (tm.year, tm.month, tm.day), week_str(tm), end='')
    print("\t农历 %s年 %s年%s%s " % (lunar_year(year), change_year(year), lunar_month(month), lunar_day(day))) # 根据数组索引确定
    print("一\t二\t三\t四\t五\t六\t日")

    c = calendar.Calendar(0)
    ds = [d for d in c.itermonthdays(tm.year, tm.month)]

    #print(len(ds), ds)
    # 利用calendar直接获取指定年月日期
    count = 0
    for d in ds:
        if d == 0:
            print("\t", end='')
            count += 1
            continue
        (year, month, day) = get_ludar_date(datetime(tm.year, tm.month, d))
        if count % 7 == 0: # 换行
            print("\n", end='')
        d_str = str(d)
        if d == tm.day:
            d_str = "*" + d_str
        print("%s\t" % (d_str + lunar_day1(month, day)), end='')
        count += 1
    print("")


def show_month(year, month, day):
    if year > 2100 or year < 1901:
        return
    if month > 13 or month < 1:
        return

    tmp = datetime(year, month, day)
    _show_month(tmp)
    print('===========================================================================')

def this_month():
    #print(calendar.month(datetime.now().year, datetime.now().month))
    #print('--------------------------')
    show_month(datetime.now().year, datetime.now().month, datetime.now().day)

#this_month()
show_month(2017, 1, 4)
#show_month(1934, 1, 1)
#show_month(2033, 12, 27)
show_month(2034, 1, 1)



