'''
有外星人撞到飞船时，将余下的飞船数减1，
创建一群新的外星人，并将飞船重新放到屏幕底端的中央。
另外，让游戏暂停片刻，让玩家在新外星人群出现前注意到发生了碰撞并将重新创建外星人群。

'''


class GameStats:
    '''跟踪游戏的统计信息'''

    def __init__(self, ai_game):
        '''初始化统计信息'''
        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = False

    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ships_left = self.settings.ship_limit
