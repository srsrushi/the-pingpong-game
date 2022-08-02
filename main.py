from turtle import Turtle
from turtle import Screen

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("The Ping-Pong Game")
screen.tracer(0)

paddle = Turtle()
paddle.color('white')
paddle.shape('square')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


is_game_on = True
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

while is_game_on:
    screen.update()

screen.exitonclick()
