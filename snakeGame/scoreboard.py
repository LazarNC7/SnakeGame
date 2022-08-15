from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, score, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__()
        
        self.refreshScore(score)

    def refreshScore(self, score):
        self.reset()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,280)
        self.write(f"Score: {score}", move=False, align="center", font=('Arial', 13, 'bold'))

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=('Arial', 13, 'bold'))