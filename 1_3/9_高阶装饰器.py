# 多个装饰器一起装饰
# 就近原则解读



def wrapper1(fn):
    def inner(*args, **kwargs):
        print('wrapper1-before')
        ret = fn(*args, **kwargs)
        print('wrapper1-after')
        return ret
    return inner

def wrapper2(fn):
    def inner(*args, **kwargs):
        print('wrapper2-before')
        ret = fn(*args, **kwargs)
        print('wrapper2-after')
        return ret
    return inner

def wrapper3(fn):
    def inner(*args, **kwargs):
        print('wrapper3-before')
        ret = fn(*args, **kwargs)
        print('wrapper3-after')
        return ret
    return inner



'''
执行顺序：
wrapper3-before
wrapper2-before
wrapper1-before
我是add
wrapper1-after
wrapper2-after
wrapper3-after
'''

@wrapper3
@wrapper2
@wrapper1
def add():
    print('我是add')



