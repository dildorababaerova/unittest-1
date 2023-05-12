import turtle as t

from random import randint, random






def draw_star (self, points, size, col, x, y):
    x1 = input("Anna  -x koordinaatin raja")
    x2 = input("Anna  x koordinaatin raja")
    y1 = input ("Anna -y koordinatin raja")
    y2 = input ("Anna y koordinatin raja")
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2 
 

    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()    
    print(x, y)
    


    for i in range (points):

        t.forward(size)

        t.right(angle)

        t.end_fill()
        
def rectangle(horizontal, vertical, color):    
    t.pendown()

    angle = 90
    t.forward(self.x2, self.y2)
    t.right(angle)
    t.forward(self.x2, self.y1)
    t.right(angle)
    t.forward(self.x1, self.y1)
    t.right(angle)
    t.forward(self.x1, self.y2) 
    t.end_fill()


# Pääohjelma

t.Screen ().bgcolor('dark blue')

while True:

    ranPts = randint(2, 5) * 2 + 1
    ranSize = randint (10, 50)
    ranCol = (random(), random(), random())    

    ranX = randint(x1, x2)
    ranY = randint(y1, y2)

    draw_star(ranPts, ranSize, ranCol, ranX, ranY)
    draw_kub(point, x, y)