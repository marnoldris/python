#!/usr/bin/python

import turtle

""" Code for grabbing the image """
import tkinter as tk
from PIL import ImageGrab
WIDTH = 500
HEIGHT = 500
def dump_gui():
    print('Saving turtle image as png...')
    x0 = root.winfo_rootx() + 1
    y0 = root.winfo_rooty() + 1
    x1 = x0 + root.winfo_width()
    y1 = y0 + root.winfo_height()
    ImageGrab.grab().crop((x0, y0, x1, y1)).save('output.png')
root = tk.Tk()
root.attributes('-alpha', 0.3)
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()
t = turtle.RawTurtle(canvas)
# Note: Make all turtle calls t.call
#       and add dump_gui() at the end.
""" End code for grabbing image """

t.ht() #add this
t.speed(20)
t.color('red','yellow')

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

dump_gui()
