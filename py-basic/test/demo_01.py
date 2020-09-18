a = 1


def test1():
    if a > 1:
        print("xxx")
    elif a == 1:
        print(a)
    else:
        print("yyy")
        pass
    if 1 == 1:
        b = 1
    else:
        c = 2
    pass


if __name__ == '__main__':
    result = type("123") == str
    # False True
    print(result)
    test1()
    pass

'''
多行注释
'''


# 单行注释
