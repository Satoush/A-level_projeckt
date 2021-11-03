import pygame
#from Bullet import bullet
import math

screen = pygame.display.set_mode((800, 600))

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/User_icon.png')
        self.X = 400
        self.Y = 300
        self.changeX = 0
        self.changeY = 0
        self.velocity = 1
        self.rect = self.image.get_rect(midbottom = (400,300))

    def draw_character(self):
        # Gets mouse position
        mx, my = pygame.mouse.get_pos()

        # Gets the position of the X and Y
        x = (self.X + self.rect[2] // 2)
        y = (self.Y + self.rect[3] // 2)

        # Calculates the distance between the mouse and the player icon
        difX = mx - x
        difY = my - y
        # angle = 0

        # Calculates the angle of the player and the mouse
        angle = math.atan2(difX, difY) * (180 / math.pi) - 5
        #print(angle)
        rotated_image = pygame.transform.rotate(self.image, angle) # This changes the rotation of the players image where the position of the mouse would be
        screen.blit(rotated_image, (self.X, self.Y)) # Draws the player and the rotation of the player

    def player_input(self):
        key = pygame.key.get_pressed()
        p = pygame
        self.changeX = 0
        self.changeY = 0
        if key[p.K_DOWN] or key[p.K_UP] or key[p.K_w] or key[p.K_s]:
            self.changeY = self.velocity * - (int(key[p.K_UP] or key[p.K_w]) * 2 - 1)
        if key[p.K_LEFT] or key[p.K_RIGHT] or key[p.K_a] or key[p.K_d]:
            self.changeX = self.velocity * - (int(key[p.K_LEFT] or key[p.K_a]) * 2 - 1)
        self.X += self.changeX
        self.Y += self.changeY

    def boundaries(self):
        if self.X <= 0:
            self.X = 0
        elif self.X >= 750:
            self.X = 750

        if self.Y <= 0:
            self.Y = 0
        elif self.Y >= 555:
            self.Y = 555

    def update(self):
        self.boundaries()
        self.draw_character()
        self.player_input()

