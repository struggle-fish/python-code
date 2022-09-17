# 安装 requests
# pip install requests
import requests


query = input('输入一个你喜欢的明星')
url = f'http://www.sogou.com/web?query={query}'

# 带着浏览器标识
headersdic = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
}

resp = requests.get(url, headers=headersdic)

print(resp.text) # 拿到页面源代码
