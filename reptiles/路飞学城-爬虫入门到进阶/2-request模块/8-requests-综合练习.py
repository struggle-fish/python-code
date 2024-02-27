'''

获取知乎的搜索
获取前三页的数据
'''
import requests
import os

# 创建文件夹
if not os.path.exists('./pages'):
    os.mkdir('./pages')

word = input('请输入关键词')

# 动态指定页面的范围
start_pageNum = int(input('请输入起始页码'))
end_pageNum = int(input('请输入结束页码'))

url = 'https://zhihu.sogou.com/zhihu'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

for page in range(start_pageNum, end_pageNum + 1):
    params = {
        'query': word,
        'page': page,
        'ie': 'utf-8'
    }
    response = requests.get(url=url, params=params, headers=headers)
    # 获取指定页码的数据
    page_text = response.text
    # 持久化存储
    fileName = word + str(page) + '.html'
    filePath = 'pages/' + fileName
    with open(filePath, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
        print('第%d页数据写入成功' % page)
