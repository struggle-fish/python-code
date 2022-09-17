
# 循环删除列表
# 方案一
lst = ['列表1', '列表2', '列表3']
new_list = []

for name in lst:
    if name.startswith('列表'):
        new_list.append(name)

for a in new_list:
    lst.remove(a)

print(lst)


# 方案二
for name in lst[:]:
    if name.startswith('列表'):
        lst.remove(name)


# 字典的删除
# 把要删除的内容记录在列表中，循环列表删除字典

dic = {'jay': '周杰伦', '55k': '卢本伟'}
lst = list(dic.keys())
for k in lst:
    dic.pop(k)

# == 和 is
# == 判断的是两个内容的值是否一致
# is 判断的是两个内容的内存地址是否一致
# 一般用 is 判断是否为空 is None
#
c = None
if c is None:
    pass
else:
    pass


# while 循环
# while 条件:
#   pass
# else: # 条件不成立的时候执行
#   pass

# 判断一个数是否是质数
# 质数：能被1 和自身整除的数

n = int(input('请输入数字').strip())

i = 2
while i < n:
    if n % i == 0: # 整除不是质数
        print('不是质数')
        break
    i += 1
else:
    print('是质数')













