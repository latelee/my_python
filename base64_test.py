#!/usr/bin/python3
# encoding: utf-8
# base64编码、解码示例

import base64
# b64encode接受的是bytes，不是str
passwd = b'rtl8019as=100'

encode_data = base64.b64encode(passwd)
print("base64 encode: %s" % encode_data)

decode_data = base64.b64decode(encode_data)
print("base64 decode: %s" % decode_data)
