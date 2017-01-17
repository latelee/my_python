#!/usr/bin/python
# encoding: utf-8

import os
import datetime
import time

SRC = "gbkuni30.txt"
DST = "gbkuni30_gen1.h"
ARRAY = "gbkuni30"

buffer = [0]*65535 # 初始化65535个空列表
max_num = 0

try:
    f = open(SRC, 'r')
    while True:
        l = f.readline()
        if l == '':
            break;
        s = l.strip().split(':') #以:分割，生成不同个数的列表
        if len(s) == 2:
            x1 = int(s[0], 16) # 字符串转换为十六进制
            x2 = int(s[1], 16)
            buffer[x2] = x1 # 针对索引赋值
            if x2 > max_num:
                max_num = x2
            #print("%04x %04x" % (x2, x1))
    print("max num %d %x len: %d" % (max_num, max_num, len(buffer)))
except:
    raise

f = open(DST, "w")

test = "/**********************************************************************************/\n"
test += "/* GBK(GB18030) to UNICODE table, powered by Late Lee */\n"
test += "/* http://www.latelee.org */\n"
test += "/* %s */\n" % (datetime.datetime.now())
test += "/* The source file comes from: */\n"
test += "/* http://icu-project.org/repos/icu/data/trunk/charset/source/gb18030/gbkuni30.txt*/\n"

test += "/**********************************************************************************/\n"

test += "#ifndef __GBK2UNICODE__H\n"
test += "#define __GBK2UNICODE__H\n\n"

test += "static unsigned short %s[] = \n{\n" % (ARRAY)

f.write(test) # write text to file
####
cnt=0
for i in range(0x8140, max_num+1):
    #print("%x -- 0x%x" % (i, buffer[i]))
    ch = "0x%04x, " % (buffer[i])
    f.write(ch)
    cnt+=1;
    if cnt % 10 == 0:
        tmp = " // line num %d \n" % (cnt / 10 - 1)
        f.write(tmp)


########
test= "\n"
test+= "};\n\n"
test+= "#endif //__GBK2UNICODE__H\n"
    
f.write(test) # write text to file
f.close()
