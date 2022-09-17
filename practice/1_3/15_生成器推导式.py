g = (i for i in range(5))
print(g)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# 一次性把生成器的数据全拿出来
# 1. 直接for 循环
# for item in g:
#     print(item)

# 2、可以使用 list tuple set 直接把生成器拿空
# print(list(g))
# print(tuple(g))
# print(set(g))

############## 惰性机制
def func():
    print(111)
    yield 222 # 票

g = func() # 创建生成器  黄牛1
g1 = (i for i in g) # g1 是一个生成器  黄牛2
g2 = (i for i in g1) # g2 也是生成器  黄牛3

print(list(g)) # [222]
print(list(g1)) # []
print(list(g2)) # []

# 返回值的 yield

def func2():
    lst1 = ['麻花1', '沈腾1', '大聪明1']
    lst2 = ['麻花2', '沈腾2', '大聪明2']

    # for item in lst1:
    #     yield item
    #
    # for item in lst2:
    #     yield item

    yield from lst1 # 把可迭代对象中的每一项一次返回
    yield from lst2


g = func2()
print(list(g))