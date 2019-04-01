# -*- coding: utf-8 -*-

# 闭包 = 函数+环境变量
# 现场

'''
闭包：

　　在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。

'''
a = 25
def curve_pre():
    a = 25
    def curve(x):
        return  a*x*x
    return curve

a = 10
f = curve_pre()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
# curve(2)
print(f(2))
# 环境变量