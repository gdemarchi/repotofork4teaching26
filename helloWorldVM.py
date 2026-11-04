#Created by Viktoria Myhsok

import turtle

x = turtle.Turtle()
x.penup()
x.goto(0,60)
x.write("Jeder der nichts weiß, malt nen Kreis", align = "center", font = ("Comic Sans MS", 20, "normal"))

x.penup()
x.goto(0,-130)
x.pendown()
x.circle(90)

x.penup()
x.goto(35, 0)
x.setheading(0)
x.pendown()
x.circle(10)

x.penup()
x.goto(35, 10)
x.dot(8, "black")

x.penup()
x.goto(-35, 0)
x.setheading(0)
x.pendown()
x.circle(10)

x.penup()
x.goto(-35, 10)
x.dot(8, "black")

x.penup()
x.goto(-60, -50)
x.setheading(270)
x.pendown()
x.circle(60, 180)

x.penup()
x.goto(-60, -50)
x.setheading(0)
x.pendown()
x.forward(120)
x.penup()

x.hideturtle()
turtle.done()

print("Good Night!")