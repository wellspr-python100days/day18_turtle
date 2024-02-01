# import colorgram
#
# extracted_colors = colorgram.extract("image.jpg", 30)
#
# colors = []
#
# for color_obj in extracted_colors:
#    r = color_obj.rgb.r
#    g = color_obj.rgb.g
#    b = color_obj.rgb.b
#
#    colors.append((r, g, b))
#
# print(colors)

from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()

colors = [
#    (233, 233, 232),
#    (230, 233, 237),
#    (236, 231, 233),
#    (227, 234, 229),
    (206, 161, 82),
    (55, 88, 130),
    (142, 91, 41),
    (221, 207, 108),
    (139, 26, 49),
    (133, 175, 200),
    (157, 48, 84),
    (46, 55, 102),
    (169, 159, 41),
    (130, 188, 145),
    (82, 20, 43),
    (37, 43, 66),
    (189, 139, 162),
    (186, 93, 106),
    (87, 115, 177),
    (87, 156, 97),
    (59, 39, 32),
    (79, 154, 165),
    (55, 127, 120),
    (196, 82, 70),
    (162, 202, 217),
    (45, 73, 76),
    (44, 75, 73),
    (77, 75, 44),
    (166, 207, 165),
    (218, 176, 187),
]

t.speed('fastest')
s.colormode(255)
t.penup()
t.hideturtle()
x = -250
y = 230

for i in range(10):
    for j in range(10):
        t.goto(x + i*50, y -j*50)
        t.dot(20, random.choice(colors))


s.exitonclick()