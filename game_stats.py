class GameStats():
    '''Отслеживание статистики для игры Alien Invasion.'''

    def __init__(self, ai_settings):
        '''Инициализирует статистику.'''
        self.ai_settings = ai_settings
        self.reset_stats()
        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False
        # флаг для остановки игры
        self.game_pause = True
        # Рекорд не должен сбрасываться.
        self.high_score = 0

    def reset_stats(self):
        '''Инициализирует статистику, изменяющуюся в ходе игры.'''
        self.hurts_left = self.ai_settings.hurts_limit
        self.score = 0
        self.level = 1
