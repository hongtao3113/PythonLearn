#!/usr/bin/python3.6.6
# coding=utf-8

"""
list列表：
支持切片截取语法
变量[start:end:步进]
"""
strList1=['a','b','c']
strList2=['a','b','c']
print("类型",type(strList1)) # <class 'list'>
print("列表拼接",strList1+strList2)
print("长度 ",len(strList1))
print("第一个元素 ",strList1[0])
print("倒数第二个元素 ",strList1[-1])
strList1.append("d") # 添加
print("list1 ",strList1)
strList1.insert(0,1) # 插入
print("list1",strList1)
print(strList1*3) # 重复列表3次输出

strList1.pop() # 默认删除最后一个
print(strList1)
strList1.pop(0) # 删除指定下标的元素
print(strList1)
strList1[0]='abc'
print(strList1)

strList3=['a','b','c',[1,2,3]]
print(len(strList3)) # list嵌套
print(strList3[3][0])
print(strList3[0:1])

if __name__ == '__main__':
    # 大概与Java中的main方法相同
    pass
