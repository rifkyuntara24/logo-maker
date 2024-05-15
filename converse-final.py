import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("white")

# Create a turtle to draw the my_turtle
logo_turtle = turtle.Turtle()
logo_turtle.speed(1)

# Draw the star
logo_turtle.penup()
logo_turtle.goto(-40, 0)
logo_turtle.pendown()
logo_turtle.fillcolor("black")
logo_turtle.begin_fill()

# Set the initial heading
logo_turtle.setheading(-20)  # Change this value to adjust the initial angle

for i in range(5):
    logo_turtle.forward(40)  # Change this line to adjust the size of the star
    logo_turtle.right(144)
    logo_turtle.forward(40)  # And this one
    logo_turtle.left(72)
logo_turtle.end_fill()


def draw_parallelogram(turtle, x, y, heading, length1, length2, angle):
    # Move the turtle to the specified coordinate and set its heading
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.pendown()

    # Start filling the color
    turtle.begin_fill()

    # Draw a parallelogram
    for i in range(2):
        turtle.forward(length1)
        turtle.left(angle)
        turtle.forward(length2)
        turtle.left(180 - angle)

    # End filling the color
    turtle.end_fill()

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
my_turtle = turtle.Turtle()

# Set the fill color to black
my_turtle.fillcolor("black")

# Draw two parallelograms
draw_parallelogram(my_turtle, 200, -10, 150, 160, 100, 30)
draw_parallelogram(my_turtle, 100, -10, -150, 160, 100, 150)  # Mirrored parallelogram

my_turtle.penup()
my_turtle.goto(-150, -190)  # Adjust position as needed
my_turtle.pendown()
my_turtle.color("black")  # Set a valid color
my_turtle.penup()
my_turtle.goto(-150, -190)  # Adjust the position as needed
my_turtle.write("CONVERSE", font=("Futura", 40, "bold"))

# Hide the turtle and display the result
logo_turtle.hideturtle()
turtle.done()
