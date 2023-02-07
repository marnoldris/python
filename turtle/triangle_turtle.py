#!/usr/bin/python

import turtle as t

t.speed(8)

def draw_triangle():
    t.forward(150)
    t.right(120)
    t.forward(150)
    t.right(120)
    t.forward(150)
def draw_square():
    """ Your code here """
def draw_pentagon():
    for i in range(5):
        t.forward(72)
        t.right(72)
    
def draw_n_shape(num_sides):
    for i in range(num_sides):
        t.forward(50)
        t.right(360/num_sides)

for i in range(72):
    draw_n_shape(12)
    t.right(5)


t.exitonclick()



