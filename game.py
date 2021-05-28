import pygame
from pygame.sndarray import array
from player_card import Player_Card
from color import Color
from label import Label

class Game:

    def __init__(self, screen, width, height, name, current_loc):
        self.SIZE_CASE = 210
        self.WIDTH = width
        self.HEIGHT = height
        self.CARD_HEIGHT = 100
        self.screen = screen
        self.COLOR_RECT_GAME = Color.LIGHT_GRAY.value
        self.rect_game = pygame.Rect(0, self.CARD_HEIGHT, self.WIDTH, self.HEIGHT - self.CARD_HEIGHT * 2)
        pos_card_one = (0,0, self.WIDTH, self.CARD_HEIGHT)
        pos_card_two = (0, self.HEIGHT - self.CARD_HEIGHT, self.WIDTH, self.CARD_HEIGHT)
        self.player_one = Player_Card(name, f"{current_loc}/images/profil.png", pos_card_one, Color.RED, self.__draw_circle)
        self.player_two = Player_Card("Karim", f"{current_loc}/images/profil.png", pos_card_two, Color.BLUE, self.__draw_cross)
        self.player_one.my_turn = True
        self.grid = [[0,0,0], [0,0,0], [0,0,0]] # 0 = neutre , 1 = player one , 2 = player two
        self.number_turn = 0
        self.font_winner = pygame.font.SysFont(None, 25)
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def __draw_cross(self, color, pos, grid = True):
        if grid:
            pygame.draw.line(self.screen, color, (pos[0] * self.SIZE_CASE + 20, pos[1] * self.SIZE_CASE + self.CARD_HEIGHT + 20), (pos[0] * self.SIZE_CASE + self.SIZE_CASE - 20, pos[1] * self.SIZE_CASE + self.CARD_HEIGHT + 20 + self.SIZE_CASE - 40), width=10)
            pygame.draw.line(self.screen, color, (pos[0] * self.SIZE_CASE + 20, pos[1] * self.SIZE_CASE + self.CARD_HEIGHT + self.SIZE_CASE - 20), (pos[0] * self.SIZE_CASE + self.SIZE_CASE - 20, pos[1] * self.SIZE_CASE + self.CARD_HEIGHT + 20), width=10)
        # Draw form to the card player
        else:
            pygame.draw.line(self.screen, color, (pos[0] - 40, pos[1] + 20), (pos[0] + 20, pos[1] + 80), width=6)
            pygame.draw.line(self.screen, color, (pos[0] + 20, pos[1] + 20), (pos[0] - 40, pos[1] + 80), width=6)
        pygame.display.update()

    def __draw_circle(self, color, pos, grid = True):
        if grid:
            pygame.draw.circle(self.screen, color, (pos[0] * self.SIZE_CASE + 105, pos[1] * self.SIZE_CASE + 205), 90, width=5)
        # Draw form to the card player
        else:
            pygame.draw.circle(self.screen, color, (pos[0], pos[1] + 50), 30, width=3)
        pygame.display.update()

    def check_win(self):  
        result = self.__check_win()
        if result != 0:
            if result == 1 :
                self.player_one.score[0] += 1
                self.player_two.score[1] += 1
                return self.player_one
            elif result == 2 : 
                self.player_two.score[0] += 1
                self.player_one.score[1] += 1
                return self.player_two
        return None
        
    def draw_winner(self, winner: Player_Card):
        victory = Label("VICTOIRE !", self.screen, self.font_winner, Color.GREEN.value, (self.WIDTH / 2 - 64 + 70, self.HEIGHT / 2 - 65))
        name = Label(winner.name, self.screen, winner.font_name, winner.color_name, (self.WIDTH / 2 - 64 + 70, self.HEIGHT / 2 - 20))
        # + 100 width is for text of victory
        length_add = name.get_width() - 100
        if length_add < 0:
            length_add = 0
        length_add += 10 # 10 is for the padding right
        pygame.draw.rect(self.screen, Color.WHITE.value, pygame.Rect(self.WIDTH / 2 - 75, self.HEIGHT/2 - 70, 80 + 100 + length_add, 75))
        self.screen.blit(winner.image, (self.WIDTH / 2 - 64, self.HEIGHT / 2 - 64))
        victory.show_label()
        name.show_label()
        pygame.display.update()

    def draw_form(self, pos_mouse: array):
        if pos_mouse[1] <= self.CARD_HEIGHT or pos_mouse[1] >= self.HEIGHT - self.CARD_HEIGHT: return False
        pos_x = int((pos_mouse[0]) / self.SIZE_CASE)
        pos_y = int((pos_mouse[1] - self.CARD_HEIGHT) / self.SIZE_CASE)
        if self.grid[pos_x][pos_y] != 0: return False
        # Player one
        if self.player_one.my_turn:
            self.grid[pos_x][pos_y] = 1
            self.player_one.draw_form((pos_x, pos_y))
            self.player_one.my_turn = False
            self.player_two.my_turn = True
        # Player two
        elif self.player_two.my_turn:
            self.grid[pos_x][pos_y] = 2
            self.player_two.draw_form((pos_x, pos_y))
            self.player_two.my_turn = False
            self.player_one.my_turn = True
        self.player_one.draw_card(self.screen)
        self.player_two.draw_card(self.screen)
        self.number_turn += 1
        pygame.display.update()
        return True
        

    def reset(self):
        self.grid = [[0,0,0], [0,0,0], [0,0,0]]
        pygame.draw.rect(self.screen, self.COLOR_RECT_GAME, self.rect_game)
        self.__draw_grid()
        self.player_one.draw_card(self.screen)
        self.player_two.draw_card(self.screen)
        self.number_turn = 0
        pygame.display.update()

    def __check_win(self):
        grid = self.grid
        # 1 = player_one ; 2 = player_two
        for i in range(1,3):
            # CHECK LINE
            if grid[0][0] == i and grid[1][0] == i and grid[2][0] == i:
                return i
            if grid[0][1] == i and grid[1][1] == i and grid[2][1] == i:
                return i
            if grid[0][2] == i and grid[1][2] == i and grid[2][2] == i:
                return i
            # CHECK COLUMN
            if grid[0][0] == i and grid[0][1] == i and grid[0][2] == i:
                return i
            if grid[1][0] == i and grid[1][1] == i and grid[1][2] == i:
                return i
            if grid[2][0] == i and grid[2][1] == i and grid[2][2] == i:
                return i
            # CHECK DIAGONAL
            if grid[0][0] == i and grid[1][1] == i and grid[2][2] == i:
                return i
            if grid[0][2] == i and grid[1][1] == i and grid[2][0] == i:
                return i

        return 0 # no winner

    def draw_game(self):
        self.player_one.draw_card(self.screen)
        self.player_two.draw_card(self.screen)
        pygame.draw.rect(self.screen, self.COLOR_RECT_GAME, self.rect_game)
        self.__draw_grid()
        pygame.display.update()
    
    def __draw_grid(self):
        pygame.draw.line(self.screen, Color.BLACK.value, (0, self.SIZE_CASE + self.CARD_HEIGHT), (self.WIDTH, self.SIZE_CASE + self.CARD_HEIGHT), width=2)
        pygame.draw.line(self.screen, Color.BLACK.value, (0, self.SIZE_CASE * 2 + self.CARD_HEIGHT), (self.WIDTH, self.SIZE_CASE * 2 + self.CARD_HEIGHT), width=2)
        pygame.draw.line(self.screen, Color.BLACK.value, (self.SIZE_CASE, self.CARD_HEIGHT), (self.SIZE_CASE, self.HEIGHT - self.CARD_HEIGHT), width=2)
        pygame.draw.line(self.screen, Color.BLACK.value, (self.SIZE_CASE * 2, self.CARD_HEIGHT), (self.SIZE_CASE * 2, self.HEIGHT - self.CARD_HEIGHT), width=2)