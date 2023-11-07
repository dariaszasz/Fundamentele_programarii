def addition(zahlenliste):
    if not zahlenliste:
        return []

    key=int(zahlenliste[0])
    verschluesselte_liste=[str(int(zahl)+key) for zahl in zahlenliste]

    return verschluesselte_liste




def multiplikation(zahlenliste):
    if not zahlenliste:
        return []

    key=int(zahlenliste[0])
    verschluesselte_liste=[str(int(zahl)*key) for zahl in zahlenliste]

    return verschluesselte_liste




def xor(zahlenliste):
    if not zahlenliste:
        return []

    key=int(zahlenliste[0])
    verschluesselte_liste=[str(int(zahl)^key) for zahl in zahlenliste]

    return verschluesselte_liste




liste = ["31", "42", "53", "64"]
methode = "addition"  # kann man Ändern
if methode == "addition":
    verschluesselte_liste=addition(liste)
elif methode == "multiplikation":
    verschluesselte_liste=multiplikation(liste)
elif methode == "xor":
    verschluesselte_liste=xor(liste)
else:
    print("Ungültige Methode")
    verschluesselte_liste=[]

print("Verschlüsselte Liste:", verschluesselte_liste)
