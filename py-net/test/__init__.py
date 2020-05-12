# coding=utf-8
import requests

'''
要先安装requests包
No module named 'requests'
pip3 install requests

抓取图片，放在本地
'''
response = requests.get("https://img-bss.csdnimg.cn/201906261028104896.png")
pic = open('photo.jpg', 'wb')
pic.write(response.content)
