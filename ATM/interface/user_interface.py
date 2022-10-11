'''
逻辑接口
    用户接口
'''
from db import db_handler

# 注册接口
def register_interface(username, password, balance=15000,):
    # 3) 用户存在，则让用户重新输入
    user_dic = db_handler.select(username)
    if user_dic:
        return False, '用户已经存在'

    # 4) 若用户不存在，保存用户数据
    # 4.1）组织用户的数据的字典信息
    user_dic = {
        'username': username,
        'password': password,
        'balance': balance,
        'flow': [],
        'shop_car': {},
        'locked': False,  # False 未被冻结，True 已被冻结

    }

    # 保存数据
    db_handler.save(user_dic)
    return True, f'{username} 注册成功'
