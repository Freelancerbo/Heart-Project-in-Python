
import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("Black")

def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) -5 * \
        math.cos(2*n) - 2* math.cos(3*n) - \
        math.cos(4*n)
    return x, y

t.penup()
for i in range(15):
    t.goto(0,0)
    t.pendown()
    for n in range(0,100,2):
        x,y = corazon(n/10)
        t.goto(x*2 ,y*2 + (i*40))

    t.penup()

t.hideturtle()
turtle.done()
