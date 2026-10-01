#!/usr/bin/python3
from turtle import penup, pendown, left, right, forward, shape, color
turtle.shape('turtle')
turtle.color(fill_color='lightseagreen')
def write(a):
    if a == 1:
        penup()
        right(90)
        forward(50)
        left(135)
        pendown()
        forward(5000*(0.5))
        right(135)
        forward(100)
        penup()
        left(180)
        forward(100)
        right(90)
        forward(25)
    if a == 2:
        pendown()
        forward(50)
        right(90)
        forward(50)
        right(45)
        forward(5000**(0.5))
        left(135)
        forward(50)
        penup()
        forward(25)
        left(90)
        forward(100)
        right(90)
    if a == 3:
        pendown()
        forward(50)
        left(135)
        forward(5000**(0.5))
        left(135)
        forward(50)
        right(135)
        forward(5000**(0.5))
        penup()
        left(135)
        forward(75)
        left(90)
        forward(100)
        right(90)
    if a == 4:
        pendown()
    if a == 5:
    if a == 6:
    if a == 7:
    if a == 8:
    if a == 9:
    if a == 0:
print('Введите индекс:')
a = list(map(int, input))
for i in a:
    write(a)

