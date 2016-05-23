#!/usr/bin/python
# encoding: utf-8

# ��������ʾ��

import collections

def counter_test():
    ''' simple counter test '''
    c = collections.Counter()
    a='hello'
    c.update({a:1}) # ���ָ�ʽ���ַ���hello��ͳ��
    c.update({a:1})
    c.update({a:1})
    print("counter: %s" % c)

    c.update(a) # ������ʽ��h e l l o��ͳ�ƣ�����l����2��
    print("counter: %s" % c)

    # ��counterת����list
    l_c = list(c.elements())
    print("counter elements: %s" % l_c)

    print("counter values: %s" % c.values())
    print("counter items: %s" % c.items())
    print("counter most_common: %s" % c.most_common()) # Ĭ�Ϸ�������Ԫ�أ����ָ��3���򷵻�ǰ��3��

    print("counter most_common list: %s" % list(c.most_common()))

    # ��ӡ����
    for key, count in c.most_common():
        print("%s: %d" % (key, count))
        
# ͳ���ļ�����ĸ���ֵ�Ƶ��
def file_counter(file):
    c = collections.Counter()
    with open(file, "rt") as f:
        for line in f:
            c.update(line.rstrip().lower())
    print("top 10:")
    # ��ӡ����
    for key, count in c.most_common(10):
        print("%s: %d" % (key, count))


#### main
if __name__ == '__main__':
    #counter_test()
    file_counter("test.txt")






        