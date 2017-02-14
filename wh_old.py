#!/usr/bin/python
# encoding: utf-8

# 外汇计算
# 注：不考虑交叉盘

# EUR/USD 1手表示10万欧元
# USD/JPY 1手表示10万美元

import string 

# 美元人民币汇率
usbrmb_quote = 6.8491


# 计算点值
# usd为1表示USD在前面
# lotsize 手数，如1表示1手，0.01表示0.01手
# tick_size 最小变动点，如0.001、0.0001。
# current_quote：当前汇率 (用于USB在前面的)
# 一手为10万基础货币
def calc_pip(usd, lotsize, tick_size, current_quote=1):
    if usd == 0: # eg. EUR/USD
        pip = lotsize * 100000 * tick_size # 手数 * 最小变动点
        return pip
    else: # eg. USD/JPY
        pip = lotsize * 100000 * tick_size / current_quote # 手数 * 最小变动点
        return pip

def calc_pip2(name, lotsize, current_quote='1'):
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

    usd = 0;
    s = name.strip().split('/')
    if len(s) == 2:
        if (s[0].lower() == 'usd'): # usd/xxx
           usd = 1
        #elif (s[1].lower() == 'usd'): # xxx/usd
        #    usd = 0
    else:
        if (name[0:3].lower() == 'usd'): # usd/xxx
           usd = 1
        #elif (name[3:6].lower() == 'usd'): # xxx/usd
        #    usd = 0

    if usd == 0: # eg. EUR/USD
        pip = lotsize * 100000 * base # 手数 * 最小变动点
        return pip
    else: # eg. USD/JPY
        pip = lotsize * 100000 * base / float(current_quote) # 手数 * 最小变动点
        return pip

# new
def calc_pip1(name, lotsize=1, tick_size=1, current_quote=1):
    usd = 0;
    s = name.strip().split('/')
    if len(s) == 2:
        if (s[0].lower() == 'usd'): # usd/xxx
           usd = 1
        #elif (s[1].lower() == 'usd'): # xxx/usd
        #    usd = 0
    else:
        if (name[0:3].lower() == 'usd'): # usd/xxx
           usd = 1
        #elif (name[3:6].lower() == 'usd'): # xxx/usd
        #    usd = 0
    if usd == 1: # eg. USD/JPY
        pip = lotsize * 100000 * tick_size / current_quote # 手数 * 最小变动点
    else: # eg. EUR/USD
        pip = lotsize * 100000 * tick_size # 手数 * 最小变动点
    return pip

# 点值盈亏计算
# op 买卖操作
# quote1 建仓价格 quote2 现在价格
def profit(op, quote1, quote2):
    losse = 1 # 盈亏标志
    if (op == "buy" and quote1 > quote2) or (op == "sell" and quote1 < quote2):
        losse = -1

    tick = abs(quote1 - quote2) / 0.00001 # 多少个点，计算绝对值
    tick *= losse
    print("tick: %d" % tick);
    tick = tick * calc_pip(0, 0.1, 0.00001, quote2)
    print("profit: $%.2f(RMB:%.2f)" % (tick, tick*usbrmb_quote))

def profit1(name, op, lotsize, quote1, quote2):
    #tmp=string.atof(tick_size)
    base = 1.0
    #tmp = "%f" % tick_size
    #print(quote2);
    l = len(quote2)
    for i in range(l):
        ch = quote2[l - i - 1]
        if (ch == '.'):
            break;
        base /= 10.00

    losse = 1 # 盈亏标志
    if (op == "buy" and quote1 > quote2) or (op == "sell" and quote1 < quote2):
        losse = -1

    tick = abs(float(quote1) - float(quote2)) / base # 由当前价格计算出盈/亏多少个点，计算绝对值
    tick *= losse
    print("tick: %d" % tick);
    tick = tick * calc_pip2(name, lotsize, quote2)
    print("profit: $%.2f(RMB:%.2f)" % (tick, tick*usbrmb_quote))
# 杠杆计算

# 波动风险计算


#### main
if __name__ == '__main__':
    '''pip = calc_pip2("usd/jpy", 0.1, '113.601')
    print("pip: $%.4f" % pip)
    pip = calc_pip1("usd/jpy", 0.1, 0.001, 113.601) # USD/JPY
    print("pip: $%.4f" % pip)
    pip = calc_pip2("eur/usd", 0.1, '1.07283')
    print("pip: $%.4f" % pip)
    pip = calc_pip1("eur/usd", 0.1, 0.00001, 1.07283) # USD/JPY
    print("pip: $%.4f" % pip)'''
    
    
    #print("pip: $%.2f" % pip)
    #pip = calc_pip1("usd/jpy", 0.1, 0.001, 113.502) # USD/JPY
    #print("pip: $%.2f" % pip)

    profit("sell", 1.05957, 1.06074)
    #profit1("eur/usd", "sell", 1, '1.05957', '1.06074')
    profit1("usd/cfd", "buy", 3, '1.2000', '1.1950') # 和网上计算一致
    profit1("eur/usd", "sell", 2, '1.4350', '1.4400')
    profit1("usd/jpy", "buy", 0.1, '113.923', '113.326')
    
    #calc_pip1("usdjpy");
    #calc_pip1("eurusd");
    # 按任意键退出
    #input("press any key to quit")