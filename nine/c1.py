# -*- coding: utf-8 -*-

# 面向对象
# 有意义的面向对象的代码
# 类 = 面向对象
# 类、对象
# 类的名字首字母需要大写，不要像变量一样用下划线
# 实例化
# 类最基本的作用：封装代码
# 类和对象
class Student():
    sum = 0
    name = 'mf'  # 类变量，这个类的所有实例之间共享，可以使用Student.name来分享
    age = 0

    # '类变量' 和 '实例变量'
    def __init__(self, name, age):  # 实例方法 对象
        # __init__()是特殊方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        # 初始化对象的属性
        self.name = name  # 实例变量
        self.age = age

        # 目前score是公开的，即public
        # self.score = 0 #代表实例对象中有这个变量

        # 在变量或方法名前面加__(双下划线)，就变成私有的
        self.__score = 0

        self.__class__.sum += 100

    def set_score(self, score):
        if score < 0 :
            return '分数不能为负数'
        self.__score = score
        print(self.name + '同学本次考试分数为：'+ str(self.score))

    # 普通函数
    # 行为 与 特征
    def do_homework(self):
        print('homework')

    @classmethod  # 函数装饰器 类方法 类本身
    # 修饰的函数不需要实例化，但是必须传第一个参数，表示自身类的 cls 参数，
    # 可以来调用类的属性，类的方法，实例化对象等。
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    @staticmethod
    def add():
        print(Student.sum)
        print('This is a static method')

# 类就是一个印刷机、模版，类实例化可以产生很多个对象
# 类里面可以传入多个特征

# class Printer():
#     def print_file(self):
#         print('name: ' + self.name)
#         print('age: ' + str(self.age))

# print_file()  类不负责执行代码，只负责定义

# class StudentHomework():
#     homework_name = ''

# 方法 和 函数的区别
# 方法：设计层面 函数：程序运行、过程式的一种称谓
# 数据成员 变量

# student = Student()  # 类实例化
# student.print_file()  # 调用类的方法
# 类实例化和调用不要放在定义类的文件里

# 创建对象时必须传入构造函数的参数，否则报错
student1 = Student('哈哈', 18)
print(student1.name)  # 是实例的变量
print(Student.name)  # 是类的变量
print(student1.__dict__)  # 显示所有的实例变量
print("student1.sum: ", student1.sum)

# 可以直接给score赋值，这样赋值不安全
student1.score = -1
print(student1.score)




# 使用提供的方法来给score赋值。可以限制赋值的内容
student1.set_score(-1)


#

# a = student1.__init__()
# print(a)
# print(type(a))
# student2 = Student()
# student3 = Student()
#

# 查看对象在内存中的地址
# print(id(student1))
# print(id(student2))
# print(id(student3))


'''
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
'''
# print("Student.__doc__:", Student.__doc__)
# print("Student.__name__:", Student.__name__)
# print("Student.__module__:", Student.__module__)
# print("Student.__bases__:", Student.__bases__)
# print("Student.__dict__:", Student.__dict__)