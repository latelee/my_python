#!/usr/bin/python3
# encoding: utf-8
# Author: Late Lee
# 2017.2.11

#阴历数据 每个元素的存储格式如下：
#   26~25   24~20   19~17    16~13    12          11~0
#   春节月  春节日  立春日  闰几月 闰月日数  1~12月份农历日数

#  27~25   24~23   22~18    17~14   13        12              11~0
#  立春日  春节月  春节日 闰几月 闰月日数  是否闰月    1~12月份农历日数

#    ~13          12~7         6~5    4~0
# 农历有多少天 离元旦多少天  春节月  春节日



#####################################################################################
# 1901~2100年阴历数据表
# powered by Late Lee, http://www.latelee.org
# 2017-02-12 23:02:06.546446
#阴历数据 每个元素的存储格式如下：
#  16~13    12         11~0
# 闰几月 闰月日数 1~12月份农历日数
# 注：1、bit0表示农历1月份日数，为1表示30天，为0表示29天。bit1表示农历2月份日数，依次类推。
#     2、bit12表示闰月日数，1为30天，0为29天。bit17~bit14表示第几月是闰月(注：为0表示该年无闰月)
# 数据来源: http://data.weather.gov.hk/gts/time/conversion1_text_c.htm 由Jim Kent编写python爬虫强力分析
#####################################################################################
my_g_lunar_month_day = [
	0x00752, 0x00ea5, 0x0ab2a, 0x0064b, 0x00a9b, 0x09aa6, 0x0056a, 0x00b59, 0x04baa, 0x00752, # 1901 ~ 1910
	0x0cda5, 0x00b25, 0x00a4b, 0x0ba4b, 0x002ad, 0x0056b, 0x045b5, 0x00da9, 0x0fe92, 0x00e92, # 1911 ~ 1920
	0x00d25, 0x0ad2d, 0x00a56, 0x002b6, 0x09ad5, 0x006d4, 0x00ea9, 0x04f4a, 0x00e92, 0x0c6a6, # 1921 ~ 1930
	0x0052b, 0x00a57, 0x0b956, 0x00b5a, 0x006d4, 0x07761, 0x00749, 0x0fb13, 0x00a93, 0x0052b, # 1931 ~ 1940
	0x0d51b, 0x00aad, 0x0056a, 0x09da5, 0x00ba4, 0x00b49, 0x04d4b, 0x00a95, 0x0eaad, 0x00536, # 1941 ~ 1950
	0x00aad, 0x0baca, 0x005b2, 0x00da5, 0x07ea2, 0x00d4a, 0x10595, 0x00a97, 0x00556, 0x0c575, # 1951 ~ 1960
	0x00ad5, 0x006d2, 0x08755, 0x00ea5, 0x0064a, 0x0664f, 0x00a9b, 0x0eada, 0x0056a, 0x00b69, # 1961 ~ 1970
	0x0abb2, 0x00b52, 0x00b25, 0x08b2b, 0x00a4b, 0x10aab, 0x002ad, 0x0056d, 0x0d5a9, 0x00da9, # 1971 ~ 1980
	0x00d92, 0x08e95, 0x00d25, 0x14e4d, 0x00a56, 0x002b6, 0x0c2f5, 0x006d5, 0x00ea9, 0x0af52, # 1981 ~ 1990
	0x00e92, 0x00d26, 0x0652e, 0x00a57, 0x10ad6, 0x0035a, 0x006d5, 0x0ab69, 0x00749, 0x00693, # 1991 ~ 2000
	0x08a9b, 0x0052b, 0x00a5b, 0x04aae, 0x0056a, 0x0edd5, 0x00ba4, 0x00b49, 0x0ad53, 0x00a95, # 2001 ~ 2010
	0x0052d, 0x0855d, 0x00ab5, 0x12baa, 0x005d2, 0x00da5, 0x0de8a, 0x00d4a, 0x00c95, 0x08a9e, # 2011 ~ 2020
	0x00556, 0x00ab5, 0x04ada, 0x006d2, 0x0c765, 0x00725, 0x0064b, 0x0a657, 0x00cab, 0x0055a, # 2021 ~ 2030
	0x0656e, 0x00b69, 0x16f52, 0x00b52, 0x00b25, 0x0dd0b, 0x00a4b, 0x004ab, 0x0a2bb, 0x005ad, # 2031 ~ 2040
	0x00b6a, 0x04daa, 0x00d92, 0x0eea5, 0x00d25, 0x00a55, 0x0ba4d, 0x004b6, 0x005b5, ]

#    12~7         6~5    4~0
# 离元旦多少天  春节月  春节日

