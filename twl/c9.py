# -*- coding: utf-8 -*-

import time


def decorator(func):
    # 参数
    # 当装饰器不知道 函数f 到底有多少个参数时，我们可以用 *args 来代替：
    # 函数的所有参数完整地传递到 func 中去.这样就不影响 函数f 的业务逻辑了

    # 关键字参数
    # 如果 foo 函数还定义了一些关键字参数, 我们可以用 **kwargs 来代替：
    # args是一个数组，kwargs一个字典
    def wrapper(*args, **kwargs):  # args通用叫法
        print('执行时间:', time.time())
        func(*args, **kwargs)

    return wrapper


@decorator  # 装饰器的一个语法糖 @符号
def f1(func_name):
    print('This is a function named ' + func_name)


@decorator
def f2(func_name1, func_name2):
    print('This is a function named ' + func_name1)
    print('This is a function named ' + func_name2)


@decorator
def f3(func_name1, func_name2, age=None, height=None):  # 关键字参数
    print('This is a function named ' + func_name1)
    print('This is a function named ' + func_name2)
    print("age %s, height %s" % (age, height))


f3('test func1', 'test func2', age=25, height=200)
# f1('test func')
# f2('test func1','hha')
