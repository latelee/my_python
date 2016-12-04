#!/usr/bin/python3
# encoding: utf-8

# 根据mac号查询对应的公司名字
# TODO　解析一个conf文件，而不是写死mac


# 注意：如果使用urllib库，源码文件不能是urllib.py。。。。
import urllib.request
import json

mac_addr = ["a4:44:d1", "0c:f4:05", "08:00:20", "fc:d7:33", "da:a1:19", "7c:e9:d3", "94:65:9c", "d0:c7:c0", "68:3e:34", 
            "9c:4e:36", "a4:d1:8c", "08:11:96", "30:0c:23", "c0:ee:fb", "ac:bc:32", "34:80:b3"]

def simple_test():
    for i in range(len(mac_addr)):
        oui_url = ("http://www.macvendorlookup.com/api/v2/" + mac_addr[i]) 
        request = urllib.request.Request(oui_url)
        response = urllib.request.urlopen(request)
        #print(response.read())

        # 打印网页源码
        #print(response.read())
        encodedjson = bytes.decode(response.read()) # bytes to string
        #print(encodedjson)
        if (encodedjson == ''):
            #print("empty....")
            continue
        decodejson = json.loads(encodedjson)
        #d1 = json.dumps(decodejson,sort_keys=True,indent=4)
        #print(d1)
        #print(type(decodejson))　# 这时已经是一个list
        # 打印需要的字段
        print("mac地址：" + mac_addr[i] + "\t" + decodejson[0]["country"] + "  公司：" + decodejson[0]["company"] + "\t地址：" + decodejson[0]["addressL3"])

#### main
if __name__ == '__main__':
    print("url test")
    simple_test()



