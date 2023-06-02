import pygame
from pygame.sprite import Sprite

class Hurt(Sprite):
    '''Класс для жизней у игрока.'''

    def __init__(self, ai_settings, screen):
        '''Инициализирует сердечко.'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения сердечка и создание прямоугольника.
        self.image = pygame.image.load('images/hurt.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Сердечко появляется у правого верхнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        

    
    
