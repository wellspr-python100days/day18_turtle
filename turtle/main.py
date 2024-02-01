from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()

t.shape("turtle")


def draw_line(length):
    t.forward(length)


def draw_dashed(length):
    for _ in range(int(length/20)):
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)


def draw_square(side):
    for _ in range(4):
        draw_line(side)
        t.left(90)


def draw_regular_figure(sides, length):
    ''' Draws a regular geometric figure.
        sides - number of sides
        length - length of sides
    '''
    for _ in range(sides):
        t.forward(length)
        t.left(360/sides)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_many_figures():
    t.penup()
    t.goto(-50, -100)
    t.pendown()
    s.colormode(255)

    for i in range(3, 11):
        t.color(random_color())
        draw_regular_figure(length=100, sides=i)

    t.hideturtle()


def draw_random_walk(steps, size):
    t.pensize(5)
    s.colormode(255)

    for i in range(steps+1):
        
        t.color(random_color())

        rand_dir = random.choice([0, 90, 180, 270])
        print(f"{i}: {rand_dir}")

        t.setheading(rand_dir)
        t.forward(size)


def draw_spirograph(steps, radius):
    s.colormode(255)
    for _ in range(steps):
        t.color(random_color())
        t.left(360/steps)
        t.circle(radius)

t.speed("fastest")
t.hideturtle()
#draw_random_walk(100, 20)

draw_spirograph(steps=100, radius=100)
""" t.pensize(5)
draw_line(100)

t.home()

t.color('red')
t.pensize(1)
draw_dashed(100)

draw_square(100)
 """


s.exitonclick()