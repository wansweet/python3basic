# -*- coding: utf-8 -*-

import re

s = '83C72D1D8E67'
# None
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
r = re.match('\d',s)
# 返回一个元组包含匹配 (开始,结束) 的位置
print(r.span())

# re.search 扫描整个字符串并返回第一个成功的匹配。
r1 = re.search('\d',s)
print(r1.group())


r2 = re.findall('\d',s)
print(r2)
