# 登录-> 得到 cookie
# 带着cookie 去请求到书架url -> 书架上的内容

# 可以使用 session 进行请求 -> session 可以认为是一连串的请求， 在这个过程中 cookie 不会丢失


import requests

# # 会话
# session = requests.session()
#
# data = {
#     'loginName': '18510006974',
#     'password': 'a123456789',
#     'appKey': '1351550300'
# }
#
# # 登录
# url = 'https://h5.17k.com/ck/user/login'
# resp = session.post(url, data=data)
# # print(resp.cookies) # cookie
#
# # https://user.17k.com/ck/author/shelf?platform=4&appKey=1351550300
#
# # 获取我的书架的书
# bookresp = session.get('https://user.17k.com/ck/author/shelf?platform=4&appKey=1351550300')
# print(bookresp.json())



# requests
test = requests.get('https://user.17k.com/ck/author/shelf?platform=4&appKey=1351550300')
print(test.json())