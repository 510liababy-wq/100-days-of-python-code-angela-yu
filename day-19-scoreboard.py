from turtle import Turtle
FONT = ("Courier New", 25, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-50, 260)
        self.score = 0
        self.color("PaleVioletRed1")
        self.write(f"Score: {self.score} ", font=FONT)

    def game_over(self):
        self.goto(-40,0)
        self.write(f"GAME OVER", font=FONT)


    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ", font=FONT)
