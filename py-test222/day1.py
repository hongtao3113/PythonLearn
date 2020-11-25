import requests
import json

resp = requests.get(
    'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=4155714&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1')
result = resp.text.replace(");", "").replace("fetchJSON_comment98(", "")
print(result)
jsonData = '{"age":1,"name":"李白"}'
json_loads = json.loads(jsonData)
print(json_loads['age'])
print(json_loads['name'])