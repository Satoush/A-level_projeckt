import pygame
import math

screen = pygame.display.set_mode((800, 600))



class Character():
    def __init__(self, Image, X, Y, changeX, changeY, velocity):
        self.Image = Image
        self.X = X
        self.Y = Y
        self.changeX = changeX
        self.changeY = changeY
        self.velocity = velocity
        self.bullet_state = 'Ready'

    def draw(self,mx,my):

        difX = mx - self.X +5
        difY = my - self.Y +5
        angle = 0
        if difY != 0:
            angle = math.atan(difX / difY) *(180/math.pi)
            print(angle)
        rotated_image = pygame.transform.rotate(self.Image, angle)

        screen.blit(rotated_image, (self.X, self.Y))




    def fire_bullet(self):
        global bullet_state
        pass




'''
  def Test(self):
        print("hello")
'''

