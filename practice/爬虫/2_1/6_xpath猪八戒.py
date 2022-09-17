# 拿页面源代码
# 提取解析数据
import requests
from lxml import etree
url = 'https://beijing.zbj.com/search/f/?kw=sass'
resp = requests.get(url)

html = etree.HTML(resp.text)

# 拿到每个服务商div
divs = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div/div')
# print(divs)
for div in divs: # 每个服务商信息
    price = div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip('￥')
    title = 'sass'.join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
    com_name = div.xpath("./div/div/a[1]/div[1]/p/text()")[1].strip()
    city = div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
    # print(com_name)

