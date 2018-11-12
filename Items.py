# imporing pygame, sys, time and random
import pygame, sys, time
from random import randrange, choice

# importing constant variables
from global_variables import *

# other items
class Items:

    beginner = 40
    amateur = 20
    pro = 0

    def button(self, button_x, button_y, button_width, button_height, colour, action = None):

        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if (button_x + button_width) > cursor[0] > button_x and (button_y + button_height) > cursor[1] > button_y:
            pygame.draw.rect(self.screen, colour, (button_x, button_y, button_width, button_height))

            if click[0] == 1 and action != None:

                if action == "main_menu":

                    self.main_menu()

                if action == "single_play":

                    self.choose_difficulty()

                if action == "multi_play":

                    self.single_player = False
                    self.multi_player = True

                    self.game_loop()

                if action == "beginner":

                    self.single_player = True
                    self.multi_player = False

                    self.difficulty = self.beginner
                    self.game_loop()

                if action == "amateur":

                    self.single_player = True
                    self.multi_player = False

                    self.difficulty = self.amateur
                    self.game_loop()

                if action == "pro":

                    self.single_player = True
                    self.multi_player = False

                    self.difficulty = self.pro
                    self.game_loop()
