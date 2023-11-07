def umkehr(n): #Umkehrbare einer Zahl
     inv=0
     while n>0:
         inv=inv*10 + n%10
         n=int(n/10)
     return inv

def symmetrisch(zahlenliste):
     ct=0
     for i in range(len(zahlenliste)):
         for j in range(i+1,len(zahlenliste)):
             if zahlenliste[i]==(umkehr(zahlenliste[j])): #man sucht das Umkehrbare El 
                 ct+=1
                 break

     return ct


liste=[21,12,33,65,48,69,12,33,12,56]
print(symmetrisch(liste))
