
import turtle as t

t.color('royal blue', 'green yellow')
t.speed(10)
t.begin_fill()
screen = t.Screen()
screen.screensize(1280, 720)

def draw_triangle():
    t.forward(150)
    t.right(120)
    t.forward(150)
    t.right(120)
    t.forward(150)
    t.right(120)

for i in range(1):
    draw_triangle()
    t.right(5)

t.end_fill()
t.exitonclick()
