class Settings:
    '''存储游戏中所有的设置'''

    def __init__(self):
        '''初始化设置'''
        self.screen_width = 1500
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)

        # 飞船速度
        self.ship_limit = 1

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 30

        # 外星人设置
        self.fleet_drop_speed = 10

        # 加快游戏节奏的速度
        self.speedup_scale = 2
        # 外星人分数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化游戏进行而变化的设置'''
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 2.5
        # fleet_direction 为1 表示向右，-1表示向左
        self.fleet_direction = 1
        # 记分
        self.alien_points = 50

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
