
from turtle import Turtle,Screen

MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0



class Snake:
    def __init__(self) -> None:
        self.x_beggining=[0,-20,-40]
        
        self.snake=[]
        for index in range(3):
            newPart=self.segment()
            self.snake.append(newPart)

        self.length=3

    def segment(self):
        newPart=Turtle(shape="square")

        if len(self.snake) <= 2:
            newPart.goto(x=self.x_beggining[len(self.x_beggining)-1], y=0)

        else:
            newPart.goto(x=self.snake[-1].xcor(),y=self.snake[-1].ycor())
        
        newPart.penup()
        newPart.color("white")
        

        return newPart

    def newSegment(self):
        newPart=self.segment()
        self.snake.append(newPart)
        self.length+=1
 

    def moveSnake(self):
        
        for seg_num in range(self.length-1, 0, -1):
            new_x=self.snake[seg_num-1].xcor()
            new_y=self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x,new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake[0].heading()!=DOWN:
            self.snake[0].setheading(UP)
        # self.moveSnake()

    def down(self):
        if self.snake[0].heading()!=UP:
            self.snake[0].setheading(DOWN)
        # self.moveSnake()

    def left(self):
        if self.snake[0].heading()!=RIGHT:
            self.snake[0].setheading(LEFT)
        # self.moveSnake()

    def right(self):
        if self.snake[0].heading()!=LEFT:
            self.snake[0].setheading(RIGHT)
        # self.moveSnake()
        
        
        