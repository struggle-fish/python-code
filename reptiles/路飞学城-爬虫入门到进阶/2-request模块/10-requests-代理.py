'''

代理操作：
- 1.代理：第三方代理本体执行相关的事物。生活：代购，微商，中介
- 2.为什么要使用代理？
    - 反爬操作。
    - 反反爬手段
- 3.分类：
    - 正向代理：代替客户端获取数据
    - 反向代理：代理服务器端提供数据
- 4.免费代理ip的网站提供商：
    - www.goubanjia.com
    - 快代理
    - 西祠代理

'''

import requests

url = 'https://www.baidu.com/s?ie=utf-8&wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
proxy = {
    'http': '77.73.69.120:3128'
}

response = requests.get(url=url, proxies=proxy, headers=headers)
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)
