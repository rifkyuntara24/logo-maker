import turtle

def draw_figure(start_x, start_y, angle):
    # Create a new turtle screen and set its background color
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a new turtle object
    t = turtle.Turtle()

    # Move the turtle to the start position without drawing anything
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    # Set the heading angle
    t.setheading(angle)

    # Draw a rectangle
    t.fillcolor("blue")
    t.begin_fill()
    for _ in range(4):
        t.forward(100)  # Draw a side
        t.right(90)     # Turn right 90 degrees
    t.end_fill()

    # Draw a right triangle on top of the rectangle without a separating line
    t.fillcolor("blue")
    t.begin_fill()
    t.left(45)      # Turn left 45 degrees to align the base of the triangle with the rectangle
    t.forward(141)  # Draw hypotenuse
    t.right(135)    # Turn right 135 degrees
    t.forward(100)  # Draw height
    t.right(90)     # Turn right 90 degrees
    t.penup()       # Lift the pen to avoid drawing an extra line
    t.forward(100)  # Move to the start without drawing
    t.pendown()     # Put the pen down
    t.end_fill()

    # Hide the turtle and close the drawing
    t.hideturtle()

    # This line is needed to keep the window open
    

# Call the function to draw the figure at the specified coordinates and angle
draw_figure(-200, 50, 0)
draw_figure(10, 150, 270)
draw_figure(110, -60, 180)
draw_figure(-100, -160, 90)

turtle.done()