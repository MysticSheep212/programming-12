from turtle import*
import math

shape("turtle")

def diamond(size):
    right(45)
    for i in range(4):
        right(90)
        forward(size)

# diamond(100)

def arrow(size, direction):
    right(direction + 45)
    forward(size/3 * 2)
    right(135)
    forward(size/3)
    left(90)
    forward(size)
    right(90)
    forward(size/3)
    right(90)
    forward(size)
    left(90)
    forward(size/3)
    right(135)
    forward(size/3 * 2)

arrow(500, 146)

Screen().exitonclick()