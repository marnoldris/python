#!/usr/bin/python

import turtle as t
import random

t.ht()

t.color('red','yellow')
t.begin_fill()

def draw_square():
    sq_length = 60
    t.forward(sq_length)
    for i in range(3):
        t.right(90)
        t.forward(sq_length)

t.tracer(0,0)

for i in range(3):
    t.penup()
    t.goto(random.randrange(10, 500), random.randrange(10, 500))
    t.pendown()
    for i in range(72):
        draw_square()
        t.right(5)

t.end_fill()    
t.update()
t.exitonclick()
