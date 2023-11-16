import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

from game_stats import GameStats

from button import Button
from scoreboard import Scoreboard


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

        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)
        # 创建记分牌
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # 创建play 按钮
        self.play_button = Button(self, 'Play')

    def run_game(self):
        '''开始游戏主循环'''
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
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
        available_space_y = (self.settings.screen_height - (2 * alien_height) - ship_height)
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
        '''更新子弹的位置，并删除消失的子弹'''
        '''
        Python要求该列表的长度在整个循环中保持不变。因为不能从for循环遍历的列表或编组中删除元素，
        所以必须遍历编组的副本
        '''
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        '''检查是否有子弹击中了外星人'''
        ''''如果有，删除相应的子弹和外星人'''
        '''
        这些新增的代码将self.bullets中所有的子弹都与self.aliens中所有的外星人进行比较，看它们是否重叠在一起。每当有子弹和外星人的rect重叠时，groupcollide()就在它返回的字典中添加一个键值对。两个实参True让Pygame删除发生碰撞的子弹和外星人。（要模拟能够飞行到屏幕顶端、消灭击中的每个外星人的高能子弹，可将第一个布尔实参设置为False，并保留第二个布尔参数为True。
        这样被击中的外星人将消失，但所有的子弹都始终有效，直到抵达屏幕顶端后消失。）
        '''
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            '''
            如果字典collisions存在，就遍历其中的所有值。别忘了，每个值都是一个列表，包含被同一颗子弹击中的所有外星人。对于每个列表，都将其包含的外星人数量乘以一个外星人的分数，并将结果加入当前得分。为测试这一点，
            请将子弹宽度改为300像素，并核实得到了其击中的每个外星人的分数，再将子弹宽度恢复正常值。
            '''
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        '''
        
        检查编组aliens是否为空。空编组相当于False，因此这是一种检查编组是否为空的简单方式。如果编组aliens为空
        Flase 取反 not 
        '''
        if not self.aliens:
            '''删除所有子弹 并创建新的外星人'''
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # 提高等级
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        '''更新外星人群中所有外星人的位置'''
        self._check_fleet_edges()
        self.aliens.update()

        '''
        检测外星人和飞船碰撞
        函数spritecollideany()接受两个实参：一个精灵和一个编组。它检查编组是否有成员与精灵发生了碰撞，并在找到与精灵发生碰撞的成员后停止遍历编组。
        在这里，它遍历编组aliens，并返回找到的第一个与飞船发生碰撞的外星人。
        '''
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            '''
            有外星人撞到飞船时，需要执行很多任务：
            删除余下的外星人和子弹，
            让飞船重新居中，
            以及创建一群新的外星人。
            '''
            self._ship_hit()
            print('ship hit!!')

        # 检查是否有外星人到达了屏幕底部
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        '''检查是否有外星人到达了屏幕底部'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理
                self._ship_hit()
                break

    def _ship_hit(self):
        '''响应飞船被外星人撞到'''
        if self.stats.ships_left > 0:
            # 将ships_left 减1 并更新记分牌
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人，并将飞船放到屏幕底部中央
            self._create_fleet()
            self.ship.center_ship()

            # 暂停一会儿
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_fleet_edges(self):
        '''有外星人到达边缘采取相应措施'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''将整群外星人下移，并改变他们的方向'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _check_events(self):
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        '''在玩家点击play时候开始游戏'''
        '''
        仅当玩家单击了Play按钮且游戏当前处于非活动状态时，游戏才重新开始
        '''
        if button_clicked and not self.stats.game_active:
            # 重置游戏设置
            self.settings.initialize_dynamic_settings()
            # 重置统计信息
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人并让飞船居中
            self._create_fleet()
            self.ship.center_ship()
            # 隐藏鼠标
            pygame.mouse.set_visible(False)

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
        # 显示得分
        self.sb.show_score()
        # 如果游戏处于非活动状态，就绘制开始按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
