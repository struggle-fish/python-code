'''
if 嵌套

if 条件1:
    if 条件2:
        结果1
    else:
        结果2
else:
    结果3
'''

# 模拟登录
userName = input('请输入您的用户名')
passWord = input('请输入密码')

if userName == 'admin':
    # pass 保证语法结构的完整
    if passWord == '123':
        print('登录成功')
    else:
        print('密码错误')
else:
    print('输入错了')