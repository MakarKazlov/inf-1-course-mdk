#!/usr/bin/python3
import turtle
def circle(direction='left'):
    for _ in range(360):
        turtle.forward(1)
        if direction == 'left':
            turtle.left(1)
        elif direction == 'right':
            turtle.right(1)
        else:
            print('ERROR')
            return
def eight():
    circle('left')
    circle('right')
turtle.speed(0)
turtle.shape('turtle')
for _ in range(3):
    eight()
    turtle.left(60)

turtle.mainloop()
