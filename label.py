import pygame

class Label:
    def __init__(self, text, screen, font, color, pos = [], antialias = True):
        self.pos = pos
        self.screen = screen
        self.font = font
        self.color = color
        self.antialias = antialias
        self.set_text(text)

    def set_pos(self, pos):
        self.pos = pos

    def set_text(self, text):
        self.text = text
        self.label = self.label_init()

    def show_label(self):
        self.screen.blit(self.label, self.pos)

    def label_init(self):
        return self.font.render(self.text, self.antialias, self.color)

    def get_size(self):
        return self.get_width(), self.get_height()

    def get_width(self):
        return self.label.get_width()

    def get_height(self):
        return self.label.get_height()

class LabelOpacity(Label):
    def __init__(self, text, screen, font, color, pos = [], antialias = True):
        super().__init__(text, screen, font, color, pos, antialias)
        self.opacity = 250
        self.__up_opacity = False
        self.alpha_img = pygame.Surface(self.label.get_size(), pygame.SRCALPHA)
        self.__update_alpha_img()

    def __update_alpha_img(self):
        self.label = self.label_init()
        self.alpha_img.fill((255, 255, 255, self.opacity))
        self.label.blit(self.alpha_img, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def update_opacity(self):
        self.opacity += 10 if self.__up_opacity else -10
        if self.opacity == 0: self.__up_opacity = True
        elif self.opacity == 250: self.__up_opacity = False

        self.__update_alpha_img()


