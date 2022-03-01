import time
from turtle import *
from PIL import Image
import turtle

pen = turtle.Turtle()

color("red")
begin_fill()
left(40)
forward(150)

circle(90,180)
left(280)
circle(90,180)
forward(150)
end_fill()
pen.up()

# Move turtle to a given position
pen.setpos(-120,120)
pen.write("Happy marriage anniversary \n", font=("Helvetica", 14, "bold"))
pen.write("           Mom and Dad ", font=("Helvetica", 14, "bold"))
time.sleep(6)
img = Image.open("Pic1.jpg")
print(img.size)
img.show()

