#!/usr/bin/python3
# encoding: utf-8
# Author: Late Lee
# 2017.1.26
# linux+python3

# 抓取HK天文台日历数据
#http://data.weather.gov.hk/gts/time/conversion1_text_c.htm
# 地址：
# http://data.weather.gov.hk/gts/time/calendar/text/T1903c.txt   # T1903C表示1903年日历，其它年份类似

#　算法
# 1、获取天文台网页(big5编码格式)，将每行分隔成列表形式(具体参考上述网址)
#   2063(癸未 - 肖羊)年公曆與農曆日期對照表
#
#   公曆日期              農曆日期    星期        節氣
#   2063年1月1日          初二        星期一
#   2063年1月2日          初三        星期二
#   2063年1月3日          初四        星期三
#   2063年1月4日          初五        星期四
# 。。。
#   2063年1月28日         廿九        星期日
#   2063年1月29日         正月        星期一
#   2063年1月30日         初二        星期二
#   2063年1月31日         初三        星期三
# 2、遍历列表，获取“XX月”那一行，前一行即为上月月份天数 －－所以代码中需要进行减1操作
# 3、由于农历跨年，所以需要全局变量，并且只能在“正月”才能统计上一年日历数据
# 4、闰月根据关键字判断，由于是计算“上月”，所以闰月需要与相同的月份交换
# 5、将需要信息依次保存到yearlist列表。再转换成二进制。最终生成的格式如下：
#        ~23      22~17   16~13    12          11~0
#   农历总天数 离元旦天数 闰几月 闰月天数  1~12月份农历天数
# 6、个别网页个别日历有误，在代码中手工修正
#


import os
import sys
import re
import time
from datetime import date, datetime

import urllib.request

mydict = {'正月': 13, '二月': 2, '三月': 3, '四月': 4, '五月': 5, '六月': 6, '七月': 7, '八月': 8, '九月': 9, '十月': 10, '十一月': 11, '十二月': 12}

# 大小月
monthdict = {'廿九': 0, '三十': 1}

gl = "" # 公历日期
yue = "" # 月份
jieqi = "" #节气
y, m, d = 0, 0, 0 # 数字形式

leapmonth_m, leapmonth_d, leapmonth_is = 0, 0, 0
chunjie_m, chunjie_d = 0, 0  # 春节月份、日期
days_yuandan = 0
day_cnt = 1 # 大小月份标志  为1表示30天，为0表示29天。
y_nl = 0
leap_flag = 0
yearlist=[0]*20 # 第一个即为年份

binary_data = 0

out_f=None

error_f = None

# 网页第一行数据即为“XX月”，需要返回上一网页获取最后一行才是上月真正天数
# 如2014年第一行即为“十二月”，需要返回2013年查看十一月的天数
# 
def get_last_date(url, year):
    new_url = url + "T%dc.txt" % year
    request = urllib.request.Request(new_url)
    response = urllib.request.urlopen(request)
    src = response.read().decode('big5')

    print(" ---check again for %s " % (new_url))
    tmp = src.split('\n')

    # 最后一行可能为空，可能为其它数据，这里倒序查找
    # 如1956年最后一行不是日历数据
    j = 0
    for i in range(1, 100):
        a = tmp[-i].split()
        print("last--: %s" % a)
        if len(a) == 3 or len(a) == 4: # 正常日历数据，列表长度应该为3或4(有节气)
            j = i
            break;
    ret = monthdict[tmp[-j].split()[1]]
    #print(" ret: %d" % (ret))

    return ret

def open_file(file):
    global out_f
    global error_f

    out_f = open(file, "w")
    error_f = open("error.txt", "w")

