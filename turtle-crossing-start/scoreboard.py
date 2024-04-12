import turtle as t
FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.level =1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align="left", font=FONT)
    def inc_lv(self):
        self.level +=1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!!", align="left", font=FONT)