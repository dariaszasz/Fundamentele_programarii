import turtle
t = turtle.Pen()
alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'u',
        'x', 'y', 'z', '.', '?', '!']

def delete2():
    t.home()
    t.clear()
def delete():
    t.home()
    t.clear()
    t.up()
    t.backward(300)
    t.down()
def space():
    t.up()
    t.forward(15)
    t.down()

def a():
    t.up()
    t.forward(7)
    t.down()
    t.forward(15)
    t.back(15)
    t.left(60)
    t.back(17)
    t.forward(34)
    t.right(120)
    t.forward(34)
    t.back(17)

    t.left(60)  # zuruck nach rechts fur den nachsten Buchstaben
    t.up()
    t.forward(21)
    t.down()

def b():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(10)
    t.right(45)
    t.forward(3)
    t.left(90)
    t.forward(3)
    t.right(45)
    t.forward(10)
    t.right(45)
    t.forward(5)
    t.right(45)
    t.forward(10)
    t.right(90)
    t.up()
    t.forward(15)
    t.right(90)
    t.forward(2)
    t.down()
    t.forward(12)

    t.up()
    t.forward(17)
    t.down()


def c():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.up()
    t.right(90)
    t.forward(30)
    t.left(90)
    t.down()
    t.back(20)

    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.down()


def d():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(15)
    t.right(30)
    t.forward(5)
    t.right(60)
    t.forward(26)
    t.right(60)
    t.forward(5)
    t.right(30)
    t.forward(15)

    t.up()
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.down()


def e():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.up()
    t.right(90)
    t.forward(30)
    t.left(90)
    t.down()
    t.back(20)


    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.up()
    t.forward(15)
    t.down()


def f():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.up()
    t.right(90)
    t.forward(30)
    t.left(90)
    t.back(20)
    t.down()

    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.up()
    t.forward(15)
    t.down()


def g():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.up()
    t.right(90)
    t.forward(17)
    t.down()
    t.left(90)
    t.back(8)
    t.forward(8)
    t.right(90)
    t.forward(13)
    t.left(90)
    t.back(20)

    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.down()


def h():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.back(15)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.back(15)
    t.forward(30)
    t.back(15)

    t.up()
    t.right(90)
    t.forward(15)
    t.down()


def i():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.back(15)

    t.up()
    t.right(90)
    t.forward(15)
    t.down()


def j():
    t.up()
    t.right(90)
    t.forward(5)
    t.down()
    t.forward(10)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(30)
    t.back(15)

    t.up()
    t.right(90)
    t.forward(15)
    t.down()


def k():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.back(15)
    t.right(45)
    t.forward(20)
    t.back(20)
    t.right(90)
    t.forward(20)
    t.back(20)
    t.left(45)

    t.up()
    t.forward(35)
    t.down()


def l():
    t.left(90)
    t.forward(15)
    t.back(30)
    t.right(90)
    t.forward(20)
    t.back(20)
    t.left(90)
    t.forward(15)

    t.up()
    t.right(90)
    t.forward(35)
    t.down()


def m():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(135)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.right(135)
    t.forward(30)
    t.back(15)

    t.up()
    t.left(90)
    t.forward(15)
    t.down()


def n():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(150)
    t.forward(35)
    t.left(150)
    t.forward(30)

    t.up()
    t.back(15)
    t.right(90)
    t.forward(15)
    t.down()


def o(t):
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(20)

    t.up()
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.down()


def p():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(13)
    t.right(90)
    t.forward(20)

    t.up()
    t.left(90)
    t.forward(2)
    t.left(90)
    t.forward(35)
    t.down()


def q():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.up()
    t.forward(5)
    t.right(135)
    t.down()
    t.forward(10)
    t.back(10)
    t.left(135)
    t.up()
    t.back(5)
    t.down()
    t.left(90)
    t.forward(15)

    t.up()
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.down()


