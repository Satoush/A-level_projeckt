import pygame
import random
import math
from Character import Character
from Enemy import enemy

# Intialize pygame
pygame.init()

WHITE = (255, 255, 255)
screen = pygame.display.set_mode((800, 600))
########################################################################################
playerX = 400
playerY = 300
playerX_change = 0
playerY_change = 0
player_velocity = 1

enemy_image_path = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_velocity = 0.01
num_of_enemies = 6
i = 0

person = Character(pygame.image.load('Assets/User_icon.png'), playerX, playerY, playerX_change, playerY_change,
                   player_velocity)

zombie = enemy(enemy_image_path, enemyX, enemyY, enemyX_change, enemyY_change,)
"""
#enemies_list = []
for i in range(num_of_enemies):
    enemy_image_path.append(zombie)
#enemies_list[0]

"""
for i in range(num_of_enemies):
    enemy_image_path.append(pygame.image.load('Assets/zombie.png'))
    enemyX.append(random.randint(0, 725))
    enemyY.append(random.randint(0, 600))
    enemyX_change.append(0.001)  # initial speed of the  character
    enemyY_change.append(0)

################################################################################################################################################################################
running = True

while running:
    screen.fill(WHITE)

    # mouse input
    mx, my = pygame.mouse.get_pos()





    rotation = 0
    location = [mx, my]
    #person.X, personY = mx,my
    #print(mx,my)
    #screen.blit(pygame.transform.rotate(person.Image, rotation), (location[0], location[1]))


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

        if event.type == pygame.KEYUP:
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

    # enemy movement

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        #enemyY[i] += enemyY_change[i]

        if enemyX[i] >= 750:
            enemyX_change[i] *= -1
        elif enemyX[i] <= 0:
            enemyX_change[i] *= 1

        if enemyY[i] >= 545:
            enemyY_change[i] *= -1
        elif enemyY[i] <= 0:
            enemyY_change[i] *= 1
        ##################################################################################

        if enemyX[i] > person.X:
            enemyX_change[i] = -1 * enemy_velocity

        elif enemyX[i] < person.X:
            enemyX_change[i] =  enemy_velocity

        elif enemyX[i] == person.X:
            enemyX_change[i] =  0

        ##################################################################################
        if enemyY[i] > person.X:
            enemyX_change[i] = -1 * enemy_velocity

        elif enemyX[i] < person.X:
            enemyX_change[i] =  enemy_velocity

        elif enemyX[i] == person.X:
            enemyX_change[i] =  0




        zombie.draw(i, enemyX[i], enemyY[i])
        #zombie.move_to_player(enemyX[i], person.X)

    person.draw(mx,my)

    pygame.display.update()










"""
#enemies_list = []
for i in range(num_of_enemies):
    enemy_image_path.append(zombie)
#enemies_list[0]

"""

#adding enemies to the list
"""
for i in range(num_of_enemies):
    enemy_image_path.append(pygame.image.load('Assets/zombie.png'))
    enemyX.append(random.randint(0, 725))
    enemyY.append(random.randint(0, 600))
    enemyX_change.append(enemy_velocity)  # initial speed of the  character
    enemyY_change.append(enemy_velocity)

"""

