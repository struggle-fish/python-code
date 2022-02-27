# 匿名函数

def func(n):
    return n ** 2

ret = func(10)
print(ret)

# 匿名函数有被称作 lambda 表达式
# 语法: lambda 参数: 返回值

fn = lambda n : n ** 2
print(fn(2))


fn2 = lambda a, b: (a + b, a - b)
print(fn2(2, 4))
# 注意事项：
# 1、函数可以有多个参数，逗号隔开
# 2、匿名函数不管多复杂，只能写一行，且逻辑结束后返回数据
# 3、返回值和正常的函数一样，可以是任意数据类型

