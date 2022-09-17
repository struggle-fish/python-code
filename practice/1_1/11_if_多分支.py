'''
多分支语法

if 条件1:
    结果1
elif 条件2:
    结果2
elif 条件3:
    结果3
else:
    其他
'''

money = int(input('请输入数字'))

if money > 1000:
    print('财富自由')
elif money > 500:
    print('特别有钱')
elif money > 300:
    print('有钱啊')
else:
    print('啥也不是')


