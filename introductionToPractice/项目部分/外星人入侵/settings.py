class Settings:
    '''存储游戏中所有的设置'''

    def __init__(self):
        '''初始化设置'''
        self.screen_width = 400
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # 飞船速度
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
