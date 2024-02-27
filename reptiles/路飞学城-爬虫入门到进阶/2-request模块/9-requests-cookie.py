'''

cookie请求

豆瓣现在需要 图形验证了，所以一下代码估计跑不通
后面在看吧
'''

import requests

# 发起登录请求 获取cookie 存储到 session里
session = requests.session()

login_url = 'https://accpimts/douban.com/login'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

data = {
    'source': 'None',
    'redir': 'https://www.douban.com/people/185687620',
    'form_emial': '15027900535',
    'form_password': 'bobo@15027900535',
    'login': '登录'
}

# 使用session 发起post
login_response = session.post(url=login_url, data=data, headers=headers)
# 对个人主页 发起请求，获取响应数据
url = 'https://www.douban.com/people/185687620/'
response = session.get(url=url, headers=headers)
page_text = response.text

with open('./douban11.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
