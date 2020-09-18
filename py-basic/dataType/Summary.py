# coding=utf-8

"""
Python中的数据类型

"""

# 数字类型（Number）
# int整数类型 没有Python2中的long
a = 1
print("整型", type(a))

# bool类型
b = True
print("bool型", type(b))

# float类型 浮点数
c = 1.1
print("浮点型", type(c))

d = 1.2 + 2j
print("complex复数", type(d))

# 加减乘除
n = 9
x = 10
print("除", n / 3)  # 3.0
print("不会自动取整",x / 3)  # 3.3333333333333335
print("取整", x // 3)  # 取整
print("取余", x % 3)
print("乘法", n * x)
print("次方", n ** 2)

# 字符串（String）单引双引没区别
# str类型
word = 'abcdefgh'
print("字符串", type(word))

# 字符串切片截取
# 变量[起始下标:结束下标:步进]
str2 = 'hello2\''  # 使用反斜杠(\)+n转义特殊字符
str3 = r'hello\\'  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print('不转义', str3)
print("字符串截取", word[0:2]) # [0:2)
print("字符串截取", word[:2]) # [0:2) 这种方式与[0:2]相同
print(word[2:]) # [2:) # [2:~] 从下标2开始至字符串末
print("步进",word[::2]) # aceg a 12 c 12 e 12 g
print("回文",word[::-1]) # 回文 利用步进倒着取
print(word[0:-1])           # 输出第一个到倒数第二个的所有字符
print(word[0])              # 输出字符串第一个字符
print(word[2:5])            # 输出从第三个开始到第五个的字符
print(word[2:])             # 输出从第三个开始的后的所有字符
print(word * 2)             # 输出字符串两次

# 常用字符串操作len() replace() index() find() split()...
words="hello,a"
print(words.replace("a","树哥")) #字符串替换
print(words.index("h")," ",words.find("h")) # 获取字母索引
print(words.split("ll")) # 以ll分隔，转为数组
print(words.count("l")) # 某个字符出现的次数
# 字符串的拼接 3种方式
print('123'+'456') # +的方式拼接
list_str=['a','b','c']
string2 = ''.join(list_str)
print("list方式",string2)

string3='我是{}，我很困{}'.format('马云','啊') # format方式
print(string3)

