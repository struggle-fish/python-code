# 列表推导式
# [结果 for 循环 if条件]

lst = [i for i in range(1, 11)]
lst2 = [i for i in range(1, 11) if i % 2 == 1]

# python x 1 ~ pyton x 255
lst3 = ['python x %s' % i for i in range(1, 256)]


# 字典推导式
# { key: value for 循环 if }
lst4 = ['你好', '不好', '好不好'] # => {0: '你好', 1: '不好', 2: '好不好'}
d = {i: lst4[i] for i in range(len(lst4))}
print(d)



# 集合推导式
# { key for 循环 if }

lst5 = ['张无忌', '张三丰', '张无忌']
s = { item for item in lst5 }
print(s)

# python 中没有元祖推导式






