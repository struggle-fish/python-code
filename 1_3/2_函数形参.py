# 函数的形参
# 第一类：位置参数, 从左到右顺序写变量
# 第二类： 默认传参
# 第三类： 动态传参
# 形参：在函数声明的位置编写的变量

# def func(a, b, c):
#     print(a, b, c)
#
# # 位置参数
# func(11, 22, 33)

# 默认值参数
# def func(name, age, gender='男'):
#     print(name, age, gender)
#
# func('小鱼儿', 18)

# 如果默认值参数是可变的数据类型，会提前声明好，引用
# def func(val, lst=[]):
#     lst.append(val)
#     print(lst)
#
# func(10086)     # [10086]
# func(10010)     # [10086, 10010]



# 动态传参
# 给出多个参数，在形参位置，一次性接收
# *args: 动态接收位置参数，自动打包成元祖

# def func(*food):
#     print(food)     # 收到的是元祖
#
# func('啊哈哈')
# func('hahah', '啊哈哈问额')

# **kwargs: 动态接受关键字参数
# 接收到的是参数是字典
# def chi(**food):
#     print(food)
#
# chi(main_food="面条", fu_food="西红柿")


# 实参：
# 1、位置参数
# 2、关键字参数
# 3、混合参数：先位置，后关键字

# 形参：
# 1、位置参数
# 2、默认值参数
# 3、动态传参
#       混合使用，一定要注意顺序
#       顺序：位置参数 》*args 》 默认值参数 》**kwargs
#       上面的参数可以任意搭配使用，但是顺序不能变

# def func(a, *args, c='哈哈', **kwargs):
#     print(a, *args, c, **kwargs)

def func(*args, **kwargs): # 表示该函数可以接收任意的参数
    print(args)
    print(kwargs)

func('你好', '你不好说', a='哈哈哈', b='哼哼')


