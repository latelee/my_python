#!/usr/bin/python3
# encoding: utf-8
# 基于python 3.4 发送邮件测试示例，本代码文件使用UTF-8格式
# 隐藏账户信息

import os
import base64

import smtplib
import email.utils
from email.mime.text import MIMEText

# 接收邮件地址
to_email = 'li@latelee.org'
# TODO：群发多个email
#to_email = str.split(to_email, ",")

# 发送者信息
smtpserver = 'smtp.exmail.qq.com'
snd_email = 'robot@latelee.org'
username = snd_email
password = b'Um9ib3QhPTI1MAo='

subject = 'python email test'

def send_email(to_list, sub, content):
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = email.utils.formataddr(('py智能机器人', snd_email)) # 发件人：py发送者<xxx@163.com>
    #msg['From'] = snd_email
    msg['To'] = to_list
    #msg['Date'] = formatdate(localtime=True)

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, bytes.decode(base64.b64decode(password)))
        #smtp.login(username, bytes.decode(password))
        smtp.sendmail(snd_email, to_list, msg.as_string())
        smtp.quit()
        return 0
    except Exception as e:
        print(str(e))
        return -1

# main...
if __name__ == '__main__':  
    if send_email(to_email, "hello", "hello world!\n This is python robot from robot") == 0:  
        print("send %s ok" % to_email)
    else:  
        print("send failed")