# imporing pygame, sys, time and random
import pygame, sys, time
from random import randrange, choice

# importing constant variables
from global_variables import *

# Enemy class
class Enemy:

    #x, y, width, height
    enemy_x = width - (gap + 17)
    enemy_y = height / 2

    enemy_width = 17
    enemy_height = 90

    # movement variable and score
    enemy_move = 0
    enemy_score = 0

    # drawing enemy
    def draw_enemy(self):

        # enemy movement
        self.enemy_y += self.enemy_move

        pygame.draw.rect(self.screen, white, [self.enemy_x, self.enemy_y, self.enemy_width, self.enemy_height])

    # disabling enemy to move off-screen
    def enemy_borders(self):

        if self.enemy_y < 0:

            self.enemy_y = 0
            self.enemy_move = 0

        if self.enemy_y > height - self.enemy_height:

            self.enemy_y = height - self.enemy_height
            self.enemy_move = 0

    # creating a function for the enemy AI
    def enemy_AI(self):

        for ball in self.balls:

            # if the ball is past the half-line, the enemy is alert
            if ball[3] > 0:

                # if the ball is above the centre of the paddle move the paddle
                if self.enemy_y + (self.enemy_height / 2) < ball[1] - self.difficulty:

                    self.enemy_move = step

                #if the ball is below the centre of the paddle move the paddle
                elif self.enemy_y + (self.enemy_height / 2) > ball[1] + self.difficulty:

                    self.enemy_move = -step

            # if the ball is on the other side, the enemy is not alert
            else:

                if self.enemy_y + (self.enemy_height / 2) < (height / 2) - 100:

                    self.enemy_move = step

                elif self.enemy_y + (self.enemy_height / 2) > (height / 2) + 100:

                    self.enemy_move = -step
