import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
game = True

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game = False
        else:
            print(event.type)

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()