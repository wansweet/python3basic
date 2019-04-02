# -*- coding: utf-8 -*-

# map()函数使用举例
# 功能：map()接受一个函数f和一个或多个list，将f依次作用在list的每个元素，得到一个新的列表
# 语法：map(方法名，列表，[列表2])
# 注意：map()函数的返回值需要强制转换成list类型，且不改变原列表值

# 单个参数
def double_function(number):
    return number * 2

list_1 = [1, 2, 3, 4, 5]

list_result = list(map(double_function, list_1))
print("单参数map结果：", list_result)


list_x = [1,2,3,4,5,6,7,8]
list_y = [1,4,9,16,25,36,49,64]

def square(x,y):
    return x * y

# for x in list_x:
#     square(x)

r = map(square,list_x,list_y)
print(type(r))
print("多参数map结果：", list(r))