def get_nongli(url, year1, year2):
    global out_f
    global error_f

    open_file("nongli.txt")

    ###########
    text  = "#####################################################################################\n"
    text += "# 1901~2099年农历数据表\n"
    text += "# powered by Late Lee, http://www.latelee.org \n"
    text += "# %s \n" % (datetime.now())
    text += "#农历数据 每个元素的存储格式如下： \n"
    text += "#      ~23      22~17   16~13    12          11~0  \n"
    text += "# 农历总天数 离元旦天数 闰几月 闰月天数  1~12月份农历天数  \n"
    text += "# 注：1、bit0表示农历1月份天数，为1表示30天，为0表示29天。bit1表示农历2月份天数，依次类推。 \n"
    text += "#     2、bit12表示闰月天数，1为30天，0为29天。bit13~bit17表示第几月是闰月(注：为0表示该年无闰月) \n"
    text += "# 数据来源: http://data.weather.gov.hk/gts/time/conversion1_text_c.htm \n""# 由Jim Kent编写python爬虫强力收集并组装\n"
    text += "#####################################################################################\n"
    ###############################

    text += "g_lunar_month_day = [\n\t"
    out_f.write(text)

    for year in range(year1, year2+1):
        get_the_year(url, year)

    text = "]\n"
    out_f.write(text)
    
    
    out_f.close()
    error_f.close()

# 丢弃
def get_nongli2(url, year1, year2):
    global out_f
    global error_f

    ###########
    text  = "\n\n"
    text += "#农历数据 每个元素的存储格式如下： \n"
    text += "#    12~7         6~5    4~0  \n"
    text += "#  离元旦多少天  春节月  春节日  \n"
    text += "#####################################################################################\n"
    ###############################

    text += "g_lunar_year_day = [\n\t"
    out_f.write(text)

    for year in range(year1, year2+1):
        bbb(url, year)

    text = "]\n"
    out_f.write(text)
    out_f.close()

    error_f.close()

