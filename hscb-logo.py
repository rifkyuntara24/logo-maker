import turtle

def draw_triangle(color, x, y, heading):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(heading)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for _ in range(3):
        turtle.forward(90)
        turtle.right(120)
    turtle.end_fill()

def draw_hsbc_logo():
    turtle.speed(3)

    # Draw the red triangles
    draw_triangle("red", -90, -70, 90)  # Facing east
    draw_triangle("red", 100, 20, 270)  # Facing west
    draw_triangle("red", -40, 60, 0)  # Facing north
    draw_triangle("red", 50, -110, 180)  # Facing south

    # # Draw the white triangles
    # draw_triangle("white", 50, 0, 60)  # Facing north
    # draw_triangle("white", -50, 0, -60)  # Facing south

    turtle.hideturtle()  # Hide the turtle cursor
    turtle.done()  # Finish drawing

draw_hsbc_logo()
