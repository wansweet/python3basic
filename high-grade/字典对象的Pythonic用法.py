#!/usr/bin/python 
# encoding: utf-8
'''
@author: dongwan
@file: 字典对象的Pythonic用法.py
@time: 2019/4/2 15:54
@desc:
'''

# 0. 使用 in/not in 检查 key 是否存在于字典
# if key in dictionary:
#     print(True)
#
# else:
#     print(False)


# 1. 使用 setdefault() 初始化字典键值

#
# dictionary = {}
# if "key" not in dictionary:
#     dictionary["key"] = []
# dictionary["key"].append("list_item")

dictionary = {}
dictionary.setdefault("key", []).append("list_item")

print(dictionary)
