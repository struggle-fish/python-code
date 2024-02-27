'''
1、抓取验证码
2、把图片保存本地
3、把图片给第三方平台  云打码

'''
import requests
from lxml import etree

url = 'https://xkczb.jtw.beijing.gov.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

page_text = requests.get(url, headers=headers).text

# 解析验证码，验证码图片下载到本地
codeimg_url = 'https://apply.jtw.beijing.gov.cn/apply/app/common/validCodeImage?ee=1'

# 图片验证码二进制数值
code_img = requests.get(url=codeimg_url, headers=headers).content
# print(code_img)

# 把图片保存到本地
with open('./code.jpg', 'wb') as fp:
    fp.write(code_img)
