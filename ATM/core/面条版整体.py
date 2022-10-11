def register():
    while True:
        # 1) 让用户输入用户名与密码进行校验
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请确认密码：').strip()

        # 小逻辑处理，两次输入密码是否一致
        if password == re_password:
            import json
            import os
            from conf import settings
            user_path = os.path.join(
                settings.USER_DATA_PATH,
                f'{username}.json'
            )
            # 接收到注册之后的结果，并打印
            # 2）查看用户是否存在
            if os.path.exists(user_path):

                with open(user_path, 'r', encoding='utf-8') as f:
                    user_dic = json.load(f)
                if user_dic:
                    print('用户已经存在了，请重新输入')
                    continue



            # 3) 用户存在，则让用户重新输入
            # 4) 若用户不存在，保存用户数据
            # 4.1）组织用户的数据的字典信息
            user_dic = {
                'username': username,
                'password': password,
                'balance': 15000,
                'flow': [],
                'shop_car': {},
                'locked': False,  # False 未被冻结，True 已被冻结

            }

            # 存不是目的，目的是为了更方便的获取数据
            # 用户数据， 用户名.json xxx.json
            # 4.2）拼接用户的json文件路径
            with open(user_path, 'w', encoding='utf-8') as f:
                json.dump(user_dic, f, ensure_ascii=False)