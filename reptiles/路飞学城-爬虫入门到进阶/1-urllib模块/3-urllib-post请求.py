import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# post 携带参数处理

data = {
    'kw': '西瓜'
}

# parse 编码

data = urllib.parse.urlencode(data)

# 将 编码后的结果转成 byte 类型
data = data.encode()

# 发起post
response = urllib.request.urlopen(url=url, data=data)

print(response.read())
