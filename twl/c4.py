# -*- coding: utf-8 -*-

from functools import reduce

# reduce(function, iterable, initializer(可选))
# 参数：
#   function -- 函数，有两个参数
#   iterable -- 可迭代对象
#   initializer -- 可选，初始参数

def add(x, y) :            # 两数相加
     return x + y

result = reduce(add, [1,2,3,4,5], 100)   # 计算列表和：100(初始值)  +  1+2+3+4+5
print(result)

reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数


# 连续计算，连续调用lambda
list_x = ['1','2','3','4','5','6','7','8']
r = reduce(lambda x,y:x+y,list_x,'aaa',)  # aaa为初始值
print(r)

(((1+2)+3)+4)+5

# map/reduce 编程模型 映射 归约 并行计算
# 函数式编程
