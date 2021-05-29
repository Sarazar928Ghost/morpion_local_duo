from player_card import Player_Card
from label import Label
from color import Color
import pygame

class Winner_Card:

    def __init__(self, screen, player: Player_Card, width, height):
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.player = player
        self.victory = Label("VICTOIRE !", self.screen, pygame.font.SysFont(None, 25), Color.GREEN.value)
        self.blit_profil_image = self.__init_box()

    def __init_box(self):
        padding = {
            "top": 6,
            "bottom": 6,
            "right": 12,
            "left": 10
        }
        self.label_name_player = Label(self.player.name, self.screen, self.player.font_name, self.player.color_name)
        length_add = self.label_name_player.get_width() - self.victory.get_width()
        if length_add < 0 : length_add = 0
        player_width_image = self.player.image.get_width()
        player_height_image = self.player.image.get_height()

        middle_width = self.WIDTH / 2
        middle_height = self.HEIGHT / 2
        height_message_player = player_height_image + 12
        width_message_player = padding["right"] + padding["left"] + player_width_image + self.victory.get_width() + length_add

        pos_x = middle_width - width_message_player / 2
        pos_y = middle_height - height_message_player / 2
        self.rect = pygame.Rect(pos_x, pos_y, width_message_player, height_message_player)

        self.victory.set_pos((pos_x + 15 + player_width_image, pos_y + padding["top"]))
        self.label_name_player.set_pos((pos_x + 15 + player_width_image, pos_y + height_message_player - padding["bottom"] - self.label_name_player.get_height()))
        
        return self.player.image, (pos_x + padding["left"], pos_y + padding["top"])


    def draw_winner(self):
        pygame.draw.rect(self.screen, Color.WHITE.value, self.rect)
        self.screen.blit(*self.blit_profil_image)
        self.victory.show_label()
        self.label_name_player.show_label()