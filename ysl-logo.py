import turtle

window = turtle.Screen()
logo = turtle.Turtle()

# Y
logo.penup()
logo.goto(-40, 80)  # Adjust position as needed
logo.pendown()
logo.color("black")  # Set a valid color
logo.penup()
logo.goto(-50, 80)  # Adjust the position as needed
logo.write("Y", font=("Vera Humana 95", 170, "normal"))

# S
logo.penup()
logo.goto(-50, 0)  # Adjust position as needed
logo.pendown()
logo.color("black")  # Set a valid color
logo.penup()
logo.goto(-50, 0)  # Adjust the position as needed
logo.write("s", font=("Vera Humana 95", 250, "normal"))

# L
logo.penup()
logo.goto(-10, -30)  # Adjust position as needed
logo.pendown()
logo.color("black")  # Set a valid color
logo.penup()
logo.goto(-10, -30)  # Adjust the position as needed
logo.write("L", font=("Vera Humana 95", 170, "normal"))

logo.penup()
logo.goto(-200, -50)  # Adjust position as needed
logo.pendown()
logo.color("black")  # Set a valid color
logo.penup()
logo.goto(-200, -50)  # Adjust the position as needed
logo.write("Yves Saint Laurent", font=("Vera Humana 95", 40, "normal"))

turtle.done()