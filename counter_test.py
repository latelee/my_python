#!/usr/bin/python
# encoding: utf-8

# 计数测试示例

import collections

def counter_test():
    ''' simple counter test '''
    c = collections.Counter()
    a='hello'
    c.update({a:1}) # 这种格式是字符串hello的统计
    c.update({a:1})
    c.update({a:1})
    print("counter: %s" % c)

    c.update(a) # 这种形式是h e l l o的统计，其中l出现2次
    print("counter: %s" % c)

    # 将counter转换成list
    l_c = list(c.elements())
    print("counter elements: %s" % l_c)

    print("counter values: %s" % c.values())
    print("counter items: %s" % c.items())
    print("counter most_common: %s" % c.most_common()) # 默认返回所有元素，如果指定3，则返回前面3个

    print("counter most_common list: %s" % list(c.most_common()))

    # 打印出来
    for key, count in c.most_common():
        print("%s: %d" % (key, count))
        
# 统计文件中字母出现的频率
def file_counter(file):
    c = collections.Counter()
    with open(file, "rt") as f:
        for line in f:
            c.update(line.rstrip().lower())
    print("top 10:")
    # 打印出来
    for key, count in c.most_common(10):
        print("%s: %d" % (key, count))


#### main
if __name__ == '__main__':
    #counter_test()
    file_counter("test.txt")






        