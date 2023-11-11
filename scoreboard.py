from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.goto(-50, 340)
        self.color('white')
        self.write(arg=f'Score\n {self.left_score} : {self.right_score}', font=('Arial', 24, 'normal'))

    def increase_left_score(self):
        self.clear()
        self.left_score += 1
        self.write(arg=f'Score\n {self.left_score} : {self.right_score}', font=('Arial', 24, 'normal'))

    def increase_right_score(self):
        self.clear()
        self.right_score += 1
        self.write(arg=f'Score\n {self.left_score} : {self.right_score}', font=('Arial', 24, 'normal'))
