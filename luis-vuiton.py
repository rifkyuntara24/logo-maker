import turtle

window = turtle.Screen()
logo = turtle.Turtle()

logo.penup()
logo.goto(-80, -20)  # Adjust position as needed
logo.pendown()
logo.color("black")  # Set a valid color
logo.penup()
logo.goto(-80, -20)  # Adjust the position as needed
logo.write("L", font=("Courier", 200, "normal"))

logo.penup()
logo.goto(-90, 20)  # Adjust position as needed
logo.pendown()
logo.color("black")  # Set a valid color
logo.penup()
logo.goto(-90, 20)  # Adjust the position as needed
logo.write("V", font=("Courier", 180, "normal"))

logo.penup()
logo.goto(-90, 20)  # Adjust position as needed
logo.pendown()
logo.color("black")  # Set a valid color
logo.penup()
logo.goto(-90, 20)  # Adjust the position as needed
logo.write("LOUIS VUITTON", font=("Sans Serif", 20, "normal"))

turtle.done()
