#!/usr/bin/python3
from turtle import forward, left, stamp, shape
shape('turtle')
for i in range (24):
    forward(300)
    stamp()
    left(180)
    forward(300)
    left(360/24)

