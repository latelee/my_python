#!/usr/bin/python3
# encoding: utf-8

#　bytes和str的示例
# 说明：如果是bytes，print打印时会有前缀'b'
# bytes属于二进制，另还有bytearray和memoryview
# 注：关键字/类名/函数名不要作为变量，会出现问题

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


#############################################
# str1ing 使用示例
str1 = "hello-world"

print(str1);
print(str1[0:6]);
print(str1[3:6]);
print(str1[3:]);
print(str1[0:-1]); # -1表示去掉最后一个字符，-2表示去掉倒数第二后面的字符

str1 = r"hello\t-world" # 不转义

print(str1);


# str1对象使用
# 使用形式较自由，如可以是str1
str1 = "helloworld goodbye";
print(str1.capitalize()); # 首字符大写
#str1 = ("hello", "world", "goog")

print("-".join(str1)); # 每个字符之间用“-”连接

str1 = ["hello", "world"]
print("-".join(str1)); # 每个字符之间用“-”连接


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print("L2: %s" % L2);
