import recognition
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

client = recognition.recog()

id = 'https://cdn.chinahadoop.cn/pimages/material/20191220/dc644c63dd3afc7b30cc518593703c54.png'
image = requests.get(id).content

res = client.basicGeneral(image)

for i in range(len(res['words_result'])):
    print(res['words_result'][i]['words'])
