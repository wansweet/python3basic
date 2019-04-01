# -*- coding: utf-8 -*-

import re

s = 'life is short,i use python,i love python'
r = re.search('life(.*)python(.*)python',s)
# 表示匹配到的完整文本字符
print(r.group(0))
# 得到第一组匹配结果，也就是(.*)匹配到的
print(r.group(1))
# 得到第二组匹配结果，也就是(.*?)匹配到的
print(r.group(2))

print(r.group(0,1,2))   #返回元组

print(r.group())


# r = re.findall('life(.*)python',s)
# print(r)