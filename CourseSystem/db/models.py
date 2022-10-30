'''
用于存放各种类
学校类、学员类、课程类、讲师类、管理员类
'''

from db import db_handler


# 父类，让所有子类都继承 select 与 save 方法
class Base:
    pass


# 管理员类
class Admin(Base):
    # 调用类的时候触发
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)
        return obj

    # 保存数据
    def save(self):
        db_handler.save_data(self)


class School(Base):
    pass


class Student(Base):
    pass


class Course(Base):
    pass


class Teacher(Base):
    pass
