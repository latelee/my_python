#!/usr/bin/python3
# encoding: utf-8

#��bytes��str��ʾ��
# ˵���������bytes��print��ӡʱ����ǰ׺'b'

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

# ����һ�ַ�ʽת��
print(str.encode(s))
print(bytes.decode(b))