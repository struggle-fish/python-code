# 随机模块
import random

# 一个随机数 (0, 1)
# print(random.random())

# 随机小数
# random.uniform(5, 9)
# random.randint(3, 8) 随机整数 可以取到边界

# random.choice(lst) 随机选择一个

# random.sample(lst, 2) 随机抽出几个

# lst = ['屠龙刀', 'AK', '金箍棒', '2w']
# print(random.sample(lst, 2))


# 随机生成4位验证码
# 4位验证码，一个个的生成
# 可能会有数字，可能会大写字母，也可能小写字母

def rand_num():
    return str(random.randint(0, 9))
def rand_upper():
    return chr(random.randint(65, 90))
def rand_lower():
    return chr(random.randint(97, 122))

def rand_verify_code(n = 4):
    lst = []
    for i in range(n):
        which = random.randint(1, 3)
        if which == 1: # 随机数字
            s = rand_num()
        elif which == 2: # 随机大写字母
            s = rand_upper()
        elif which == 3:
            s = rand_lower()
        lst.append(s)
    return ''.join(lst)

print(rand_verify_code())

















