# dir() 可以查看可以执行哪些操作

# 所有可迭代的对象，都有 __iter__的功能

# iterable 可迭代的

lst = ['你好', '好'] # 列表不是迭代器，是可迭代
it = lst.__iter__() # iterator 迭代器  迭代器本身是一个可迭代对象，迭代器可以使用 for
ret = it.__next__()
print(ret)

it = iter(lst)
print(next(it))
print(next(it))

# 使用步骤：
# 1、通过__iter__拿到可迭代对象中的迭代器
# 2、用迭代器执行 __next__ 拿到元素
# 3、重复第二步，反复执行，直到最后出现了StopIteration结束

# 坑：
# 1、想让迭代器重头拿数据，需要重新迭代
# 2、不适合等价代换  必须用变量存一下


