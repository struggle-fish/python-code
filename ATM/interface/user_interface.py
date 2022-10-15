'''
逻辑接口
    用户接口
'''
from db import db_handler
from lib import common

# 根据不同的接口类型传入不同的日志对象
user_logger = common.get_logger(log_type='user')


# 注册接口
def register_interface(username, password, balance=15000, ):
    # 3) 用户存在，则让用户重新输入
    user_dic = db_handler.select(username)
    if user_dic:
        return False, '用户已经存在'

    # 做密码加密
    password = common.get_pwd_md5(password)

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
    msg = f'{username} 注册成功'
    # 3.3）记录日志
    user_logger.info(msg)
    return True, msg


# 登录接口
def login_interface(username, password):
    # 1) 先查看当前用户数据是否存在
    user_dic = db_handler.select(username)

    # 2) 判断用户是否存在
    if user_dic:

        # 用户是否被冻结
        if user_dic.get('locked'):
            return False, '当前用户已被锁定'

        # 3) 校验密码是否一致
        password = common.get_pwd_md5(password)
        if password == user_dic.get('password'):
            msg = f'用户：[{username}] 登录成功'
            user_logger.info(msg)
            return True, msg
        else:
            msg = f'用户[{username}] 密码错误'
            user_logger.warn(msg)
            return False, msg

    msg = f'用户[{username}] 用户不存在，请重新输入'
    user_logger.warn(msg)
    return False, msg


# 查看余额接口
def check_bal_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['balance']
