import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("THE SNAKE GAME")
screen.tracer(0)

snake = Snake()

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()









screen.exitonclick()