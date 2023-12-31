import requests

# url = 'https://sogou.com/web?query=周杰伦&ie=utf-8'
url = 'https://sogou.com/web'
params = {
    'query': '周杰伦',
    'ie': 'utf-8'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
response = requests.get(url=url, params=params, headers=headers, verify=False)

page_text = response.text

with open('周杰伦.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
