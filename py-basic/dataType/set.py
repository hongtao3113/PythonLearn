#!/usr/bin/python3.6.6
# coding=utf-8
"""
Set集合
重复的元素会被覆盖
"""
set1 = {"1", "2", "3"}
print(type(set1))  #

list1 = [1, 2, 3, 3]
set2 = set(list1)
print(set2)  # 去除list1重复的元素

# 添加删除元素
set1.add("4")
set1.add("5")
set1.remove("1")
print(set1)

# 对数组做一些交集或并集的操作
set3 = {1, 2, 3}
set4 = {3, 4, 5}
print(set3 & set4)  # 交集
print(set3 | set4)  # 并集
