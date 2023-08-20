import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.settings = Settings()
        # 窗口大小
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        '''开始游戏主循环'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            # 让最近绘制的屏幕可见
            self._update_screen()

    def _create_fleet(self):
        '''创建外星人群'''
        # 创建一个外星人并计算一行可容纳多少个
        # 外星人的间距为外星人的宽度

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        '''
        要创建外星人群，需要计算屏幕可容纳多少行，并将创建一行外星人的循环重复执行相应的次数。为计算可容纳的行数，要先计算可用的垂直空间：用屏幕高度减去第一行外星人的上边距（外星人高度）、
        飞船的高度以及外星人群最初与飞船之间的距离（外星人高度的两倍）：
        '''
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        numbers_rows = available_space_y // (2 * alien_height)

        # 创建一行外星人
        for row_number in range(numbers_rows):
            for alien_number in range(number_aliens_x):
                '''
                修改外星人的[插图]坐标（见❹）并在第一行外星人上方留出与外星人等高的空白区域。相邻外星人行的[插图]坐标相差外星人高度的两倍，因此将外星人高度乘以2，再乘以行号。
                第一行的行号为0，因此第一行的垂直位置不变，而其他行都沿屏幕依次向下放置。
                '''
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        '''创建一个外星人并将其放在当前行'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        '''
        并通过设置[插图]坐标将其加入当前行（见❺）。将每个外星人都往右推一个外星人宽度。接下来，将外星人宽度乘以2，得到每个外星人占据的空间（其中包括右边的空白区域），再据此计算当前外星人在当前行的位置。我们使用外星人的属性x来设置其rect的位置。
        最后，将每个新创建的外星人都添加到编组aliens中。
        '''
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_bullets(self):
        self.bullets.update()
        # 子弹消失
        '''
        Python要求该列表的长度在整个循环中保持不变。因为不能从for循环遍历的列表或编组中删除元素，
        所以必须遍历编组的副本
        '''
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _check_events(self):
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # 向右移动飞船
        if event.key == pygame.K_RIGHT:
            # 向右移动
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''创建一颗子弹，将其加入编组bullets中'''
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        # 更新屏幕上的图像，切换到新屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # 将图片绘制到屏幕上
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
