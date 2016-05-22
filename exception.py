#!/usr/bin/python
# python类学习

# 异常
class Error(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value
    def __repr__(self):
        return str(self)

list=[1, 2, 3, 4]
if list.count(7) != 0:
    print("list: %s" % list)
else:
    raise Error('nottttt')