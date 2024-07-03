from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
WIDTH = [2]
LEN = [3,4,5]

class Cubics(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cubics = []
        start_x = -320  # Starting x position (left side of the screen)
        start_y = 250  # Starting y position (near the top of the screen)
        x_spacing = 70  # Horizontal spacing between turtles
        y_spacing = 50  # Vertical spacing between rows
        rows = 7
        columns = 10

        for row in range(rows):
            for col in range(columns):

                c = Turtle()
                c.shape("square")
                c.shapesize(stretch_wid=random.choice(WIDTH),stretch_len=random.choice(LEN))
                c.color("white")
                c.begin_fill()
                c.fillcolor(random.choice(COLORS))
                c.penup()
                x = start_x + col * x_spacing
                y = start_y - row * y_spacing
                c.goto(x,y)
                self.all_cubics.append(c)






