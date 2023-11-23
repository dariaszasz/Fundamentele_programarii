from Buchstaben import *
def auto_zeichnen():
    delete()
    word = input("Wort=")
    for letter in word:
        al[letter]()