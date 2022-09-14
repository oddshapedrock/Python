import turtle
#accepts arguments (x pos, y pos, witdth, and color)
#draws a square
def square(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()

#accepts arguments (x pos, y pos, radius, and color)
#draws a circle
def circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
 
#accepts arguments (x pos, y pos, x pos, y pos, and color)
#draws a line
def line(startX, startY, endX, endY, color):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(endX, endY)