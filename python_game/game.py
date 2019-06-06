import pygame
import os
import random

# some basic shit
pygame.init()
screen = pygame.display.set_mode((400, 300))
game = True
x = 10
y = 10
counter = 0
image__path = os.path.dirname(os.path.abspath(__file__)) + "/Resources/rock.png"
number_of_obstacles_on_screen = 5


# class of the obstacle (obviously) that will be falling down
class Obstacle:

    def __init__(self, x, y, z, speed):
        self.x = x
        self.y = y
        self.z = z
        self.speed = speed
        image = pygame.image.load(image__path)
        self.image = pygame.transform.scale(image, (int(self.z * 1.334), self.z))

    def __repr__(self):
        return "x: %s, y: %s, z: %s, speed: %s" % (self.x, self.y, self.z, self.speed)


# actual fuckin' game
while game:

    # you know. game should close when you hit the cross thingy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game = False

        # controls for arrow keys (this will be changed soon)
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]: y -= 10
        if pressed[pygame.K_DOWN]: y += 10
        if pressed[pygame.K_LEFT]: x -= 10
        if pressed[pygame.K_RIGHT]: x += 10

    #screen shit
    screen.fill((0, 0, 0))
    
    #creating list of obstacles
    if counter // 108000 == 0: # 1 minute = 216, 000 (maybe)
        number_of_obstacles_on_screen += 1
        list_of_obstacles = []

        for i in range(number_of_obstacles):
            obstacle = "obstacle" + str(i)
            print(obstacle)
            list_of_obstacles.append(obstacle)
            print(list_of_obstacles)
            z = random.randint(70, 170)
            list_of_obstacles[i] = Obstacle((10 * i), (10 * i), z, 10)
    
    #getting obstacles to the screen
    for i in range(len(list_of_obstacles)):
        screen.blit(list_of_obstacles[i].image, (list_of_obstacles[i].x, list_of_obstacles[i].y))

    #end shit
    counter += 1
    pygame.display.flip()
    pygame.time.Clock().tick(60)
