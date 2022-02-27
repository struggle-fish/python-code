# 函数的基本概念
# 函数是对功能或动作的封装


# 函数定义
# def 函数名()
#     函数体

# 函数的返回值 return

# def yue():
#     print('出来单挑呀')
#     return '敢不敢呀，给个话'
# # 调用
# a = yue()
# print(a)


# 关于 return
# 1. 遇到return 后面的立即停止
# 2. 函数中如果没有写 return 默认返回 None

def func(type, c, d): # 形参
    print(type, c, d)
    print(f'买菜{type}')
    return '鱼', '白菜'
# ret = func('我') # 返回的是元祖
# print(ret)

# 按照形参的名字传递参数
func(type = '我', d = '谁', c = '不知道')

# 形参在执行的时候必须得有明确的数据，实参的数量必须和形参一致



