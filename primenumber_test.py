#!/usr/bin/python3
# encoding: utf-8

from math import sqrt

# 输出指定范围内的素数

def primenumber(lower, upper):
    for num in range(lower,upper + 1):
        # 素数大于 1
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def primenumber1(lower, upper):
    count = 0
    for i in range(lower, upper):
        if is_prime(i):
            count = count + 1
            #print('{}:{}'.format(count, i))
            print(i)

if __name__ == '__main__':
    primenumber(1, 100);
    primenumber1(1, 100);