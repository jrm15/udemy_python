from turtle import Turtle
#tomy = turtle.Turtle()
import turtle
# importamos del modulo turtle la clase Turtle ya creada en el
# esto es igual que:

from turtle import Turtle, Screen
tommy = Turtle()
# llamamos a un metodo de la clase y definimos lo necesario para que actue:
tommy.shape("turtle")
tommy.color("cyan")
print(tommy.position())
tommy.forward(100)
print(tommy.position())


my_screen = Screen()
# accedemos a un atributo del objeto:
print(my_screen.canvheight)
# ahora accedemos a un metodo del objeto:
my_screen.exitonclick()

