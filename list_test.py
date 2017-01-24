#!/usr/bin/python3
# encoding: utf-8

# list等的测试
# list元素可修改

mylist = list(range(20)) # 依次0~9
print("mylist: %s" % (mylist));
# 前5、后5
print("firt 5: %s last 5: %s" % (mylist[:5], mylist[-5:]));

print("10~12: %s" % (mylist[10:12]));

# 前10个数，每隔5个取1个
print("5::%s" % (mylist[::5]));

mylist = [0]*5 # 5个元素，值为0。。。
print("mylist: %s len: %d" % (mylist, len(mylist)));


mylist = [200, '核力量', 1997, 2000]

print("mylist: %s" % (mylist));

# 索引方式修改元素，注意不能超过范围。
mylist[0] = 400
mylist[3] = 250
del mylist[1] # 删除
print("new mylist: %s" % (mylist));

print("mylist[-1]: %s max number: %d" % (mylist[-1], max(mylist)));
