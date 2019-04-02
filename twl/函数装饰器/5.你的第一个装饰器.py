#!/usr/bin/python 
# encoding: utf-8
'''
@author: dongwan
@file: 5.你的第一个装饰器.py
@time: 2019/4/2 11:35
@desc:
'''

# a_new_decorator是一个装饰器
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()
        # print(a_func.__name__)
        # print(a_func.__doc__)

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


# 执行a_function_requiring_decoration函数
# a_function_requiring_decoration()

# 将函数的返回wrapTheFunction（也是函数）传给变量a_function_requiring_decoration
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

# 进行调用变量传给变量a_function_requiring_decoration
# a_function_requiring_decoration()


@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


a_function_requiring_decoration()

# 原本应该打印"a_function_requiring_decoration"。这里打印wrapTheFunction
# 这里的函数被warpTheFunction替代了。它重写了我们函数的名字和注释文档(docstring)
# 使用functools.wraps来解决装饰模式
# print(a_function_requiring_decoration.__name__)

# the @a_new_decorator is just a short way of saying:
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)