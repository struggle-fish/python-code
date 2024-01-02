'''

post 请求
'''

import requests

post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

data = {
    'cname': '',
    'pid': '',
    'keyword': '上海',
    'pageIndex': '1',
    'pageSize': '10'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

response = requests.post(url=post_url, headers=headers, data=data)

print(response.text)
