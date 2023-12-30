'''

urllib
    python 中自带的一个基于爬虫的模块

    可以使用代码模拟浏览器发送请求  request parse

    使用流程：
        指定url
        针对指定的url发起一个请求
        获取服务器响应回来的页面数据
        持久化存储


TODO: https://blog.51cto.com/u_14523369/6111479
    报错“SSL: CERTIFICATE_VERIFY_FAILED”
    Python 升级到 2.7.9 之后引入了一个新特性，当使用urllib.urlopen打开一个 https 链接时，会验证一次 SSL 证书。而当目标网站使用的是自签名的证书时就会抛出此异常。


   解决方案：
    1）使用ssl创建未经验证的上下文，在urlopen中传入上下文参数
        import ssl
        context = ssl._create_unverified_context()
        webPage = urllib.request.urlopen(req,context=context)
    2）全局取消证书验证
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
'''

# 需求 爬取 搜狗首页数据
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 指定url
url = 'http://www.sogou.com/'
# 发起请求 根据指定的url 发起请求 返回一个响应对象
response = urllib.request.urlopen(url)
# 获取页面数据 read 返回的是页面数据
page_text = response.read()
print(page_text)

# 持久化存储
with open('sougou.html', 'wb') as fp:
    fp.write(page_text)
    print('写入成功')
