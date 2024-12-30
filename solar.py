import turtle
import math
from math import *

screen = turtle.Screen()  # Creating the screen
screen.tracer(10)  # Set to 10 for smoother animation (adjust as needed)
sun = turtle.Turtle()  # Turtle object for sun
sun.shape('circle')  # Shape of sun
sun.color('yellow')  # Color of sun

class Planet(turtle.Turtle):
    def __init__(self, name, radius, color):  # Initialize function
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()  # Use penup() instead of pd()
        self.angle = 0

    def move(self):
        x = self.radius * cos(self.angle)  # Angle in radians
        y = self.radius * sin(self.angle)
        self.goto(sun.xcor() + x, sun.ycor() + y)  # Moving to calculated coordinates

# Creating planets
mercury = Planet("Mercury", 40, 'grey')
venus = Planet("Venus", 80, 'orange')
earth = Planet("Earth", 100, 'blue')
mars = Planet("Mars", 150, 'red')
jupiter = Planet("Jupiter", 180, 'brown')
saturn = Planet("Saturn", 230, 'pink')
uranus = Planet("Uranus", 250, 'light blue')
neptune = Planet("Neptune", 280, 'black')

# Adding planets to a list
myList = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Main animation loop
while True:
    screen.update()  # Updating the screen
    for planet in myList:
        planet.move()  # Moving each planet in the list

    # Increase each planet's angle to simulate orbiting
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007
    jupiter.angle += 0.02
    saturn.angle += 0.018
    uranus.angle += 0.016
    neptune.angle += 0.005

# Keep the window open
turtle.mainloop()  # Add this line to keep the window open
