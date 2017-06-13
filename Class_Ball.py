# imporing pygame, sys, time and random
import pygame, sys, time
from random import randrange, choice

# importing constant variables
from global_variables import *

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
