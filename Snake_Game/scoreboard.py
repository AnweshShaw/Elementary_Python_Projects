from turtle import Turtle
ALIGN= "center"
FONT = "Arial,20,normal"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Inheritance in Python
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        # noinspection PyTypeChecker
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        # noinspection PyTypeChecker
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()