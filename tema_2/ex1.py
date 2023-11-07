def entferne_doppelte_Zahlen(zahlenliste):
    liste=[] #eine neue leere Liste

    for n in zahlenliste:
        if n not in liste: #Überprüfen, ob die Zahl bereits gesehen wurde
            liste.append(n)

    return liste

print(entferne_doppelte_Zahlen(["11", "22", "33", "11", "44", "55", "22"]))
