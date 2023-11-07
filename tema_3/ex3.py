import turtle

def house():

    #Quadrat
    turtle.penup()
    turtle.goto(-100,-100)
    turtle.pendown()
    for i in range(4):
        turtle.forward(200)
        turtle.left(90)

    #Dach=Dreieck
    turtle.penup()
    turtle.goto(-100,100)
    turtle.pendown()
    for i in range(3):
        turtle.forward(200)
        turtle.left(120)

    #Fenster
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)

    #Tür
    turtle.penup()
    turtle.goto(-40,-100)
    turtle.pendown()
    for i in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(80)
        turtle.left(90)




house()