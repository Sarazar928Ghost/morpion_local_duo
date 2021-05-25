import pygame
from game import Game
import time

def start_running():
    running = True
    can_draw = True
    game = Game()
    game.draw_game()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and can_draw:
                pos = pygame.mouse.get_pos()
                success = game.draw_form(pos)
                if success : 
                    winner = game.check_win()
                    if winner != None: 
                        can_draw = False
                        now = int(time.time())
                    elif game.number_turn == 9:
                        game.reset()

        if not can_draw:
            game.draw_winner(winner)
            if int(time.time()) - now > 2:
                can_draw = True
                game.reset()

        pygame.display.update()

if __name__ == "__main__":
    start_running()
