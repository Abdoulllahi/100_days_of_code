'''
 # @ Author: Abdou Lahi DIOP
 # @ Create Time: 2022-12-21 14:41:27
 # @ Modified by: Abdou Lahi DIOP
 # @ Modified time: 2022-12-22 15:05:07
 # @ Description:
 '''

import random
import turtle as t


turtle = t.Turtle()
t.colormode(255)
turtle.speed(0)

# turtle.hideturtle()
# for _ in range(25):
#     turtle.forward(5)
#     turtle.penup()
#     turtle.forward(5)
#     turtle.pendown()
# for _ in range(4):
#     turtle.forward(100)
#     turtle.left(90)
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]
# directions = [0, 90, 180, 270]

# TODO: draw different shapes
# def draw_figure(sides):
#     turtle.shape()
#     # turtle.color("black", "red")
#     for _ in range(sides):
#         angle = 360 / sides
#         turtle.forward(100)
#         turtle.right(angle)
#     # screen = Screen()
#     # screen.exitonclick()

# for shape_side_n in range(3, 10):
#     turtle.color(random.choice(colours))
#     draw_figure(shape_side_n)

# draw_figure(10)

# TODO: random walk


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# turtle.pensize(10)
# for _ in range(200):
#     turtle.color(random_color())
#     turtle.forward(30)
#     turtle.setheading(random.choice(directions))


#TODO: Spirograph


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()
