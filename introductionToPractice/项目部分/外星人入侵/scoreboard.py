import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    '''显示得分信息'''

    def __init__(self, ai_game):
        '''初始化显示得分的属性'''
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备输出得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''将得分转化成一幅图'''
        rounded_score = round(self.stats.score, -1)
        # 格式化 数字 1000 -> 1,000
        score_str = "{:,}".format(rounded_score)

        self.score_image = self.font.render(
            score_str,
            True,
            self.text_color,
            self.settings.bg_color)

        # 在屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''将最高得分转化为可渲染的图像'''
        hight_score = round(self.stats.high_score, -1)
        hight_score_str = "{:,}".format(hight_score)

        self.hight_score_image = self.font.render(
            hight_score_str,
            True,
            self.text_color,
            self.settings.bg_color
        )

        # 将最高得分放在屏幕顶部中央
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = self.score_rect.top

    def check_high_score(self):
        '''检查是否诞生了新的最高分'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        '''将等级转化成图像渲染'''
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str,
            True,
            self.text_color,
            self.settings.bg_color
        )
        # 将等级放在得分下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''显示剩下多少飞船'''
        '''
        为填充这个编组，根据玩家还有多少艘飞船以相应的次数运行一个循环（见❷）。在这个循环中，创建新飞船并设置其[插图]坐标，让整个飞船编组都位于屏幕左边，且每艘飞船的左边距都为10像素（见❸）。还将[插图]坐标设置为离屏幕上边缘10像素，让所有飞船都出现在屏幕左上角（见❹）。
        最后，将每艘新飞船都添加到编组ships中（见❺）。
        '''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        '''显示得分'''
        self.screen.blit(
            self.score_image,
            self.score_rect
        )
        self.screen.blit(
            self.hight_score_image,
            self.hight_score_rect
        )
        self.screen.blit(
            self.level_image,
            self.level_rect
        )
        self.ships.draw(self.screen)
