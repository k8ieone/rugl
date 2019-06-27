import pygame
import os
import random

pygame.init()
width = 800
heigh = 800
screen = pygame.display.set_mode((width, heigh))
lenght_of_snake = 2
game = True
pause = False
pressed_left = False
pressed_right = False
pressed_up = False
pressed_down = True
end = False
snake_cell_list = []
x = 400
y = 400
speed = 10
path = os.path.dirname(os.path.abspath(__file__))
font = pygame.font.Font(path + "/Resources/Uplifting.otf", 26)
score = 0

class snake_cell:
    def __init__(self, x, y, previous_x, previous_y):
        self.x = x
        self.y = y
        self.previous_x = previous_x
        self.previous_y = previous_y

    def __repr__(self):
        return "x:  %s y:  %s" % (self.x, self.y) 
        
for i in range(lenght_of_snake):
    cell = "cell" + str(i)
    cell = snake_cell(x, y - (i * 10), x, y - (i * 10))
    snake_cell_list.append(cell)

class bonus:
    def __init__(self, x, y):
        self.x = x
        self.y = y

bonus = bonus(round(random.randint(10, 790), -1), round(random.randint(10, 790), -1))

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            game = False      

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            
            if not end:
                if pause:
                    pause = False

                else:
                    pause = True

        elif event.type == pygame.KEYDOWN:          # check for key presses          
            if event.key == pygame.K_LEFT and not pressed_right:        # left arrow pressed
                pressed_left = True
                pressed_right = False
                pressed_up = False
                pressed_down = False

            elif event.key == pygame.K_RIGHT and not pressed_left:     # right arrow pressed
                pressed_left = False
                pressed_right = True
                pressed_up = False
                pressed_down = False

            elif event.key == pygame.K_UP and not pressed_down:
                pressed_left = False
                pressed_right = False
                pressed_up = True
                pressed_down = False

            elif event.key == pygame.K_DOWN and not pressed_up:
                pressed_left = False
                pressed_right = False
                pressed_up = False
                pressed_down = True
                
    if pressed_left and not pause:
        snake_cell_list[0].x -= speed
    if pressed_right and not pause:
        snake_cell_list[0].x += speed
    if pressed_up and not pause:
        snake_cell_list[0].y -= speed
    if pressed_down and not pause:
        snake_cell_list[0].y += speed

    if not end:
        pygame.draw.rect(screen, (255,255,255), (snake_cell_list[0].x, snake_cell_list[0].y, 10, 10), 0)
        pygame.draw.rect(screen, (255, 0, 0), (bonus.x, bonus.y, 10, 10), 0)

        for i in range(1, len(snake_cell_list)):
            pygame.draw.rect(screen, (255,255,255), (snake_cell_list[i].x, snake_cell_list[i].y, 10, 10), 0)

            snake_cell_list[0].previous_x = snake_cell_list[0].x
            snake_cell_list[0].previous_y = snake_cell_list[0].y

        for i in range(1, len(snake_cell_list)):
            snake_cell_list[i].previous_x = snake_cell_list[i].x
            snake_cell_list[i].previous_y = snake_cell_list[i].y
            if snake_cell_list[0].x == snake_cell_list[i].x and snake_cell_list[0].y == snake_cell_list[i].y:
                end = True

            snake_cell_list[i].x = snake_cell_list[i - 1].previous_x
            snake_cell_list[i].y = snake_cell_list[i - 1].previous_y

        text_surface_score = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(text_surface_score, (width - 80, heigh - 45))

    if end:
        text_surface_end0 = font.render("Gameover!", True, (255, 255, 255))
        text_surface_end1 = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(text_surface_end0, (350, 400))
        screen.blit(text_surface_end1, (350, 430))

    if snake_cell_list[0].x >= 800 or snake_cell_list[0].x <= 0 or snake_cell_list[0].y >= 800 or snake_cell_list[0].y <= 0:
        end = True

    if snake_cell_list[0].x == bonus.x and snake_cell_list[0].y == bonus.y:
        bonus.x = round(random.randint(10, 790), -1)
        bonus.y = round(random.randint(10, 190), -1)
        score += 1
        cell = "cell" + str(i)
        cell = snake_cell(snake_cell_list[-1].x, snake_cell_list[-1].y, snake_cell_list[-1].x, snake_cell_list[-1].y)
        snake_cell_list.append(cell)

    pygame.display.flip()
    screen.fill((0, 0, 0))
    pygame.time.Clock().tick(30)
    