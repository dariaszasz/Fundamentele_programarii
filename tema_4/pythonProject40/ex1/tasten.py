import turtle

def forward():
    turtle.forward(10)
    with open('datei.txt', 'a') as file:
        file.write("w")

def backwards():
    turtle.forward(-10)
    with open('datei.txt', 'a') as file:
        file.write("s")

def right():
    turtle.right(45)
    with open('datei.txt', 'a') as file:
        file.write("d")

def left():
    turtle.left(45)
    with open('datei.txt', 'a') as file:
        file.write("a")

def lift():
    turtle.up()
    with open('datei.txt', 'a') as file:
        file.write("f")

def putdown():
    turtle.down()
    with open('datei.txt', 'a') as file:
        file.write("g")

def clear_screen():
    turtle.clear()
    with open('datei.txt', 'a') as file:
        file.write("c")

def zeichnen():
    turtle.home()
    turtle.clear()
    turtle.onkey(forward, 'w')
    turtle.onkey(backwards, 's')
    turtle.onkey(right, 'd')
    turtle.onkey(left, 'a')
    turtle.onkey(lift, 'f')
    turtle.onkey(putdown, 'g')
    turtle.onkey(clear_screen, 'c')
    turtle.onkey(exit, 'Return')
    turtle.listen()
    turtle.done()