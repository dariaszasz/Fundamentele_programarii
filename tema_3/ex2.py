import turtle

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

def herz():

    turtle.left(140)
    turtle.forward(113)

    curve()
    turtle.left(120)

    curve()

    turtle.forward(112)



herz()