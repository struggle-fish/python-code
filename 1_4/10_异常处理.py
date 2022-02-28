'''
1、处理异常
try:
    xxx
except 错误1 as 变量1:
    xxx
except 错误2 as 变量2:
    xxx
except Exception as e:
    最终错误

2、抛出异常
     raise Exception('不是int类型，无法计算')
'''

# try:
#     print(1/0)
# except ZeroDivisionError as z:
#     print('除数为0')
# except FileExistsError as f:
#     print('文件不存在')
# except Exception as e: # 万能的错误接受
#     print('系统错误')
# finally:    # 不论是否出错，都会走这个
#     print('收尾')


# 程序是可以自己抛出异常的

def func(a, b): # 计算两个int类型的数字和
    if type(a) == int and type(b) == int:
        return a + b
    else:
        raise Exception('不是int类型，无法计算') # 抛出异常，谁调用，谁接收异常


func('haha', 1)



