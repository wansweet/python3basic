#!/usr/bin/python 
# encoding: utf-8
'''
@author: dongwan
@file: 3.使用wraps.py
@time: 2019/4/2 14:31
@desc:
'''

from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__)      # 输出 'f'
        print(func.__doc__)      # 输出 'does some math'
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

log = logged(f)
print(log.__name__)
print(log.__doc__)

# f
# does some math