my_g_lunar_day = [
	0x18d3, 0x1348, 0x0e3d, 0x1750, 0x1144, 0x0c39, 0x15cd, 0x1042, 0x0ab6, 0x144a, # 1901 ~ 1910
	0x0ebe, 0x1852, 0x1246, 0x0cba, 0x164e, 0x10c3, 0x0b37, 0x14cb, 0x0fc1, 0x1954, # 1911 ~ 1920
	0x1348, 0x0dbc, 0x1750, 0x11c5, 0x0bb8, 0x15cd, 0x1042, 0x0b37, 0x144a, 0x0ebe, # 1921 ~ 1930
	0x17d1, 0x1246, 0x0cba, 0x164e, 0x1144, 0x0bb8, 0x14cb, 0x0f3f, 0x18d3, 0x1348, # 1931 ~ 1940
	0x0d3b, 0x16cf, 0x11c5, 0x0c39, 0x15cd, 0x1042, 0x0ab6, 0x144a, 0x0e3d, 0x17d1, # 1941 ~ 1950
	0x1246, 0x0d3b, 0x164e, 0x10c3, 0x0bb8, 0x154c, 0x0f3f, 0x1852, 0x1348, 0x0dbc, # 1951 ~ 1960
	0x16cf, 0x11c5, 0x0c39, 0x15cd, 0x1042, 0x0a35, 0x13c9, 0x0ebe, 0x17d1, 0x1246, # 1961 ~ 1970
	0x0d3b, 0x16cf, 0x10c3, 0x0b37, 0x14cb, 0x0f3f, 0x1852, 0x12c7, 0x0dbc, 0x1750, # 1971 ~ 1980
	0x11c5, 0x0c39, 0x15cd, 0x1042, 0x1954, 0x13c9, 0x0e3d, 0x17d1, 0x1246, 0x0d3b, # 1981 ~ 1990
	0x16cf, 0x1144, 0x0b37, 0x144a, 0x0f3f, 0x18d3, 0x12c7, 0x0dbc, 0x1750, 0x11c5, # 1991 ~ 2000
	0x0bb8, 0x154c, 0x0fc1, 0x0ab6, 0x13c9, 0x0e3d, 0x1852, 0x12c7, 0x0cba, 0x164e, # 2001 ~ 2010
	0x10c3, 0x0b37, 0x144a, 0x0f3f, 0x18d3, 0x1348, 0x0dbc, 0x1750, 0x11c5, 0x0c39, # 2011 ~ 2020
	0x154c, 0x0fc1, 0x0ab6, 0x144a, 0x0e3d, 0x17d1, 0x1246, 0x0cba, 0x15cd, 0x10c3, # 2021 ~ 2030
	0x0b37, 0x14cb, 0x0f3f, 0x18d3, 0x1348, 0x0dbc, 0x16cf, 0x1144, 0x0bb8, 0x154c, # 2031 ~ 2040
	0x0fc1, 0x0ab6, 0x144a, 0x0ebe, 0x17d1, 0x1246, 0x0cba, 0x164e, 0x1042, 0x0b37, # 2041 ~ 2050
	]

#==================================================================================

from datetime import date, datetime
import calendar

START_YEAR = 1901

LM_DAY_BIT = 12
LM_NUM_BIT = 13

#　todo：正月初一 == 春节   腊月二十九/三十 == 除夕
yuefeng = ["正月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "冬月", "腊月"]
riqi = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
    "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "廿十",
    "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"]

xingqi = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

tiangan   = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhi     = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
shengxiao = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]

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

def d_lunar(ld):
    return riqi[(ld - 1) % 30]

def m_lunar(lm):
    leap = (lm>>4)&0xf
    m = lm&0xf
    month = yuefeng[(m - 1) % 12]
    if leap == m:
        month = "闰" + month
    return month

def d_lunar1(lm, ld):
    if ld == 1:
        return m_lunar(lm)
    else:
        return riqi[ld - 1]

def y_lunar(ly):
    return tiangan[(ly - 4) % 10] + dizhi[(ly - 4) % 12] + '[' + shengxiao[(ly - 4) % 12] + ']'

def date_diff(tm):
    return (tm - datetime(1901, 1, 1)).days

# 返回：
# a b c
# 闰几月，该闰月多少天 传入月份多少天
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
    leap_month = (tmp >> LM_NUM_BIT) & 0xf
    if leap_month:
        if (tmp & (1<<LM_DAY_BIT)):
            leap_day = 30
        else:
            leap_day = 29

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
    leap_month = (tmp >> LM_NUM_BIT) & 0xf
    if leap_month:
        if (tmp & (1<<LM_DAY_BIT)):
            lm_days = 30
        else:
            lm_days = 29
        days += lm_days
        #print("%d has leap month %d %d" % (year, leap_month, lm_days))
    #print("%d total day: %d" % (year, days))
    return days

