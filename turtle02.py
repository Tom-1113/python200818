import turtle
a = turtle.Turtle()

s = turtle.Screen()
s.title("zodkeofji")
s.bgcolor("cyan")

a.pensize(5)
a.color("green")
a.shape("turtle")
a.back(100)
i=0

while i<360:
    a.forward(1)
    a.left(1)
    i=i+1
turtle.done()