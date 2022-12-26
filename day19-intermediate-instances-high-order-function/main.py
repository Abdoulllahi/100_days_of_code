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



def move_backward():
    tim.backward(50)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# screen.listen()
# screen.onkey(fun=move_forward, key="space")
# screen.exitonclick()

#TODO: Z = Forwards, B = Backwards, A = Counter-Clockwise, D = Clockwise, C = Clear Drawing

screen.listen()
screen.onkey(fun=move_forward, key="z")
screen.onkey(fun=move_backward, key="b")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clear, key="c")
screen.exitonclick()