# 算农历日期
# 返回的月份中，高4bit为闰月月份，低4bit为其它正常月份
# 注：此函数每次计算均从1901年开始，较耗时
def get_ludar_date(tm):
    span_days = date_diff(tm)
    #print("span_days %d" % span_days)
    #阳历1901年2月19日为阴历1901年正月初一
    #阳历1901年1月1日到2月19日共有49天
    if (span_days < 49):
        year = START_YEAR - 1
        if (span_days < 19):
          month = 11;
          day = 11 + span_days
        else:
            month = 12;
            day = span_days - 18
        return (year, month, day)

    span_days -= 49
    year, month, day = START_YEAR, 1, 1 # 从1901.1.1开始计算
    #计算年
    tmp = lunar_year_days(year)
    # 如果间隔大于1901年，则要继续循环计算时间，否则在1901年
    while span_days >= tmp:
        span_days -= tmp
        year += 1
        tmp = lunar_year_days(year)
    # span还有，说明是下一年之内的，则计算月
    #计算月
    (leap_month, foo, tmp) = lunar_month_days(year, month)
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

# 算农历日期
# 返回的月份中，高4bit为闰月月份，低4bit为其它正常月份
# 注：新方式
def get_ludar_date1(tm):
    year, month, day = tm.year, 1, 1
    code_data = my_g_lunar_day[year-1901]
    days_tmp = (code_data >> 7) & 0x3f
    chunjie_d = (code_data >> 0) & 0x1f
    chunjie_m = (code_data >> 5) & 0x3
    span_days = (tm - datetime(year, chunjie_m, chunjie_d)).days
    #print("span_day: ", days_tmp, span_days, chunjie_m, chunjie_d)

    # 日期在该年农历之后
    if (span_days >= 0):
        (leap_month, foo, tmp) = lunar_month_days(year, month)
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
        day += span_days
        #print("----m, d ", month&0xf, day)
        return year, month, day
    # 倒算日历
    else:
        month = 12
        year -= 1
        (leap_month, foo, tmp) = lunar_month_days(year, month)
        #print("++ ", month, leap_month, span_days, tmp)
        while abs(span_days) >= tmp:
            span_days += tmp
            month -= 1
            #print("-- ", month, leap_month, span_days, tmp)
            if (month == leap_month): # tocheck
                #print("  -- ", leap_month)
                (leap_month, tmp, foo) = lunar_month_days(year, month)
                if (abs(span_days) < tmp): # 指定日期在闰月中
                    month = (leap_month<<4) | month
                    break
                span_days += tmp
            (leap_month, foo, tmp) = lunar_month_days(year, month)
        day += (tmp + span_days) # 从月份总数中倒扣 得到天数
        return year, month, day

def show_month1(tm):
    (ly, lm, ld) = get_ludar_date1(tm)
    print("%d年%d月%d日" % (tm.year, tm.month, tm.day), week_str(tm), end='')
    print("\t农历 %s年 %s年%s%s " % (y_lunar(ly), change_year(ly), m_lunar(lm), d_lunar(ld))) # 根据数组索引确定
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

        (ly, lm, ld) = get_ludar_date(datetime(tm.year, tm.month, d))

        if count % 7 == 0:
            print("\n", end='')
        d_str = str(d)
        if d == tm.day:
            d_str = "*" + d_str
        print("%s\t" % (d_str + d_lunar1(lm, ld)), end='')
        #print("%s\t" % (d_str), end='')
        count += 1
    print("")

def show_month(tm):
    (ly, lm, ld) = get_ludar_date(tm)
    print("%d年%d月%d日" % (tm.year, tm.month, tm.day), week_str(tm), end='')
    print("\t农历 %s年 %s年%s%s " % (y_lunar(ly), change_year(ly), m_lunar(lm), d_lunar(ld))) # 根据数组索引确定
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

        (ly, lm, ld) = get_ludar_date(datetime(tm.year, tm.month, d))

        if count % 7 == 0:
            print("\n", end='')
        d_str = str(d)
        if d == tm.day:
            d_str = "*" + d_str
        print("%s\t" % (d_str + d_lunar1(lm, ld)), end='')
        #print("%s\t" % (d_str), end='')
        count += 1
    print("")

def _show_month(year, month, day):
    tmp = datetime(year, month, day)
    show_month1(tmp)
    print('==========================================')

def this_month():
    #print(calendar.month(datetime.now().year, datetime.now().month))
    #print('--------------------------')
    _show_month(datetime.now().year, datetime.now().month, datetime.now().day)

_show_month(1962, 2, 4)
_show_month(1934, 1, 1)
_show_month(2033, 12, 27)
_show_month(2034, 1, 1)
_show_month(2034, 2, 1)
_show_month(2034, 3, 1)
#this_month()
#_show_month(2029, 3, 1)
#_show_month(2047, 6, 1)
#_show_month(1903, 4, 1)

