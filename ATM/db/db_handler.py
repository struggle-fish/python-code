'''
数据处理层
    - 专门用户处理数据的
'''

# 查看用户是否存在数据
import json
import os

from conf import settings


def select(username):
    # 1) 接收接口层传过来的username用户名，拼接用户json文件路径
    user_path = os.path.join(
        settings.USER_DATA_PATH,
        f'{username}.json'
    )
    # 2）校验用户json文件是否存在
    if os.path.exists(user_path):
        # 3) 打开数据，并返回给接口层
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic
    # 4) 不return，默认return None


# 保存数据
def save(user_dic):
    username = user_dic.get('username')
    user_path = os.path.join(
        settings.USER_DATA_PATH,
        f'{username}.json'
    )
    # 存不是目的，目的是为了更方便的获取数据
    # 用户数据， 用户名.json xxx.json
    # 4.2）拼接用户的json文件路径
    with open(user_path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f, ensure_ascii=False)
