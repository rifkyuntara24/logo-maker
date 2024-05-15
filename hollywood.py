import turtle

window = turtle.Screen()
logo = turtle.Turtle()

logo.penup()
logo.goto(-180, 0)  # Adjust position as needed
logo.pendown()
logo.color("black")  # Set a valid color
logo.penup()
logo.goto(-180, 0)  # Adjust the position as needed
logo.write("HOLLYWOOD", font=("SF Hollywood Hills", 70, "bold"))

turtle.done()

