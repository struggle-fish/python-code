# 把 python 中的字典或者列表，转成json字符串
# 前端返回的json 字符串，想办法变成python中的字典
import json

dic = {'id': 1, 'name': '小鱼儿'}
s = json.dumps(dic, ensure_ascii=False) # json 处理中文 ensure_ascii=False
print(s)

s1 = '{"id": 1, "name": "小鱼儿"}'
d = json.loads(s1)
print(d, type(d))

# dumps: 可以把对象转成json
# loads: 可以把json转成对象

# 前端的json 和 python 中的字典的区别
d2 = { 'id': 1, 'isLogin': True, 'hasGirl': None }
print(json.dumps(d2))
# 前端json {"id": 1, "isLogin": true, "hasGirl": null}
# True -> true
# None -> null
# False -> false

json.dump(d2, open('j.txt', mode='w', encoding='utf-8'), ensure_ascii=False)



'''
    1、json是一种数据交互的数据格式
    2、来自前端
    3、dumps
    4、loads
    5、dump
    6、load
'''






