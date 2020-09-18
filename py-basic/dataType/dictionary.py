# coding=utf-8
"""
字典 key value
"""
dictionary = {}
dictionary = {"name": "wk", "age": 18, 1: 'xxxx'}
print("类型：", type(dictionary))
print(dictionary)
print(dictionary['name'], " ", dictionary[1])  # 通过key 获取value

dictionary["addr"] = '北京'  # 添加
dictionary["addr"] = '北京2'  # 值覆盖

print("判断key是否存在：", "addr" in dictionary)

print(dictionary.get("name2"))  # 返回None dictionary.get(key,v) 可以指定返回值，若不存在返回v
dictionary.pop(1);
dictionary.pop('name');  # 删除指定Key
print(dictionary)
