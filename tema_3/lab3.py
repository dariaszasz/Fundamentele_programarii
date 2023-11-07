import turtle


def rechteck():
    # Erstes Rechteck (100x200)
    turtle.forward(200)  # Zeichnet die obere Kante(Breite)
    turtle.left(90)  # Dreht um 90 Grad nach links
    turtle.forward(100)  # Zeichnet die rechte Kante (Höhe)
    turtle.left(90)
    turtle.forward(200)  # Zeichnet die untere Kante (Breite)
    turtle.left(90)
    turtle.forward(100)  # Zeichnet die linke Kante (Höhe)
    turtle.left(90)

    # Zweites Rechteck (25x50) innerhalb des ersten Rechtecks
    turtle.penup()  # Stift heben
    turtle.goto(70, 40)  #  Mitte des ersten Rechtecks
    turtle.pendown()  # Stift senken
    turtle.forward(50)  # Zeichnet die obere Kante(Breite)
    turtle.left(90)
    turtle.forward(25)  # Zeichnet die rechte Kante(Höhe)
    turtle.left(90)
    turtle.forward(50)  # Zeichnet die untere Kante(Breite)
    turtle.left(90)
    turtle.forward(25)  # Zeichnet die linke Kante(Höhe)
    turtle.left(90)

    turtle.done()






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


    turtle.done()









def house():

    #Quadrat
    turtle.penup()
    turtle.goto(-100,-100)
    turtle.pendown()
    for i in range(4):
        turtle.forward(200)
        turtle.left(90)

    turtle.penup()
    turtle.goto(130,-100)
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

    turtle.penup()
    turtle.goto(130,100)
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

    turtle.penup()
    turtle.goto(170,0)
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

    turtle.penup()
    turtle.goto(220,-100)
    turtle.pendown()
    for i in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(80)
        turtle.left(90)


    turtle.done()





def menu():
    return """
        1-Rechtecke
        2-Herz
        3-Haus
        0-exit
    """

def main():
    while True:
        print(menu())
        opt= int(input('opt= '))

        if opt==1:
            rechteck()


        if opt==2:
            herz()


        if opt==3:
            house()


        if opt==0:
            break




main()