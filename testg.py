import pygame

pygame.init()

WHITE = (255, 255, 255)
screen = pygame.display.set_mode((800, 600))

mySurface = pygame.Surface((50, 50))

def main():
    running = True

    #Loop
    while running:

        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(mySurface,(375,275))


        pygame.display.update()

main()