import pygame
from player_card import Player_Card
from color import Color

class Game:

    def __init__(self):
        pygame.init()
        self.current_loc = "c:/Users/Kévin/Desktop/python test/morpion/client"
        pygame.display.set_caption("MorpionKev")
        pygame.display.set_icon(pygame.image.load(f"{self.current_loc}/images/morpion.png"))
        self.SIZE_CASE = 210
        self.WIDTH = 630
        self.HEIGHT = 830
        self.CARD_HEIGHT = 100
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.COLOR_RECT_GAME = Color.LIGHT_GRAY.value
        self.rect_game = pygame.Rect(0, self.CARD_HEIGHT, self.WIDTH, self.HEIGHT - self.CARD_HEIGHT * 2)
        pos_card_one = (0,0, self.WIDTH, self.CARD_HEIGHT)
        pos_card_two = (0, self.HEIGHT - self.CARD_HEIGHT, self.WIDTH, self.CARD_HEIGHT)
        self.player_one = Player_Card("Kevin", f"{self.current_loc}/images/profil.png", pos_card_one, Color.PURPLE_KEVIN, self.__draw_circle)
        self.player_two = Player_Card("Maman", f"{self.current_loc}/images/profil.png", pos_card_two, Color.GREEN_MAMAN, self.__draw_cross)
        self.turn = True # True == Player One
        self.grid = [[0,0,0], [0,0,0], [0,0,0]] # 0 = neutre , 1 = player one , 2 = player two
        self.number_turn = 0
        self.font_winner = pygame.font.SysFont(None, 25)

    def __draw_cross(self, color, pos):
        pygame.draw.line(self.screen, color, (pos[0] * self.SIZE_CASE + 20, pos[1] * self.SIZE_CASE + self.CARD_HEIGHT + 20), (pos[0] * self.SIZE_CASE + self.SIZE_CASE - 20, pos[1] * self.SIZE_CASE + self.CARD_HEIGHT + 20 + self.SIZE_CASE - 40), width=10)
        pygame.draw.line(self.screen, color, (pos[0] * self.SIZE_CASE + 20, pos[1] * self.SIZE_CASE + self.CARD_HEIGHT + self.SIZE_CASE - 20), (pos[0] * self.SIZE_CASE + self.SIZE_CASE - 20, pos[1] * self.SIZE_CASE + self.CARD_HEIGHT + 20), width=10)

    def __draw_circle(self, color, pos):
        pygame.draw.circle(self.screen, color, (pos[0] * self.SIZE_CASE + 105, pos[1] * self.SIZE_CASE + 205), 90, width=5)

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
        victory = self.font_winner.render(f"VICTOIRE !", True, Color.GREEN.value)
        name = winner.font_name.render(winner.name, True, winner.color_name)
        self.screen.blit(winner.image, (self.WIDTH / 2 - 64, self.HEIGHT / 2 - 64))
        self.screen.blit(victory, (self.WIDTH / 2 - 64 + 70, self.HEIGHT / 2 - 60))
        self.screen.blit(name, (self.WIDTH / 2 - 64 + 70, self.HEIGHT / 2 - 20))

    def draw_form(self, pos_mouse):
        if pos_mouse[1] <= self.CARD_HEIGHT or pos_mouse[1] >= self.HEIGHT - self.CARD_HEIGHT: return False
        pos_x = int((pos_mouse[0]) / self.SIZE_CASE)
        pos_y = int((pos_mouse[1] - self.CARD_HEIGHT) / self.SIZE_CASE)
        if self.grid[pos_x][pos_y] != 0: return False
        # Player one
        if self.turn:
            self.grid[pos_x][pos_y] = 1
            self.player_one.draw_form((pos_x, pos_y))
        # Player two
        elif not self.turn:
            self.grid[pos_x][pos_y] = 2
            self.player_two.draw_form((pos_x, pos_y))
        self.turn = not self.turn
        self.number_turn += 1
        
        return True
        

    def reset(self):
        self.grid = [[0,0,0], [0,0,0], [0,0,0]]
        pygame.draw.rect(self.screen, self.COLOR_RECT_GAME, self.rect_game)
        self.__draw_grid()
        self.player_one.draw_card(self.screen)
        self.player_two.draw_card(self.screen)
        self.number_turn = 0

    def __check_win(self):
        grid = self.grid

        # Player One Line
        if grid[0][0] == 1 and grid[1][0] == 1 and grid[2][0] == 1:
            return 1
        if grid[0][1] == 1 and grid[1][1] == 1 and grid[2][1] == 1:
            return 1
        if grid[0][2] == 1 and grid[1][2] == 1 and grid[2][2] == 1:
            return 1

        # Player Two Line
        if grid[0][0] == 2 and grid[1][0] == 2 and grid[2][0] == 2:
            return 2
        if grid[0][1] == 2 and grid[1][1] == 2 and grid[2][1] == 2:
            return 2
        if grid[0][2] == 2 and grid[1][2] == 2 and grid[2][2] == 2:
            return 2

        # Player One Colonum
        if grid[0][0] == 1 and grid[0][1] == 1 and grid[0][2] == 1:
            return 1
        if grid[1][0] == 1 and grid[1][1] == 1 and grid[1][2] == 1:
            return 1
        if grid[2][0] == 1 and grid[2][1] == 1 and grid[2][2] == 1:
            return 1

        # Player Two Colonum
        if grid[0][0] == 2 and grid[0][1] == 2 and grid[0][2] == 2:
            return 2
        if grid[1][0] == 2 and grid[1][1] == 2 and grid[1][2] == 2:
            return 2
        if grid[2][0] == 2 and grid[2][1] == 2 and grid[2][2] == 2:
            return 2

        # Player One Diagonal
        if grid[0][0] == 1 and grid[1][1] == 1 and grid[2][2] == 1:
            return 1
        if grid[0][2] == 1 and grid[1][1] == 1 and grid[2][0] == 1:
            return 1

        # Player Two Diagonal
        if grid[0][0] == 2 and grid[1][1] == 2 and grid[2][2] == 2:
            return 2
        if grid[0][2] == 2 and grid[1][1] == 2 and grid[2][0] == 2:
            return 2

        return 0

    def draw_game(self):
        self.player_one.draw_card(self.screen)
        self.player_two.draw_card(self.screen)
        pygame.draw.rect(self.screen, self.COLOR_RECT_GAME, self.rect_game)
        self.__draw_grid()
    
    def __draw_grid(self):
        pygame.draw.line(self.screen, Color.BLACK.value, (0, self.SIZE_CASE + self.CARD_HEIGHT), (self.WIDTH, self.SIZE_CASE + self.CARD_HEIGHT), width=1)
        pygame.draw.line(self.screen, Color.BLACK.value, (0, self.SIZE_CASE * 2 + self.CARD_HEIGHT), (self.WIDTH, self.SIZE_CASE * 2 + self.CARD_HEIGHT), width=1)
        pygame.draw.line(self.screen, Color.BLACK.value, (self.SIZE_CASE, self.CARD_HEIGHT), (self.SIZE_CASE, self.HEIGHT - self.CARD_HEIGHT), width=1)
        pygame.draw.line(self.screen, Color.BLACK.value, (self.SIZE_CASE * 2, self.CARD_HEIGHT), (self.SIZE_CASE * 2, self.HEIGHT - self.CARD_HEIGHT), width=1)