import turtle

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
logo = turtle.Turtle()

# Draw the 'citi' text
logo.penup()
logo.goto(-100, -30)
logo.pendown()
logo.color("blue")
logo.write("CITI", font=("Arial", 80, "normal"))

# Draw the arc
logo.penup()
logo.goto(0, 90)
logo.pendown()
logo.color("red")
logo.width(10)
logo.left(90)
for _ in range(180):
    logo.forward(1)
    logo.right(1)

# Hide the turtle and display the result
logo.hideturtle()
turtle.done()


