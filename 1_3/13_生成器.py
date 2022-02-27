# 生成器本质就是迭代器
# 通过生成器函数生成
# 通过生成器表达式实现
# 生成器节省内存


def func(): # 生成器函数
    print(123)
    yield '你好' # 函数中有 yield 中就是生成器函数, yeild 也有返回的意思
    yield '好不好呢'

gen = func() # 生成器函数在执行的时候，创建生成器
print(gen) # <generator object func at 0x7fc9880aaba0>
ret = gen.__next__() # next 可以让生成器函数执行到下一个 yield
print(ret)
ret2 = gen.__next__() # 执行下一个yeild
print(ret2)
# ret3 = gen.__next__() # 后面没有 yield 之后，会报错，StopIteration


'''
    生成器函数：
        1、里面有yield
        2、生成器函数在执行的时候，实际上是创建了一个生成器出来
        3、必须使用 __next__() 来执行一段代码，会自动的执行到下一个yield结束
        4、yield 也是返回的意思，可以让一个函数分段执行
        5、当后面没有 yield 之后 ，再次__next__() 会报错 StopIteration
'''


def order():
    for i in range(10000): # 1w件衣服，用多少个，出多少个，而不思一次性的出1w个
        yield f'衣服{i}'


g = order()
print(g.__next__())
print(g.__next__())
print(g.__next__())


def order2():
    lst = []
    for i in range(10000): #  50一次
        lst.append(f'衣服{i}')
        if len(lst) == 50:
            yield lst
            lst = []


g2 = order2()
print(g2.__next__())
print(g2.__next__())
print(g2.__next__())


# send

def func():
    print('111')
    a = yield '早饭'
    print('222', a)
    b = yield '午饭'
    print('333', b)
    yield '晚饭'


g3 = func()
r1 = g3.__next__() # 第一次调用必须是next, 不能send
print(r1)
r2 = g3.send('不是吃了吗') # send 给上一个yield 传参
print(r2)
r3 = g3.send('还吃不吃了')
print(r3)


'''
__next__
send
    相同点：可以执行到一下个yield
    不同点：send 可以给上一个yield 传值
'''






