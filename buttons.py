import pygame.font

class PlayButton():

    def __init__(self, ai_settings, screen, msg):
        '''Инициализирует атрибуты кнопки.'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Назаничение размеров и свойств кнопок.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки создаётся только один раз.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''Преобразет msg в прямоугольник и выравнивает текст по центру.
        '''
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''Отображение пустой кнопки и вывод сообщения.'''
        # Рисует прямоугольную часть кнопки
        self.screen.fill(self.button_color, self.rect)
        # Выводит изображение текста на экран с передачей изображения
        # и объекта rect, связанного с изображением.
        self.screen.blit(self.msg_image, self.msg_image_rect)


class PauseButton():

    def __init__(self, ai_settings, screen, msg):
        '''Инициализирует атрибуты кнопки.'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Назаничение размеров и свойств кнопок.
        self.width, self.height = 50, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (25, 75)

        # Сообщение кнопки создаётся только один раз.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''Преобразет msg в прямоугольник и выравнивает текст по центру.
        '''
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''Отображение пустой кнопки и вывод сообщения.'''
        # Рисует прямоугольную часть кнопки
        self.screen.fill(self.button_color, self.rect)
        # Выводит изображение текста на экран с передачей изображения
        # и объекта rect, связанного с изображением.
        self.screen.blit(self.msg_image, self.msg_image_rect)
