#!/usr/bin/python3
# encoding: utf-8

#��bytes��str��ʾ��
# ˵���������bytes��print��ӡʱ����ǰ׺'b'
# bytes���ڶ����ƣ�����bytearray��memoryview
# ע���ؼ���/����/��������Ҫ��Ϊ���������������

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
# str1ing ʹ��ʾ��
str1 = "hello-world"

print(str1);
print(str1[0:6]);
print(str1[3:6]);
print(str1[3:]);
print(str1[0:-1]); # -1��ʾȥ�����һ���ַ���-2��ʾȥ�������ڶ�������ַ�

str1 = r"hello\t-world" # ��ת��

print(str1);


# str1����ʹ��
# ʹ����ʽ�����ɣ��������str1
str1 = "helloworld goodbye";
print(str1.capitalize()); # ���ַ���д
#str1 = ("hello", "world", "goog")

print("-".join(str1)); # ÿ���ַ�֮���á�-������

str1 = ["hello", "world"]
print("-".join(str1)); # ÿ���ַ�֮���á�-������


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print("L2: %s" % L2);
