# -*- coding: utf-8 -*-

class Student():
    sum = 0
    name = 'mf'  # 类变量，这个类的所有实例之间共享，可以使用Student.name来分享
    age = 0

    # '类变量' 和 '实例变量'
    def __init__(self, name, age):  # 实例方法 对象
        self.name = name  # 实例变量
        self.age = age

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


# 创建对象时必须传入构造函数的参数，否则报错
student1 = Student('哈哈', 18)
student2 = Student('谷歌', 20)

# 使用提供的方法来给score赋值。可以限制赋值的内容
student1.set_score(-1)

# python的动态语言特性，这里实际上是给student1新添加了一个属性__score
# 并不是在构造方法中self.__score的变量
student1.__score = 200
print(student1.__score) #这里没有报错，
print(student1.__dict__) #'_Student__score': 0,python把原来的__score变量，名字改了

# 私有变量也是可以读的，但是不要这么读取
print(student1._Student__score)

# print(student2.__score) #这里会报错
