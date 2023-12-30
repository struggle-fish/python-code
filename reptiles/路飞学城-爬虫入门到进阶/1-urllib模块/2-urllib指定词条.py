import urllib.request
import urllib.parse

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# UA伪装


url = 'https://sogou.com/web?query='
word = urllib.parse.quote('前端')
url += word

# 自定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# url 中不可以存在非ASCII编码的字符数据
response = urllib.request.urlopen(request)

page_text = response.read()

# print(page_text)
with open('前端.html', 'wb') as fp:
    fp.write(page_text)
