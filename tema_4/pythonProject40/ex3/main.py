import random
def SSP():
    zeichen=["Schere", "Stein", "Papier"]

    spieler_pkt=0
    computer_pkt=0

    for i in range(3):
        computer_wahl=random.choice(zeichen)

        benutzer_wahl = input("Schere, Stein oder Papier? ").capitalize()

        if benutzer_wahl in zeichen:
            print("Computer wählt",computer_wahl)
            if benutzer_wahl == computer_wahl:
                print("Unentschieden!")
            elif (
                (benutzer_wahl == "Schere" and computer_wahl == "Papier") or
                (benutzer_wahl == "Stein" and computer_wahl == "Schere") or
                (benutzer_wahl == "Papier" and computer_wahl == "Stein")
            ):
                print("Du gewinnst diese Runde!")
                spieler_pkt += 1
            else:
                print("Computer gewinnt diese Runde!")
                computer_pkt += 1
        else:
            print("Ungültige Eingabe.")


    if spieler_pkt > computer_pkt:
        print("Du gewinnst!")
    elif spieler_pkt < computer_pkt:
        print("Computer gewinnt!")
    else:
        print("Das Spiel endet unentschieden!")


SSP()
