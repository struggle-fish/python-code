class Settings:
    '''存储游戏中所有的设置'''

    def __init__(self):
        '''初始化设置'''
        self.screen_width = 400
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # 飞船速度
        self.ship_speed = 1.5

