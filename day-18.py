import turtle as t

import random


tim = t.Turtle()
tim.width(2)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


t.colormode(255)

directions = [0, 90, 180, 270, 360]
tim.speed("fastest")


while tim.heading() < 360:
    tim.pencolor((random_color()))
    tim.circle(100)
    tim.left(1)


screen = t.Screen()
screen.exitonclick()
