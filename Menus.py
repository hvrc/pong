# imporing pygame, sys, time and random
import pygame, sys, time
from random import randrange, choice

# importing constant variables
from global_variables import *

# Menus class
class Menus:

    def __init__(self):

        self.clock = pygame.time.Clock()

    # main menu, call this function on startup
    def main_menu(self):

        # on startup scores are zero
        self.player_score = 0
        self.enemy_score = 0

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            self.fill(space)

            self.button(width / 3.05, 275, 200, 50, grey, "multi_play")
            self.button(width / 3.05, 350, 200, 50, grey, "single_play")

            self.title_text = self.large_font.render("PONG", True, white)
            self.multi_text = self.small_font.render("MULTI PLAYER", True, white)
            self.single_text = self.small_font.render("SINGLE PLAYER", True, white)

            self.screen.blit(self.title_text, [width / 3.05, 50])
            self.screen.blit(self.multi_text, [width / 2.69, 290])
            self.screen.blit(self.single_text, [width / 2.77, 365])

            self.render(self.clock, FPS)

    # displays message when player wins
    def player_wins(self):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            self.fill(space)

            self.button(width / 3.05, 400, 200, 50, grey, "main_menu")

            self.title_text = self.medium_font.render("Player 1 Wins!", True, white)
            self.back_text = self.large_font.render("...", True, white)

            self.screen.blit(self.title_text, [width / 3.87, 50])
            self.screen.blit(self.back_text, [width / 2.22, 375])

            self.render(self.clock, FPS)

    # displays message when enemy wins
    def enemy_wins(self):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            self.fill(space)

            self.button(width / 3.05, 400, 200, 50, grey, "main_menu")

            self.title_text = self.medium_font.render("Player 2 Wins!", True, white)
            self.back_text = self.large_font.render("...", True, white)

            self.screen.blit(self.title_text, [width / 3.87, 50])
            self.screen.blit(self.back_text, [width / 2.22, 375])

            self.render(self.clock, FPS)

    # choose difficulty in this menu
    def choose_difficulty(self):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            self.fill(space)

            self.button(width / 3.05, 150, 200, 50, grey, "beginner")
            self.button(width / 3.05, 225, 200, 50, grey, "amateur")
            self.button(width / 3.05, 300, 200, 50, grey, "pro")

            self.title_text = self.medium_font.render("Choose your Difficulty", True, white)
            self.beginner_text = self.small_font.render("BEGINNER", True, white)
            self.amateur_text = self.small_font.render("AMATEUR", True, white)
            self.pro_text = self.small_font.render("PRO", True, white)

            self.screen.blit(self.title_text, [80, 50])
            self.screen.blit(self.beginner_text, [width / 2.5, 165])
            self.screen.blit(self.amateur_text, [width / 2.48, 240])
            self.screen.blit(self.pro_text, [width / 2.22, 315])

            self.render(self.clock, FPS)
