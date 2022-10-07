# 一：递归的定义
# 函数的递归调用：是函数嵌套调用的一种特殊形式
# 具体是指：
#        在调用一个函数的过程中又直接或者间接地调用到本身

# 直接调用本身
# def f1():
#     print('是我是我还是我')
#     f1()
# f1()

# 间接接调用本身
# def f1():
#     print('===>f1')
#     f2()
#
# def f2():
#     print('===>f2')
#     f1()
#
# f1()


# 一段代码的循环运行的方案有两种
# 方式一：while、for循环
# while True:
#     print(1111)
#     print(2222)
#     print(3333)

# 方式二：递归的本质就是循环：
# def f1():
#     print(1111)
#     print(2222)
#     print(3333)
#     f1()
# f1()


# 二：需要强调的的一点是：
# 递归调用不应该无限地调用下去，必须在满足某种条件下结束递归调用
# n=0
# while n < 10:
#     print(n)
#     n+=1


# def f1(n):
#     if n == 10:
#         return
#     print(n)
#     n+=1
#     f1(n)
#
# f1(0)

# 三：递归的两个阶段
# 回溯：一层一层调用下去
# 递推：满足某种结束条件，结束递归调用，然后一层一层返回

# age(5) = age(4) + 10
# age(4) = age(3) + 10
# age(3) = age(2) + 10
# age(2) = age(1) + 10
# age(1) = 18

# def age(n):
#     if n == 1:
#         return 18
#     return age(n-1) + 10
#
#
# res=age(5)
# print(res)

# 四：递归的应用
l=[1,2,[3,[4,[5,[6,[7,[8,[9,10,11,[12,[13,]]]]]]]]]]

def f1(list1):
    for x in list1:
        if type(x) is list:
            # 如果是列表，应该再循环、再判断,即重新运行本身的代码
            f1(x)
        else:
            print(x)

f1(l)


