# 装饰器是一个种固定语法，可以让我们在不修改原有函数内部代码的基础上，给函数添加新的功能
#
def wrapper(fn): # 把被装饰的函数传递进来
    def inner():
        # 被装饰函数之前，做些事情
        fn() # 执行被装饰的函数
        # 被装饰函数之后，做些事情
    return inner # 把内层函数返回



def add():
    print('我是新增函数')

add = wrapper(add)
add() # 执行的是 inner 函数



# 语法糖

def wrapper2(fn): # 把被装饰的函数传递进来
    def inner():
        # 被装饰函数之前，做些事情
        print('装饰之前')
        fn() # 执行被装饰的函数
        # 被装饰函数之后，做些事情
        print('装饰之后')
    return inner # 把内层函数返回

@wrapper2
def add():
    print('我是新增函数')

add()






