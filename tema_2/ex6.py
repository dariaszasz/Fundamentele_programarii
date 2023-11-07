def verif(a,b): #überprüfen ob "domino"
     if int(a%10)==int(b/10):
         return True
     return False

def domino(zahlenliste):
     jetzt=[zahlenliste[0]]
     max=[zahlenliste[0]]
     lange_jetzt=0
     lange_max=0
     for i in range(1,len(zahlenliste)):
         if verif(zahlenliste[i-1],zahlenliste[i])==True: #man überprüft je zwei aufeinanderfolgende Zahlen
             jetzt.append(zahlenliste[i]) # es "erinnert" sich nur um die wahre Bedingungen
             lange_jetzt += 1
         else:
             if lange_max<lange_jetzt: #daca nu se reseteaza toate "contoarele"
                lange_max=lange_jetzt
                max=jetzt
             lange_jetzt=1
             jetzt=[zahlenliste[i]]
     if lange_max<=lange_jetzt: #man finder die längste Dominofolge
         lange_max=lange_jetzt
         max=jetzt

     return max


print(domino([89,95,56,20,98,89,97,73]))


