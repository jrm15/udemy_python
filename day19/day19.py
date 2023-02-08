from turtle import Turtle, Screen


tommy = Turtle()
tommy.shape("turtle")
tommy.color("cyan")


def forw():
    tommy.forward(50)
def ret():
    tommy.back(50)
def clock():
    tommy.right(10)
def count_clock():
    tommy.left(10)
def clear():
    tommy.clear()
    tommy.penup()
    tommy.home()
    tommy.pendown()


my_screen = Screen()
# accedemos a un atributo del objeto:
print(my_screen.canvheight)
# Se pueden pasar funciones como argumento de otras funciones (SIN PARENTESIS AL FINAL):
my_screen.onkey(fun = forw, key = "W")
my_screen.onkey(fun = ret, key = "S")
my_screen.onkey(fun = count_clock, key = "A")
my_screen.onkey(fun = clock, key = "D")
my_screen.onkey(fun = clear, key = "C")
my_screen.listen()
# ahora accedemos a un metodo del objeto:
my_screen.exitonclick()
