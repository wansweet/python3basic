#!/usr/bin/python 
# encoding: utf-8
'''
@author: dongwan
@file: 1.一切皆对象.py
@time: 2019/4/2 11:29
@desc:
'''


def hi(name="yasoob"):
    return "hi " + name


print(hi())
# output: 'hi yasoob'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个

print(greet())
# output: 'hi yasoob'

# 如果我们删掉旧的hi函数，看看会发生什么！
del hi
print(hi())
# outputs: NameError

print(greet())
# outputs: 'hi yasoob'