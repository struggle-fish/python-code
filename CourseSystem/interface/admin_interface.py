'''

管理员接口
'''

from db import models


def admin_register_interface(username, password):
    # 1、判断用户是否存在
    # 调用 Admin 类中的 select 方法
    # 由该方法去调用 db_handler 中的 select_data 功能获取对象

    admin_obj = models.Admin.select(username)
    # 1.1) 若存在不允许注册，返回用户已存在给视图层
    if admin_obj:
        return False, '用户已存在'

    # 1.2) 若不存在则允许注册，调用类实例化得到对象并保存
    admin_obj = models.Admin(username, password)
    # 对象调用 save 会将 admin_obj 传给 save 方法
    admin_obj.save()
    return True, '注册成功'

