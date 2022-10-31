'''
学生视图
'''
from lib import common
from interface import student_interface
from interface import common_interface

student_info = {
    'user': None
}


# 1.注册
def register():
    while True:
        username = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()
        re_password = input('请确认密码: ').strip()
        # 小的逻辑判断
        if password == re_password:
            # 调用接口层，学生注册接口
            flag, msg = student_interface.student_register_interface(
                username, password
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致，请重新输入')


# 2.登录功能
def login():
    while True:
        username = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()
        # 1.登录接口
        flag, msg = common_interface.login_interface(
            username, password, user_type='student'
        )
        if flag:
            print(msg)
            # 记录当前用户登录状态
            # 可变类型不需要global
            student_info['user'] = username
            break

        else:
            print(msg)


# 3.选择校区
@common.auth('student')
def choice_school():
    while True:
        # 1、获取所有学校，让学生选择
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break

        for index, school_name in enumerate(school_list):
            print(f'编号： {index} 学校名：{school_name}')

        # 2、让学生输入学校编号
        choice = input('请输入选择的学校编号：').strip()
        if not choice.isdigit():
            print('输入有误')
            continue

        choice = int(choice)
        if choice not in range(len(school_list)):
            print('输入编号有误')
            continue

        school_name = school_list[choice]
        # 3、开始调用学生选择学校接口
        flag, msg = student_interface.add_school_interface(
            school_name,
            student_info.get('user')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 4.选择课程
@common.auth('student')
def choice_course():
    pass


# 5.查看分数
@common.auth('student')
def check_score():
    pass


func_dict = {
    '1': register,
    '2': login,
    '3': choice_school,
    '4': choice_course,
    '5': check_score,
}


def student_view():
    while True:
        print('''
            - 1.注册
            - 2.登录功能
            - 3.选择校区
            - 4.选择课程
            - 5.查看分数
            ''')
        choice = input('请输入功能编号：').strip()
        if choice == 'q':
            break
        if choice not in func_dict:
            print('输入有误，请重新输入')
            continue

        func_dict.get(choice)()
