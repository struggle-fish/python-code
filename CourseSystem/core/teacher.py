'''
老师视图

'''
from lib import common
from interface import common_interface
teacher_info = {
    'user': None
}


# 1.登录
def login():
    while True:
        username = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()

        # 1.调用管理员登录接口
        flag, msg = common_interface.login_interface(
            username, password, user_type='teacher'
        )
        if flag:
            print(msg)
            # 记录当前用户登录状态
            # 可变类型不需要global
            teacher_info['user'] = username
            break

        else:
            print(msg)
    pass


# 2.查看教授课程
@common.auth('teacher')
def check_course():
    pass


# 3.选择教授课程
@common.auth('teacher')
def choose_course():
    pass


# 4.查看课程下学生
@common.auth('teacher')
def check_stu_from_course():
    pass


# 5.修改学生分数
@common.auth('teacher')
def change_score_from_student():
    pass


func_dict = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_stu_from_course,
    '5': change_score_from_student,
}


def teacher_view():
    while True:
        print('''
            - 1.登录
            - 2.查看教授课程
            - 3.选择教授课程
            - 4.查看课程下学生
            - 5.修改学生分数
            ''')
        choice = input('请输入功能编号：').strip()
        if choice == 'q':
            break
        if choice not in func_dict:
            print('输入有误，请重新输入')
            continue

        func_dict.get(choice)()
