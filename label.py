import pygame

class Label:
    def __init__(self, text, screen, font, color, pos = [], antialias = True):
        self.pos = pos
        self.text = text
        self.screen = screen
        self.font = font
        self.color = color
        self.antialias = antialias
        self.label = self.__label_init()

    def set_pos(self, pos):
        self.pos = pos

    def __label_init(self):
        return self.font.render(self.text, self.antialias, self.color)

    def show_label(self):
        self.screen.blit(self.label, self.pos)

    def get_width(self):
        return self.label.get_width()

    def get_height(self):
        return self.label.get_height()

class LabelOpacity(Label):
    pass