from turtle import Turtle, Screen
import random


def fw(turtle):
    z = int(random.randrange(5, 21))
    turtle.forward(z)


t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()

screen = Screen()
screen.setup(500, 400)
winner = screen.textinput("RACE", "Choose a colour: ")

colors = ["red", "blue", "yellow", "orange", "purple", "green"]
turtles = [t1, t2, t3, t4, t5, t6]

x = -240
y = 190
for turtle, color in zip(turtles, colors):
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(color)
    turtle.goto(x=x, y=y)
    y = y-70


color_winner = ''
while x <= 250:
    for turtle in turtles:
        fw(turtle)
        x = turtle.xcor()
        if x >= 250:
            color_winner = turtle.pencolor()
            break


if winner == color_winner:
    print(f'YOU WIN, the winner was the {color_winner} turtle.')
else:
    print(f'YOU LOOSE, the winner was the {color_winner} turtle.')


screen.bye()