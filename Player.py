# imporing pygame, sys, time and random
import pygame, sys, time
from random import randrange, choice

# importing constant variables
from global_variables import *

# Player class
class Player:

    # x, y, width, height
    player_x = gap
    player_y = height / 2

    player_width = 17
    player_height = 90

    # movement variable and score
    player_move = 0
    player_score = 0

    # drawing the player
    def draw_player(self):

        # player movement
        self.player_y += self.player_move

        pygame.draw.rect(self.screen, white, [self.player_x, self.player_y, self.player_width, self.player_height])

    # disabling player to move off-screen
    def player_borders(self):

        if self.player_y < 0:

            self.player_y = 0
            self.player_move = 0

        if self.player_y > height - self.player_height:

            self.player_y = height - self.player_height
            self.player_move = 0
