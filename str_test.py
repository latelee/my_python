#!/usr/bin/python3
# encoding: utf-8

#　bytes和str的示例
# 说明：如果是bytes，print打印时会有前缀'b'

# bytes object
b = b"byte string"

# str object
s = "string"

print("byte string: %s string: %s" % (b, s))

# str to bytes
result = bytes(s, "utf8")
print("to byte: %s" % result)

# bytes to str
result = str(b, "utf-8")
print("to string: %s" % result)

# 另外一种方式转换
print(str.encode(s))
print(bytes.decode(b))