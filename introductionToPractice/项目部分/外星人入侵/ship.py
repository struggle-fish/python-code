import pygame


class Ship:
    '''管理飞船类'''

    def __init__(self, ai_game):
        # ai_game 是父类的 self
        '''初始化飞船并设置初始化位置'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图片
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每个飞船，都放到底部
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志调整飞机的位置
            小飞机的右侧不能过界
            左侧得大于0
        '''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        '''指定位置绘制'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''让飞船在屏幕底部居中'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
