import urllib.request

'''
看看格式就行了，这个需要 证书
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

'''
response = urllib.request.urlopen('https://m.douban.com/movie/', None, 2)
print(response)
html = response.read().decode('utf8')

f = open('code1.txt', 'w', encoding='utf8')
f.write(html)
f.close()
