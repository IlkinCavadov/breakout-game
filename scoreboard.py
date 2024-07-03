from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-250, 270)
        self.update_scoreboard()
        #self.update_try()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="right", font=FONT)



    def increase_score(self):
        self.score += 10
        self.update_scoreboard()



    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over\n Your score : {self.score}", align="center", font=FONT)