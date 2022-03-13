# HTML(Hyper Text Markup Language)超文本标记语言, 是我们编写 网⻚的最基本也是最核心的一种语言.
# 其语法规则就是用不同的标签 对网⻚上的内容进行标记, 从而使网⻚显示出不同的展示效果

# <标签 属="属性值">被标记的内容</标签>
# <标签/>


# 通过标签定位内容
import requests
from bs4 import BeautifulSoup


# 1. 拿到页面源代码
# 2. 使用bs4 进行解析拿到数据
url = 'http://www.xinfadi.com.cn/index.html'
resp = requests.get(url)
# print(resp.text)


# 解析数据
# 1.把页面源代码交给 BeautifulSoup

page = BeautifulSoup(resp.text, 'html.parser')

# 2.从bs对象中查找数据
# find('标签', 属性=值)
# findAll('标签', 属性=值)

table = page.find('div', attrs={
    'class': 'tablebox'
})
# print(table)
# 拿到所有的 tr
trs = table.find_all('tr')[1:]

for tr in trs:
    th = tr.find_all('th')
    name = th[0].text
    price = th[1].text
    pingjunprice = th[2].text
    print(name)
    print(price)
    print(pingjunprice)










