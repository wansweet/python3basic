#!/usr/bin/python 
# encoding: utf-8
'''
@author: dongwan
@file: 8.案例日志.py
@time: 2019/4/2 13:59
@desc:
'''
import logging


# use_logging是对装饰器的封装,并返回一个装饰器
def use_logging(level):
    # 函数装饰器
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)

        return wrapper

    return decorator


@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)


foo()
