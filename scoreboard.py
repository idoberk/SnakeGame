from turtle import Turtle

SCORE_COLOR = "white"
SCORE_ALIGN = "center"
SCORE_FONT = ("Cambria", 24, "normal")
SCORE_COORDS = [-20, 260]


class ScoreBoard(Turtle):

    def __init__(self):
        """ScoreBoard class constructor."""
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.pencolor(SCORE_COLOR)
        self.penup()
        self.hideturtle()
        self.goto(x = SCORE_COORDS[0], y = SCORE_COORDS[1])
        self.update_score_board()

    def update_score_board(self):
        """Updates the scoreboard."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = SCORE_ALIGN, font = SCORE_FONT)

    def increase_score(self):
        """Increases the score by 1."""
        self.score += 1
        self.update_score_board()

    def reset_score(self):
        """Set high-score if it's higher than current score and reset score."""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score_board()