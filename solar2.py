import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System Simulation")

# Draw the Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(2.5, 2.5)

# Planet data (distance from sun, size, speed, color)
planets = [
    {"name": "Mercury", "distance": 50, "size": 0.5, "speed": 0.04, "color": "gray"},
    {"name": "Venus", "distance": 70, "size": 0.8, "speed": 0.03, "color": "orange"},
    {"name": "Earth", "distance": 100, "size": 1, "speed": 0.02, "color": "blue"},
    {"name": "Mars", "distance": 150, "size": 0.9, "speed": 0.015, "color": "red"},
    {"name": "Jupiter", "distance": 200, "size": 2, "speed": 0.01, "color": "brown"},
    {"name": "Saturn", "distance": 250, "size": 1.7, "speed": 0.007, "color": "gold"},
    {"name": "Uranus", "distance": 300, "size": 1.5, "speed": 0.005, "color": "lightblue"},
    {"name": "Neptune", "distance": 350, "size": 1.5, "speed": 0.004, "color": "blue"},
]

# Create turtles for each planet
planet_turtles = []
for planet in planets:
    planet_turtle = turtle.Turtle()
    planet_turtle.shape("circle")
    planet_turtle.color(planet["color"])
    planet_turtle.shapesize(planet["size"], planet["size"])
    planet_turtle.penup()
    planet_turtle.goto(planet["distance"], 0)
    planet_turtles.append({"turtle": planet_turtle, "angle": 0, "distance": planet["distance"], "speed": planet["speed"]})

# Animate the planets in their orbits
while True:
    for planet_data in planet_turtles:
        # Update angle for the planet's orbit
        planet_data["angle"] += planet_data["speed"]
        angle_rad = math.radians(planet_data["angle"])

        # Update the planet's position
        x = planet_data["distance"] * math.cos(angle_rad)
        y = planet_data["distance"] * math.sin(angle_rad)
        planet_data["turtle"].goto(x, y)

# Close the window on click
turtle.done()