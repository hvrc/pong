"""
Pong
Wednesday, 25th January 2017

Harsh Rajmachikar
https://github.com/hvrc
harshavardhan@rajmachikar.com

"""

# imporing pygame, time and random
import pygame, time
from random import randrange, choice

# defining FPS, screen dimensions, colours and some other variables
FPS = 60

width = 600
height = 450

gap = 40
step = 10

white = (200, 200, 205)
grey = (40, 40, 45)
space = (30, 30, 35)

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

# Ball class
class Ball:

    # creating array/list of balls
    balls = []

    delta_control = 4

    score_limit = 10

    # creating a list called ball in which we input the values of x, y, size, x_move, y_move
    # then we append the list 'ball' to the list 'ball', and call it whenever necessary
    def init_ball(self):

        ball = [width / 2, randrange(100, height - 100), 17, choice([-5, 5]), 0]
        self.balls.append(ball)

    # drawing the ball
    def draw_ball(self):

        for ball in self.balls:

            ball[0] += ball[3]
            ball[1] += ball[4]

            ball_x = ball[0]
            ball_y = ball[1]

            ball_size = ball[2]

            ball_move_x = ball[3]
            ball_move_y = ball[4]

            pygame.draw.ellipse(self.screen, white, [ball_x, ball_y, ball_size, ball_size])

    # defining borders for the ball
    def ball_borders(self):

        for ball in self.balls:

            # if ball hits the left or right extreme, delete that ball and re-initialize it
            # increase score
            # if score equals score limit, end game
            if ball[0] <= 0:

                self.balls.remove(self.balls[0])
                self.init_ball()

                self.enemy_score += 1

                if self.enemy_score == self.score_limit:

                    self.enemy_wins()

            if ball[0] + ball[2] >= width:

                self.balls.remove(self.balls[0])
                self.init_ball()

                self.player_score += 1

                if self.player_score == self.score_limit:

                    self.player_wins()

            # if ball hits the top or bottom, the ball is deflected
            if ball[1] <= 0:

                ball[4] *= -1

            if ball[1] + ball[2] >= height:

                ball[4] *= -1

    # ball deflecting off the player's paddle
    def ball_collision_player(self):

        for ball in self.balls:

            # this variable returns the difference between the ball and the centre of the paddle
            # (value can be positive or negative)
            delta_y = int(ball[1] + (ball[2] / 2)) - (self.player_y + (self.player_height / 2 ))

            # by nesting the '*' if statements, if the ball touches the paddle anywhere, it is deflected
            #* if ball hits the x axis
            if self.player_x <= ball[0] <= self.player_x + self.player_width:

                #* if ball hits the bottom y axis of the paddle
                if ball[1] <= self.player_y + self.player_height:

                    #* if ball hits the top y axis of the paddle
                    if ball[1] + ball[2] >= self.player_y:

                        # Ball hits the top of the paddle
                        if ball[1] + (ball[2] / 2) < self.player_y + (self.player_height / 2):

                            # deflection of the ball y move variable depends on the delta variable divided by delta control
                            ball[4] = delta_y / self.delta_control

                            # if ball is coming from the top, deflect it back
                            if delta_y < 0:

                                ball[3] *= -1

                            # if ball is coming from the bottom, deflect it to the other direction
                            if delta_y > 0:

                                ball[3] *= -1
                                ball[4] *= -1

                        # Ball hits the bottom of the paddle
                        if ball[1] + (ball[2] / 2) > self.player_y + (self.player_height / 2):

                            # deflection of the ball y move depends on the delta variable divided by delta control
                            ball[4] = delta_y / self.delta_control

                            # if ball is coming from the bottom, deflect it back
                            if delta_y > 0:

                                ball[3] *= -1

                            # if ball is coming from the top, deflect it to the other direction
                            if delta_y < 0:

                                ball[3] *= -1
                                ball[4] *= -1

                        # Ball hits the centre
                        if ball[1] + (ball[2] / 2) == self.player_y + (self.player_height / 2):

                            ball[3] *= -1
                            ball[4] = 0

    # ball deflecting off the player's paddle
    def ball_collision_enemy(self):

        for ball in self.balls:

            # this variable returns the difference between the ball and the centre of the paddle
            # (value can be positive or negative)
            delta_y = int(ball[1] + (ball[2] / 2)) - (self.enemy_y + (self.enemy_height / 2))

            # by nesting the '*' if statements, if the ball touches the paddle anywhere, it is deflected
            #* if ball hits the x axis
            if self.enemy_x >= ball[0] >= self.enemy_x - self.enemy_width:

                #* if ball hits the bottom y axis of the paddle
                if ball[1] <= self.enemy_y + self.enemy_height:

                    #* if ball hits the top y axis of the paddle
                    if ball[1] + ball[2] >= self.enemy_y:

                        # Ball hits the top of the paddle
                        if ball[1] + (ball[2] / 2) < self.enemy_y + (self.enemy_height / 2):

                            # deflection of the ball y move depends on the delta variable divided by delta control
                            ball[4] = delta_y / self.delta_control

                            # if ball is coming from the bottom, deflect it back
                            if delta_y < 0:

                                ball[3] *= -1

                            # if ball is coming from the top, deflect it to the other direction
                            if delta_y > 0:

                                ball[3] *= -1
                                ball[4] *= -1

                        # Ball hits the bottom of the paddle
                        if ball[1] + (ball[2] / 2) > self.enemy_y + (self.enemy_height / 2):

                            # deflection of the ball y move depends on the delta variable divided by delta control
                            ball[4] = delta_y / self.delta_control

                            # if ball is coming from the bottom, deflect it back
                            if delta_y > 0:

                                ball[3] *= -1

                            # if ball is coming from the top, deflect it to the other direction
                            if delta_y < 0:

                                ball[3] *= -1
                                ball[4] *= -1

                        # Ball hits the centre
                        if ball[1] + (ball[2] / 2) == self.enemy_y + (self.enemy_height / 2):

                            ball[3] *= -1
                            ball[4] = 0

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

# Runs fundamental code
class Sketch(Player, Enemy, Ball, Menus, Items):

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
    Sketch().main_menu()
