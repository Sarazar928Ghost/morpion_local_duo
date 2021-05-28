import pygame
from color import Color
from label import Label

class Player_Card:
    def __init__(self, name, image, pos, color_name, function_draw, color_card = Color.WHITE):
        self.name = name
        self.image = pygame.image.load(image)
        self.color_card = color_card.value
        self.pos = pos
        self.color_name = color_name.value # example (255,0,0)
        self.function_draw = function_draw
        self.score = [0,0]
        self.font_text = pygame.font.SysFont(None, 20)
        self.font_name = pygame.font.SysFont(None, 24)
        self.my_turn = False

    def draw_card(self, screen):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.pos[2], self.pos[3])
        pygame.draw.rect(screen, self.color_card, rect)
        screen.blit(self.image, (self.pos[0] + 25, self.pos[1] + 20))
        name = Label(self.name, screen, self.font_name, self.color_name, (self.pos[0] + 95, self.pos[1] + 70))
        name.show_label()
        self.__draw_score(screen)
        self.draw_form((self.pos[2] - 50, self.pos[1]), False)
        if self.my_turn:
            self.__draw_message_turn(screen)

    def __draw_message_turn(self, screen):
        message_turn = Label("Your Turn !", screen, self.font_name, Color.GREEN.value)
        message_turn_width = message_turn.get_width()
        message_turn_height = message_turn.get_height()
        pos_x = self.pos[0] + self.pos[2] / 2 - message_turn_width / 2
        pos_y = self.pos[1] - message_turn_height / 2 + self.pos[3] / 2
        message_turn.set_pos((pos_x, pos_y))
        message_turn.show_label()

    def __draw_score(self, screen):
        victory = Label(f"V: {self.score[0]}", screen, self.font_text, Color.GREEN.value, (self.pos[0] + 95, self.pos[1] + 25))
        defeate = Label(f"D: {self.score[1]}", screen, self.font_text, Color.RED.value, (self.pos[0] + 95, self.pos[1] + 45))
        victory.show_label()
        defeate.show_label()

    def draw_form(self, pos, grid = True):
        self.function_draw(self.color_name, pos, grid)
        
