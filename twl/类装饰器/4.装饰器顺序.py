#!/usr/bin/python 
# encoding: utf-8
'''
@author: dongwan
@file: 4.装饰器顺序.py
@time: 2019/4/2 14:44
@desc:
'''

# 装饰器顺序
# 一个函数还可以同时定义多个装饰器，比如：

# @a
# @b
# @c
# def f ():
#     pass
# 它的执行顺序是从里到外，最先调用最里层的装饰器，最后调用最外层的装饰器，它等效于

# f = a(b(c(f)))