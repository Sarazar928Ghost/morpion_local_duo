import pygame
from color import Color

class Menu:

    def __init__(self, image_path):
        self.WIDTH = 626
        self.HEIGHT = 626
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.image = pygame.image.load(image_path)
        self.input_rect = pygame.Rect(50,50,self.WIDTH - 100,80)
        self.button_rect = pygame.Rect(200,self.HEIGHT - 150, self.WIDTH - 400, 100)
        self.color_rect_inactive = Color.WHITE.value
        self.color_rect_active = Color.LIGHT_BLUE.value
        self.font_name = pygame.font.SysFont(None, 50)
        self.font_button = pygame.font.SysFont(None, 75)

    def draw_menu(self):
        self.screen.blit(self.image, (0,0))
        self.__draw_rect(self.color_rect_inactive)

    def __draw_rect(self, color):
        pygame.draw.rect(self.screen, color, self.input_rect)
        pygame.display.update()

    def __draw_button_play(self, color, text):
        pygame.draw.rect(self.screen, color, self.button_rect, border_radius=10)
        length_width = text.get_width()
        length_height = text.get_height()
        self.screen.blit(text, (self.WIDTH / 2 - length_width / 2, self.HEIGHT - 150 + length_height / 2))
        pygame.display.update()

    def __draw_name(self, name, color):
        message = self.font_name.render(name, True, color)
        length = message.get_width()
        self.screen.blit(message, (self.WIDTH / 2 - length / 2,75))
        pygame.display.update()

    def listen(self, clock):
        done = False
        active = True
        color_rect = self.color_rect_active
        color_name = Color.BLACK.value
        name = ""
        while not done:
            pos_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return (False, None)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_rect.collidepoint(pos_mouse[0], pos_mouse[1]):
                        active = True
                        color_rect = self.color_rect_active
                    elif self.button_rect.collidepoint(pos_mouse[0], pos_mouse[1]) :
                        if len(name.strip().replace(" ", "")) > 3:
                            done = True
                    else:
                        active = False
                        color_rect = self.color_rect_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_BACKSPACE:
                            name = name[:-1]
                        else:
                            if len(name) != 16 and event.key != pygame.K_TAB and event.key != pygame.K_RETURN and event.key != 1073741912:
                                name += event.unicode
                        color_rect = self.color_rect_active
                    else:
                        color_rect = self.color_rect_inactive
                if self.button_rect.collidepoint(pos_mouse[0], pos_mouse[1]) or self.input_rect.collidepoint(pos_mouse[0], pos_mouse[1]):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)

                self.__draw_rect(color_rect)
                self.__draw_name(name, color_name)
                self.__draw_button_play(Color.PURPLE.value, self.font_button.render("PLAY", True, Color.DARK_PURPLE.value))
                    
            clock.tick(30)
        return (True, name)


