#!/usr/bin/python 
# encoding: utf-8
'''
@author: dongwan
@file: 7.案例.py
@time: 2019/4/2 13:20
@desc:
'''
from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func():
    return ("Function is running")


can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run