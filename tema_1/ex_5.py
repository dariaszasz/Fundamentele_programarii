def exponent(n,p):
    exp = 0
    # cat timp p il imparte pe n exponentul lui p va creste cu 1 apoi numarul va fi impartit cu p pana cand p nu il mai imparte numarul
    while n % p == 0:
        exp += 1
        n = n // p

    #daca exponentul este mai mare de 0 adica daca p l-a impartit pe n macar o data se va afisa mesajul...., iar daca nu inseamna ca p nu este un factor prim care il imparte pe n
    if exp > 0:
        print(f"Der Exponent von {p} in der Primfaktorzerlegung von {n} ist {exp}.")
    else:
        print(f"{p} ist kein Primfaktor von {n}.")


print(exponent(120,2))




#verificare daca un numar este prim
def prim(nr):
    is_prime = True

    for div in range(2, nr // 2):
        if nr % div == 0:
            is_prime = False

    if is_prime:
        return True
    else:
        return False


def längste_Teilfolge(reihe):
    länge_max=0
    länge=0
    position_max=0
    position = 0

    #parcurgem secventa si verificam daca doua numere consecutive sunr prime
    for i in range(1, len(reihe)):
        if prim(reihe[i]) and prim(reihe[i-1]): # daca este adevarat lungimea subsecventei creste cu 1
            länge+=1
        else: #daca nu se reseteaza
            länge=0
            position = i

        if länge > länge_max: #daca lungimea este mai mare decat lungimea maxima atunci lung.max va primi valoarea cea mai mare gasita
            länge_max = länge
            position_max = position

    return reihe[position_max:position_max+länge_max+2] # se returneaza cea mai lunga subsecventa de numere prime



print(längste_Teilfolge([2, 3, 4, 5, 7, 20, 11, 13, 17, 19, 23, 29, 31]))
