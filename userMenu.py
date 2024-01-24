def menu_choice():
    print("[1]  Spara ner till JSON")
    print("[2]  Lägg till person")
    print("[3]  Ta bort person")
    print("[4]  Visa data")
    print("[5]  Spara data")
    print("[6]  Avsluta program.")


# Användarens alternativ är mellan 1-3.
def menu_select(choice):
    if choice == 1:
        print('du har valt alterinativ 1')
    elif choice == 2:
        print('du har valt alterinativ 2')
        person_manager.add_person()
    elif choice == 3:
        print('du har valt alterinativ 3')
        person_manager.remove_person()
    elif choice == 4:
        print('du har valt alterinativ 4')
    elif choice == 5:
        print('du har valt alterinativ 5')
    elif choice == 6:
        exit()
    else:
        print("Ogiltigt val, var vänlig ange rätt alternativ.")


# Funktion som letar efter vilket val det är som användaren har skrivit in. Kopplad till funktion menu_operator.
def main():
    while True:
        menu_choice()
        try:
            choice = int(input("Vänligen ange ditt val."))
            menu_select(choice)
        except ValueError:
            print("Ogiltig inmatning.")


# Kontrollerar om python-filen körs direkt eller om den importeras som en modul i ett annat program.
if __name__ == "__main__":
    main()