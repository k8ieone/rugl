import random
from turtle import *

number = 100
Number = range(number)
NameList = []
setworldcoordinates(-3, 0, 3, 10)
bgcolor("black")

x = 0
y = 0

bigListX = []
bigListY = []

def NameGenerator():
    global NameList
    global number
    
    for x in range(number):
        Name = "turtle" + str(Number[x])
        NameList.append(Name)
        NameList[x] = Turtle()
        NameList[x].speed(0)
        NameList[x].penup()
        NameList[x].ht()

def Draw():
    global number
    global NameList
    global bigListX
    global bigListY
    
    for x in range(number):
        #NameList[x].penup # This seems to have no effect
        NameList[x].setposition(bigListX[x], bigListY[x])
        NameList[x].dot(2, "green")
        
def getPoint():
    
    global x
    global y
    global number
    global bigListX
    global bigListY
    
    for i in range(number):
        r = random.uniform(0, 100)
        #print(r)
            
        if r < 1:
            nextX = 0 # There was an unnessesary semicolon here (probably a typo)
            nextY = 0.16 * y
                
        elif r < 86:
            nextX = 0.85 * x + 0.04 * y
            nextY = -0.04 * x + 0.85 * y + 1.6
                
        elif r < 93:
            nextX = 0.20 * x + - 0.26 * y
            nextY = 0.23 * x + 0.22 * y + 1.6
                
        else:
            nextX = -0.15 * x + 0.28 * y
            nextY = 0.26 * x + 0.24 * y + 0.44
                  
        x = nextX
        y = nextY
        bigListX.append(x)
        bigListY.append(y)
 
NameGenerator()

while True:
    getPoint()
    Draw()
    
    print(NameList[0].position())
    bigListX = []
    bigListY = []
