# import re

# re.findall() # 匹配字符串中所有符合正则的内容
# re.finditer() # 匹配字符串中所有内容，返回的是迭代器
# re.search() # search 返回的是 match 对象 ，只匹配1次
# re.match() # 从头开始匹配
# re.compile() # 预加载正则
# re.sub() #

#(?P<名字>正则)




# 豆瓣250

import requests
import re
import csv

url = 'http://movie.douban.com/top250'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
}
resp = requests.get(url, headers=headers)

page_content = resp.text

#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp;'
                 r'.*?<span class="rating_num" property="v:average">(?P<rate>.*?)</span>'
                 r'.*?<span>(?P<num>.*?)人评价</span>', re.S)

result = obj.finditer(page_content)
f = open('data.csv', mode='w')
cscwriter = csv.writer(f)
for it in result:
    # print(it.group('name'))
    # print(it.group('rate'))
    # print(it.group('num'))
    # print(it.group('year').strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    cscwriter.writerow(dic.values())
f.close()










