import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from cubics import Cubics
from  scoreboard import Scoreboard
from try_count import TryCount


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -270))
ball = Ball()
cubics = Cubics()
scoreboard = Scoreboard()
try_count= TryCount()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")
game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    #Detect bounce with wall

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()


    elif ball.ycor() < -280:
        ball.reset_position()
        try_count.decrease_try()


    elif ball.ycor() > 280:
        ball.bounce_y()

        # Detect bounce with paddle
    if ball.distance(paddle) < 100 and ball.ycor() < -250:
        ball.bounce_y()

    #if ball.distance(cubics) < 25:
    for c in cubics.all_cubics:
        if ball.distance(c) < 25:

            c.hideturtle()
            cubics.all_cubics.remove(c)
            scoreboard.increase_score()
            ball.bounce_y()

    if try_count.try_number == 0:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()