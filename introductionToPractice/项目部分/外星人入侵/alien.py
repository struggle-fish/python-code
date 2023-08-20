import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    '''表示单个外星人类'''

    def __init__(self, ai_game):
        '''初始化外星人并设置其实位置'''
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # 加载外星人图片
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)

    def check_edges(self):
        '''如果外星人位于屏幕边缘，就返回True'''
        '''
        可对任意外星人调用新方法check_edges()，看其是否位于屏幕左边缘或右边缘。如果外星人的rect的属性right大于或等于屏幕的rect的right属性，就说明外星人位于屏幕右边缘；
        如果外星人的rect的left属性小于或等于0，就说明外星人位于屏幕左边缘（见❶）。
        '''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        '''向右移动外星人'''
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
