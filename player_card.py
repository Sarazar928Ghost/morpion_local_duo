import pygame
from color import Color
from label import Label
from label import LabelOpacity

class Player_Card:
    def __init__(self, name, image, pos, color_name, function_draw, screen, color_card = Color.WHITE):
        self.name = name
        self.image = pygame.image.load(image)
        self.color_card = color_card.value
        self.pos = pos
        self.color_name = color_name.value # example (255,0,0)
        self.function_draw = function_draw
        self.score = [0,0]
        self.screen = screen
        self.font_text = pygame.font.SysFont(None, 20)
        self.font_name = pygame.font.SysFont(None, 24)
        self.my_turn = False

        # Card init
        self.rect_card = pygame.Rect(self.pos[0], self.pos[1], self.pos[2], self.pos[3])
        self.name_card = Label(self.name, self.screen, self.font_name, self.color_name, (self.pos[0] + 95, self.pos[1] + 70))
        self.victory = Label(f"V: {self.score[0]}", self.screen, self.font_text, Color.GREEN.value, (self.pos[0] + 95, self.pos[1] + 25))
        self.defeate = Label(f"D: {self.score[1]}", self.screen, self.font_text, Color.RED.value, (self.pos[0] + 95, self.pos[1] + 45))

        # Turn message init
        self.message_turn = LabelOpacity("Your Turn !", screen, self.font_name, Color.GREEN.value)
        self.message_turn_width, self.message_turn_height = self.message_turn.get_size()
        self.pos_x_turn_message = self.pos[0] + self.pos[2] / 2 - self.message_turn_width / 2
        self.pos_y_turn_message = self.pos[1] - self.message_turn_height / 2 + self.pos[3] / 2
        self.message_turn.set_pos((self.pos_x_turn_message, self.pos_y_turn_message))
        self.rect_blank = pygame.Rect(*self.message_turn.pos, self.message_turn_width, self.message_turn_height)

    def draw_card(self):
        pygame.draw.rect(self.screen, self.color_card, self.rect_card)
        self.screen.blit(self.image, (self.pos[0] + 25, self.pos[1] + 20))
        self.name_card.show_label()
        self.__draw_score()
        self.draw_form((self.pos[2] - 50, self.pos[1]), False)
        if self.my_turn:
            self.draw_message_turn()

    def draw_message_turn(self):
        pygame.draw.rect(self.screen, self.color_card, self.rect_blank)
        self.message_turn.show_label()

    def __draw_score(self):
        self.victory.set_text(f"V: {self.score[0]}")
        self.defeate.set_text(f"D: {self.score[1]}")
        self.victory.show_label()
        self.defeate.show_label()

    def draw_form(self, pos, grid = True):
        self.function_draw(self.color_name, pos, grid)
        
