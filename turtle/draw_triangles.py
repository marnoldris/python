#!/usr/bin/python

import turtle as t
import random as r

t.screensize(1280, 720)
t.tracer(0,0)
t.ht()

t.color('red','yellow')

def draw_triangle():
    tr_size = 320
    for i in range(3):
        t.forward(tr_size)
        t.right(120)

for i in range(3):
    t.penup()
    x_val = r.randrange(-550, 550)
    y_val = r.randrange(-550, 550)
    t.goto(x_val, y_val)
    t.pendown()
    t.begin_fill()
    for i in range(72):
        draw_triangle()
        t.right(5)
    t.end_fill()

t.update()
t.exitonclick()
