import io


def readFile(path):
    with open(path, 'r') as rf:
        # readlines读取文件中的全部内容
        content = rf.readlines()
        rf.close()
        return content
    pass


def writeFile(path):
    with open(path, 'w') as wf:
        wf.write('Python读写文件,eeeeee')
        wf.close()
    pass


# 文件路径
path = "C:\\Users\\wk\\Desktop\\1.txt"

# 写入文件
writeFile(path)

# 读取文件
content = readFile(path)
print(content)
