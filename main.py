from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1200, height=800)
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle(-550, 0)

right_paddle = Paddle(550, 0)

game_over = Turtle()
ball = Ball()
score = Score()

screen.listen()

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")


is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.wall_bounce()

    # detect collision with right paddle
    if ball.distance(right_paddle) <= 60 and ball.xcor() > 530:
        ball.paddle_bounce()

    # detect collision with left paddle
    if ball.distance(left_paddle) <= 60 and ball.xcor() < -530:
        ball.paddle_bounce()

    # detect right paddle miss
    if ball.xcor() >= 620:
        score.increase_left_score()
        ball.hideturtle()
        ball.reset_position()
        ball.showturtle()

    # detect left paddle miss
    if ball.xcor() <= -620:
        score.increase_right_score()
        ball.hideturtle()
        ball.reset_position()
        ball.showturtle()

screen.exitonclick()
