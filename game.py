import pygame
import os
import random

pygame.init()
screen = pygame.display.set_mode((400, 300))
game = True
x = 10
y = 10
counter = 0
image__path = os.path.dirname(os.path.abspath(__file__)) + "/Resources/rock.png"

class Obstacle:

    def __init__(self, x, y, z, speed):
        self.x = x
        self.y = y
        self.z = z
        self.speed = speed
        self.image = pygame.image.load(image__path)

    def __repr__(self):
        return "x: %s, y: %s, z: %s, speed: %s" % (self.x, self.y, self.z, self.speed)

    def resize(self):
        self.image = pygame.transform.scale(self.image, (int(self.z * 1.334), self.z))

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game = False

        pressed = pygame.key.get_pressed()

        while pressed[pygame.K_UP]: y -= 10
        while pressed[pygame.K_DOWN]: y += 10
        while pressed[pygame.K_LEFT]: x -= 10
        while pressed[pygame.K_RIGHT]: x += 10

    screen.fill((0, 0, 0))
    
    if counter // 120 == 0 or counter == 0:
        number_of_obstacles = random.randint(1, 10)
        list_of_obstacles = []

        for i in range(number_of_obstacles):
            obstacle = "obstacle" + str(i)
            print(obstacle)
            list_of_obstacles.append(obstacle)
            print(list_of_obstacles)
            z = random.randint(70, 170)
            list_of_obstacles[i] = Obstacle((10 * i), (10 * i), z, 10)
    
    for i in range(len(list_of_obstacles)):
        screen.blit(list_of_obstacles[i].image, (list_of_obstacles[i].x, list_of_obstacles[i].y))

    counter += 1
    pygame.display.flip()
    pygame.time.Clock().tick(60)
