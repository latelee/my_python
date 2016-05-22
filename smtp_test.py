#!/usr/bin/python
# encoding: utf-8
# 基于python 3.4 发送邮件测试示例，本代码文件使用UTF-8格式

import os
import base64

import smtplib
import email.utils
from email.mime.text import MIMEText

# 接收邮件地址
#to_email = 'lijj@signalway.com.cn'
to_email = 'latelee@163.com'

# 发送者信(最好是马甲邮箱)
smtpserver = 'smtp.163.com'
snd_email = 'rtl8019as@163.com'
username = snd_email
password = b'cnRsODAxOWFzPTEwMA=='

subject = 'python email test'

msg = MIMEText('这是一个测试邮件', 'html', 'utf-8')

msg['Subject'] = subject
msg['From'] = email.utils.formataddr(('py发送者', snd_email)) # 发件人：py发送者<xxx@163.com>
msg['To'] = to_email
#msg['Date'] = formatdate(localtime=True)

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, bytes.decode(base64.b64decode(password)))
smtp.sendmail(snd_email, to_email, msg.as_string())
smtp.quit()