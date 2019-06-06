import pygame
import os
import random
import time

# some basic shit
pygame.init()
width = 800
heigh = 800
screen = pygame.display.set_mode((width, heigh))
game = True
x = 10
y = 10
image__path = os.path.dirname(os.path.abspath(__file__)) + "/Resources/rock.png"
number_of_obstacles_on_screen = 5
obstacles = 0
list_of_obstacles = []
speed1 = 2
speed2 = 5
past = time.clock()

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

def obstacleCreator(speed1, speed2):

    global list_of_obstacles
    global number_of_obstacles_on_screen

    for i in range(number_of_obstacles_on_screen):
        
        try:
            dummy = list_of_obstacles[i]

        except:
            z = random.randint(50, 100)
            x = random.randint(0, width)
            speed = random.randint(speed1, speed2)
            dummy = Obstacle(x, 0, z, speed)
            list_of_obstacles.append(dummy)

obstacleCreator(speed1, speed2)

# actual fuckin' game
while game: 

    # you know. game should close when you hit the cross thingy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game = False

        # controls for arrow keys (this will be changed soon)
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            y -= 10
        if pressed[pygame.K_DOWN]: 
            y += 10
        if pressed[pygame.K_LEFT]: 
            x -= 10
        if pressed[pygame.K_RIGHT]:
            x += 10

    #screen shit
    screen.fill((0, 0, 0))
    
    #creating list of obstacles
    now = time.clock()
    if int(now) == int((past + 30)): # 1 minute = 3600
        number_of_obstacles_on_screen += 1
        speed1 += 1
        speed2 += 2
        obstacleCreator(speed1, speed2)
        past = time.clock()
    
    #getting obstacles to the screen
    for i in range(len(list_of_obstacles)):
        screen.blit(list_of_obstacles[i].image, (list_of_obstacles[i].x, list_of_obstacles[i].y + list_of_obstacles[i].speed))
        list_of_obstacles[i].y = list_of_obstacles[i].y + list_of_obstacles[i].speed
        if list_of_obstacles[i].y > heigh:
            list_of_obstacles.pop(i)
            obstacleCreator(speed1, speed2)

    #end shit
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    

