import turtle

def rechteck():
    # Erstes Rechteck (100x200)
    turtle.forward(200)  # Zeichnet die obere Kante(Breite)
    turtle.left(90)  # Dreht um 90 Grad nach links
    turtle.forward(100)  # Zeichnet die rechte Kante (Höhe)
    turtle.left(90)  # Dreht um 90 Grad nach links
    turtle.forward(200)  # Zeichnet die untere Kante (Breite)
    turtle.left(90)  # Dreht um 90 Grad nach links
    turtle.forward(100)  # Zeichnet die linke Kante (Höhe)
    turtle.left(90)  # Dreht um 90 Grad nach links

    # Zweites Rechteck (25x50) innerhalb des ersten Rechtecks
    turtle.penup()  # Stift heben
    turtle.goto(25, 25)  # Positionieren den Turtle-Stift in der Mitte des ersten Rechtecks
    turtle.pendown()  # Stift senken
    turtle.forward(50)  # Zeichnet die obere Kante des inneren Rechtecks (Breite)
    turtle.left(90)  # Dreht um 90 Grad nach links
    turtle.forward(25)  # Zeichnet die rechte Kante des inneren Rechtecks (Höhe)
    turtle.left(90)  # Dreht um 90 Grad nach links
    turtle.forward(50)  # Zeichnet die untere Kante des inneren Rechtecks (Breite)
    turtle.left(90)  # Dreht um 90 Grad nach links
    turtle.forward(25)  # Zeichnet die linke Kante des inneren Rechtecks (Höhe)
    turtle.left(90)  # Dreht um 90 Grad nach links

    turtle.done()

rechteck()
