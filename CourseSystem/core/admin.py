'''
管理员视图

'''

from interface import admin_interface
from lib import common
admin_info = {
    'user': None
}

# 1.注册
def register():
    while True:
        username = input('请输入用户名').strip()
        password = input('请输入密码').strip()
        re_password = input('请确认密码').strip()
        # 密码判断
        if password == re_password:
            # 调用接口，管理员注册
            flag, msg = admin_interface.admin_register_interface(
                username,
                password
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致，请重新输入')


# 2.登录
def login():
    while True:
        username = input('请输入用户名').strip()
        password = input('请输入密码').strip()
        # 1、调用管理员登录接口
        flag, msg = admin_interface.admin_login_interface(
            username,
            password
        )
        if flag:
            print(msg)
            # 记录当前用户登录状态
            # 可变类型不需要global
            admin_info['user'] = username
            break
        else:
            print(msg)


# 3.创建学校
@common.auth('admin')
def create_school():
    pass


# 4.创建课程
@common.auth('admin')
def create_course():
    pass


# 5.创建讲师
@common.auth('admin')
def create_teacher():
    pass


func_dict = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_course,
    '5': create_teacher,
}


def admin_view():
    while True:
        print('''
            - 1.注册
            - 2.登录
            - 3.创建学校
            - 4.创建课程
            - 5.创建讲师
            ''')
        choice = input('请输入功能编号：').strip()
        if choice == 'q':
            break
        if choice not in func_dict:
            print('输入有误，请重新输入')
            continue

        func_dict.get(choice)()
