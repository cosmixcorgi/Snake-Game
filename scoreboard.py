from turtle import Turtle

SCORE_FONT = ("Arial", 16, "bold")
GAMEOVER_FONT = ("Arial", 40, "bold")
SUB_FONT = ("Arial", 16, "normal")
HINT_FONT = ("Arial", 11, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('#39FF14')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 305)
        self.write(f"SCORE  {self.score:03d}     BEST  {self.high_score:03d}",
                   align="center", font=SCORE_FONT)

    def game_over(self):
        overlay = Turtle()
        overlay.hideturtle()
        overlay.penup()
        overlay.color('#FF073A')
        overlay.goto(0, 40)
        overlay.write("GAME OVER", align="center", font=GAMEOVER_FONT)
        overlay.goto(0, -10)
        overlay.color('#FFFFFF')
        overlay.write(f"Score: {self.score}", align="center", font=SUB_FONT)
        overlay.goto(0, -45)
        overlay.color('#666666')
        overlay.write("click to exit", align="center", font=HINT_FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()
