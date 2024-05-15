import turtle

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("blue")

# Create a new turtle object for the lines
t = turtle.Turtle()

# Set the line color
t.color("red")

# Set the line width
t.width(10)

# Draw four vertical lines
for i in range(1, 5):
    t.penup()
    t.goto(i*100 - 200, -100)
    t.pendown()
    t.goto(i*100 - 200, 300)

# Draw one horizontal line
t.penup()
t.goto(-200, 100)
t.pendown()
t.goto(400, 100)

# Create a new turtle object for the text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()  # Hide the turtle

# Set the text color
text_turtle.color("white")

# Add "UOB" to the right side of the logo
text_turtle.penup()
text_turtle.goto(400, 100)  # Adjust the position for the text
text_turtle.write("UOB", align="left", font=("Arial", 16, "normal"))

# Hide the turtle for the lines
t.hideturtle()

# Keep the window open
turtle.done()
