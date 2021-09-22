import pygame
import random

screen = pygame.display.set_mode((800, 600))


class enemy():
    def __init__(self, Image_path, X, Y, changeX, changeY):
        self.Image_path = Image_path
        self.X = X
        self.Y = Y
        self.changeX = changeX
        self.changeY = changeY
        self.velocity = 0.01
        self.num_of_enemies = 6

    def draw(self, i, X, Y):
        screen.blit(self.Image_path[i], (X, Y))

    def adding_multiple_enemies(self):
        for i in range(self.num_of_enemies):
            self.Image_path.append(pygame.image.load('Assets/zombie.png'))
            self.X.append(random.randint(0, 725))
            self.Y.append(random.randint(0, 600))
            self.changeX.append(self.velocity)  # initial speed of the  character
            self.changeY.append(self.velocity)

    def move_to_player(self, PlayerX,PlayerY):
        for i in range(self.num_of_enemies):

            if self.X[i] > PlayerX:
                self.changeX[i] =  -1 * self.velocity

            elif self.X[i] < PlayerX:
                self.changeX[i] = self.velocity

            else:
                if self.Y[i] == PlayerX:
                    self.changeX[i] = 0


            if self.Y[i] > PlayerY:
                self.changeY[i] =  -1 * self.velocity

            elif self.Y[i] < PlayerY:
                self.changeY[i] = self.velocity

            else:
                if self.Y[i] == PlayerY:
                    self.changeY[i] = 0


            self.X[i] += self.changeX[i]
            self.Y[i] += self.changeY[i]


""""
        dirvect = pygame.math.Vector2(PlayerX - self.x,
                                      player.rect.y - self.rect.y)
        dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        dirvect.scale_to_length(self.speed)
        self.rect.move_ip(dirvect)
"""

"""

"""
# def move_to_player(self,playerX,playerY):
#    for i in range (self.num_of_enemies):
#       if self.X >= playerX:
