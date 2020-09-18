# coding=utf-8

"""
函数调用
"""
print("调用绝对值函数abs:", abs(-100))
b = 0
b = max(1, 2, 3, 4)
print("max函数", b)
print("min函数", min(1, 2, 3, 4))

"""
数据类型转换
"""
string1 = '123'
string1 = int(string1)
print('数据类型转换int', type(string1))
string1 = float(string1)
print("数据类型转换float", type(string1))
print()


class A:
    def method(self):
        if not isinstance(self, (int, float)):
            return type(self)

    pass


string1 = str(string1)
print("调用函数类型转换", A.method(string1))


# 空函数
def method():
    pass
