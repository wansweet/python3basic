#!/usr/bin/python 
# encoding: utf-8
'''
@author: dongwan
@file: 4.将函数作为参数传给另一个函数.py
@time: 2019/4/2 11:33
@desc:
'''


def hi():
    return "hi yasoob!"


def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())


doSomethingBeforeHi(hi)
# outputs:I am doing some boring work before executing hi()
#        hi yasoob!