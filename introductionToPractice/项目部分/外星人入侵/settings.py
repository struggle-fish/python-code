class Settings:
    '''存储游戏中所有的设置'''

    def __init__(self):
        '''初始化设置'''
        self.screen_width = 1000
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)

        # 飞船速度
        self.ship_speed = 1.5
        self.ship_limit = 1

        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 30

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        # fleet_direction 为1 表示向右，-1表示向左
        self.fleet_direction = 1
