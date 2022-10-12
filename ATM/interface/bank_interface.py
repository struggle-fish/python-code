'''
银行相关业务的接口
'''

from db import db_handler


# 提现接口
def withdraw_interface(username, money):
    # 1) 先获取用户字典
    user_dic = db_handler.select(username)
    balance = int(user_dic.get('balance'))

    # 提现本金 + 手续费
    money2 = int(money) * 1.05

    # 判断用户金额是否足够
    if balance >= money2:
        # 2）修改用户字典中的金额
        balance -= money2
        user_dic['balance'] = balance
        # 3）再保存数据，或更新数据
        db_handler.save(user_dic)
        return True, f'用户[{username}] 提现金额{money}, 手续费为：[{money2 - float(money)}], 余额是[{balance}]'

    return False, '提现金额不足，请重新输入'


# 还款接口
def repay_interface(username, money):
    '''
        1.获取用户的金额
        2.给用户的金额做加钱的操作
        :return:
    '''
    # 1.获取用户字典
    user_dic = db_handler.select(username)

    # 2.直接做加钱操作
    user_dic['balance'] += money
    # 3.记录流水
    flow = f'用户：[{username}]  还款：[{money}]成功!'
    user_dic['flow'].append(flow)

    # 4.调用数据处理层，将修改后的数据更新
    return True, flow