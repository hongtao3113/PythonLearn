# coding=utf-8
# /bin/py3.6


class Student(object):
    classes = 1

    def __init__(self, name, age, score):
        """
        类似于Java的构造函数，self 大概就是相当于Java的this吧
        :param name:
        :param age:
          """

        self.name = name
        self.age = age
        self.__score = score  # 对象的属性私有化，不能通过对象.属性的方式 ,可以通过get set方法来操作属性
        pass

    def print_age(self):
        print('%s: %s' % (self.name, self.age))  # 这是什么写法
        pass

    def get_age(self):
        if self.age >= 18:
            return "成年人"
        else:
            return "未成年人"
        pass

    def get_score(self):
        return self.__score
        pass

    def set_score(self, score):
        self.__score = score
        pass

    pass


# 实例化一个对象
student1 = Student('李白', 12, 100)
Student.print_age(student1)
print("输出对象内存地址", id(student1))
print(student1.name)
print(Student.get_age(student1))
student1.name = "杜甫"
student1.age = 18
student1.set_score(10)
print(student1.name)
print(student1.get_score())
print(Student.get_age(student1))
Student.classes = 2
print("类的属性", Student.classes)

# 对象 属性私有 self.__param
