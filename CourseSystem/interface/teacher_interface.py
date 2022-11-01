'''
老师接口
'''

from db import models


# 老师查看课程接口
def check_course_interface(teacher_name):
    # 1、获取当前老师对象
    teacher_obj = models.Teacher.select(teacher_name)
    # 2、判断老师对象中课程列表是否有值
    # 让老师对象，调用查看教授课程方法，返回课程
    # course_list = teacher_obj.course_list_from_tea
    course_list = teacher_obj.show_course()
    # 3、若有则返回True， 无则返回False
    if not course_list:
        return False, '老师没有选择课程'

    return True, course_list
