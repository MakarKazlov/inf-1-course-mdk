#!/usr/bin/python3
from turtle import forward, left, penup, pendown, shape
shape('turtle')
l = 20
for i in range(10):
    pendown()
    for j in range(4):
        forward(l)
        left(90)
    l+=20
    penup()
    left(225)
    forward(14)
    left(135)


