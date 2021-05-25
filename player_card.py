import pygame
from color import Color

class Player_Card:
    def __init__(self, name, image, pos, color_name, function_draw, color_card = Color.WHITE.value):
        self.name = name
        self.image = pygame.image.load(image)
        self.color_card = color_card
        self.pos = pos
        self.color_name = color_name.value # example (255,0,0)
        self.function_draw = function_draw
        self.score = [0,0]
        self.font_text = pygame.font.SysFont(None, 20)
        self.font_name = pygame.font.SysFont(None, 24)

    def draw_card(self, screen):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.pos[2], self.pos[3])
        pygame.draw.rect(screen, self.color_card, rect)
        screen.blit(self.image, (self.pos[0] + 25, self.pos[1] + 20))
        name = self.font_name.render(self.name, True, self.color_name)
        screen.blit(name, (self.pos[0] + 95, self.pos[1] + 70))
        self.__draw_score(screen)

    def __draw_score(self, screen):
        victory = self.font_text.render(f"V: {self.score[0]}", True, Color.GREEN.value)
        defeate = self.font_text.render(f"D: {self.score[1]}", True, Color.RED.value)
        screen.blit(victory, (self.pos[0] + 95, self.pos[1] + 25))
        screen.blit(defeate, (self.pos[0] + 95, self.pos[1] + 45))

    def draw_form(self, pos):
        self.function_draw(self.color_name, pos)
        
