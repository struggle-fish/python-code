# 爬虫： 通过编写程序来获取到互联网上的资源

# 需求：用程序模拟浏览器，输入一个网址，从该网址中获取资源或内容

from urllib.request import urlopen

url = 'http://www.baidu.com'

resp = urlopen(url)


with open('mybaidu.html', mode='w') as f:
    f.write(resp.read().decode('utf-8'))

