#!/usr/bin/python3
import turtle
import math
r = 20
turtle.speed(0)
turtle.shape('turtle')
turtle.left(90)
def circle(r, direction='left'):
    for _ in range(360):
        turtle.forward((2 * math.pi * r) / 360)
        if direction == 'left':
            turtle.left(1)
        elif direction == 'right':
            turtle.right(1)
        else:
            print('ERROR')
            return
def eight(r):
    circle(r, 'left')
    circle(r, 'right')
for i in range(10):
    eight(r)
    r+=10

