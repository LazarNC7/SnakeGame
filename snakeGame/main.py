from distutils.command import check
from random import gauss
from turtle import Screen
import time
from snakeGameClass import Snake
from food import Food
from scoreboard import Scoreboard

def checkCollisionWall():
    return snake.snake[0].xcor() > 290 or snake.snake[0].xcor() < -290 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -290
        

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

def createSnake():
    snake=[]
    for index in range(3):
        snake.append(Snake(index))

    return snake

score=0

snake=Snake()
food=Food()
score_board=Scoreboard(score)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.moveSnake()

    # Collision with food
    
    
    if snake.snake[0].distance(food) < 15:
        food.refresh()
        score+=1
        score_board.refreshScore(score)
        snake.newSegment()

    # Collision with wall

    if checkCollisionWall():
        game_is_on=False
        score_board.gameOver()

    # Collision with tail
    head=snake.snake[0]
    for seg in snake.snake[1:]:
        
        if head.distance(seg) < 10:
            game_is_on=False
            score_board.gameOver()

screen.exitonclick()