import pygame
from pygame.sndarray import array
from player_card import Player_Card
from color import Color
from label import Label
from winner_card import Winner_Card

class Game:

    def __init__(self, screen, width, height, name, current_loc):

        # Init Game
        self.SIZE_CASE = 210
        self.WIDTH = width
        self.HEIGHT = height
        self.CARD_HEIGHT = 100
        self.screen = screen
        self.number_turn = 0
        self.grid = [[0,0,0], [0,0,0], [0,0,0]] # 0 = neutre , 1 = player one , 2 = player two

        # Init Game gui
        self.COLOR_RECT_GAME = Color.LIGHT_GRAY.value
        self.rect_game = pygame.Rect(0, self.CARD_HEIGHT, self.WIDTH, self.HEIGHT - self.CARD_HEIGHT * 2)

        # Init Cards Players
        pos_card_one = (0,0, self.WIDTH, self.CARD_HEIGHT)
        pos_card_two = (0, self.HEIGHT - self.CARD_HEIGHT, self.WIDTH, self.CARD_HEIGHT)
        self.player_one = Player_Card(name, f"{current_loc}/images/profil.png", pos_card_one, Color.RED, self.__draw_circle, screen)
        self.player_two = Player_Card("Karim", f"{current_loc}/images/profil.png", pos_card_two, Color.BLUE, self.__draw_cross, screen)
        self.winner_card_one = Winner_Card(screen, self.player_one, width, height)
        self.winner_card_two = Winner_Card(screen, self.player_two, width, height)
        self.player_one.my_turn = True


        pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def __draw_cross(self, color, pos, grid = True):
        if grid:
            pygame.draw.line(self.screen, color, (pos[0] * self.SIZE_CASE + 20, pos[1] * self.SIZE_CASE + self.CARD_HEIGHT + 20), (pos[0] * self.SIZE_CASE + self.SIZE_CASE - 20, pos[1] * self.SIZE_CASE + self.CARD_HEIGHT + 20 + self.SIZE_CASE - 40), width=10)
            pygame.draw.line(self.screen, color, (pos[0] * self.SIZE_CASE + 20, pos[1] * self.SIZE_CASE + self.CARD_HEIGHT + self.SIZE_CASE - 20), (pos[0] * self.SIZE_CASE + self.SIZE_CASE - 20, pos[1] * self.SIZE_CASE + self.CARD_HEIGHT + 20), width=10)
        # Draw form to the card player
        else:
            pygame.draw.line(self.screen, color, (pos[0] - 40, pos[1] + 20), (pos[0] + 20, pos[1] + 80), width=6)
            pygame.draw.line(self.screen, color, (pos[0] + 20, pos[1] + 20), (pos[0] - 40, pos[1] + 80), width=6)
        

    def __draw_circle(self, color, pos, grid = True):
        if grid:
            pygame.draw.circle(self.screen, color, (pos[0] * self.SIZE_CASE + 105, pos[1] * self.SIZE_CASE + 205), 90, width=5)
        # Draw form to the card player
        else:
            pygame.draw.circle(self.screen, color, (pos[0], pos[1] + 50), 30, width=3)
        

    def update_opacity_message_turn(self):
        if self.player_one.my_turn:
            self.player_one.message_turn.update_opacity()
            self.player_one.draw_message_turn()
        elif self.player_two.my_turn:
            self.player_two.message_turn.update_opacity()
            self.player_two.draw_message_turn()
        

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
        if winner.name == self.player_one.name:
            self.winner_card_one.draw_winner()
        else:
            self.winner_card_two.draw_winner()
        

    def draw_form(self, pos_mouse: array):
        if pos_mouse[1] <= self.CARD_HEIGHT or pos_mouse[1] >= self.HEIGHT - self.CARD_HEIGHT: return False
        pos_x = int((pos_mouse[0]) / self.SIZE_CASE)
        pos_y = int((pos_mouse[1] - self.CARD_HEIGHT) / self.SIZE_CASE)
        if self.grid[pos_x][pos_y] != 0: return False
        # Player one
        if self.player_one.my_turn:
            self.grid[pos_x][pos_y] = 1
            self.player_one.draw_form((pos_x, pos_y))
        # Player two
        elif self.player_two.my_turn:
            self.grid[pos_x][pos_y] = 2
            self.player_two.draw_form((pos_x, pos_y))
        self.player_one.my_turn = not self.player_one.my_turn
        self.player_two.my_turn = not self.player_two.my_turn
        self.draws_cards_players()
        self.number_turn += 1
        
        return True
        

    def reset(self):
        self.grid = [[0,0,0], [0,0,0], [0,0,0]]
        pygame.draw.rect(self.screen, self.COLOR_RECT_GAME, self.rect_game)
        self.__draw_grid()
        self.draws_cards_players()
        self.number_turn = 0
        

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

    def draws_cards_players(self):
        self.player_one.draw_card()
        self.player_two.draw_card()

    def draw_game(self):
        self.draws_cards_players()
        pygame.draw.rect(self.screen, self.COLOR_RECT_GAME, self.rect_game)
        self.__draw_grid()
        
    
    def __draw_grid(self):
        pygame.draw.line(self.screen, Color.BLACK.value, (0, self.SIZE_CASE + self.CARD_HEIGHT), (self.WIDTH, self.SIZE_CASE + self.CARD_HEIGHT), width=2)
        pygame.draw.line(self.screen, Color.BLACK.value, (0, self.SIZE_CASE * 2 + self.CARD_HEIGHT), (self.WIDTH, self.SIZE_CASE * 2 + self.CARD_HEIGHT), width=2)
        pygame.draw.line(self.screen, Color.BLACK.value, (self.SIZE_CASE, self.CARD_HEIGHT), (self.SIZE_CASE, self.HEIGHT - self.CARD_HEIGHT), width=2)
        pygame.draw.line(self.screen, Color.BLACK.value, (self.SIZE_CASE * 2, self.CARD_HEIGHT), (self.SIZE_CASE * 2, self.HEIGHT - self.CARD_HEIGHT), width=2)