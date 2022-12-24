"""
 # @ Author: Abdou Lahi DIOP
 # @ Create Time: 2022-12-24 20:57:46
 # @ Modified by: Abdou Lahi DIOP
 # @ Modified time: 2022-12-24 21:00:49
 # @ Description:
 """

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(50)


screen.listen()
screen.onkey(fun=move_forward, key="space")
screen.exitonclick()
