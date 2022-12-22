import random
from turtle import Turtle, Screen


turtle = Turtle()


# turtle.hideturtle()
# for _ in range(25):
#     turtle.forward(5)
#     turtle.penup()
#     turtle.forward(5)
#     turtle.pendown()
# for _ in range(4):
#     turtle.forward(100)
#     turtle.left(90)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", 
           "SeaGreen"]
directions = [0, 90, 180, 270]

#TODO: draw differenr shapes
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

#TODO: random walk
turtle.pensize(10)
for _ in range(200):
    turtle.color(random.choice(colours))
    turtle.forward(30)
    turtle.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()   