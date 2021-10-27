import pygame
import math

screen = pygame.display.set_mode((800, 600))

class bullet():
    def __init__(self,Image_path, pos_X, pos_Y, angle,direction):
        self.Image_path = Image_path
        self.posX  = pos_X
        self.posY = pos_Y
        self.angle = angle
        self.velocity_x = 0
        self.velocity_y = 0
        self.velocity = 5

    # Velocity
    def set_vel(self):
        temp_angle = self.angle

        if abs(self.angle) > abs(90):
            temp_angle = 180 - abs(self.angle) # Converts obtuse angle into acute angle

        # Value that converts the direction to be left or right
        x_direction = 1
        y_direction = 1

        if self.angle < 0:
            x_direction = -1

        if abs(self.angle) > 90:
            y_direction = -1

        # Creates the value for the x and y velocity
        self.velocity_y = self.velocity * abs(math.cos(temp_angle))* y_direction
        self.velocity_x = self.velocity * math.sin(temp_angle)* x_direction

        return self.velocity_x, self.velocity_y

    # Makes the bullet move
    def move(self):
        self.posY += self.velocity_y
        self.posX += self.velocity_x










# Makes every number positive
def abs(num):
    return ((num)**2)**0.5

