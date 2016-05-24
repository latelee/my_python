#!/usr/bin/python3
# encoding: utf-8

# 注意：如果使用urllib库，源码文件不能是urllib.py。。。。
import urllib.request

def simple_test():
    request = urllib.request.Request("http://www.baidu.com")
    response = urllib.request.urlopen(request)
    # 打印网页源码
    print(response.read())

def test2():
    with urllib.request.urlopen('http://www.178448.com/fjzt-1.html?page=1') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))


#### main
if __name__ == '__main__':
    print("url test")
    test2()



