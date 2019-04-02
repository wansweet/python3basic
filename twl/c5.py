# -*- coding: utf-8 -*-

# filter 过滤
# 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# 参数
#   第一个为函数
#   第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素

list_x = [1,0,1,0,0,1]
list_u = ['a','B','c','F','e']
# r = filter(lambda x: True if x==1 else False,list_x)
r = filter(lambda x: x,list_x)
print(r)  # 返回集合类型
print(list(r))
