class Settings():
    '''Класс для хранения всех настроек игры Alien Invasion.'''

    def __init__(self):
        '''Инициализирует статистические настройки игры.'''
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Скорость корабля
        self.ship_speed_factor = 1.3
        self.hurts_limit = 3

        # Параметры пули
        self.bullet_speed_factor = 1.7
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев.
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        
        # Темп ускорения игры
        self.speedup_scale = 1.1
        
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        # Динамичные настройки, изменяющиеся в ходе игры.
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Инициализирует настройки, изменяющиеся в ходе игры.'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # Подсчёт очков
        self.alien_points = 50
        
        # fleet_direction = 1 обозначает движение в право, -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        '''Увеличивает настройки скорости и стоимость пришельцев.'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)





















        

        
        
