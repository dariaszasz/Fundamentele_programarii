def ordnen_desc(zahlenliste): #fallende Ordung der Zahlen aus der Liste
    for i in range(len(zahlenliste)):
        for j in range(i+1,len(zahlenliste)):
            if zahlenliste[i]<zahlenliste[j]:
                zahlenliste[i],zahlenliste[j]=zahlenliste[j], zahlenliste[i] # wächseln der Zahlen zwischeneinander

    return zahlenliste

def konkatenation(zahlenliste):
    ordnen_desc(zahlenliste) # man ordnet die gegebene Liste
    nummer=zahlenliste[0] # Nummer nimmt die erste Zahl aus der Liste, alo die grösste
    for i in range(1, len(zahlenliste)): # man bildet die Konkatenation
        nummer=int(nummer*100+zahlenliste[i])

    return nummer


liste=[98,56,44,10,64]
print(konkatenation(liste))