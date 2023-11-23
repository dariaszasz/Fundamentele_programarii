from menu import *
from tasten import zeichnen
from auto_zeichnen import auto_zeichnen
from Buchstaben import delete,delete2

def main():
   with open('datei.txt', 'a') as file:
       file.write("\n")
   while True:
        print(meniu())
        opt = int(input("Option="))
        if opt == 1:
            auto_zeichnen()
        if opt == 2:
            delete2()
            print(meniu_manual_zeichnen())
            zeichnen()
        if opt == 0:
            break

main()