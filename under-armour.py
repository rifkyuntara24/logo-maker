import turtle

def draw_sector(my_turtle, x, y, angle, radius):
    # Move the turtle to the specified coordinates without drawing anything
    my_turtle.penup()
    my_turtle.goto(x, y)
    my_turtle.pendown()

    # Rotate the turtle by the specified angle
    my_turtle.setheading(angle)

    # Start filling with color
    my_turtle.begin_fill()

    # Draw a quarter circle
    my_turtle.circle(radius, 90)

    # Draw the remaining part of the triangle
    my_turtle.left(90)
    my_turtle.forward(radius)
    my_turtle.left(90)
    my_turtle.forward(radius)

    # End filling with color
    my_turtle.end_fill()

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
my_turtle = turtle.Turtle()

# Set the pen size to make the line thicker
my_turtle.pensize(5)

# Set the fill color to black
my_turtle.fillcolor("black")

# Draw four sectors
draw_sector(my_turtle, -100, 0, 180, 70)
draw_sector(my_turtle, 100, -68, 90, 70)
draw_sector(my_turtle, -170, 75, 270, 70)
draw_sector(my_turtle, 30, 5, 0, 70)


def draw_ellipse(turtle, x, y, angle, color, pensize, radius1, radius2):
    # Set the fill color
    turtle.fillcolor(color)

    # Move the turtle to start position without drawing anything
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Rotate the turtle
    turtle.right(angle)

    # Start filling the shape
    turtle.begin_fill()

    # Draw the ellipse
    for _ in range(2):
        turtle.circle(radius1, 90)  # Draw the top half of the ellipse
        turtle.circle(radius2, 90)  # Draw the bottom half of the ellipse

    # End filling the shape
    turtle.end_fill()

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
my_turtle = turtle.Turtle()

# Increase the thickness of the turtle's pen
my_turtle.pensize(5)

# Draw the first ellipse
draw_ellipse(my_turtle, -110, 0, 45, "black", 5, 100, 15)

# Draw the second ellipse
draw_ellipse(my_turtle, -90, 0, 0, "white", 8, 70, 12.5)

my_turtle.penup()
my_turtle.goto(-250, -150)  # Adjust position as needed
my_turtle.pendown()
my_turtle.color("black")  # Set a valid color
my_turtle.penup()
my_turtle.goto(-250, -150)  # Adjust the position as needed
my_turtle.write("UNDER ARMOUR", font=("Futura", 40, "bold"))

# Hide the turtle
my_turtle.hideturtle()

# Keep the window open
turtle.done()
