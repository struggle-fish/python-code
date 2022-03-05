# 1. 从服务器获取到网页的源代码
# 2. 从网页源代码中提取到你想要的数据
import ssl
import re
from urllib.request import Request, urlopen
ssl._create_default_https_context = ssl._create_unverified_context

# https://www.jianshu.com/p/7d8eee279e7d


def get_page(url):
    # 1. 准备请求信息
    r = Request(url, headers={
        # 模拟浏览器
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36"
    })
    # 发送请求
    resp = urlopen(r)
    return resp.read().decode('utf-8')



def parse_page(s):
    obj = re.compile(r'<div class="item">.*?<em class="">(?P<rate>.*?)</em>.*?<span class="title">(?P<movie>.*?)</span>.*?<span class="rating_num" property="v:average">(?P<rating_num>.*?)</span>.*?<span>(?P<person_num>.*?)人评价</span>', re.S)
    res = obj.finditer(s)
    lst = []
    for item in res:
        dic = item.groupdict()
        lst.append(dic)
    return lst

def main():
    f = open('dir1/movie.txt', mode='w', encoding='utf-8')
    for i in range(10):
        s = get_page(f'https://movie.douban.com/top250?start={i * 25}')
        result = parse_page(s)
        for d in result:
            f.write(str(d))
            f.write('\n')
main()