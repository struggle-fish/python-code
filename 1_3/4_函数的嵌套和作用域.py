# python 程序在加载的时候，会给解释器内部的需要的内置一些变量加载，加载的位置叫内置命名空间
# 你自己写的，会统一放在全局命名空间
# 当程序执行到函数的时候，函数内部会有自己的变量，python 会为每一个正在执行的函数单独开辟内存, 局部命名空间

# a = 10
# print('你好全世界')
#
# def func():
#     a = 20
#     print(a)

# 内置命名空间：python 自己的内容
# 全局命名空间： 全局变量 + 内置
# 局部命名空间： 函数被调用的时候，当函数执行完毕，会被回收

# 作用域
# 一个变量能够发挥作用的范围，能在哪儿调用
# 全局作用域，整个py文件中随意使用
# 局部作用域，只能在局部命名空间使用


# globals() 可以查看全局作用域中的变量
# locals() 查看当前作用域中的变量
# print(globals())


# 全局作用域内容：全局命名空间 + 内置命名空间







