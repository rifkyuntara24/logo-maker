import turtle

def draw_pyramid(x, y, size):
    # Create a turtle named "Pyramid"
    pyramid = turtle.Turtle()
    pyramid.color("black")
    pyramid.speed(5)

    # Draw a pyramid silhouette
    pyramid.penup()
    pyramid.goto(x, y)
    pyramid.pendown()
    pyramid.begin_fill()
    for _ in range(3):
        pyramid.forward(size)  # Base of the pyramid
        pyramid.left(120)
    pyramid.end_fill()

    # Hide the turtle
    pyramid.hideturtle()

def draw_separator(x, y, length, angle):
    # Create a turtle named "Separator"
    separator = turtle.Turtle()
    separator.color("white")
    separator.penup()
    separator.goto(x, y)
    separator.right(angle)
    separator.pendown()
    
    # Make the separator line thicker
    separator.pensize(7)
    
    separator.forward(length)

    # Hide the separator turtle
    separator.hideturtle()


# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")

# Call the function to draw pyramids
draw_pyramid(-100, 0, 200)
draw_pyramid(20, 5, 160)

# Call the function to draw the separator with a specific angle
draw_separator(60, 70, 100, 60)


letter = turtle.Turtle()
letter.penup()
letter.goto(-50, -50)  # Adjust position as needed
letter.pendown()
letter.color("black")  # Set a valid color
letter.penup()
letter.goto(-50, -50)  # Adjust the position as needed
letter.write("PYRAMIDS", font=("Calibri", 30, "bold"))

# Keep the window open until it's clicked
wn.exitonclick()
