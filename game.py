import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
game = True
x = 10
y = 10

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game = False

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]: y -= 10
        if pressed[pygame.K_DOWN]: y += 10
        if pressed[pygame.K_LEFT]: x -= 10
        if pressed[pygame.K_RIGHT]: x += 10

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 60, 60))

    pygame.display.flip()