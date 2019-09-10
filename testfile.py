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
babbage.circle(10)
#draw all petal
for i in range (1,24):
    babbage.left(15)
    babbage.forward(50)
    babbage.left(157)
    babbage.forward(50)
#tidey up window
window.exitonclick()