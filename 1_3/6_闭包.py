# 把函数作为参数和返回值返回
# 闭包：内层函数对外层函数的变量的使用
# 作用1：可以让一个变量封锁起来，外界只能看到，但是不能修改
# 作用2： 可以让一个变量常驻内存

def func():
    a = 10
    def inner():
        print(a)
        return a
    return inner

fn = func()




