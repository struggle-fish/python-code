'''
管理员视图

'''


# 1.注册
def register():
    while True:
        username = input('请输入用户名').strip()
        password = input('请输入密码').strip()
        re_password = input('请确认密码').strip()
        # 密码判断
        if password == re_password:
            # 调用接口，管理员注册
            pass
        else:
            print('两次密码不一致，请重新输入')


# 2.登录
def login():
    pass


# 3.创建学校
def create_school():
    pass


# 4.创建课程
def create_course():
    pass


# 5.创建讲师
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
