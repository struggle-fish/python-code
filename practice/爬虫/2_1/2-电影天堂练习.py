# 1. 定位到2022必看
# 2. 从2022必看中提取到子页面的链接地址
# 3. 请求子页面的链接地址，拿到下载地址
import re
import requests

domain = 'https://dytt89.com/'

resp = requests.get(domain, verify=False) # verify=False 去掉安全验证
resp.encoding = 'gb2312'


obj1 = re.compile(r'2022必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="'
                  r'(?P<download>.*?)>', re.S)
result1 = obj1.finditer(resp.text)
child_href_lst = []
for it in result1:
    ul = it.group('ul')
    # print(ul)

    # 提取子链接地址
    result2 = obj2.finditer(ul)
    for itt in result2:
        # 拼接子页面地址
        child_href = domain + itt.group('href').strip('/')
        child_href_lst.append(child_href)


# 提取子页面内容
for href in child_href_lst:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = 'gb2312'
    result3 = obj3.search(child_resp.text)
    print(result3.group('movie'))
    print(result3.group('download'))








