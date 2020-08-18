import turtle
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
i = 0
c.right(90)
d.right(90)
while i<360:
    a.forward(1)
    a.left(1)
    b.forward(1)
    b.right(1)
    i=i+1
    c.forward(1)
    c.left(1)
    d.forward(1)
    d.right(1)
