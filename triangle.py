import turtle

# Luo Turtle-olio
t = turtle.Turtle()

# Piirrä neliö
for i in range(2):
    t.forward(100) # Siirry eteenpäin 100 yksikköä
    t.left(90)
    t.forward(20) 
    t.left(90) # Käänny vasemmalle 90 astetta

# Pysäytä ikkuna kun klikataan hiirellä
turtle.done()
