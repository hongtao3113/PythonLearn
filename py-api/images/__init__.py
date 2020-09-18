from aip import AipOcr
import re

# 百度应用授权
APP_ID = '21834800'
API_KEY = 'gzsi6XkPupAE4xbhUcfq4TPO'
SECRET_KEY = '5O74roabd3cz2MFbreyQAaDGQkUc6NR8'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
i = open('C:\\Users\\wk\\Desktop\\Image.png', 'rb')
# python 读取文件时报错UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 205: illegal multibyte sequence

img = i.read()
# 得到数据信息字典
message = client.basicGeneral(img)
# print(message)
# print(message.get('words_result'))

# 给出识别的文字的字典的列表。
for i in message.get('words_result'):
    print(i.get('words'))