def r():
    t.left(90)
    t.back(15)
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(13)
    t.right(90)
    t.forward(20)
    t.left(135)
    t.forward(24)
    t.back(22)

    t.up()
    t.left(45)
    t.forward(35)
    t.down()


def s():
    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.down()
    t.forward(20)
    t.back(20)
    t.right(90)
    t.forward(15)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(20)

    t.up()
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(35)
    t.down()


def T():
    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.down()
    t.forward(20)
    t.back(10)
    t.right(90)
    t.forward(30)
    t.back(15)

    t.up()
    t.left(90)
    t.forward(25)
    t.down()


def u(t):
    t.left(90)
    t.forward(15)
    t.back(30)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(30)
    t.back(15)

    t.up()
    t.right(90)
    t.forward(15)
    t.down()


def v():
    t.up()
    t.left(90)
    t.forward(15)
    t.right(150)
    t.down()
    t.forward(30)
    t.left(120)
    t.forward(32)

    t.up()
    t.back(18)
    t.right(60)
    t.forward(20)
    t.down()


def w():
    t.up()
    t.left(90)
    t.forward(15)
    t.right(165)
    t.down()
    t.forward(30)
    t.left(150)
    t.forward(30)
    t.right(150)
    t.forward(30)
    t.left(150)
    t.forward(30)

    t.up()
    t.back(16)
    t.right(75)
    t.forward(17)
    t.down()


def x():
    t.up()
    t.left(90)
    t.forward(15)
    t.down()
    t.right(150)
    t.forward(36)
    t.up()
    t.left(150)
    t.forward(31)
    t.down()
    t.left(150)
    t.forward(36)

    t.up()
    t.back(19)
    t.left(120)
    t.forward(22)
    t.down()


def y():
    t.up()
    t.left(90)
    t.forward(15)
    t.down()
    t.right(150)
    t.forward(15)
    t.left(120)
    t.forward(15)
    t.back(15)
    t.right(150)
    t.forward(17)

    t.up()
    t.back(15)
    t.left(90)
    t.forward(20)
    t.down()


def z():
    t.up()
    t.left(90)
    t.forward(15)
    t.down()
    t.right(90)
    t.forward(20)
    t.left(245)
    t.forward(32)
    t.right(245)
    t.forward(20)

    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.forward(15)
    t.down()

def Dot():
     t.up()
     t.right(90)
     t.forward(13)
     t.down()
     t.forward(2)
     t.left(90)
     t.forward(2)
     t.left(90)
     t.forward(2)
     t.left(90)
     t.forward(2)
     t.right(90)
     t.up()
     t.forward(13)
     t.right(90)
     t.forward(15)
     t.down()

def Frage():
    t.up()
    t.left(90)
    t.forward(15)
    t.right(90)
    t.down()
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(15)
    t.left(90)
    t.forward(17)
    t.up()
    t.forward(2)
    t.down()
    t.forward(1)
    t.up()
    t.back(15)
    t.left(90)
    t.forward(30)
    t.down()

def Ausrufezeichen():
    t.up()
    t.left(90)
    t.forward(15)
    t.down()
    t.right(180)
    t.forward(25)
    t.up()
    t.forward(3)
    t.down()
    t.forward(2)
    t.up()
    t.back(15)
    t.left(90)
    t.forward(20)
    t.down()





al = {'a': a,
      'b': b,
      'c': c,
      'd': d,
      'e': e,
      'f': f,
      'g': g,
      'h': h,
      'i': i,
      'j': j,
      'k': k,
      'l': l,
      'm': m,
      'n': n,
      'o': o,
      'p': p,
      'q': q,
      'r': r,
      's': s,
      't': T,
      'u': u,
      'v': v,
      'w': w,
      'x': x,
      'y': y,
      'z': z,
      '.': Dot,
      '?': Frage,
      '!': Ausrufezeichen,
      ' ': space
      }