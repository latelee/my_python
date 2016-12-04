#!/usr/bin/python3
# encoding: utf-8
'''
Created on 2016年6月23日

@author: liuc
使用find对百度搜索的天气报告做解析并打印
'''

import urllib.request
import time

import json

index = '</span><span class=\"op_pm25_grade3\">'.find('grade')

#citys = ['北京','天津','石家庄','太原','西安','重庆','成都','贵阳','上海','苏州','杭州','南京','广州','深圳','厦门','武汉','南宁','柳州']
citys = ['北京', '上海', '广州', '深圳', '南宁', '岑溪']
time = time.strftime('%Y-%m-%d')
for i in range(len(citys)):
    citys_q = urllib.parse.quote(citys[i])
    url_aqi = ('http://www.baidu.com/s?ie=utf-8&bs=' + citys_q + 'aqi&f=8&rsv_bp=1&rsv_spt=3&wd=' + citys_q + 'aqi&inputT=0')
    url_tem = 'http://www.baidu.com/s?ie=utf-8&bs=' + citys_q + '{}&f=8&rsv_bp=1&rsv_spt=3&wd='.format(urllib.parse.quote('天气')) + citys_q + '{}&inputT=0'.format(urllib.parse.quote('天气'))
    #print('地址：'+url_aqi)
    #print('地址：'+url_tem)
    content_aqi = urllib.request.urlopen(url_aqi).read().decode('utf-8')
    content_tem = urllib.request.urlopen(url_tem).read().decode('utf-8')
    index_aqi_1 = content_aqi.find('class="op_pm25_graexp\">')
    index_aqi_2 = content_aqi.find('</span><span class=\"op_pm25_grade')
    index_aqi_grade_1 = content_aqi.find('</span><span class=\"op_pm25_grade')
    index_aqi_grade_2 = content_aqi[index_aqi_grade_1:index_aqi_grade_1+200].find('</span></div>')
    index_aqi_grade_2 += index_aqi_grade_1;
    index_tem_1 = content_tem.find('twoicon_temp\">')
    index_tem_2 = content_tem.find('<sup>℃</sup>')
    print(citys[i]+':')
    if (index_aqi_1 != -1): 
        print('空气质量指数：' + content_aqi[index_aqi_1 + 23:index_aqi_2] + '    等级：' + content_aqi[index_aqi_grade_1+36:index_aqi_grade_2])
    print ('温度：' + content_tem[index_tem_1 + 14:index_tem_2] + '     时间：' + time)