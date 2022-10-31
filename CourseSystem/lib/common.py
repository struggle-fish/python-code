'''
公共方法
'''
from db import models


# 多用户登录认证装饰器
def auth(role):
    '''
    :param role: 角色 ---》 管理员、学生、老师
    :return:
    '''
    from core import admin, student, teacher

    def login_auth(func):
        def inner(*args, **kwargs):
            if role == 'admin':
                if admin.admin_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    admin.login()

            elif role == 'student':
                if student.student_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    student.login()

            elif role == 'teacher':
                if teacher.teacher_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    teacher.login()
            else:
                print('当前视图没有权限~')

        return inner

    return login_auth


# 公共登录接口
def login_interface(user, pwd, user_type):
    if user_type == 'admin':
        obj = models.Admin.select(user)
    elif user_type == 'student':
        obj = models.Student.select(user)
    elif user_type == 'teacher':
        obj = models.Teacher.select(user)
    else:
        return False, '登录角色不对，请输入角色'

    # 1.判断用户是否存在
    if obj:
        # 2.若用户存在，则校验密码
        if pwd == obj.pwd:
            return True, '登录成功'
        else:
            return False, '密码错误'
    # 3.若不存在，则证明用户不存在并返回给视图层
    else:
        return False, '用户名不存在'
