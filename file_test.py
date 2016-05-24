#!/usr/bin/python
# python类学习

import os

test = '''This is a program about file I/O.

Author: Late Lee
Date: 2016.5.14'''

# 打开方式有：w r a r+ w+ a+
f = open("test.txt", "w")
f.write(test) # write text to file
f.close()

# 默认为r
f = open("test.txt")
print("name: %s --%s size:%d" % (os.path.basename(f.name), os.path.dirname(f.name), os.path.getsize(f.name)))


while True:
    line = f.readline()
    if len(line) == 0:  # zero length indicates the EOF of the file
        break
    print(line)

f.close()

##################################
## 读配置文件

try:
    f = open('cdist.txt', 'r')
    while True:
        l = f.readline()
        if l == '': # 结束
            break

        if len(l) > 0 and l[0] == '#':
            continue

        s = l.strip().split() #　分割，生成不同个数的列表，如['a','b','c']
        if len(s) == 2:
            print("%s == %s" % (s[0], s[1]))
            print("%s" % s[0][0]) #第一个字符
except:
    raise