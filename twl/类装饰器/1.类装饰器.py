#!/usr/bin/python 
# encoding: utf-8
'''
@author: dongwan
@file: 1.类装饰器.py
@time: 2019/4/2 14:16
@desc:
'''

from functools import wraps

# 类装饰器主要依靠类的__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()