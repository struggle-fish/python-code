# 函数内部，不允许直接更改外部变量的值

# a = 10
# def func():
#     a = a + 1 # 不允许更改



# a = 10
# def func():
#     global a # 引入全局
#     a = a + 1
#
# func()
# print(a)



def fun1():
    a = 10
    def fun2():
        nonlocal a # 必须在局部，引入局部变量
        a += 1
    fun2()
    print(a)

fun1()


