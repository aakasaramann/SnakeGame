from turtle import Turtle
STARTING_SCORE = 0
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total_score = STARTING_SCORE
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"Score: {self.total_score}", align=ALIGNMENT, font=FONT)

    def update_score(self, current_score):
        self.write(f"Score: {current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.total_score += 1
        self.clear()
        self.update_score(self.total_score)
