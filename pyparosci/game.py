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
y = 730
start_path = os.path.dirname(os.path.abspath(__file__))
rock0 = pygame.image.load(start_path + "/Resources/rock0.png")
rock1 = pygame.image.load(start_path + "/Resources/rock1.png")
rock2 = pygame.image.load(start_path + "/Resources/rock2.png")
bonus = pygame.image.load(start_path + "/Resources/bonus.png")
player = pygame.image.load(start_path + "/Resources/player.png")
number_of_obstacles_on_screen = 5
obstacles = 0
list_of_obstacles = []
speed1 = 2
speed2 = 5
past_update = time.clock()
past_bonus = time.clock()
bonus_switch = False
pygame.font.init()
score = 0
lifes = 3
font = pygame.font.Font(start_path + "/Resources/fonts/8bitOperatorPlus8-Regular.ttf", 26)
text_surface_score = font.render(str(score), False, (255, 255, 255))
text_surface_lifes = font.render(str(lifes), False, (255, 255, 255))

class Player:
    def __init__(self):
        self.lives = 3
        self.speed = 6
        image = player
        self.image = pygame.transform.scale(image, (57, 50))

    def __repr__(self):
        return "lives: %s, speed: %s" % (self.lives, self.speed)

class Bonus:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.transform.scale(bonus, (45, 40))

    def __repr__(self):
        return "x: %s, y: %s, speed: %s" % (self.x, self.y, self.speed)

class Obstacle:
    def __init__(self, x, y, z, speed):
        self.x = x
        self.y = y
        self.z = z
        self.speed = speed
        rockrandom = random.randint(0, 2)
        if rockrandom == 0:
            image = rock0

        elif rockrandom == 1:
            image = rock1

        elif rockrandom == 2:
            image = rock2

        self.image = pygame.transform.scale(image, (int(z * 1.4), z))

    def __repr__(self):
        return "x: %s, y: %s, z: %s, speed: %s" % (self.x, self.y, self.z, self.speed)

def obstacleCreator(speed1, speed2):
    global list_of_obstacles
    global number_of_obstacles_on_screen

    for i in range(number_of_obstacles_on_screen):
        
        try:
            dummy = list_of_obstacles[i]

        except IndexError:
            z = random.randint(50, 100)
            x = random.randint(0, width)
            speed = random.randint(speed1, speed2)
            dummy = Obstacle(x, 0, z, speed)
            list_of_obstacles.append(dummy)

player = Player()
bonus = Bonus(0, (heigh * (-1)) - 50, 0)
obstacleCreator(speed1, speed2)

# actual fuckin' game
while game: 

    # you know. game should close when you hit the cross thingy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                game = False

        # controls for arrow keys (this will be changed soon)
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]: 
            x -= 10
        if pressed[pygame.K_RIGHT]:
            x += 10

    #screen shit
    screen.fill((0, 0, 0))
    
    #creating list of obstacles
    now = time.clock()

    if int(now) >= int((past_update + 30)): # 1 minute = 60
        number_of_obstacles_on_screen += 1
        speed1 += 1
        speed2 += 2
        obstacleCreator(speed1, speed2)
        past_update = time.clock()

    if int(now) >= int((past_bonus + 30)): # 1 minute = 60
        bonus.x = random.randint(0, width)
        bonus.y = 0
        bonus.speed = random.randint(10, 15)
        bonus_switch = True
        past_bonus = time.clock()
    
    #getting obstacles to the screen
    for i in range(len(list_of_obstacles)):
        screen.blit(list_of_obstacles[i].image, (list_of_obstacles[i].x, list_of_obstacles[i].y + list_of_obstacles[i].speed))
        list_of_obstacles[i].y += list_of_obstacles[i].speed
        if list_of_obstacles[i].y > heigh:
            list_of_obstacles.pop(i)
            score += 1
            obstacleCreator(speed1, speed2)

        if list_of_obstacles[i].y + (list_of_obstacles[i].z / 2) >= 760 and not set(range(x - 105, x - 10)).isdisjoint(set(range((list_of_obstacles[i].x + 10) - int(list_of_obstacles[i].z * 1.4), list_of_obstacles[i].x - 20))):

            list_of_obstacles.pop(i)
            obstacleCreator(speed1, speed2)

            if lifes - 1 == 0:
                #print("END")
                exit()

            else:
                #print("LIFES -1")
                lifes -= 1
                player.speed -= 1
            
    if bonus_switch:
        screen.blit(bonus.image, (bonus.x, bonus.y + bonus.speed))
        bonus.y += bonus.speed

        if bonus.y > heigh:
            bonus.y = (heigh * (-1)) - 50
            bonus.speed = 0
            bonus_switch = False

    if bonus.y + 20 >= y and not set(range(x - 105, x - 10)).isdisjoint(set(range(bonus.x - 47, bonus.x))):
        bonus.y = (heigh * (-1)) - 50
        bonus.speed = 0
        lifes += 1
        player.speed += 1
        bonus_switch = False

    screen.blit(player.image, (x, y))
    text_surface_score = font.render("Score: " + str(score), True, (255, 255, 255))
    text_surface_lifes = font.render("Lifes: " + str(lifes), True, (255, 255, 255))
    screen.blit(text_surface_lifes, (width - 160, heigh - 40))
    screen.blit(text_surface_score, (width - 160, heigh - 20))

    #end shit
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
