import requests


url = 'https://movie.douban.com/j/chart/top_list'

# 重新封装参数

paramsdata = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'
}
resp = requests.get(url=url, params=paramsdata, headers=headers)
# print(resp.request.url)
print(resp.json())

resp.close()  # 要关闭