def get_the_year(url, year):
    global leapmonth_m, leapmonth_d, leapmonth_is
    global chunjie_m, chunjie_d
    global day_cnt
    global y, m, d
    global yy_nl
    global yearlist
    global binary_data
    global out_f
    global leap_flag

    new_url = url + "T%dc.txt" % year
    request = urllib.request.Request(new_url)
    response = urllib.request.urlopen(request)
    src = response.read().decode('big5')
    print("parsing for %s" % new_url)

    tmp = src.split('\n')

    # 第三行才是真正的数据
    start_row = 3
    # 1901年起始年，特殊处理
    if year == 1901:
        for i in range(start_row, len(tmp)-start_row):
            start_row += 1 #正月的行数
            tmpp = tmp[i].split()
            gl = tmpp[0]
            gl_tmp = re.findall(r'\d+', gl)
            y, m, d = int(gl_tmp[0]), int(gl_tmp[1]), int(gl_tmp[2])
            yy_nl = y
            yue = tmpp[1]
            if yue != "正月":
                continue
            else:
                # 第一个春节日期
                chunjie_m = m
                chunjie_d = d
                #print("计算农历%d年日历" % (yy_nl), end='')
                #print("  --春节：%d年%d月%d日" % (yy_nl, m, d))
                break;


    total_date = 0
    for i in range(start_row, len(tmp)): # len(tmp)-3
        tmpp = tmp[i].split() # 格式：1903年01月01日 初三 星期四 [节气]
        if (len(tmpp)) == 0:
            break;
        gl = tmpp[0] # 日期，形式不固定，如：1903年01月01日、2011年12月1日
        gl_tmp = re.findall(r'\d+', gl) # 正则表示式获取日期数字，如 1903年01月01日 --> ['1903', '01', '01']
        y, m, d = int(gl_tmp[0]), int(gl_tmp[1]), int(gl_tmp[2])
        #print(y, m, d)
        if len(tmpp) == 4: # 长度为4表明有节气
            jieqi = tmpp[3]
            #print(jieqi, end='')
        yue = tmpp[1]
        #print(gl, yue)
        # 在某年正月时，计算上年的日历信息
        if yue == "正月":
            day_cnt = monthdict[tmp[i-1].split()[1]] # 正月才能确认腊月天数
            yy_nl = y - 1
            yearlist[0] = yy_nl
            yearlist[mydict[yue[0:]]-1] = day_cnt
            # 由于计算月份日期是在次月方知，所以闰月与非闰月是相反的 (如得到的闰五月日期数实为五月日期数)，这里调换
            if leap_flag == 1:
                #print("!!! 有闰月 %d %d " % (leapmonth_m, leapmonth_d))
                changed_tmp = leapmonth_d
                leapmonth_d = yearlist[leapmonth_m]
                yearlist[leapmonth_m] = changed_tmp
                leap_flag = 0
            # 消掉全局变量，全年没有闰月时，清零
            else:
                leapmonth_m, leapmonth_d, leapmonth_is = 0, 0, 0

            # 计算该年正月离元旦天数
            days_yuandan = (datetime(year, chunjie_m, chunjie_d) - datetime(year, 1, 1)).days
            
            # 合并成二进制准备的列表
            i = 13
            yearlist[i] = leapmonth_d # 闰月天数 1为大月30gd ，0为小月29天
            i+=1
            yearlist[i] = leapmonth_m # 闰月月份
            i+=1
            yearlist[i] = days_yuandan # 该年正月离元旦天数
            i+=1
            #yearlist[i] = chunjie_d
            #i+=1
            #yearlist[i] = chunjie_m
            #i+=1

            #############################################################
            #　转换成二进制
            for j in range(1, 13):
                k = yearlist[j]
                if k == 1:
                    binary_data |= k << (j-1)# 月份
                    total_date += 30
                else:
                    total_date += 29
            if leapmonth_m:
                if leapmonth_d:
                    total_date += 30
                else:
                    total_date += 29
            j = 13
            binary_data |= yearlist[j] << 12 # 闰月天数
            j+=1
            binary_data |= yearlist[j] << 13 # 闰月月份
            j+=1
            binary_data |= yearlist[j] << 17 # 该年正月离元旦天数
            binary_data |= total_date << 23 # 该年农历日期总天数

            ######################################################
            #text = str(hex(binary_data)) + ", "
            text = "0x%05x, " % binary_data # 格式化好一点，前补0
            if yy_nl % 10 == 0:
                text += "# %d ~ %d \n\t" % (yy_nl-10+1, yy_nl)

            out_f.write(text)
            ######################################################
            #j+=1
            #binary_data |= yearlist[j] << 24
            #j+=1
            #binary_data |= yearlist[j] << 25
            #print("%d月 有%d天" % (mydict[yue[0:]]-1, day_cnt))
            print("农历%d年日历小结　" % (yy_nl))
            print("  --春节：%d年%d月%d日 离该年元旦有%d天 农历总日期：%d" % (yy_nl, chunjie_m, chunjie_d, days_yuandan, total_date))
            if leapmonth_m != 0:
                if leapmonth_d:
                    print("  --闰%d月 30天" % (leapmonth_m))
                else:
                    print("  --闰%d月 29天" % (leapmonth_m))
                
            print("数据: ", yearlist)

            print("生成二进制数据：%s" % str(hex(binary_data)))
            yearlist=[0]*20
            binary_data = 0
            #print("-------------------\n计算农历%d年日历" % (y))
            chunjie_m = m
            chunjie_d = d
            #print("    -- new春节：%d年%d月%d日" % (y, chunjie_m, chunjie_d))
        elif yue.find('月') != -1:
            if i == start_row:
                day_cnt = get_last_date(url, year - 1)
            else:
                try:
                    day_cnt = monthdict[tmp[i-1].split()[1]]
                except Exception:
                    print("error data at: %s " % (gl))
                    error_text = "error data found: %s source: %s\n" %(new_url, tmpp)
                    error_f.write(error_text)

                    # 下面这些是格式错误的，要特殊处理。。。
                    if gl == '2053年12月10日': # 前一天：农历十月三十 星期二
                        day_cnt = 1
                    if gl == '2056年3月16日':  # 前一天：农历正月三十 星期三
                        day_cnt = 1
                    if gl == '2063年7月26日': # 前一天：农历六月三十 星期三
                        day_cnt = 1
                    if gl == '2063年10月22日': # 前一天：农历八月三十 星期日
                        day_cnt = 1
                    if gl == '2063年12月20日': # 前一天：农历十月三十 星期三
                        day_cnt = 1
            if yue.find('閏') != -1:
                leap_flag = 1
                leapmonth_is = 1
                leapmonth_m = mydict[yue[1:]] # 闰月在该月后面，所以无须减1，如五月后面就是闰五月
                leapmonth_d = day_cnt
                #print("闰%d月 有%d天 %d %d %d" % (mydict[yue[1:]], day_cnt, leapmonth_is, leapmonth_d, leapmonth_m))
            else:
                yearlist[mydict[yue[0:]]-1] = day_cnt
                #print("%d月 有%d天" % (mydict[yue[0:]]-1, day_cnt))
    #time.sleep(1) # 不要那么快访问服务器，以防被拒绝


