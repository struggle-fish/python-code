from db import db_handler
from lib import common

# 根据不同的接口类型传入不同的日志对象
admin_logger = common.get_logger(log_type='admin')


# 修改额度接口
def change_balance_interface(username, money):
    user_dic = db_handler.select(username)

    if user_dic:
        user_dic['balance'] = int(money)

        db_handler.save(user_dic)
        msg = f'管理员修改用户：[{username}] 额度修改成功'
        admin_logger.info(msg)
        return True, msg
    return False, '修改额度用户不存在'


# 冻结账户接口
def lock_user_interface(username):
    user_dic = db_handler.select(username)
    if user_dic:
        user_dic['locked'] = True
        db_handler.save(user_dic)
        msg = f'用户{username}冻结成功'
        admin_logger.info(msg)
        return True, msg
    return False, '冻结用户不存在'
