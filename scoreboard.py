from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def write_score(self):
       self.score += 1
       self.clear()  # Clear previous score
       self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def new_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

