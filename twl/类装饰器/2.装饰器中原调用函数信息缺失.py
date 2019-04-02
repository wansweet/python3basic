#!/usr/bin/python 
# encoding: utf-8
'''
@author: dongwan
@file: 2.装饰器中原调用函数信息缺失.py
@time: 2019/4/2 14:19
@desc:
'''
# 装饰器
def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__)      # 输出 'with_logging'
        print(func.__doc__)       # 输出 None
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def f(x):
   """does some math"""
   return x + x * x


log = logged(f)
print(log.__name__)
print(log.__doc__)

# with_logging
# None