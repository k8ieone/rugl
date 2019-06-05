import pygame
import os
import random

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
game = True
x = 10
y = 10
image__path = os.path.dirname(os.path.abspath(__file__)) + "/Recourses/rock.png"


while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game = False

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]: y -= 10
        if pressed[pygame.K_DOWN]: y += 10
        if pressed[pygame.K_LEFT]: x -= 10
        if pressed[pygame.K_RIGHT]: x += 10

    screen.fill((0, 0, 0))
    
    z = random.randint(70, 170)

    screen.blit(pygame.transform.scale(pygame.image.load(image__path), (int(z * 1.34), z)), (x, y))

    pygame.display.flip()
    clock.tick(60)