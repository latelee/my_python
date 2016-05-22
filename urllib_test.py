#!/usr/bin/python
# 注意：如果使用urllib库，源码文件不能是urllib.py。。。。
import urllib.request

request = urllib.request.Request("http://www.baidu.com")
response = urllib.request.urlopen(request)
# 打印网页源码
print(response.read())
