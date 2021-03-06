import pygame
from color import Color
from label import Label

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
        label_button = Label("PLAY", self.screen, self.font_button, Color.DARK_PURPLE.value)
        length_width, length_height = label_button.get_size()
        label_button.set_pos((self.WIDTH / 2 - length_width / 2, self.HEIGHT - 150 + length_height / 2))
        self.__draw_button_play(Color.PURPLE.value, label_button)

    def __draw_rect(self, color):
        pygame.draw.rect(self.screen, color, self.input_rect)
        

    def __draw_button_play(self, color, label_button):
        pygame.draw.rect(self.screen, color, self.button_rect, border_radius=10)
        label_button.show_label()
        

    def __draw_name(self, name, color):
        message = Label(name, self.screen, self.font_name, color)
        length = message.get_width()
        message.set_pos((self.WIDTH / 2 - length / 2,75))
        message.show_label()
        

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
                        if len(name.strip().replace(" ", "")) > 2:
                            done = True
                    else:
                        active = False
                        color_rect = self.color_rect_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_BACKSPACE:
                            name = name[:-1]
                        else:
                            if event.key == pygame.K_RETURN or event.key == 1073741912:
                                if len(name.strip().replace(" ", "")) > 2:
                                    done = True
                            elif len(name) != 16 and event.key != pygame.K_TAB and event.unicode.encode('utf-8') != b'\x16':
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
            pygame.display.update()
            clock.tick(30)
        return (True, name)


