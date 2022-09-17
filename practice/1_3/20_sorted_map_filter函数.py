# sorted()
# map()
# filter()

# sorted() 排序
lst = [1, 12, 34, 6, 90, 29]
res = sorted(lst, reverse=True)
print(res)


lst1 = ['赵本山', '周杰伦', '文静']

# 自定义排序规则
def func(item):
    return len(item)

res1 = sorted(lst1, key=func)
print(res1)

# filter 筛选
lst2 = [7, 29, 90, 33, 6]
f = filter(lambda x: x % 3 == 0, lst2)
print(list(f))


# map 映射函数
lst3 = [1, 3, 5]
m = map(lambda x: x + 1, lst3)
print(list(m))











