# -*- coding: utf-8 -*-
from c6 import Human


# Student 继承 Human
class Student(Human):
    # sum = 0

    # 子类自己的变量：school
    def __init__(self, school, name, age):
        self.school = school

        # 子类构造中把参数传入父类构造
        # 假设修改继承父类，后来不继承父类了
        # Human.__init__(self, name, age)

        super(Student, self).__init__(name ,age)
        self.__score = 0
        self.__class__.sum += 1

    def do_homework(self):
        print('english homework')
        print(self.school)


# 子类可以继承到父类的 实例变量，成员变量，实例方法
student1 = Student("学军小学", '哈哈', 18)
print("student1.sum: ", student1.sum)
print("Student.sum: ", Student.sum)
print("student1.name: ", student1.name)
print("student1.age: ", student1.age)
student1.get_name()

student1.do_homework()
# 类调用实例方法,会报错
# Student.do_homework()

# 如果一定要用类调用实例方法
# 把实例对象传给self，这样做并不是很好
Student.do_homework(student1)