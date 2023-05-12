import turtle as t

from random import randint, random


# Piirrä neliö
for i in range(2):
    t.forward(450) # Siirry eteenpäin 100 yksikköä
    t.left(90)
    t.forward(350) 
    t.left(90) # Käänny vasemmalle 90 astetta

# Pysäytä ikkuna kun klikataan hiirellä
t.done()


def draw_star (points, size, col, x, y):
    
    # x1 = input("Anna  -x koordinaatin raja")
    # x2 = input("Anna  x koordinaatin raja")
    # y1 = input("Anna -y koordinatin raja")
    # y2 = input("Anna y koordinatin raja")
       
    
    t.penup()    
    t.goto(x,y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()   

    for i in range (points):
        t.forward(size)
        t.right(angle)
        t.end_fill()
        
    

# Pääohjelma

t.Screen ().bgcolor('dark blue')

while True:

    ranPts = randint(2, 5) * 2 + 1
    ranSize = randint (10, 50)
    ranCol = (random(), random(), random())    

    ranX = randint(-350, 100)
    ranY = randint(-200, 150)

    draw_star(ranPts, ranSize, ranCol, ranX, ranY)
    draw_star(4, ranSize, ranCol, ranX, ranY)
    