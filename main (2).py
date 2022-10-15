import turtle
from turtle import *
import colorsys

wn=Screen()
wn.setup(1200,680)
wn.bgcolor('black')

t = Turtle()
t.speed(0)
t.hideturtle()
hue=0.0

for i in range(400):
    color=colorsys.hsv_to_rgb(hue,1,1)
    t.pencolor(color)
    t.pensize(2)
    t.begin_fill()
    t.fd(i)
    t.rt(160)

    for j in range(3):
        t.fd(i)
        t.rt(198)
    t.end_fill()
    hue=0.01


