#!/usr/bin/python3
# encoding: utf-8
# 执行系统ping命令，失败发送邮件通知对应的人。
# 实际就由crontab来定时执行此程序
# ifconfig eth0 add 192.168.1.87
# 隐藏账户信息
import os
import base64

import smtplib
import email.utils
from email.mime.text import MIMEText
from email.header import Header

import time
import datetime

import subprocess

# 接收邮件地址
to_email = ['aa@163.com'] # 多个收件人，在其后添加
#to_email = ['aa@163.com', 'bb@163.com']

# 发送者信息
smtpserver = 'smtp.exmail.qq.com'
snd_email = 'XXX@XXX.com.cn'
username = snd_email
password = b'333Fsd2F5MjAxMUpKTA=='

def send_email(to_list, sub, content):
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = Header("py机器人", 'utf-8')
    #msg['From'] = email.utils.formataddr(('py发送者', snd_email)) # 发件人：py发送者<xxx@163.com>
    #msg['From'] = snd_email
    #msg['To'] = to_list
    msg['To'] = ",".join(to_list)
    #msg['Date'] = formatdate(localtime=True)

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, bytes.decode(base64.b64decode(password)))
        smtp.sendmail(snd_email, to_list, msg.as_string())
        smtp.quit()
        return 0
    except Exception as e:
        print(str(e))
        return -1

#######################################
# ping -c 2 172.18.44.63 | grep '0 received' | wc -l
def ping_device(ip):
    cmd = "ping -c 1 " + ip  + " | grep '0 received' | wc -l"
    t = os.popen(cmd)
    #print("cmd: %s" % cmd)
    str = t.readline()
    if len(str) > 0 and str[0] == '0':
        #print("ping ok")
        ret = 0
    else:
        #print("no ping")
        ret = -1
    #print("%s " % str)
    t.close()
    return ret
    
######################################
def wirte_file(content):
    f = open("/home/sig/test.txt", "a+")
    tmp = content + "\n"
    f.write(tmp) # write text to file
    f.close()

################################
device_ip = ["172.18.37.121", "192.168.1.11", "172.18.44.65", "192.168.1.65", "172.18.44.112", "192.168.1.112"]
# main...
if __name__ == '__main__':
    total_ret = 0
    buffer = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " "
    nowtime = datetime.datetime.now().strftime("%H:%M")
    buffer += "ping测试结果:</br>\n"

    for i in range(len(device_ip)):
        ret = ping_device(device_ip[i])
        if ret != 0:
            total_ret += 1;
        buffer += "ping设备IP %s 结果: %s </br>\n" % (device_ip[i], ret and "失败" or "成功") # 组装
        time.sleep(0.1)
    
    buffer += "</br></br> [本邮件为系统自动发送，勿回复] </br>\n"
    buffer += "</br>\n"

    # 如果出错,立即发送
    if total_ret > 0:
        wirte_file(buffer)
        send_email(to_email, "ping测试结果", buffer)
        #print("ping  fail")
    # 否则17点发送
    else:
        if (nowtime == '17:00'):
            wirte_file(buffer)
            send_email(to_email, "ping测试结果", buffer)
