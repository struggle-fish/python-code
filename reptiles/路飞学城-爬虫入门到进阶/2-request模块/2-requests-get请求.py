'''
获取 搜狗首页数据

'''
import requests

# 指定url

url = 'https://sogou.com/'

# get 请求
response = requests.get(url=url, verify=False)
# 获取数据 text 获取字符串形式的页面数据
page_data = response.text

print(page_data)

# 持久化
with open('sougou.html', 'w', encoding='utf-8') as fp:
    fp.write(page_data)
