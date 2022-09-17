def gua_outer(name):
    def gua(fn):
        def inner(*args, **kwargs):
            print(f'开启{name}外挂')
            ret = fn(*args, **kwargs)
            print('关闭外挂')
            return ret
        return inner
    return gua

@gua_outer('你好') # 先执行gua_outer 函数的调用，返回一个函数和@组合成装饰器语法糖使用
def dnf():
    print('我要我哪儿dnf')

dnf()