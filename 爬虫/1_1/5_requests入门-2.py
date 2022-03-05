# 获取百度翻译的结果

import requests

url = 'https://fanyi.baidu.com/sug'
s = input('请输入你要翻译的英文')
dat = {
    'kw': s
}
# post 发送数据 data
resp = requests.post(url, data=dat)

print(resp.json()) # 将数据处理成json



