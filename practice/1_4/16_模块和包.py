# 模块的搜索路径
# sys.path: python 的环境变量

# 先找自己文件夹，再找项目，最后找python

print(__name__) # 每个模块中都会有这个内置变量

# 当次模块被直接运行的时候 __main__ 程序的入口 运行的入口
# 当这个模块被导入的时候  就是文件的名字

# 以下内容：自己运行的时候可以正常执行
# 如果被别人以模块的形式导入的时候，不希望执行

if __name__ == '__main__':
    print('自己执行可以看见，外部引入看不见')


# as 别名
import html as html1

# from
# from xx import xxx

