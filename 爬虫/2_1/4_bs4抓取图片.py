# 1.拿到主页面的源代码，提取子页面的链接地址，href
# 2. 通过href拿到子页面的内容，从子页面中找到图片的下周地址 img -> src
# 3. 下载图片


import requests
from bs4 import BeautifulSoup
import time
url = 'https://www.umeitu.com/meinvtupian/xingganmeinv/'
resp = requests.get(url)
resp.encoding = 'utf-8'


# 把源代码交给 bs
main_page = BeautifulSoup(resp.text, 'html.parser')
alist = main_page.find('div', class_='TypeList').find_all('a')


# bizhitupian/weimeibizhi/225259.htm
for a in alist:
    # print(a.get('href'))
    href = a.get('href')
    # https://www.umeitu.com/bizhitupian/weimeibizhi/225260.htm
    # print(href)
    # # 获取子页面的源代码
    # https://www.umeitu.com/meinvtupian/xingganmeinv/243430.htm
    child_page_reps = requests.get(f'https://www.umeitu.com/{href}')
    child_page_reps.encoding = 'utf-8'
    child_page_text = child_page_reps.text
    # 子页面中拿到图片下载地址
    child_page = BeautifulSoup(child_page_text, 'html.parser')
    p = child_page.find('div', class_="ImageBody")
    img = p.find('img')
    imgsrc = img.get('src')
    # print(img.get('src'))
    img_resp = requests.get(imgsrc)
    # img_resp.content  # 这里拿到的是字节

    # https://kr.zutuanla.com/file/2020/1031/6b72c57a1423c866d2b9dc10d0473f27.jpg
    img_name = imgsrc.split('/')[-1] # 拿到url中租后一个/以后的内容
    with open('images/' + img_name, mode='wb') as f:
        f.write(img_resp.content)  # 图片内容写入文件
    print('over!!', img_name)
    # time.sleep(1)

print('下载完毕')