#!/usr/bin/python3
# encoding: utf-8

#��bytes��str��ʾ��
# ˵���������bytes��print��ӡʱ����ǰ׺'b'
# bytes���ڶ����ƣ�����bytearray��memoryview
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


#############################################
# string ʹ��ʾ��
str = "hello-world"

print(str);
print(str[0:6]);
print(str[3:6]);
print(str[3:]);
print(str[0:-1]); # -1��ʾȥ�����һ���ַ���-2��ʾȥ�������ڶ�������ַ�

str = r"hello\t-world" # ��ת��

print(str);


# str����ʹ��
# ʹ����ʽ�����ɣ��������str
str = "helloworld goodbye";
print(str.capitalize()); # ���ַ���д
#str = ("hello", "world", "goog")

print("-".join(str)); # ÿ���ַ�֮���á�-������

str = ["hello", "world"]
print("-".join(str)); # ÿ���ַ�֮���á�-������