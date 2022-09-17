# 三元运算
a = 10
b = 20
c = a if a > b else b


# 递归
# 函数自己调用自己

# 递归可以完美的遍历一个文件夹
# os 可以访问计算机的文件夹系统
import os
def read(path, ceng):
    lst = os.listdir(path)
    for name in lst:
        # 需要拼接出正确的文件路径
        real_path = os.path.join(path, name)
        if os.path.isdir(real_path):
            # 文件夹
            # 进入递归
            print("\t" * ceng, name)
            read(real_path, ceng + 1)
        else:
            # 普通文件
            print("\t" * ceng, name)

read('../..', 0)














