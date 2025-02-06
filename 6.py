from turtle import *
screensize(10000, 10000)
tracer(1)
k = 5
pensize(4)
left(90)
down()
for i in range(3):
    forward(45 * k)
    right(90)
    forward(13 * k)
    right(90)
up()
forward(-2 * k)
right(90)
forward(4 * k)
left(90)
down()
for i in range(4):
    forward(76 * k)
    right(90)
    forward(72 * k)
    right(90)
up()

for i in range(-200, 200):
    for j in range(-200, 200):
        goto(i * k, j * k)
        dot(4, 'red')

