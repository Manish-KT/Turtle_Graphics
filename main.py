import random
from turtle import Turtle, Screen

torti = Turtle()
screen = Screen()

torti.shape("turtle")
torti.color("red")
torti.speed("fastest")


def draw_spirograph(size):
    for i in range(int(360 / size)):
        torti.pencolor(random.random(), random.random(), random.random())
        torti.circle(100)
        torti.right(size)


draw_spirograph(int(input("enter gap size of spirograph: ")))

screen.exitonclick()
