import requests
import json

headers = {
    'Cookie': 'OCSSID=4df0bjva6j7ejussu8al3eqo03',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
resp = requests.get(
    'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=4155714&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    , headers=headers)
result = resp.text.replace(");", "").replace("fetchJSON_comment98(", "")
print(result)
jsonData = '{"age":1,"name":"李白"}'
json_loads = json.loads(jsonData)
print(json_loads['age'])
print(json_loads['name'])