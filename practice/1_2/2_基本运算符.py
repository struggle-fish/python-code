a = 10
b = 20
#算数运算 + - * /
print(a // b) # 计算商
print(a % b) # 计算余数

print(3 ** 2) # 3 的 2次方



# 比较运算 >  <  == !=  >=  <=


# 赋值运算
a = b # 把 b 得值 赋值给 a
a += b # 累加计算
a -= b
a *= b
a /= b
a %= b



# 逻辑运算
# and   并且  -> &&
# or    或者  -> ||
# not   非    -> !

print(True and False)
print(True or False)

# 重点  当出现 and or not () 混合使用的时候
# 运算顺序
# () > not > and > or
print(True or (False and True) or not False and True)
print(1 > 2 or 3 < 4 and 4 > 6)

# 非常规问题
# 非0 -> True
# 0 -> Flase
print(1 or 2 and 3)

print(0 or 3 and 4 or 0 and 5 or 1 and 0)


# 成员运算  in , not in
# 可以用来滤过敏感词
content = input('请输入评论')
if '苍井空' in content:
    print('敏感词')
else:
    print('评论通过')




















