import time
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from buttons import PlayButton, PauseButton
from ship import Ship
from alien import Alien
import game_functions as gf


class Game:

    def __init__(self):
        # Инициализирует pygame,settings и объект экрана
        pygame.init()
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((
                self.ai_settings.screen_width, 
                self.ai_settings.screen_height))
        pygame.display.set_caption('Space Invaders')

        # Создание кнопки Play
        self.play_button = PlayButton(
            self.ai_settings, self.screen, 'Play')
        self.pause_button = PauseButton(
            self.ai_settings, self.screen, '||')
        
        # Создание экземпляров GameStats и Scoreboard
        self.stats = GameStats(self.ai_settings)
        self.sb = Scoreboard(self.ai_settings, self.screen, self.stats)

        # Создание корабля, группы пуль и группы пришельцев
        self.ship = Ship(self.ai_settings, self.screen)
        self.bullets = Group()
        self.aliens = Group()

        # Создание флота пришельцев.
        gf.create_fleet(self.ai_settings, self.screen, self.ship, 
            self.aliens)
        
        # Назначение цвета фона
        self.bg_color = self.ai_settings.bg_color


    def run(self):
        # Запуск основного цикла игры.
        while True:
            # Отслеживание событий клавиатуры и мыши.
            gf.check_events(self.ai_settings, self.screen, self.stats, 
                self.sb, self.play_button, self.pause_button, 
                self.ship, self.aliens, self.bullets)
            # если игра активна и не на паузе, обнови все объекты
            if self.stats.game_active and self.stats.game_pause:
                self.ship.update()
                gf.update_bullets(self.ai_settings, self.screen, 
                    self.stats, self.sb, self.ship, self.aliens, 
                    self.bullets)
                gf.update_aliens(self.ai_settings, self.screen, 
                    self.stats, self.sb, self.ship, self.aliens, 
                    self.bullets)
                # При каждом проходе цикла перерисовывается экран
            gf.update_screen(self.ai_settings, self.screen, self.stats, 
                self.sb, self.ship, self.aliens, self.bullets, 
                self.play_button, self.pause_button)
            # задежржка, для ровного перемещения пришельцев
            # независимо от мощности компьютера
            time.sleep(0.005)


if __name__ == '__main__':
    Game().run()