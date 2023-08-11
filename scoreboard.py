from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setpos(0, 270)
        self.color("white")
        self.score = 0
        with open("DATA.TXT") as file:
            contents = int(file.read())
        self.high_score = contents
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}      High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("DATA.TXT", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGN, font=FONT)

    def inc_score(self):
        self.score += 1
        self.update_scoreboard()
