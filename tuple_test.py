#!/usr/bin/python3
# encoding: utf-8

# tuple的测试

tup = tuple(range(20)) # 依次0~19
print(tup);

# 前5、后5
print("firt 5: %s last 5: %s" % (tup[:5], tup[-5:]));

tup = (); # 空
print(tup);

tup = (0,); # 空
print(tup);

tup = ('Apple', 'hehe', 1997, 2000)
# tup[0] = 100 # 不能修改
print("tup: %d" % (tup[2]));