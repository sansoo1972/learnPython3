import turtle
#create window and turtle
window = turtle.Screen()
babbage = turtle.Turtle()

#draw stem an center
babbage.color("green", "black")
babbage.left(90)
babbage.forward(100)
babbage.right(90)

#draw center
babbage.color("black", "black")
babbage.begin_fill()
babbage.circle(10)
babbage.end_fill()

#draw all petal
for i in range (1,24):
    if babbage.color() == ("red", "black"):
        babbage.color("blue", "black")
    elif babbage.color() == ("blue", "black"):
        babbage.color("purple", "black")
    else:
        babbage.color("red", "black")
    babbage.left(15)
    babbage.forward(50)
    babbage.left(157)
    babbage.forward(50)
#hide the turtle
babbage.hideturtle()
#tidy up window
window.exitonclick()
