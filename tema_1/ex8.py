def potenz(x,n):
    if n==0:#orice numar la puterea 0 este 1
        return 1
    elif n%2==0: #daca puterea este para pentru a folosi inmultire despartim puterea in doua prin impartirea ei la 2 apoi inmultim numarele optinute prin ridicarea la jumatatea puterii
        hälfte=potenz(x,n//2)
        return hälfte*hälfte
    else: #daca puterea este impara facem n-1 pentru a o face para, repetam ca mai sus, dar la final pt ca am scazut 1 de la puere trebuie sa mai inmultim din nou cu numarul dat x
        hälfte=potenz(x,(n-1)//2)
        return hälfte*hälfte*x


print(potenz(7,2))




def Teilfolge(reihe):
    max_länge=1
    länge=1
    for i in range(1,len(reihe)):#parcurgem secventa data
        if (reihe[i]>0 and reihe[i-1]<0) or (reihe[i]< 0 and reihe[i-1]>0):# verificam daca doua numere consecutive au semn opus
            länge+=1
        else: #cand doua elemente consecutive nu mai au semn opus "contorul de lungime" se reseteaza inapoi la 1
            länge=1

        if länge>max_länge: #se gaseste lungimea maxima 
            max_länge=länge

    return max_länge


print(Teilfolge([1, -2, 3, -4, 5, -6, -7, 8]))