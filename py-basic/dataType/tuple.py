# coding=utf-8
"""
tuple元组
支持切片截取语法
定义后不能被修改
Python独有的数据类型
"""
tuple1=(1,2,3)
print(type(tuple1)) #<class 'tuple'>
tuple2=(1) # <class 'int'> 元组只有一个元素必须这样写 tuple2=(1,)
print(type(tuple2))

# tuple1[0]=2 报错，本身的元素不能被修改，若修改了引用依然会报错
l=[1,3]
t=(2,l)
t[1][0]=3
print(t)