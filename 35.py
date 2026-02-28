import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(400,300)
polygon=turtle.Turtle()
num_sides=6
sidelength=70
angle=360/num_sides
for i in range(num_sides):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()    