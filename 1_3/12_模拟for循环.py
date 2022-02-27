lst = ['张无忌', '谢广坤']

# for 内部工作机制

it = lst.__iter__() #拿到迭代器

while True:
    try:
        obj = it.__next__() # 拿到数据
        print(obj)
    except StopIteration:
        break

# 迭代器的特点：
# 节省内存
# 惰性机制
# 不能反复，只能向下执行

