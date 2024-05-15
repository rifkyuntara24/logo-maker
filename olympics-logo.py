import turtle

# object tr for turtle
tr = turtle.Turtle()

# set thickness for each ring
tr.pensize(5)

def draw_ring(color, x, y):
    tr.color(color)
    tr.penup()
    tr.goto(x, y)
    tr.pendown()
    tr.circle(45)

# Draw the Olympic rings with overlap
draw_ring("blue", -110, -25)
draw_ring("black", 0, -25)
draw_ring("red", 110, -25)
draw_ring("yellow", -55, -75)
draw_ring("green", 55, -75)

# Redraw some parts of the rings to create the illusion of interlocking
tr.penup()
tr.goto(-55, -75)
tr.pendown()
tr.color("yellow")
tr.circle(45, 180)

tr.penup()
tr.goto(55, -75)
tr.pendown()
tr.color("green")
tr.circle(45, 180)

tr.hideturtle()
turtle.done()