need_write = 0

def bbb(url, year):
    global chunjie_m, chunjie_d
    global days_yuandan
    global day_cnt
    global y, m, d
    global yy_nl
    global yearlist
    global binary_data
    global out_f
    global need_write

    new_url = url + "T%dc.txt" % year
    request = urllib.request.Request(new_url)
    response = urllib.request.urlopen(request)
    src = response.read().decode('big5')
    print("parsing for %s" % new_url)

    tmp = src.split('\n')

    # 第三行才是真正的数据
    start_row = 3
    total_date = 0
    for i in range(start_row, len(tmp)): # len(tmp)-3
        tmpp = tmp[i].split() # 格式：1903年01月01日 初三 星期四 [节气]
        if (len(tmpp)) == 0:
            break;
        gl = tmpp[0] # 日期，形式不固定，如：1903年01月01日、2011年12月1日
        gl_tmp = re.findall(r'\d+', gl) # 正则表示式获取日期数字，如 1903年01月01日 --> ['1903', '01', '01']
        y, m, d = int(gl_tmp[0]), int(gl_tmp[1]), int(gl_tmp[2])
        #print(y, m, d)
        if len(tmpp) == 4: # 长度为4表明有节气
            jieqi = tmpp[3]
            #print(jieqi, end='')
        yue = tmpp[1]
        #print(gl, yue)
        if yue == "正月":
            chunjie_m = m
            chunjie_d = d
            need_write += 1
            days_yuandan = i - start_row

        # 当正月再计算
        if need_write == 2:
            need_write = 0
            print("%d年：正月：%d月%d日 离该年元旦有%d天" % (year, chunjie_m, chunjie_d, days_yuandan))
            binary_data |= chunjie_d << 0
            binary_data |= chunjie_m << 5
            binary_data |= days_yuandan << 7
            #text = str(hex(binary_data))
            text = "0x%04x, " % binary_data # 格式化好一点，前补0
            bin_text = str(bin(binary_data))
            print("二进制数据: %s %s" % (text, bin_text))
            if year % 10 == 0:
                text += "# %d ~ %d \n\t" % (year-10+1, year)

            out_f.write(text)

            binary_data = 0
    #time.sleep(2) # 不要那么快访问服务器，以防被拒绝

def init_python_env():
    if sys.version_info.major == 2:
       reload(sys)
       sys.setdefaultencoding('utf8')

#### main
if __name__ == '__main__':
    init_python_env()

    year1 = 1901
    year2 = 2100
    get_nongli("http://data.weather.gov.hk/gts/time/calendar/text/", year1, year2) # 2100  1901
    print('-------------------------------------------\n')
    #get_nongli2("http://data.weather.gov.hk/gts/time/calendar/text/", year1, year2) # 2100  1901
