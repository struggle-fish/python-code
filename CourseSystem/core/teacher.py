'''
老师视图

'''
from lib import common
from interface import common_interface
from interface import teacher_interface

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
    flag, course_list = teacher_interface.check_course_interface(
        teacher_info.get('user')
    )
    if flag:
        print(course_list)
    else:
        print(course_list)


# 3.选择教授课程
@common.auth('teacher')
def choose_course():
    while True:
        # 1、先打印所有学校，并选择
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break

        for index, school_name in enumerate(school_list):
            print(f'编号: {index}   学校名: {school_name}')

        choice = input('请输入选择的学校编号: ').strip()
        if not choice.isdigit():
            print('输入有误')
            continue

        choice = int(choice)

        if choice not in range(len(school_list)):
            print('输入编号有误!')
            continue

        # 获取选择的学校名称
        school_name = school_list[choice]

        # 2、从选择的学校中获取所有的课程
        flag2, course_list = common_interface.get_course_in_school_interface(
            school_name
        )
        if not flag2:
            print(course_list)
            break

        for index2, course_name in enumerate(course_list):
            print(f'编号: {index2}   课程名: {course_name}')

        choice2 = input('请输入选择的课程编号: ').strip()

        if not choice2.isdigit():
            print('输入有误')
            continue

        choice2 = int(choice2)

        if choice2 not in range(len(course_list)):
            print('输入编号有误!')
            continue

        # 获取选择的课程名称
        course_name = course_list[choice2]

        # 3、调用选择教授课程接口，将该课程添加到老师课程列表中
        flag3, msg = teacher_interface.add_course_interface(
            course_name, teacher_info.get('user')
        )
        if flag3:
            print(msg)
            break
        else:
            print(msg)


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
