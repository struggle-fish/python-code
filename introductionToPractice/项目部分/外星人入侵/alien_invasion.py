import sys

import pygame

from settings import Settings


class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.settins = Settings()
        # 窗口大小
        self.screen = pygame.display.set_mode((self.settins.screen_width, self.settins.screen_height))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        '''开始游戏主循环'''
        while True:
            # 监听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 让最近绘制的屏幕可见
            self.screen.fill(self.settins.bg_color)

            pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
