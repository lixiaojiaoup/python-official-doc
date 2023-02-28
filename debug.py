# -*- coding: utf-8 -*-

# Reference:************************
# @Time    : 2023/2/28 17:19
# @Author  : 夏侯仪
# @File    : debug.py
# @Intro   : PyCharm
# Reference:************************


a = [1, 2, 3]
def test(a):
    a[1] = 2222

print(a)
test(a)
print(a)
b = a
b[0] = 111
print(a, b)

i1 = [1, 2, 3]
i2 = i1
i2[1] = 111
print(i1, i2)
