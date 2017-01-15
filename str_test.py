#!/usr/bin/python3
# encoding: utf-8

#　bytes和str的示例
# 说明：如果是bytes，print打印时会有前缀'b'
# bytes属于二进制，另还有bytearray和memoryview
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
# string 使用示例
str = "hello-world"

print(str);
print(str[0:6]);
print(str[3:6]);
print(str[3:]);
print(str[0:-1]); # -1表示去掉最后一个字符，-2表示去掉倒数第二后面的字符

str = r"hello\t-world" # 不转义

print(str);


# str对象使用
# 使用形式较自由，如可以是str
str = "helloworld goodbye";
print(str.capitalize()); # 首字符大写
#str = ("hello", "world", "goog")

print("-".join(str)); # 每个字符之间用“-”连接

str = ["hello", "world"]
print("-".join(str)); # 每个字符之间用“-”连接