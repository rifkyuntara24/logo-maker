import turtle

def draw_triangle(x, y, heading):
    # Create a new turtle screen and set its background color
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a new turtle object
    t = turtle.Turtle()

    # Move the turtle to the specified coordinates
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Set the heading of the turtle
    t.setheading(heading)

    # Start filling with black color
    t.fillcolor("black")
    t.begin_fill()

    # Draw a triangle with two longer sides and a shorter base
    t.forward(20)  # Draw shorter base
    t.left(95)  # Turn left by the specified angle
    t.forward(150)  # Draw first longer side
    t.left(173)  # Turn left by the specified angle
    t.forward(150)  # Draw second longer side

    # End filling
    t.end_fill()


# Call the function with your desired parameters
draw_triangle(-110, 10, 20)
draw_triangle(-90, 20, 10)
draw_triangle(-70, 25, 0)
draw_triangle(-50, 25, -10)
draw_triangle(-30, 20, -20)


def draw_ellipse(x, y, angle, color, pensize, radius1, radius2):
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
draw_ellipse(-110, 0, 45, "black", 5, 70, 15)

# Draw the second ellipse
draw_ellipse(-90, -5, 0, "white", 8, 40, 12.5)

def draw_filled_circle(x, y):
    # Move the turtle to the specified coordinates
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Set the fill color
    turtle.fillcolor("black")

    # Start filling color
    turtle.begin_fill()

    # Draw a circle with the specified radius
    turtle.circle(10)

    # End filling color
    turtle.end_fill()

# Draw 5 filled circles at different coordinates
draw_filled_circle(-165, 150)
draw_filled_circle(-120, 170)
draw_filled_circle(-70, 175)
draw_filled_circle(-25, 175)
draw_filled_circle(20, 155)

my_turtle.penup()
my_turtle.goto(-200, -130)  # Adjust position as needed
my_turtle.pendown()
my_turtle.color("black")  # Set a valid color
my_turtle.penup()
my_turtle.goto(-200, -130)  # Adjust the position as needed
my_turtle.write("ROLEX", font=("RoundslabSerif", 70, "bold"))


# Hide the turtle
my_turtle.hideturtle()

# Keep the window open
turtle.done()