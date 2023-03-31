from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

velocity = 5
rotation_velocity = 5

def move_forwards():
    tim.forward(velocity)

def move_backwards():
    tim.backward(velocity)

def clear():
    screen.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def rotate_left():
    tim.left(rotation_velocity)

def rotate_right():
    tim.right(rotation_velocity)

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=rotate_left)
screen.onkeypress(key="d", fun=rotate_right)
screen.onkey(key="c", fun=clear)
screen.mainloop()