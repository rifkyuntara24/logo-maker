import turtle


def sclalene_triangle(x, y, heading):
    # Create a new turtle screen and set its background color
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a new turtle object
    tri = turtle.Turtle()

    # Move the turtle to the specified coordinates
    tri.penup()
    tri.goto(x, y)
    tri.pendown()

    # Set the heading of the turtle
    tri.setheading(heading)

    # Start filling with black color
    tri.fillcolor("black")
    tri.begin_fill()

    # Draw a scalene triangle
    tri.forward(450)  # Draw base
    tri.left(165)     # Turn left 120 degrees
    tri.forward(300)  # Draw second side
    tri.left(43)     # Turn left 110 degrees
    tri.forward(180)  # Draw third side

    # End filling
    tri.end_fill()

sclalene_triangle(-200, 10, -25)

def right_triangle(x, y, heading):

    # Create a new turtle object
    tri = turtle.Turtle()

    # Move the turtle to the specified coordinates
    tri.penup()
    tri.goto(x, y)
    tri.pendown()

    # Set the heading of the turtle
    tri.setheading(heading)

    # Start filling with black color
    tri.fillcolor("black")
    tri.begin_fill()

    # Draw a scalene triangle
    tri.forward(250)  # Draw base
    tri.left(165)     # Turn left 120 degrees
    tri.forward(250)  # Draw second side
    tri.left(100)     # Turn left 110 degrees
    tri.forward(80)  # Draw third side

    # End filling
    tri.end_fill()

right_triangle(130, -90, 50)

import turtle

def draw_parallelogram(x, y, angle, base, side, heading):
    # Create a new turtle screen and set its background color
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a new turtle object
    t = turtle.Turtle()

    # Move the turtle to a new position without drawing anything
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(heading)

    # Start filling with black color
    t.fillcolor("black")
    t.begin_fill()

    # Draw a mirrored parallelogram
    for i in range(2):
        t.forward(base) # draw base
        t.left(angle) # turn left by the given angle
        t.forward(side) # draw side
        t.left(180 - angle) # turn left by 180 - angle

    # End filling
    t.end_fill()


# Call the function to draw a parallelogram at (-200, 0) with an angle of 60 degrees
draw_parallelogram(-170, -140, 50, 70, 130, -25)

draw_parallelogram(-80, -180, 50, 50, 130, -25)

turtle.penup()
turtle.goto(-200, 50)  # Adjust position as needed
turtle.pendown()
turtle.color("black")  # Set a valid color
turtle.penup()
turtle.goto(-200, 50)  # Adjust the position as needed
turtle.write("Reebok", font=("Mottek", 70, "bold"))


# Hide the turtle and close the turtle graphics window
turtle.hideturtle()
turtle.done()

