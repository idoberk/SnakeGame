from turtle import Turtle

SCORE_COLOR = "white"
SCORE_ALIGN = "center"
SCORE_FONT = ("Cambria", 24, "normal")
SCORE_COORDS = [-20, 260]


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor(SCORE_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(x = SCORE_COORDS[0], y = SCORE_COORDS[1])
        self.update_score_board()

    def update_score_board(self):
        self.write(arg = f"Score: {self.score}", move = False, align = SCORE_ALIGN, font = SCORE_FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score_board()

    def game_over(self):
        self.goto(x = 0, y = 0)
        self.write(arg = "GAME OVER", align = SCORE_ALIGN, font = SCORE_FONT)