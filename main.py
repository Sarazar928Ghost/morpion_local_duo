import pygame
from game import Game
from os import path
import time
from menu import Menu

WIDTH_GAME = 630
HEIGHT_GAME = 830

def start_running():
    current_loc = path.abspath("")
    pygame.init()
    pygame.display.set_caption("MorpionKev")
    pygame.display.set_icon(pygame.image.load(f"{current_loc}/images/morpion.png"))
    clock = pygame.time.Clock()
    menu = Menu(current_loc + "/images/menu.jpg")
    menu.draw_menu()
    menu_done = menu.listen(clock)
    running, name_player = menu_done
    if running:
        screen = pygame.display.set_mode((WIDTH_GAME, HEIGHT_GAME))
        game = Game(screen, WIDTH_GAME, HEIGHT_GAME, name_player, current_loc)
        game.draw_game()
        can_draw = True
        winner_drawed = False
    
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and can_draw:
                pos_mouse = pygame.mouse.get_pos()
                success = game.draw_form(pos_mouse)
                if success : 
                    winner = game.check_win()
                    if winner != None:
                        can_draw = False
                        now = int(time.time())
                    elif game.number_turn == 9:
                        game.reset()

        if not can_draw:
            if not winner_drawed:
                game.draw_winner(winner)
                winner_drawed = True
            if int(time.time()) - now > 3:
                can_draw = True
                winner_drawed = False
                game.reset()

        clock.tick(30)
        
    pygame.quit()

if __name__ == "__main__":
    start_running()
