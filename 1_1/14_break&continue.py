'''
break: 退出循环

continue: 结束当前循环
'''

while True:
    content = input('请输入你想说的话(Q退出)')
    if content == 'Q':
        break
    print('我想对你说：' + content)

