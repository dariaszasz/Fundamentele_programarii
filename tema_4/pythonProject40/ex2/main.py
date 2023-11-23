def ersetzungen(dateipfad, zu_ersetzende_woerter, ersatzwoerter):
   with open(dateipfad, 'r') as datei:
       text = datei.read()
       text1 = text.replace(zu_ersetzende_woerter, ersatzwoerter)
       ersetzungszahl = text1.count(ersatzwoerter)
   with open(dateipfad, 'w') as datei:
       datei.write(text1)

   if ersetzungszahl > 0:
       print(f"Ersetzt {zu_ersetzende_woerter} mit {ersatzwoerter} {ersetzungszahl} mal")
   else:
       print("Keine Ersetzungen wurden in der Datei vorgenommen")

def main():
    dateipfad = 'datei.txt'
    zu_ersetzende_woerter = 'Katze'
    ersatzwoerter = 'Puppe'
    ersetzungen(dateipfad, zu_ersetzende_woerter, ersatzwoerter)

main()