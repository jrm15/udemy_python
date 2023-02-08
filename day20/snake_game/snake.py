from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_snake = Turtle()
            new_snake.shape("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.snakes.append(new_snake)

    def move(self):
        for seg in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg - 1].xcor()
            new_y = self.snakes[seg - 1].ycor()
            self.snakes[seg].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)