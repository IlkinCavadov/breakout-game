from turtle import Turtle

FONT = ("Courier", 24, "normal")

class TryCount(Turtle):
    def __init__(self):
        super().__init__()
        self.try_number = 4
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(280, 270)
        self.update_try()

    def update_try(self):
        self.clear()
        self.write(f"Try: {self.try_number}", align="left", font=FONT)


    def decrease_try(self):
        self.try_number -=1
        self.update_try()