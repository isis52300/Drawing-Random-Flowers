import turtle
from turtle import Turtle
import random

window = turtle.Screen()


class Flower(Turtle):

    def set(turtle, x, y):
        turtle.pencolor("black")
        turtle.pensize(2)
        turtle.hideturtle()
        turtle.penup()
        turtle.setx(x)
        turtle.sety(y)

    def draw(turtle, color):
        x = 0
        turtle.begin_fill()
        turtle.fillcolor(color)
        turtle.setheading(0)
        while x < 9:
            turtle.pendown()
            turtle.forward(100)
            turtle.right(160)
            x += 1
        turtle.end_fill()
        turtle.penup()
        turtle.right(20)
        turtle.forward(53)
        turtle.right(70)
        turtle.forward(13)
        turtle.pendown()
        turtle.forward(100)


pen = Flower()
pen.set(100, 100)
pen.draw("blue")
new = Flower()
new.set(-100, -100)
new.draw("yellow")
pen.set(200, -150)
pen.draw("pink")
new.set(-200, 200)
new.draw("red")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

this = 0
while this <= 10:
    weird = Flower()
    weird.set(random.randint(-300, 300), random.randint(-300, 300))
    weird.draw(colors[random.randint(0, 6)])
    this += 1


window.exitonclick()
