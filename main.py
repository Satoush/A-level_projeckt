import pygame
from pygame.locals import *
import random
# import math
from Character import Character
from Enemy import enemy

# Intialize pygame
pygame.init()

WHITE = (255, 255, 255)
screen = pygame.display.set_mode((800, 600))

########################################################################################
playerX = 400  #
playerY = 300
playerX_change = 0
playerY_change = 0
player_velocity = 1

enemy_image_path = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
# enemy_velocity = 100
num_of_enemies = 6

person = Character(pygame.image.load('Assets/User_icon.png'), playerX, playerY, playerX_change, playerY_change,
                   player_velocity)

zombie = enemy(enemy_image_path, enemyX, enemyY, enemyX_change, enemyY_change)
print(zombie)

zombie.adding_multiple_enemies()


################################################################################################################################################################################

def main():
    running = True

    #Loop
    while running:

        #Background
        screen.fill(WHITE)

        #mouse input
        mx,my = pygame.mouse.get_pos()

        rotation = 0
        location = [mx,my]
        screen.blit(pygame.transform.rotate(person.Image,rotation),(location[0],location[1]))





################################################################################################################################################################################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                # Left
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    person.changeX = person.velocity * -1
                # Right
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    person.changeX = person.velocity
                # Up
                if event.key == pygame.K_UP or event.key == ord('w'):
                    person.changeY = person.velocity * -1
                # Down
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    person.changeY = person.velocity

            elif event.type == pygame.KEYUP:
                if event.key == event.key == pygame.K_RIGHT or \
                        event.key == ord('d') or \
                        event.key == pygame.K_LEFT or \
                        event.key == ord('a') or \
                        event.key == pygame.K_UP or \
                        event.key == ord('w') or \
                        event.key == pygame.K_DOWN or \
                        event.key == ord('s'):
                    person.changeX = 0
                    person.changeY = 0

            elif event.type == pygame.MOUSEWHEEL:
                print(event.x, event.y)

        person.X += person.changeX
        person.Y += person.changeY

        # Boundaries
        if person.X <= 0:
            person.X = 0
        elif person.X >= 750:
            person.X = 750

        if person.Y <= 0:
            person.Y = 0
        elif person.Y >= 555:
            person.Y = 555

            # screen.blit(enemy_image_path[i], (enemyX[i], enemyY[i]))
        for i in range(num_of_enemies):
            zombie.draw(i, enemyX[i], enemyY[i])
            zombie.move_to_player(person.X, person.Y)

        person.draw()
        pygame.display.update()


main()
