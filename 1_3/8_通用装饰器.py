
def wrapper(fn):
    def inner(*args, **kwargs):
        ret = fn(*args, **kwargs) # 目标函数可能有返回值
        return ret
    return inner

# 被装饰的函数有参数情况

@wrapper
def add(name):
    print(f'{name}-哈哈哈')
    return '玩儿漂亮'

print(add('哈哈哈'))


# 装饰器的应用

flag = False

def login_verify(fn):
    '''
    这里是登录校验的装饰器
    :param fn: 被装饰的函数
    :return: inner
    '''
    def inner(*args, **kwargs):
        while 1: # 反复判断登录状态，直到登录成功位置
            if flag:
                ret = fn(*args, **kwargs)
                return ret
            else:
                login()
    return inner

def login():
    global flag
    username = input('请输入用户名')
    password = input('请输入密码')
    if username == 'admin' and password == '123':
        print('登录成功')
        flag = True
    else :
        print('登录失败')

@login_verify
def add():
    print('我要执行新增操作')



