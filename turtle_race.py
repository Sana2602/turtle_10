import turtle
import random

# Create the turtles
turtles = []
colors = ["red", "blue", "green", "orange", "purple", "pink", "yellow"]
for i in range(7):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-200, 100 - i * 30)
    t.pendown()
    turtles.append(t)

# Move the turtles
for i in range(100):
    for t in turtles:
        t.forward(random.randint(1, 5))

# Determine the winner
winner = turtles[0]
for t in turtles:
    if t.xcor() > winner.xcor():
        winner = t

# Print the winner
print("The winner is the", winner.color()[0], "turtle!")
