import turtle

window = turtle.Screen()
logo = turtle.Turtle()

logo.penup()
logo.goto(-180, 0)  # Adjust position as needed
logo.pendown()
logo.color("blue")  # Set a valid color
logo.penup()
logo.goto(-180, 0)  # Adjust the position as needed
logo.write("Disnepland", font=("Waltograph", 80, "normal"))

logo.penup()
logo.goto(70, -10)  # Adjust position as needed
logo.pendown()
logo.color("blue")  # Set a valid color
logo.penup()
logo.goto(70, -10)  # Adjust the position as needed
logo.write("P A R I S", font=("Calibri", 20, "bold"))

turtle.done()


