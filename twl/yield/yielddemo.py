#!/usr/bin/python 
# encoding: utf-8
'''
@author: dongwan
@file: yielddemo.py
@time: 2019/5/6 13:29
@desc:
'''
def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num

g = foo(0)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# for 循环会调用迭代器的next函数
print('继续遍历剩余的元素')
for n in g:
    print(n)


