#!/usr/bin/python
# 正则表达式学习

import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
m = re.match(r"(\w+)\s", text)
if m:
    print('%s %s' % (m.group(0), m.group(1)))
else:
    print('not match')
print(re.sub(r'\s+', '-', text)) # 空格用'-'替换