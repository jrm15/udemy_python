from turtle import Turtle, Screen
from colors_turtle import colors

tommy = Turtle()
tommy.shape("turtle")
tommy.color("cyan")

#FORM 1:
# for _ in range(4):
#     tommy.forward(100)
#     tommy.left(90)
#
# tommy.right(90)
# for _ in range(10):
#     tommy.forward(10)
#     tommy.penup()
#     tommy.forward(10)
#     tommy.pendown()

#FORM 2:
# i = 3
# b = 0
# angle = float(0)
# while i != 9:
#     tommy.color(colors[b])
#     angle = 360/i
#     for _ in range(i):
#         tommy.forward(100)
#         tommy.right(angle)
#     i += 1
#     b += 1

#FORM 3:
# import random
# angles = [0, 90, 180, 270]
# tommy.shape("classic")
# while True:
#     i = int(random.randrange(0, 4))
#     tommy.color(colors[i])
#     tommy.right(angles[i])
#     tommy.forward(10)




my_screen = Screen()
# accedemos a un atributo del objeto:
print(my_screen.canvheight)
# ahora accedemos a un metodo del objeto:
my_screen.exitonclick()
