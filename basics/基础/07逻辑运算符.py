# 2、什么是条件？什么可以当做条件？为何要要用条件？
# 第一大类：显式布尔值
# 2.1 条件可以是：比较运算符
# age = 18
# print(age > 16)  # 条件判断之后会得到一个布尔值

# 2.1 条件可以是：True、False
# is_beautiful=True
# print(is_beautiful)


# 第二大类：隐式布尔值，所有的值都可以当成条件去用
# 其中0、None、空(空字符串、空列表、空字典)=》代表的布尔值为False，其余都为真


# 一：not、and、or的基本使用
# not：就是把紧跟其后的那个条件结果取反
# ps: not与紧跟其后的那个条件是一个不可分割的整体

# print(not 16 > 13)
# print(not True)
# print(not False)
# print(not 10)
# print(not 0)
# print(not None)
# print(not '')

# and：逻辑与，and用来链接左右两个条件，两个条件同时为True，最终结果才为真
# print(True and 10 > 3)

# print(True and 10 > 3 and 10 and 0)  # 条件全为真，最终结果才为True
# print(10 > 3 and 10 and 0 and 1 > 3 and 4 == 4 and 3 != 3)  # 偷懒原则

# or：逻辑或，or用来链接左右两个条件，两个条件但凡有一个为True，最终结果就为True，
#            两个条件都为False的情况下，最终结果才为False
# print(3 > 2 or 0)
# print(3 > 4 or False or 3 != 2 or 3 > 2 or True) # 偷懒原则


# 二：优先级not>and>or
# ps：
# 如果单独就只是一串and链接，或者说单独就只是一串or链接，按照从左到右的顺讯依次运算即可（偷懒原则）
# 如果是混用，则需要考虑优先级了

# res = 3 > 4 and not 4 > 3 or 1 == 3 and 'x' == 'x' or 3 > 3
# print(res)
#
# #       False                 False              False
# res=(3>4 and (not 4>3)) or (1==3 and 'x' == 'x') or 3 >3
# print(res)


res = 3 > 4 and ((not 4 > 3) or 1 == 3) and ('x' == 'x' or 3 > 3)
print(res)
