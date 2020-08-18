import turtle
a = turtle.Turtle()
a.shape("turtle")
s = int(input('side'))
n = 360/s
for i in range(s):
    a.forward(100)
    a.left(n)
turtle.done()