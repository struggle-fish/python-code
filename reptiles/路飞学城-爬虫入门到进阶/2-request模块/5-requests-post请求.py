'''

登录豆瓣

'''

import requests

url = 'https://accounts.douban.com/login'

data = {
    'source': 'movie',
    'redir': 'https://movie.douban.com/',
    'form_email': '18510006974',
    'form_password': 'jzyo0o0o07415',
    'login': '登录'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

response = requests.post(url=url, data=data, headers=headers)

page_text = response.text
with open('豆瓣.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
