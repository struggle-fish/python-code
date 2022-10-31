'''
学生接口
'''
from db import models

# 学生注册接口
def student_register_interface(user, pwd):
    # 1.判断用户是否存在
    # 调用Student类中的，select方法，
    # 由该方法去调用db_handler中的select_data功能获取对象
    student_obj = models.Student.select(user)
    # 1.1) 若存在不允许注册，返回用户已存在给视图层
    if student_obj:
        return False, '学生用户已存在!'
    # 1.2) 若不存在则允许注册，调用类实例化得到对象并保存
    student_obj = models.Student(user, pwd)
    # 对象调用save() 会将 admin_obj传给save方法
    student_obj.save()
    return True, '注册成功!'
