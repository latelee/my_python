#!/usr/bin/python
# python学习

# 第一个打印语句
print("hello python.")

f = 4/3;
print("input %s " % f)

'''
函数定义，注意后面的冒号
如果是这种形式的注释，又是中文，则要使用UTF(有无BOM均可)
'''

def sayhello(name, age = 25):
    print('Name: %s; Age: %d' % (name, age)) # 多个变量打印
    return 0

sayhello("Jim Kent")
sayhello("Late Lee", 3)

def list_test(self):
    list=[1, 2, 3, 4]
    list.append(10)
    print(list)
    try:
        list.remove(11)
    except ValueError as ve:
        print("there is no 11 in list")
list_test("")

for x in range(0, 10):
    print("x: %d" % x)

# 打印keyword出来
import keyword
print(keyword.kwlist)

# 按任意键退出
input("press any key to quit")