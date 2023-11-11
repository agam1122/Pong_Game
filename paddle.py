from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed('fastest')
        self.goto(x_position, y_position)
        self.color("white")

    def move_up(self):
        y_position = self.ycor()
        self.goto(x=self.xcor(), y=y_position + 80)
        y_position += 20

    def move_down(self):
        y_position = self.ycor()
        self.goto(x=self.xcor(), y=y_position - 80)
        y_position += 20
