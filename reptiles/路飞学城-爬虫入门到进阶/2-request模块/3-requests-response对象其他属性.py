import requests

# 指定url

url = 'https://sogou.com/'

# get 请求
response = requests.get(url=url, verify=False)

# content 二进制 byte 类型的页面数据
page_data = response.content

# status_code 查看状态码
print(response.status_code)

# 响应头信息
print(response.headers)

# 请求的 url
print(response.url)

# print(page_data)
