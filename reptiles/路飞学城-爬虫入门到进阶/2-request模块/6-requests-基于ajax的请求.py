'''

豆瓣电影详情数据
'''

'''

https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=60&limit=20
'''

import requests

url = 'https://movie.douban.com/j/chart/top_list'

params = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '60',
    'limit': '20'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

response = requests.get(url=url, params=params, headers=headers)

print(response.text)
