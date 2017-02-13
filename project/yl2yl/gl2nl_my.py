#!/usr/bin/python3
# encoding: utf-8
# Author: Late Lee
# 2017.2.11

#####################################################################################
# 1901~2100年阴历数据表
# powered by Late Lee, http://www.latelee.org 
# 2017-02-12 23:02:06.546446 
#阴历数据 每个元素的存储格式如下： 
#    ~21       20~18   17~14    13         12         11~0  
# 农历总日数  立春日  闰几月 闰月日数  是否闰月  1~12月份农历日数  
# 注：1、bit0表示农历1月份日数，为1表示30天，为0表示29天。bit1表示农历2月份日数，依次类推。 
#    2、bit12表示该年是否有闰月，bit13表示闰月日数，1为30天，0为29天。bit17~bit14表示第几月是闰月 
# 数据来源: http://data.weather.gov.hk/gts/time/conversion1_text_c.htm 由Jim Kent编写python爬虫强力分析
#####################################################################################
my_g_lunar_month_day = [
	0x2c540752, 0x2c740ea5, 0x2ff55b2a, 0x2c50064b, 0x2c700a9b, 0x30153aa6, 0x2c54056a, 0x2c740b59, 0x30149baa, 0x2c540752, # 1901 ~ 1910 
	0x30159da5, 0x2c500b25, 0x2c500a4b, 0x30157a4b, 0x2c5402ad, 0x2c74056b, 0x301095b5, 0x2c700da9, 0x3015fe92, 0x2c500e92, # 1911 ~ 1920 
	0x2c500d25, 0x30155d2d, 0x2c540a56, 0x2c5402b6, 0x30313ad5, 0x2c5006d4, 0x2c740ea9, 0x30109f4a, 0x2c500e92, 0x2ff596a6, # 1921 ~ 1930 
	0x2c54052b, 0x2c740a57, 0x30117956, 0x2c700b5a, 0x2c5406d4, 0x3010f761, 0x2c500749, 0x3015fb13, 0x2c540a93, 0x2c54052b, # 1931 ~ 1940 
	0x3011b51b, 0x2c740aad, 0x2c54056a, 0x30313da5, 0x2c500ba4, 0x2c500b49, 0x30149d4b, 0x2c540a95, 0x3011daad, 0x2c500536, # 1941 ~ 1950 
	0x2c700aad, 0x30117aca, 0x2c5005b2, 0x2c700da5, 0x3014fea2, 0x2c540d4a, 0x2ff21595, 0x2c700a97, 0x2c500556, 0x30119575, # 1951 ~ 1960 
	0x2c700ad5, 0x2c5006d2, 0x30151755, 0x2c740ea5, 0x2c30064a, 0x3010d64f, 0x2c700a9b, 0x3011dada, 0x2c50056a, 0x2c700b69, # 1961 ~ 1970 
	0x30155bb2, 0x2c540b52, 0x2c500b25, 0x30111b2b, 0x2c500a4b, 0x30121aab, 0x2c5002ad, 0x2c70056d, 0x3015b5a9, 0x2c700da9, # 1971 ~ 1980 
	0x2c500d92, 0x30111e95, 0x2c500d25, 0x30129e4d, 0x2c500a56, 0x2c5002b6, 0x301192f5, 0x2c7006d5, 0x2c700ea9, 0x30115f52, # 1981 ~ 1990 
	0x2c500e92, 0x2c500d26, 0x2ff0d52e, 0x2c700a57, 0x30121ad6, 0x2c50035a, 0x2c7006d5, 0x30115b69, 0x2c500749, 0x2c500693, # 1991 ~ 2000 
	0x30111a9b, 0x2c50052b, 0x2c700a5b, 0x30109aae, 0x2c50056a, 0x3031ddd5, 0x2c500ba4, 0x2c500b49, 0x30115d53, 0x2c500a95, # 2001 ~ 2010 
	0x2c50052d, 0x3011155d, 0x2c700ab5, 0x30125baa, 0x2c5005d2, 0x2c700da5, 0x3011be8a, 0x2c500d4a, 0x2c500c95, 0x300d1a9e, # 2011 ~ 2020 
	0x2c4c0556, 0x2c700ab5, 0x30109ada, 0x2c5006d2, 0x30119765, 0x2c500725, 0x2c50064b, 0x300d5657, 0x2c6c0cab, 0x2c50055a, # 2021 ~ 2030 
	0x3010d56e, 0x2c700b69, 0x3012df52, 0x2c500b52, 0x2c500b25, 0x300dbd0b, 0x2c500a4b, 0x2c5004ab, 0x301152bb, 0x2c7005ad, # 2031 ~ 2040 
	0x2c6c0b6a, 0x30109daa, 0x2c500d92, 0x300ddea5, 0x2c500d25, 0x2c500a55, 0x30117a4d, 0x2c5004b6, 0x2c6c05b5, 0x3010f6d2, # 2041 ~ 2050 
	0x2c700ec9, 0x300e1f92, 0x2c4c0e92, 0x2c4c0d26, 0x2ff1b516, 0x2c6c0a57, 0x2c4c0556, 0x30113365, 0x2c700755, 0x2c500749, # 2051 ~ 2060 
	0x300cd74b, 0x2c4c0693, 0x3011daab, 0x2c4c052b, 0x2c6c0a5b, 0x30115aba, 0x2c50056a, 0x2c700b65, 0x300d1baa, 0x2c4c0b4a, # 2061 ~ 2070 
	0x30121d95, 0x2c4c0a95, 0x2c4c052d, 0x3011956d, 0x2c700ab5, 0x2c5005aa, 0x300d15d5, 0x2c6c0da5, 0x2c500d4a, 0x300cde4d, # 2071 ~ 2080 
	0x2c4c0c96, 0x300ddcce, 0x2c500556, 0x2c700ab5, 0x300d7ad2, 0x2c4c06d2, 0x2c6c0ea5, 0x2fed172a, 0x2c4c068b, 0x300e1697, # 2081 ~ 2090 
	0x2c5004ab, 0x2c70055b, 0x300db556, 0x2c6c0b6a, 0x2c4c0752, 0x300d1b95, 0x2c4c0b45, 0x2c4c0a8b, 0x30109a4f, ]

#==================================================================================

from datetime import date, datetime
import calendar 

START_YEAR = 1901

LM_BIT = 12
LM_DAY_BIT = 13
LM_NUM_BIT = 14

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
    show_month(tmp)
    print('==========================================')

def this_month():
    #print(calendar.month(datetime.now().year, datetime.now().month))
    #print('--------------------------')
    _show_month(datetime.now().year, datetime.now().month, datetime.now().day)

this_month()
_show_month(2034, 1, 1)
_show_month(2047, 6, 1)
#_show_month(1903, 4, 1)

