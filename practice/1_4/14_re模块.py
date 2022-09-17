import re

# 从一个字符串中提取所有的数字

# lst = re.findall('\d+', '我今年18岁了，喜欢5个明星')
# print(lst)

# 判断一句话中是否有数字
# search 的特点：匹配字符串，匹配到一个结果就返回，不会匹配多个结果
# res = re.search('\d+', '我今年18岁了，喜欢5个明星')
# print(res.group()) # 18
# print(res.group()) # 18

# finditer 所有的数据都会进行匹配，返回的是迭代器
# it = re.finditer('\d+', '我今年18岁了，喜欢5个明星')
#
# for item in it:
#     print(item.group())

# match 匹配，从头开始匹配

# result = re.match('\d+', '我今年18岁了，喜欢5个明星')
# print(result)



# split() 根据规则进行切割
# re.split('\d+', '我今年18岁了，喜欢5个明星')


# sub() 替换
# re.split('\d+', '_sb_', '我今年18岁了，喜欢5个明星')

# re.compile() 先加载这个正则，后面可以直接用这个正则进行匹配

# obj = re.compile('\d+')
# lst = obj.findall('我今年18岁了，喜欢5个明星')
# print(lst)


# 重点
# 爬虫必会的一个重点
# 可以在字符串前面写 r 来直接吧字符串中的内容当普通字符处理
# obj = re.compile(r'\d+') # 预编译
# print(r'我今年\n18岁了') # 加r 当成字面意思

# () 起来的是最终想要的结果
# (?P<name>正则)
bj = re.compile(r'今天吃了(?P<mian>\d+)碗面，又吃了(?P<xian>\d+)盘小菜')
res1 = bj.finditer('明天我要吃3碗面，喝8碗汤，今天吃了4碗面，又吃了8盘小菜')
for item in res1:
    print(item.group('mian'))
    print(item.group('xian'))
    print(item.groupdict()) # {'mian': '4', 'xian': '8'}










