# import colorgram
#
# rgb_colors = []
#
# colors = colorgram.extract('hirst_painting.jpg', 36)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(253, 253, 241), (236, 250, 243), (188, 19, 46), (243, 232, 66), (251, 230, 236), (216, 237, 244),
              (196, 76, 32), (218, 67, 107), (195, 175, 18), (18, 125, 173), (13, 143, 89), (108, 182, 209),
              (13, 167, 214), (206, 153, 93), (239, 232, 3), (24, 39, 74), (183, 43, 63), (36, 44, 110), (77, 174, 96),
              (214, 68, 49), (217, 130, 153), (124, 185, 120), (237, 162, 181), (6, 60, 38), (148, 209, 220),
              (7, 92, 52), (5, 86, 110), (162, 28, 26), (235, 170, 163), (155, 215, 187), (87, 24, 56), (183, 185, 210),
              (115, 119, 152), (91, 24, 21)]

from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.penup()
tim.goto(-250, -250)
y = -250
for i in range(10):
    for j in range(10):
        tim.dot(20, color_list[random.randint(0, 33)])
        tim.forward(50)
    y += 30
    tim.goto(-250, y)
screen.exitonclick()