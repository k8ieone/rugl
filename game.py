import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
game = True
x = 10
y = 10

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)

    if image == None:
        canonicalized_path = path.replace("/", os.sep).replace("\\", os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image = pygame.transform.scale(image, (70, 50))
    return image

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
    screen.blit(get_image("D:\\Users\\Gentle\\Desktop\\rock.png"), (x, y))

    pygame.display.flip()
    clock.tick(60)