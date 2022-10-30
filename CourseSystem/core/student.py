'''
学生视图
'''


# 1.注册
def register():
    pass


# 2.登录功能
def login():
    pass


# 3.选择校区
def choice_school():
    pass


# 4.选择课程
def choice_course():
    pass


# 5.查看分数
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