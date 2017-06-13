"""
Pong
Tuesday, 13th June 2017

Harsh Rajmachikar
https://github.com/hvrc
harshavardhan@rajmachikar.com

"""

# imporing pygame, time and random
import pygame, sys, time
from random import randrange, choice

# importing constant variables
from global_variables import *

# importing Classes
from Class_Player import *

from Class_Enemy import *

from Class_Ball import *

from Class_Menus import *

from Class_Items import *

# Runs fundamental code
class main(Player, Enemy, Ball, Menus, Items):

    # defining single player and multi player as None (or not yet defined)
    single_player = None
    multi_player = None

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pong")

        # redering the text
        self.small_font = pygame.font.SysFont(None, 30)
        self.medium_font = pygame.font.SysFont(None, 60)
        self.large_font = pygame.font.SysFont(None, 100)

        self.clock = pygame.time.Clock()

        # initializing rain
        self.init_ball()

    # fills the screen
    def fill(self, fill_colour):

        self.screen.fill(fill_colour)

    # drawing the half-line
    def half_line(self):

        pygame.draw.line(self.screen, grey, (width / 2, 0), (width / 2, height), 4)

    # fundamental screen rendering in pygame
    def render(self, clock, FPS):

        pygame.display.update()
        
        clock.tick(FPS)

    # display score
    def show_score(self):

        self.player_score_text = self.medium_font.render(str(self.player_score), True, grey)
        self.enemy_score_text = self.medium_font.render(str(self.enemy_score), True, grey)

        self.screen.blit(self.player_score_text, [120, 50])
        self.screen.blit(self.enemy_score_text, [width - 150, 50])

    # event handling
    def events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:

                    self.player_move = -step

                if event.key == pygame.K_z:

                    self.player_move = step

                # multiplayer controls
                if self.multi_player == True:

                    if event.key == pygame.K_k:

                        self.enemy_move = -step

                    if event.key == pygame.K_m:

                        self.enemy_move = step


            if event.type == pygame.KEYUP:

                if event.key == pygame.K_a:

                    self.player_move = 0

                if event.key == pygame.K_z:

                    self.player_move = 0

                # multiplayer controls
                if self.multi_player == True:

                    if event.key == pygame.K_k:

                        self.enemy_move = 0

                    if event.key == pygame.K_m:

                        self.enemy_move = 0

        # optional mouse movement for player

        # cursor = pygame.mouse.get_pos()
        
        # self.player_y = cursor[1] - (self.player_height / 2)

    # calling all the functions
    def game_loop(self):

        # main loop
        while True:

            # calls AI function only when single player mode is chosen
            if self.single_player == True:

                self.enemy_AI()

            self.events()

            self.fill(space)

            self.half_line()

            self.show_score()

            self.player_borders()

            self.enemy_borders()

            self.ball_borders()

            self.ball_collision_player()

            self.ball_collision_enemy()

            self.draw_player()

            self.draw_enemy()

            self.draw_ball()

            self.render(self.clock, FPS)


if __name__ == '__main__':
    main().main_menu()
