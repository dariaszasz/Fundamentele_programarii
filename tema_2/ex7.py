def ggT(a,b):
    while b:
        a,b =b,a%b
    return a

def kgV(a,b):
    # Berechnung des kleinsten gemeinsamen Vielfachen
    return a*b//ggT(a,b)

def kleinstes_gemeinsame_vielfaches(zahlenliste,from_index,to_index):
    if from_index<0 or to_index>=len(zahlenliste) or from_index>=to_index:
        return None  #ungültiger Indexbereich

    kgV_result = int(zahlenliste[from_index])  # Anfang mit dem ersten Element
    for index in range(from_index+1,to_index+1):
        zahl=int(zahlenliste[index])
        kgV_result=kgV(kgV_result,zahl)

    return kgV_result


print("Kleinstes gemeinsames Vielfache:", kleinstes_gemeinsame_vielfaches(["12", "24", "48", "36", "98"], 0, 2))
