def filtern(lista,formel):  # formula e un 'string'
     lista_numere_filtrate = []
     for nr in lista:
         x=nr//10 #cifra zecilor
         y=nr%10 #cifra unitatilor
         if eval(formel)==True:
             lista_numere_filtrate.append(nr)

     return lista_numere_filtrate

lista = [42,67,50,63,84]
print(filtern(lista,'x==y*2'))