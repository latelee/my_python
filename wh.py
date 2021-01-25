#!/usr/bin/python
# encoding: utf-8
# Author: Late Lee

# 外汇计算
# 注：不考虑交叉盘、不考虑隔夜利息
# 计值单位为美元(同时转换RMB)，其它不考虑

# EUR/USD 1手表示10万欧元
# USD/JPY 1手表示10万美元

import string 

# 美元人民币汇率
USBRMB_QUOTE = 6.8491
BASE_CURRENT = 100000 # 一手为10万基础货币

def get_usd(name):
    usd = -1;
    s = name.strip().split('/')
    if len(s) == 2:
        if (s[0].lower() == 'usd'): # usd/xxx
           usd = 1
        elif (s[1].lower() == 'usd'): # xxx/usd
            usd = 0
    else: # no '/'
        if (name[0:3].lower() == 'usd'): # usdxxx
           usd = 1
        elif (name[3:6].lower() == 'usd'): # xxxusd
            usd = 0
    return usd

# 计算点值
# usd为货币种类
# lotsize 手数，如1表示1手，0.01表示0.01手
# tick_size 最小变动点，如0.001、0.0001(不同平台显示不同，显示值也不同，但本质相同)。
# current_quote：当前汇率 (用于USB在前面的)
# 一手为10万基础货币
def calc_pip(name, lotsize=1, tick_size=1, current_quote=1):
    usd = usd = get_usd(name)
    if usd == 1: # eg. USD/JPY
        pip = lotsize * BASE_CURRENT * tick_size / current_quote # 手数 * 最小变动点
    else: # eg. EUR/USD
        pip = lotsize * BASE_CURRENT * tick_size # 手数 * 最小变动点
    return pip

# 计算点值 另一种方式
def calc_pip1(name, lotsize, current_quote='1'):
    #tmp=string.atof(tick_size)
    base = 1.0
    #tmp = "%f" % tick_size
    #print(current_quote);
    l = len(current_quote)
    for i in range(l):
        ch = current_quote[l - i - 1]
        if (ch == '.'):
            break;
        base /= 10.00
    #print("base: %f" % (base));

    usd = get_usd(name)
    if usd == 0: # eg. EUR/USD
        pip = lotsize * BASE_CURRENT * base # 手数 * 最小变动点
        return pip
    elif usd == 1: # eg. USD/JPY
        pip = lotsize * BASE_CURRENT * base / float(current_quote) # 手数 * 最小变动点
        return pip

# 交易盈亏计算
# name 交易货币种类
# op 买卖操作
# quote1 建仓价格 quote2 现在价格
def profit(name, op, lotsize, quote1, quote2):
    losse = 1 # 盈亏标志
    if (op == "buy" and quote1 > quote2) or (op == "sell" and quote1 < quote2):
        losse = -1
    
    usd = get_usd(name)
    if usd == 0: # eg. EUR/USD
        value = abs(quote2 - quote1) * losse * lotsize * 100000
    elif usd == 1: # eg. USD/JPY
        value = abs(quote2 - quote1) * losse * lotsize * 100000 / quote2

    print("profit: $%.4f(RMB:%.4f)" % (value, value*USBRMB_QUOTE))
    return value, value*USBRMB_QUOTE

# 保证金计算
def bond(name, lever, lotsize, quote=1):
    usd = get_usd(name)
    if usd == 0: # eg. EUR/USD
        value = lotsize * BASE_CURRENT * quote # tocheck
    elif usd == 1: # eg. USD/JPY
        value = lotsize * BASE_CURRENT

    value /= lever
    print("bond: $%.4f(RMB:%.4f)" % (value, value*USBRMB_QUOTE))
    return value, value*USBRMB_QUOTE

# 波动风险计算


#### main
if __name__ == '__main__':
    
    # 点值计算
    pip = calc_pip("usd/jpy", 0.1, 0.001, 113.502) # USD/JPY
    print("pip: $%.4f" % pip)
    pip = calc_pip1("usd/jpy", 100, '112.961')
    print("pip: $%.4f" % pip)

    # 盈亏计算
    profit("eur/usd", "sell", 2, 1.4350, 1.4400)
    a, b = profit("usd/jpy", "buy", 0.1, 113.923, 113.976)
    #print("my profit: $%.4f(RMB:%.4f)" % (a, b))
    profit("eur/usd", "buy", 1, 1.07490, 1.07590)
    
    profit("usd/jpy", "buy", 0.3, 116.542, 112.765)
    
    # 保证金计算
    bond('EUR/USD', 200, 3, 1.13798)
    bond('USD/JPY', 400, 0.1, 112.950)

    # 按任意键退出
    #input("press any key to quit")