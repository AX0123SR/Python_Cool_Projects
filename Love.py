import time
from turtle import *

import turtle

pen = turtle.Turtle()

color("red")
begin_fill()
left(40)
forward(138)

circle(80,180)
left(280)
circle(80,180)
forward(138)
end_fill()
pen.up()

# Move turtle to a given position
pen.setpos(-52, 120)
pen.write("I Love you", font=("Verdana", 14, "bold"))
time.sleep(6)
done