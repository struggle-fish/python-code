# pickle 就是我们的python 对象写入到文件中的一种解决方案，但是写入到文件的是bytes
# python 对象转成成字节的过程被称为序列化

import pickle

# lst = ['周杰伦', '成功', '小鱼儿']
# bs = pickle.dumps(lst) # 转成二进制字节
# print(bs)
#
# lst2 = pickle.loads(bs) # 二级制转成对应类型
# print(lst2)

# 把数据存储到文件中最合理的是用pickle
# dic = { 'name' : '小鱼儿', 'age': 19 }
# pickle.dump(dic, open('d.data', mode='wb'))

# 读取序列化后的文件
dic2 = pickle.load(open('d.data', mode='rb'))
print(dic2)

'''
    dumps   把对象（数据）转成字节
    loads   把字节转回对象（数据）
    dump    把对象序列化成字节之后写入到文件
    load    把文件中的字节反序列化成对象
'''

