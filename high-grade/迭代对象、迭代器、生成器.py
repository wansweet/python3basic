#!/usr/bin/python 
# encoding: utf-8
'''
@author: dongwan
@file: 迭代对象、迭代器、生成器.py
@time: 2019/4/2 15:02
@desc:
'''
from itertools import islice

# 容器(container)
# 容器是一种把多个元素组织在一起的数据结构，容器中的元素可以逐个地迭代获取，可以用 in , not in 关键字判断元素是否包含在容器中。通常这类数据结构把所有的元素存储在内存中（也有一些特列并不是所有的元素都放在内存）在Python中，常见的容器对象有：
#
# list, deque, ....
# set, frozensets, ....
# dict, defaultdict, OrderedDict, Counter, ....
# tuple, namedtuple, …
# str

assert 1 in [1, 2, 3]  # lists
assert 4 not in [1, 2, 3]
assert 1 in {1, 2, 3}  # sets
assert 4 not in {1, 2, 3}
assert 1 in (1, 2, 3)  # tuples
assert 4 not in (1, 2, 3)

# 询问某元素是否在dict中用dict的中key：

d = {1: 'foo', 2: 'bar', 3: 'qux'}
assert 1 in d
assert 'foo' not in d  # 'foo' 不是dict中的元素

# 询问某substring是否在string中：

s = 'foobar'
assert 'b' in s
assert 'x' not in s
assert 'foo' in s

# 可迭代对象(iterable)
# 刚才说过，很多容器都是可迭代对象，此外还有更多的对象同样也是可迭代对象，比如处于打开状态的files，sockets等等。但凡是可以返回一个 迭代器 的对象都可称之为可迭代对象，听起来可能有点困惑，没关系，可迭代对象与迭代器有一个非常重要的区别。先看一个例子：

x = [1, 2, 3]
y = iter(x)
z = iter(x)
print('next(y) = ', next(y))
print('next(y) = ' , next(y))

print('next(z) = ',next(z))
print('type(x) = ', type(x))
print('type(y) = ',type(y))


class Fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

f = Fib()
list = list(islice(f, 0, 10))
print(list)
