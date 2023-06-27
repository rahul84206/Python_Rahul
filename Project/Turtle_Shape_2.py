import turtle
import colorsys
turtle.Screen().bgcolor('black')
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
h = 0
t.penup()
t.goto(90, 0)
t.pendown()
for i in range(100):
    t.width(i//100+1)
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)

    t.left(119)
    t.circle(120, 60)
    t.right(89)
    t.penup()
    t.forward(i*2)
    t.pendown()

    h += 0.5
turtle.done()
