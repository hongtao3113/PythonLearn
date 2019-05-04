# /usr/bin/python3
# coding=utf-8

"""
函数的参数,位置参数
"""
class TestFunction:
    def methodA(x, n):
        if x==1 or x==0:
            return x
        else:
            return x ** n
        pass

    #单传一个函数，默认n=2
    def methodB(x,n=2):
        if x==1 or x==0:
            return x
        else:
            return x ** n
        pass
    def methodC(x,y,n=2):
        if x==1 and y==1:
            return "密码正确"
        else:
            return x ** n
        pass
print("求一个数的N次方：",TestFunction.methodA(2,4))
print("函数的默认参数：",TestFunction.methodB(2))
print("函数的默认参数：",TestFunction.methodB(2,3))
print("函数的默认参数：",TestFunction.methodB(2,3))
print("函数的默认参数：",TestFunction.methodC(1,1))
